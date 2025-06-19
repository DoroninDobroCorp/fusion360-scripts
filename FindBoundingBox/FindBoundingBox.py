# Импортируем необходимые библиотеки Fusion 360
import adsk.core, adsk.fusion, traceback

def run(context):
    ui = None
    try:
        # Получаем доступ к приложению и интерфейсу
        app = adsk.core.Application.get()
        ui = app.userInterface

        # --- САМАЯ ВАЖНАЯ ЧАСТЬ ---
        # Получаем доступ к эскизу, который сейчас редактируется
        activeSketch = app.activeEditObject
        if not activeSketch or activeSketch.objectType != 'adsk::fusion::Sketch':
            ui.messageBox('Пожалуйста, войдите в режим редактирования эскиза перед запуском скрипта.', 'Ошибка')
            return

        # Проверяем, есть ли в эскизе хоть какие-то кривые
        if activeSketch.sketchCurves.count == 0:
            ui.messageBox('В эскизе нет геометрии для анализа.', 'Информация')
            return

        # --- АЛГОРИТМ ПОИСКА КРАЙНИХ ТОЧЕК ---
        # Перебираем все кривые в эскизе и находим их общий "огибающий прямоугольник"
        overall_bbox = None
        for curve in activeSketch.sketchCurves:
            if overall_bbox is None:
                overall_bbox = curve.boundingBox
            else:
                # Расширяем наш общий прямоугольник, чтобы он включал прямоугольник текущей кривой
                overall_bbox.combine(curve.boundingBox)

        # --- РИСУЕМ ПРЯМОУГОЛЬНИК ---
        # Получаем координаты углов из найденного общего прямоугольника
        min_p = overall_bbox.minPoint
        max_p = overall_bbox.maxPoint
        
        # Создаем 4 точки для углов
        p1 = adsk.core.Point3D.create(min_p.x, min_p.y, 0)
        p2 = adsk.core.Point3D.create(max_p.x, min_p.y, 0)
        p3 = adsk.core.Point3D.create(max_p.x, max_p.y, 0)
        p4 = adsk.core.Point3D.create(min_p.x, max_p.y, 0)

        # Рисуем 4 вспомогательные линии, соединяя точки
        lines = activeSketch.sketchCurves.sketchLines
        line1 = lines.addByTwoPoints(p1, p2)
        line2 = lines.addByTwoPoints(p2, p3)
        line3 = lines.addByTwoPoints(p3, p4)
        line4 = lines.addByTwoPoints(p4, p1)
        
        # Делаем линии вспомогательными (пунктирными)
        line1.isConstruction = True
        line2.isConstruction = True
        line3.isConstruction = True
        line4.isConstruction = True

        ### НОВЫЙ БЛОК: СТРОИМ ЦЕНТРАЛЬНУЮ ТОЧКУ ###
        
        # Вычисляем координаты центра как среднее арифметическое между min и max точками
        center_x = (min_p.x + max_p.x) / 2
        center_y = (min_p.y + max_p.y) / 2
        
        # Создаем 3D-точку для центра
        center_p = adsk.core.Point3D.create(center_x, center_y, 0)

        # Добавляем эту точку в наш эскиз
        sketch_points = activeSketch.sketchPoints
        center_sketch_point = sketch_points.add(center_p)
        
        ### КОНЕЦ НОВОГО БЛОКА ###

        ui.messageBox('Прямоугольник и центральная точка успешно построены!', 'Готово')

    except:
        if ui:
            ui.messageBox('Произошла ошибка:\n{}'.format(traceback.format_exc()))