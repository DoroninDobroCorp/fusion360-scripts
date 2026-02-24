🇬🇧 [English](#-english) | 🇷🇺 [Русский](#-русский)

---

# 🇬🇧 English

# 🛠 Fusion 360 Scripts

> A collection of handy scripts for [Autodesk Fusion 360](https://www.autodesk.com/products/fusion-360/) that automate routine 3D-modeling tasks.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Fusion 360](https://img.shields.io/badge/Autodesk-Fusion%20360-orange.svg)](https://www.autodesk.com/products/fusion-360/)
[![Python](https://img.shields.io/badge/Python-3.x-yellow.svg)](https://www.python.org/)

---

## 📦 Scripts

### CalculateDimensions

Automatically calculates the **overall dimensions** of every unique component in an assembly and writes them to the Description field.

- Processes all occurrences while skipping duplicates
- Ignores components with no bodies (empty or utility components)
- Converts dimensions from internal units (cm) to **mm**
- Sorts dimensions in descending order: `Dimensions: X × Y × Z mm`

> 💡 Great for quickly estimating part sizes and preparing BOMs.

---

### FindBoundingBox

Draws a **bounding rectangle** and a **center point** for all geometry in the active sketch.

- Analyzes every curve in the current sketch
- Draws 4 construction lines along the boundaries
- Adds a point at the geometric center
- Requires the sketch to be in edit mode

> 💡 Useful for alignment, finding the centroid of a contour, and creating guide lines.

---

### TheOneParam

Links **all user parameters** to a single chosen master parameter through proportional coefficients.

- Lets you pick the master parameter from a list
- Calculates a `value / master` ratio for each parameter
- Updates expressions to: `MasterParam * coefficient`
- Stores a `RelativeValue` attribute in the `OpenBOM` namespace
- Detailed log of every operation

> 💡 Perfect for parametric models — change one parameter and the entire model scales proportionally.

---

## 🚀 Installation

1. **Clone** the repository:
   ```bash
   git clone https://github.com/DoroninDobroCorp/fusion360-scripts.git
   ```

2. **Copy** the desired script folder into the Fusion 360 scripts directory:

   | OS      | Path                                                                                   |
   |---------|----------------------------------------------------------------------------------------|
   | Windows | `%APPDATA%\Autodesk\Autodesk Fusion 360\API\Scripts\`                                  |
   | macOS   | `~/Library/Application Support/Autodesk/Autodesk Fusion 360/API/Scripts/` |

3. In Fusion 360, open **Utilities → Scripts and Add-Ins** (or press <kbd>Shift</kbd>+<kbd>S</kbd>).

4. Click **"+"** next to "My Scripts", point to the script folder — it will appear in the list.

5. Select the script and click **Run**.

---

## 🧰 Requirements

- **Autodesk Fusion 360** (latest version)
- The scripts use Fusion 360's built-in Python interpreter — no additional dependencies required

---

## 📁 Project Structure

```
fusion360-scripts/
├── CalculateDimensions/
│   ├── CalculateDimensions.py          # Main script
│   ├── CalculateDimensions.manifest    # Script metadata
│   └── ScriptIcon.svg                  # Icon
├── FindBoundingBox/
│   ├── FindBoundingBox.py
│   ├── FindBoundingBox.manifest
│   └── ScriptIcon.svg
├── TheOneParam/
│   ├── TheOneParam.py
│   ├── TheOneParam.manifest
│   └── ScriptIcon.svg
├── LICENSE
└── README.md
```

---

## 🤝 Contributing

Pull requests are welcome! If you have ideas for new scripts or improvements, please open an [Issue](https://github.com/DoroninDobroCorp/fusion360-scripts/issues) or submit a PR.

---

## 📄 License

This project is licensed under the [MIT](LICENSE) license.

---

<p align="center">
  <i>Made with ❤️ for the Fusion 360 community</i>
</p>

---

# 🇷🇺 Русский

# 🛠 Fusion 360 Scripts

> Набор полезных скриптов для [Autodesk Fusion 360](https://www.autodesk.com/products/fusion-360/), автоматизирующих рутинные задачи при 3D-моделировании.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Fusion 360](https://img.shields.io/badge/Autodesk-Fusion%20360-orange.svg)](https://www.autodesk.com/products/fusion-360/)
[![Python](https://img.shields.io/badge/Python-3.x-yellow.svg)](https://www.python.org/)

---

## 📦 Скрипты

### CalculateDimensions

Автоматически вычисляет **габаритные размеры** каждого уникального компонента в сборке и записывает их в поле «Описание».

- Обрабатывает все вхождения, исключая дубликаты
- Пропускает компоненты без тел (пустые, служебные)
- Конвертирует размеры из внутренних единиц (см) в **мм**
- Сортирует размеры по убыванию: `Габариты: X × Y × Z мм`

> 💡 Удобно для быстрой оценки размеров деталей и подготовки спецификаций.

---

### FindBoundingBox

Строит **ограничительный прямоугольник** (bounding box) и **центральную точку** для всей геометрии в активном эскизе.

- Анализирует все кривые в текущем эскизе
- Рисует 4 вспомогательные (конструкционные) линии по границам
- Добавляет точку в геометрическом центре
- Требует активного режима редактирования эскиза

> 💡 Полезно для выравнивания, определения центра масс контура и создания направляющих.

---

### TheOneParam

Привязывает **все пользовательские параметры** к одному выбранному мастер-параметру через пропорциональные коэффициенты.

- Позволяет выбрать мастер-параметр из списка
- Вычисляет коэффициент `значение / мастер` для каждого параметра
- Обновляет выражения: `MasterParam * коэффициент`
- Сохраняет атрибут `RelativeValue` в пространстве имён `OpenBOM`
- Детальный лог всех операций

> 💡 Идеально для параметрических моделей — измените один параметр, и вся модель пропорционально масштабируется.

---

## 🚀 Установка

1. **Скачайте** репозиторий:
   ```bash
   git clone https://github.com/DoroninDobroCorp/fusion360-scripts.git
   ```

2. **Скопируйте** нужную папку скрипта в директорию скриптов Fusion 360:

   | ОС      | Путь                                                                                   |
   |---------|----------------------------------------------------------------------------------------|
   | Windows | `%APPDATA%\Autodesk\Autodesk Fusion 360\API\Scripts\`                                  |
   | macOS   | `~/Library/Application Support/Autodesk/Autodesk Fusion 360/API/Scripts/` |

3. В Fusion 360 откройте **Utilities → Scripts and Add-Ins** (или нажмите <kbd>Shift</kbd>+<kbd>S</kbd>).

4. Нажмите **«+»** рядом с «My Scripts», укажите папку скрипта — и он появится в списке.

5. Выберите скрипт и нажмите **Run**.

---

## 🧰 Требования

- **Autodesk Fusion 360** (актуальная версия)
- Скрипты используют встроенный Python-интерпретатор Fusion 360 — дополнительных зависимостей нет

---

## 📁 Структура проекта

```
fusion360-scripts/
├── CalculateDimensions/
│   ├── CalculateDimensions.py          # Основной скрипт
│   ├── CalculateDimensions.manifest    # Метаданные скрипта
│   └── ScriptIcon.svg                  # Иконка
├── FindBoundingBox/
│   ├── FindBoundingBox.py
│   ├── FindBoundingBox.manifest
│   └── ScriptIcon.svg
├── TheOneParam/
│   ├── TheOneParam.py
│   ├── TheOneParam.manifest
│   └── ScriptIcon.svg
├── LICENSE
└── README.md
```

---

## 🤝 Вклад

Pull request'ы приветствуются! Если у вас есть идеи для новых скриптов или улучшений — создайте [Issue](https://github.com/DoroninDobroCorp/fusion360-scripts/issues) или отправьте PR.

---

## 📄 Лицензия

Проект распространяется по лицензии [MIT](LICENSE).

---

<p align="center">
  <i>Сделано с ❤️ для Fusion 360 сообщества</i>
</p>
