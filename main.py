from random import randint


def attack(char_name, char_class):
    name = char_name
    if char_class == 'warrior':
        return (f'{name} нанёс урон противнику равный {5 + randint(3, 5)}')
    if char_class == 'mage':
        return (f'{name} нанёс урон противнику равный {5 + randint(5, 10)}')
    if char_class == 'healer':
        return (f'{name} нанёс урон противнику равный {5 + randint(-3, -1)}')
    return (f'{name} нанёс урон противнику равный 5')


def defence(char_name, char_class):
    if char_class == 'warrior':
        return (f'{char_name} блокировал {10 + randint(5, 10)} урона')
    if char_class == 'mage':
        return (f'{char_name} блокировал {10 + randint(-2, 2)} урона')
    if char_class == 'healer':
        return (f'{char_name} блокировал {10 + randint(2, 5)} урона')
    return (f'{char_name} блокировал 10 урона')


def special(char_name, char_class):
    name = char_name
    if char_class == 'warrior':
        return (f'{name} применил специальное умение «Выносливость {80 + 25}»')
    if char_class == 'mage':
        return (f'{name} применил специальное умение «Атака {5 + 40}»')
    if char_class == 'healer':
        return (f'{name} применил специальное умение «Защита {10 + 30}»')
    return (f'{name} не применил специальное умение')


def start_training(char_name, char_class):
    if char_class == 'warrior':
        print(f'{char_name}, ты Воитель — отличный боец ближнего боя.')
    if char_class == 'mage':
        print(f'{char_name}, ты Маг — превосходный укротитель стихий.')
    if char_class == 'healer':
        print(f'{char_name}, ты Лекарь — чародей, способный исцелять раны.')
    print()
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: ')
    print('attack — чтобы атаковать противника')
    print('defence — чтобы блокировать атаку противника')
    print('special — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd = None
    while cmd != 'skip':
        print()
        cmd = input('Введи команду: ')
        print()
        if cmd == 'attack':
            print(attack(char_name, char_class))
        if cmd == 'defence':
            print(defence(char_name, char_class))
        if cmd == 'special':
            print(special(char_name, char_class))
    return 'Тренировка окончена.'


def choice_char_class():
    approve_choice = None
    char_class = None
    while approve_choice != 'y':
        char_class = input('''
Введи название персонажа, за которого хочешь играть.
Воитель — warrior, Маг — mage, Лекарь — healer: ''')
        if char_class == 'warrior':
            print()
            print('Воитель — дерзкий воин ближнего боя. ')
            print('Сильный, выносливый и отважный.')
        if char_class == 'mage':
            print()
            print('Маг — находчивый воин дальнего боя.')
            print('Обладает высоким интеллектом.')
        if char_class == 'healer':
            print()
            print('Лекарь — могущественный заклинатель.')
            print('Черпает силы из природы, веры и духов.')
        print()
        print('''Нажми (Y), чтобы подтвердить выбор,
или любую другую кнопку, чтобы выбрать другого персонажа ''')
        approve_choice = input().lower()
    return char_class


def main():
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print()
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class = choice_char_class()
    print(start_training(char_name, char_class))


main()
