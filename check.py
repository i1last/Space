import json

def get_sorted_distances(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        ports = data.get("Сингапур", {})

        # Сортируем порты по названию (алфавиту)
        # sorted(ports.items()) возвращает список кортежей (название, данные)
        sorted_ports = sorted(ports.items())

        print(f"{'Порт (А-Я)':<25} | {'Дистанция':<10}")
        print("-" * 40)

        for port_name, info in sorted_ports:
            # Обработка случая, если данные — это список (как в твоей ошибке)
            if isinstance(info, list) and len(info) > 0:
                # Если в списке несколько словарей, ищем distance в первом
                # Или используем info[0].get("distance")
                distance = info[0].get("distance", "Н/Д") if isinstance(info[0], dict) else "Н/Д"
            elif isinstance(info, dict):
                distance = info.get("distance", "Н/Д")
            else:
                distance = "Ошибка данных"
                
            print(f"{port_name:<25} | {distance:<10}")

    except FileNotFoundError:
        print("Файл result.json не найден в папке со скриптом.")
    except Exception as e:
        print(f"Ошибка: {e}")

get_sorted_distances('result.json')
