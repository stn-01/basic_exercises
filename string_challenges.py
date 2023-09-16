# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
print(word.count('а'))


# Вывести количество гласных букв в слове
word = 'Архангельск'
counter = 0
for char in word:
    if char.lower() in 'аеиоуэюя':
        counter += 1
print(counter)


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split(' ')))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
for word in sentence.split(' '):
    print(word[0])


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
print(len(sentence) // (len(sentence.split(' '))))