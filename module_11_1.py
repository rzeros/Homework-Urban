import requests as rqs
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup

# Использование библиотеки Requests (для работы с HTTP-запросами),
# BeautifulSoup4 (для парсинга):

url = 'https://www.python.org/about/gettingstarted/'
response = rqs.get(url)
print(response.headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    section = soup.find('section', class_='main-content with-left-sidebar')

    if section:
        for hd in section.find_all(['h1', 'h2', 'h3', 'p']):
            print(hd.get_text(separator=' ', strip=True))
    else:
        print('Ничего не найдено')

# Использование библиотеки Matplotlib для визуализации данных

x1 = [14, 19, 36, 54, 58]
y1 = [60, 20, 91, 59, 32]

x2 = ['Белая', 'Уфа', 'Инзер', 'Нугуш']
y2 = [690, 312, 253, 530]

plt.subplot(1, 2, 1)
plt.plot(x1, y1, color='purple', marker='o', markersize=9)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('1')

plt.subplot(1, 2, 2)
plt.bar(x2, y2, label='Уровень реки')
plt.xlabel('Название реки')
plt.ylabel('СМ.')
plt.title('2')
plt.legend()

plt.tight_layout()
plt.show()