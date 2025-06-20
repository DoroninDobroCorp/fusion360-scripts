import adsk.core, adsk.fusion, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface
        design = adsk.fusion.Design.cast(app.activeProduct)

        if not design:
            ui.messageBox('Сначала откройте дизайн Fusion 360.')
            return

        params = design.userParameters
        if params.count < 2:
            ui.messageBox('Нужно хотя бы 2 пользовательских параметра.')
            return

        param_names = [p.name for p in params]

        try:
            input_name = ui.inputBox(
                'Введите имя мастер-параметра из списка:\n\n' + '\n'.join(param_names),
                'Выбор мастер-параметра',
                param_names[0]
            )
        except:
            return

        if isinstance(input_name, list):
            input_name = input_name[0]
        input_name = input_name.strip()
        if not input_name:
            ui.messageBox('Имя параметра не может быть пустым.')
            return

        master_param = next((p for p in params if p.name.strip().lower() == input_name.lower()), None)
        if not master_param:
            ui.messageBox(f'Параметр "{input_name}" не найден.')
            return

        units_mgr = app.activeProduct.unitsManager
        try:
            master_val = units_mgr.evaluateExpression(master_param.expression, master_param.unit)
        except:
            ui.messageBox(f'Не удалось получить числовое значение "{master_param.name}".')
            return

        if master_val is None or abs(master_val) < 1e-9:
            ui.messageBox(f'Мастер-параметр "{master_param.name}" не должен быть 0.')
            return

        converted = []
        failed = []
        log = []

        for param in params:
            try:
                if param.name == master_param.name:
                    # Коэффициент главного параметра = 1
                    rel_val_str = '1'
                    # Удаляем старый атрибут, если есть
                    attr = param.attributes.itemByName('OpenBOM', 'RelativeValue')
                    if attr:
                        param.attributes.removeByName('OpenBOM', 'RelativeValue')
                        log.append(f'Удалён старый атрибут у {param.name}')
                    param.attributes.add('OpenBOM', 'RelativeValue', rel_val_str)
                    log.append(f'Добавлен атрибут RelativeValue={rel_val_str} к {param.name}')
                    converted.append(f'{param.name} = 1 (мастер)')
                    continue

                val = units_mgr.evaluateExpression(param.expression, param.unit)
                coeff = val / master_val
                new_expr = f'{master_param.name} * {round(coeff, 6)}'
                param.expression = new_expr

                rel_val_str = f'{coeff:.6f}'
                attr = param.attributes.itemByName('OpenBOM', 'RelativeValue')
                if attr:
                    param.attributes.removeByName('OpenBOM', 'RelativeValue')
                    log.append(f'Удалён старый атрибут у {param.name}')
                param.attributes.add('OpenBOM', 'RelativeValue', rel_val_str)
                log.append(f'Добавлен атрибут RelativeValue={rel_val_str} к {param.name}')

                converted.append(f'{param.name} = {new_expr} (относит. {rel_val_str})')

            except Exception as e:
                failed.append(param.name)
                log.append(f'Ошибка у {param.name}: {str(e)}')

        # Проверяем, реально ли созданы атрибуты:
        for param in params:
            attr = param.attributes.itemByName('OpenBOM', 'RelativeValue')
            if attr:
                log.append(f'Проверка: {param.name} атрибут RelativeValue = {attr.value}')
            else:
                log.append(f'Проверка: {param.name} нет атрибута RelativeValue!')

        # Выводим лог и отчёт
        report = ''
        if converted:
            report += f'✅ Переведено параметров: {len(converted)}\n\n' + '\n'.join(converted) + '\n\n'
        else:
            report += '⚠️ Ни один параметр не был обновлён.\n\n'

        if failed:
            report += '❌ Ошибки при обработке:\n' + '\n'.join(failed) + '\n\n'

        report += '📝 Лог действий:\n' + '\n'.join(log)

        ui.messageBox(report, 'TheOneParam с расширенным логированием')

    except:
        if ui:
            ui.messageBox('Скрипт упал:\n\n' + traceback.format_exc())