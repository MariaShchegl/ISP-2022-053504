text=''' Весь сад в дожде. Весь дождь в саду.Погибнут дождь и сад друг в друге,
оставив мне решать судьбу зимы,явившейся на юге. '''

def text_clear(txt):
    import string
    for p in string.punctuation + '\n':
        if p in txt:
            txt = txt.replace(p, '')
    return txt

def counter_words(list_word):
    count = {}
    for element in list_word:
        if count.get(element, None):
            count[element] += 1
        else:
            count[element] = 1

    sorted_values = sorted(count.items(), key=lambda n: n[1], reverse=True)
    return dict(sorted_values)

def avarage_num_word(txt):
    text = txt.replace('?', '.').replace('!', '.').replace('...', '.')
    l = text.split(' ')
    c = text.count('.')
    print(f"Среднее количество слов в предложении {len(l)/c}")


def median(your_dictionary):
    m = None
    common_words = 0
    for i in set(your_dictionary.values()):
        m = list(your_dictionary.values()).count(i)
        if m > common_words:
            common_words = m
            m = i
    print(f"Медианное количество равно: {m} и встречается {common_words} раз в тексте")


def top_k(your_dictionary):
    
    
    quastion=input("хотите поменять параметры k и n y/n?")
    if quastion=="y":
        k=int(input("Введите k "))
        n=int(input("Введите n "))
    else:
        k=10
        n=4    

    i=0  
    while k > 0 and i <= len(list(your_dictionary.values())) - 1:
        i += 1
        check = list(your_dictionary.keys())[-i]
        if len(check) != n:
            continue
        else:
            print(list(your_dictionary.values())[-i], " - ", list(your_dictionary.keys())[-i])
            k -= 1
    return your_dictionary
        

# среднее количество слов в текте
avarage_num_word(text)

#преобразование текста в список
txt = text_clear(text.lower())
list_word = txt.split()

#преобразование текста в словарь и вывод количества слов
print(counter_words(list_word))
my_dictionary=counter_words(list_word)


# медианное количество слов в предложении
median(my_dictionary)

# топ k
top_k(my_dictionary)