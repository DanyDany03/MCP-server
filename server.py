from datetime import datetime
from fastmcp import FastMCP
from routes.basic_match import setup_basic_math_routes
from routes.prompts import setup_math_prompts
from routes.resources import setup_math_resources
from routes.statistics import setup_statistics_routes
from routes.geometry import setup_geometry_routes


def create_math_server() -> FastMCP:
    """Создать и настроить математический MCP сервер."""

    server = FastMCP("Mathematical Calculator & Tutor")

    # Подключаем все модули
    setup_basic_math_routes(server)
    setup_statistics_routes(server)
    setup_geometry_routes(server)
    setup_math_resources(server)
    setup_math_prompts(server)

    # Дополнительные общие tools
    @server.tool()
    def server_info() -> dict:
        """Информация о математическом сервере."""
        return {
            "name": "Mathematical Calculator & Tutor",
            "version": "1.0.0",
            "description": "Полнофункциональный математический MCP сервер",
            "capabilities": {
                "tools": [
                    "Базовые вычисления",
                    "Решение квадратных уравнений",
                    "Статистический анализ",
                    "Геометрические вычисления",
                    "Факториалы"
                ],
                "resources": [
                    "Математические формулы",
                    "Константы",
                    "Справка по статистике",
                    "Примеры решений"
                ],
                "prompts": [
                    "Объяснение решений",
                    "Создание задач",
                    "Репетиторство",
                    "Анализ ошибок"
                ]
            },
            "created_at": datetime.now().isoformat()
        }

    @server.resource("math://help/getting_started")
    def getting_started() -> str:
        """Руководство по началу работы с математическим сервером."""
        return """
# Математический MCP Сервер - Руководство

## 🧮 Инструменты (Tools):
- `calculate_basic(expression)` - Вычисление математических выражений
- `solve_quadratic(a, b, c)` - Решение квадратных уравнений
- `analyze_dataset(numbers)` - Статистический анализ данных
- `circle_properties(radius)` - Свойства окружности
- `triangle_area(base, height)` - Площадь треугольника
- `factorial(n)` - Вычисление факториала

## 📚 Ресурсы (Resources):
- `/formulas/basic` - Основные математические формулы
- `/constants/mathematical` - Математические константы  
- `/help/statistics` - Справка по статистике
- `/examples/{operation}` - Примеры решений

## 💭 Промпты (Prompts):
- `explain_solution` - Объяснение математических решений
- `create_practice_problems` - Генерация практических задач
- `math_tutor` - Роль математического репетитора
- `analyze_math_error` - Анализ ошибок в решениях

## Примеры использования:

### Вычисления:
```
calculate_basic("2**3 + sqrt(16)")
solve_quadratic(1, -5, 6)
```

### Статистика:
```
analyze_dataset([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
correlation_coefficient([1, 2, 3], [2, 4, 6])
```

### Геометрия:
```
circle_properties(5)
distance_between_points(0, 0, 3, 4)
```
"""

    return server


# ================================
# ЗАПУСК СЕРВЕРА
# ================================

if __name__ == "__main__":
    math_server = create_math_server()
    math_server.run(transport="http", port=3333, host="0.0.0.0")
