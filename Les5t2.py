#2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

with open('t2.txt', 'r' ) as file_text:
    content = file_text.read()
    content_lines = content.split('\n')
    #print(content_lines)
    print(f'Количество строк: {len(content_lines)}')
    for line in content_lines:
        line_list = line.split(' ')
        print(f'Количество слов в строке {(content_lines.index(line)) +1 }: {len(line_list)}')






