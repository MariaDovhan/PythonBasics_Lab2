import sys
import math

def parseInput(number):
    # Дано три спроби ввести число
    for i in range(0, 2):
        try:
            natural_number = int(number)
            if (natural_number <= 0):
                print('Ви ввели не натуральне число, спробуйте ще ', end='')
                number = input()
                continue
            return natural_number
        except ValueError:
            print('Ви ввели не число, спробуйте ще ', end='')
            number = input()
    print('Спроби закінчилися, кінець програми ', end='')
    sys.exit()

def main():
    print('Ця програма знаходить прості числа в заданому інтервалі')

    # Введення початку і кінця інтервалу
    interval_start = parseInput(input('Введіть початок інтервалу '))
    interval_end = parseInput(input('Введіть кінець інтервалу '))

    # Перевірка що початок інтервалу менший або рівний за кінець
    if (interval_start > interval_end):
        print('Початок інтервалу повинен бути меншим за кінець')
        return
    
    print(f'Знайдено такі прості числа в інтервалі ({interval_start}, {interval_end}): ')

    # Перевірка кожного числа
    for current_value in range(interval_start, interval_end + 1):
        if current_value == 1: 
            continue 
        is_prime = True

        # Ділення числа на дільник від 2 до кореня з цього числа
        for divider in range(2, int(math.sqrt(current_value)) + 1):
            if current_value % divider == 0:
                is_prime = False
                break

        # Виведення числа, якщо воно просте
        if (is_prime):
            print(int(current_value), end=' ')

if __name__ == '__main__':
    main()