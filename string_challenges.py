# Вывести последнюю букву в слове
word = 'Архангельск'
print('Вывести последнюю букву в слове - ', word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
print('количество букв "а" в слове - ', word.lower().count('а'))


# Вывести количество гласных букв в слове
word = 'Архангельск'
vowel_letter = 'аеёиоуэюя'

count = 0
for letter in word.lower():
    if letter in vowel_letter:
        count += 1

print('количество гласных букв в слове - ', count)


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print('количество слов в предложении - ', len(sentence.split()))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'

print('Вывести первую букву каждого слова на отдельной строке')
for word in  sentence.split():
    print(word[0])


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'

count_words = len(sentence.split())
sum_char = 0
for word in sentence.split():
    sum_char += len(word)
avg_len_words = sum_char / count_words

print('Вывести усреднённую длину слова в предложении - ', avg_len_words)
