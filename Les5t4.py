#4. Создать (не программно) текстовый файл со следующим содержимым:
#One — 1
#Two — 2
#Three — 3
#Four — 4
#Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
#При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться
#в новый текстовый файл.

en_rus_dict = {
    'One' : 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}

with open('text4.txt', 'r') as source:
    engl_v = {}

    for line in source:
        line_list = line.split(' ')
        line_list = [str.rstrip() for str in line_list]
        print(line)

        engl_v[line_list[0]] = line_list[2]

    print(engl_v)

    rus_v = {}
    rus_v = {en_rus_dict[key]: engl_v[key] for key in en_rus_dict}

with open('text4_new.txt', 'w') as input:
    for key, val in rus_v.items():
        input.write('{}:{}\n'.format(key, val))


    #for item in rus_v.items():
        #for val in rus_v.values():
            #for value in engl_v.values():
                #new_val = value
                #val = new_val

    #print(rus_v)


#with open('text4_new.txt', 'w') as input:
    #new_dict = {}
    #for key, val in new_dict.items():
        #for key2, val2 in engl_v.items():
            #for key3, val3 in en_rus_dict.items():
                #key = en_rus_dict(key3)
                #val = engl_v[key2]
                #new_dict[key] = val
                #item = f'{key} - {val}'
                #print(item)
                #input.write(item)

#with open('text4_new.txt', 'w') as input:



    #def translate():
        #item_list = []
        #for val2 in engl_v.values():
            #for val3 in en_rus_dict.values():
                #item = str(f'{val3} - {val2}')
                #item_list = item_list.append(item)
        #return item_list

    #input.write(translate())
