from vars import *


class Decoder:
    def __init__(self, key):
        self.key = key

    """
    Возврат полученной строки в цифры
    """
    def decrypt_to_digits(self, text):
        digit_text = ''
        for i in text:
            digit_text += str(ALPHABET.index(i))
        return digit_text

    """
    Разделение токена:
    token - Сам токен с перестановленным индексом
    notation - Система счисления
    digits - Цифры-разделители
    """

    def split_token(self, full_token):
        full_token = str(full_token)
        len_key = len(self.key)
        token, full_token = full_token[:len_key], full_token[len_key:]
        notation, full_token = full_token[0], full_token[1:]
        digits = full_token
        return token, notation, digits

    """
    Перевод обратно в 10СС
    """

    def convert_to_notation(self, digit_text, scale):
        num = int(scale)
        digit_text = int(digit_text, num) if isinstance(digit_text, str) else digit_text
        alphabet_to_convert = "0123456789"
        convert_digittext = ''
        while digit_text > 0:
            digit_text, m = divmod(digit_text, 10)
            convert_digittext += alphabet_to_convert[m % 10]
        return convert_digittext[::-1]

    """
    Восстановление ключа по закодированному индексу токена
    """

    def restore_key(self, token):
        generate_key = ''
        for num in str(token):
            generate_key += self.key[int(num) - 1]
        return self._convert_text(generate_key)

    """
    Получение текстового значения ключа
    """

    def convert_key(self, generate_key):
        convert_key = ''
        for num in generate_key:
            for i, v in enumerate(self.key):
                if num == i:
                    convert_key += v
        return self._convert_text(convert_key)

    def _convert_text(self, text: str) -> int:
        convert_string = ''
        for i in text:
            if i in LETTERS.keys():
                convert_string += LETTERS.get(i)
        return convert_string

    def reshuffle_text(self, digit_key, text, token_digits):
            reshuffle_string = []
            letter_list = []
            count = 0
            text = str(text)
            while len(text) > 0:
                number = int(text[0])
                letter = text[1:number + 1]
                letter_list += letter.split()
                text = text[number + 1:]
                count += 1
            letters = []
            for i in range(len(letter_list)):
                letters += letter_list[i].split(token_digits[i])
            letters = [x for x in letters if x]    # чистим список
            count_again = 0
            count_again += 1
            for i, j in zip(letters, digit_key):
                reshuffle_string.append(str(int(i) - int(j)))
            return ''.join(reshuffle_string)

    def decode_text(self, text):
        decode_string = ''
        text = str(text)
        if len(text) % 2 == 0:
            decode_string = 'Ошибка при дешифровке'
            return decode_string
        text = [text[i:i + 3] for i in range(0, len(text), 3)]
        for i in text:
            decode_string += str(REVERSE_LETTERS.get(i))
        return decode_string

    def decrypt(self, text, token):
        normal_text = self.decrypt_to_digits(text)
        digit_token, notation, digits = self.split_token(token)

        digit_string = self.convert_to_notation(normal_text, notation)
        digit_key = self.restore_key(digit_token)
        reshuffle = self.reshuffle_text(digit_key, digit_string, digits)
        return f'''
            Расшифрованный текст: {self.decode_text(reshuffle)}
                '''
