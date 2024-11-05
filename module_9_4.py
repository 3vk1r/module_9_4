from random import choice as ch

class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return ch(self.words)

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        file = open(file_name, 'w', encoding = 'utf-8')
        for words in data_set:
            file.write(str(words))
            file.write('\n')
        file.close()
    return write_everything

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())

first = 'Мама мыла раму'
second = 'Рамена мало было'

print(list(map(lambda x,y: x==y, first, second)))

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])
