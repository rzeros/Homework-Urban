# Домашнее задание по теме "Оператор "with".

class WordsFinder:
    def __init__(self, *file_name):
        self.file_names = list(file_name)

    def get_all_words(self):
        all_words = {}
        punct = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for name in self.file_names:
            with open(name, encoding='utf-8') as file:
                text = file.read().lower()

                for p in punct:
                    text = text.replace(p, '')

                words = text.split()

                all_words[name] = words

        return all_words

    def find(self, word):
        finded = {}
        for keys, items in self.get_all_words().items():
            for i, val in enumerate(items, start=1):
                if val.lower() == word.lower():
                    finded[keys] = i
                    break
        return finded

    def count(self, word):
        counted = {}
        k = 0
        for keys, items in self.get_all_words().items():
            for i in items:
                if i.lower() == word.lower():
                    k += 1
            counted[keys] = k
        return counted

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего