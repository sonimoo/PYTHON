import math


def fall_time():
    input_str = input("Введите высоту в метрах: ")

    try:
        height = float(input_str)
        if math.isnan(height) or height < 0:
            print("Ввод не является положительным числом.")
            return
    except ValueError:
        print("Это не число!")
        return

    time = math.sqrt(2 * height / 9.8)
    print(f"Время падения с высоты {height} метров составляет {time:.2f} секунд.")


fall_time()
