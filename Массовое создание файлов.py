for i in range (1, 101):
    file_name = 'Книги/' + str(i) + '.md'
    file = open(file_name, 'w', encoding='utf-8')
    file.write('Новый файл для обсидиан')
    file.close()