# CSV Tool

Инструмент для фильтрации и агрегации CSV-файлов.

## Пример работы

![Пример работы]("testTaskWorkmate\csv_tool\testScrin\image.png" )

## Запуск

```powershell
D:/Projects-on-Python/testTaskWorkmate/.venv/Scripts/python.exe csv_tool/main.py "C:\\Users\\avdon\\Downloads\\products.csv" --where "price=>500"
```

## Аргументы
- file — путь к CSV-файлу
- --where — фильтр (например, price=>500)
- --aggregate — агрегация (например, price=avg)