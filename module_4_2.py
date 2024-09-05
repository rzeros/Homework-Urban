def test_function():
    print('объемлющая область видиомости')

    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()


test_function()
# При вызове функции 'inner_function' вне функции 'test_function', возникает ошибка  'inner_function' is not defined.
# Did you mean: 'test_function'?. Данная ошибка возникает в случаях когда функция не была определена или находится
# вне области видимости.
