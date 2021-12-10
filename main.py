from crypt import Crypto
from decrypt import Decoder

'''
Данный файл main.py используется для запуска данной программы



Для шифровки необходимо создать экземпляр класса Crypto(),
передать в него аргументом ключ для шифровки и использовать
метод crypt(), в который передать шифруемую строку.

Например:
test = Crypto('эми').crypt('ева')

Для дешифровки необходимо создать экземпляр класса Decoder(),
передать в него аргументом ключ для расшифровки и использовать
метод decrypt(), в который первым аргументом передать 
зашифрованную строку, а вторым - токен для расщифровки.

Например: 
test2 = Decoder('эми').decrypt('вдбгагвжвжгаёаёёгаежгёёеебд', 3218200)

'''
if __name__ == '__main__':
    test = Crypto('эми').crypt('ева')
    test2 = Decoder('эми').decrypt('вдбгагвжвжгаёаёёгаежгёёеебд', 3218200)
    print(test)
    print(test2)