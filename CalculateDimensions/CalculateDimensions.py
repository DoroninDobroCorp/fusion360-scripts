

import adsk.core, adsk.fusion, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface
        design = app.activeProduct
        if not design:
            ui.messageBox('Сначала откройте проект (сборку).', 'Нет активного проекта')
            return

        rootComp = design.rootComponent
        
        # Используем словарь для обработки только уникальных компонентов
        components_to_process = {}
        for occ in rootComp.allOccurrences:
            components_to_process[occ.component.entityToken] = occ.component

        processed_count = 0
        
        # Обрабатываем каждый уникальный компонент
        for comp_token in components_to_process:
            component = components_to_process[comp_token]
            
            # Пропускаем компоненты без тел (например, пустые или служебные)
            if component.bRepBodies.count == 0:
                continue

            # Вычисляем габариты в мм и сортируем от большего к меньшему
            bbox = component.boundingBox
            dims = sorted([
                (bbox.maxPoint.x - bbox.minPoint.x) * 10,
                (bbox.maxPoint.y - bbox.minPoint.y) * 10,
                (bbox.maxPoint.z - bbox.minPoint.z) * 10
            ], reverse=True)
            
            # Формируем строку с размерами
            dimension_string = f'Габариты: {dims[0]:.2f} x {dims[1]:.2f} x {dims[2]:.2f} мм'

            # Записываем строку в свойство "Описание" для ВСЕХ компонентов
            component.description = dimension_string

            processed_count += 1

        ui.messageBox(f'Скрипт завершен.\n\nРазмеры записаны в свойство "Описание" для {processed_count} уникальных компонентов.')

    except:
        if ui:
            ui.messageBox('Ошибка выполнения скрипта:\n{}'.format(traceback.format_exc()))