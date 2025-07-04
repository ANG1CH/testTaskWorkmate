# CSV Tool

Инструмент для фильтрации и агрегации CSV-файлов.

## Пример работы

![Пример работы](c:/Users/avdon/AppData/Local/Packages/MicrosoftWindows.Client.CBS_cw5n1h2txyewy/TempState/ScreenClip/{D1A0A246-72E9-4406-9C50-D6AA137680E4}.png)

## Запуск

```powershell
D:/Projects-on-Python/testTaskWorkmate/.venv/Scripts/python.exe csv_tool/main.py "C:\\Users\\avdon\\Downloads\\products.csv" --where "price=>500"
```

## Аргументы
- file — путь к CSV-файлу
- --where — фильтр (например, price=>500)
- --aggregate — агрегация (например, price=avg)