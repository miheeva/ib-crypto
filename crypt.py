from vars import *
import random


"""
Класс, предназначенный для шифрования полученной строки по ключу
"""


class Crypto:
    def __init__(self, key):
        self.key = key

    """
    Перемешивание индексов ключа
    """

    def generate_token(self):
        token = [str(i + 1) for i in range(len(self.key))]
        random.shuffle(token)
        return ''.join(token)

    """
    Превращение строки в числовой вид по готовому словарю
    """

    def _convert_text(self, text: str) -> int:
        convert_string = ''
        for i in text:
            if i in LETTERS.keys():
                convert_string += LETTERS.get(i)
        return int(convert_string)

    """
    Возвращение ключа в текстовый вид по его перемешанным индексам
    """

    def convert_key(self, token):
        convert_key = ''
        for num in str(token):
            for i, v in enumerate(self.key):
                if int(num) - 1 == i:
                    convert_key += v
        return self._convert_text(convert_key)

    """
    Добавление цифр-разделителей для двузначных чисел
    Создание списка цифр для дальнейшей передачи в токен
    """

    def add_numbers(self, key_list, text_list):
        free_number = ''
        numbers_for_token = []
        for i, j in zip(key_list, text_list):
            text_summ_shade = ''
            text_summ = ''
            for k, t in zip(i, j):
                summa = int(k) + int(t)
                text_summ_shade += str(summa)

            for number in DIGITS:
                if number not in text_summ_shade:
                    free_number = number
                    break

            for k, t in zip(i, j):
                summ = int(k) + int(t)
                text_summ += (str(summ) + free_number)
            numbers_for_token.append(free_number)
        return text_summ, numbers_for_token

    """
    Генерация токена
    """

    def generate_full_token(self, token, numbers):
        new_token = str(token) + ''.join(i for i in numbers)
        return new_token

    """
    Склеивание строки из списка числовых букв из метода add_number()
    С добавлением длины каждой буквы в начале буквы
    """

    def shuffle_text(self, digit_key: int, digit_text: int):
        shuffle_string = []
        key_list = []
        text_list = []
        for i in range(3, len(str(digit_key)) + 3, 3):
            key_list.append(str(digit_key)[i - 3:i])
        for i in range(3, len(str(digit_text)) + 3, 3):
            text_list.append(str(digit_text)[i - 3:i])
            leng = len(self.add_numbers(key_list, text_list)[0])
            qw = str(leng) + self.add_numbers(key_list, text_list)[0]
            shuffle_string.append(qw)
        token = self.add_numbers(key_list, text_list)[1]
        return int(''.join(shuffle_string)), token

    """
    Перевод строки из shuffle_text() в случайную систему счисления
    """

    def convert_to_notation(self, shuffle_string, token):
        scale = random.choice('23456789')
        if int(scale) <= 1:
            scale = int(scale)
            scale += 2
        shuffle_string = int(shuffle_string, 10) if isinstance(shuffle_string, str) else shuffle_string
        alphabet_to_convert = "0123456789"
        convert_digittext = ''
        while shuffle_string > 0:
            shuffle_string, m = divmod(shuffle_string, int(scale))
            convert_digittext += alphabet_to_convert[m % 10]
        token = str(token) + str(scale)
        return convert_digittext[::-1], token

    """
    Возвращение конвертированной строки в буквы по их индексу в алфавите
    """

    def return_to_text(self, digit_text):
        crypto_text = ''
        for i in digit_text:
            crypto_text += ALPHABET[int(i) % 33]
        return crypto_text

    """
    Главный метод
    """

    def crypt(self, text):
        reverse_token = self.generate_token()
        digit_text = self._convert_text(text)
        digit_key = self.convert_key(reverse_token)
        shuffle_string, dig_token = self.shuffle_text(digit_key, digit_text)
        digit_convert_text, generate_token = self.convert_to_notation(shuffle_string, reverse_token)
        generate_token = self.generate_full_token(generate_token, dig_token)
        return f'''
            Сгенерированный текст: {self.return_to_text(digit_convert_text)} 
            Токен для расшифровки: {generate_token}
            '''