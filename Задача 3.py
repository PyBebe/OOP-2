with open('1.txt', 'w') as f1:
    f1.write('''Начальник  полиции
лично позвонил в шестнадцатый участок. А спустя  одну минуту тридцать секунд
в дежурке и других комнатах нижнего этажа раздались звонки
     Когда Иенсен  --  комиссар  шестнадцатого  участка --  вышел  из своего
кабинета,  звонки еще  не смолкли. Иенсен был мужчина средних лет,  обычного
сложения, с лицом плоским и невыразительным. На последней ступеньке винтовой
лестницы  он задержался  и  обвел взглядом помещение дежурки. Затем поправил
галстук и проследовал к машине.''')
    
with open('2.txt', 'w') as f2:
    f2.write('Тревога началась в тринадцать часов ноль две минуты.')

with open('3.txt', 'w') as f3:
    f3.write('''     В  это время  дня  машины текли сплошным  блестящим  потоком,  а  среди
потока, будто  колонны из бетона  и стекла, высились  здания. Здесь,  в мире
резких граней,  люди  на тротуарах  выглядели  несчастными и  неприкаянными.
Одеты они были хорошо, но как-то удивительно походили друг на друга и все до
одного спешили. Они шли нестройными  вереницами, широко разливались, завидев
красный  светофор или  металлический  блеск кафе-автоматов.  Они непрестанно
озирались по сторонам и теребили портфели и сумочки.
     Полицейские  машины  с  включенными  сиренами  пробивались  сквозь  эту
толчею.''')


def archivator(file_list):
    file_archive = []
    for file in file_list:
        file_info = {'name':file}
        with open(file, 'r') as f:
            data = f.read()
        file_info['data'] = data
        with open(file, 'r') as f:
            lines_counter = 0
            for index, line in enumerate(f):
                lines_counter += 1
        file_info['lines'] = lines_counter
        file_archive.append(file_info)
    result = sorted(file_archive, key=lambda x: x['lines'])
    return result


def create_new_file(file_name, file_list):
    archive = archivator(file_list)
    with open(file_name, 'w') as f:
        f.write('Сортировка файлов по количеству строк:\n')
    with open(file_name, 'a') as f:
        for text in archive:
            f.write(f'{text["name"]}\n')
            f.write(f'{text["lines"]}\n')
            f.write(f'{text["data"]}\n')
    with open(file_name, 'r') as f:
        data = f.read()
    return data

files = ['1.txt', '2.txt', '3.txt']
new_file = '4.txt'

print(create_new_file(new_file, files))
