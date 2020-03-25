def checkBalance(string):
    # Строки с необходимыми для проверки скобками. Позиции открывающих и закрывающих скобок должны совпадать!
    brackets_open = '({[<'
    brackets_closed = '){]>'

    # Проверка на наличие скобок в строке
    cBrackets = 0

    # Проверка на пустую строку
    if len(string) == 0:
        return 'No string!'

    # Для открывающих скобок
    stack = []

    #Разбираем строчку
    for i in string:

        # Добавляем в стек открывающие скобки
        if i in brackets_open:
            cBrackets += 1
            stack.append(i)

        # Ищем закрывающие скобки
        if i in brackets_closed:
            cBrackets += 1
            # Если стек пустой, то строка не сбалансирована
            if len(stack) == 0:
                return 'Unbalanced!'
            # Если стек не пустой, сверяемся есть ли в нем соответствующая открывающая скобка.
            # Если нет - строка не сбалансирована
            # Если есть - скобку удаляем из стека и идем дальше
            index = brackets_closed.index(i)
            open_bracket = brackets_open[index]
            if stack[-1] == open_bracket:
                stack = stack[:-1]
            else:
                return 'Unbalanced!'

    # Проверяем, есть ли вообще скобки в строке
    if cBrackets == 0:
        return 'No brackets!'

    # Если в конце в стеке остались открывающие скобки, значит строка не сбалансирована
    # Если стек пустой, значит строка сбалансирована
    if (not stack) == 0:
        return 'Unbalanced'
    else:
        return 'Balanced!'


string = input('Input string:')

print (checkBalance(string))
print ("03")