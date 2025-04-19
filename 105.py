def func_one():
    print('Раз')
    func_two()

def func_two():
    print('Два')
    func_one()

func_one() # Вызываем функцию func_one()

# iDONi ошибка