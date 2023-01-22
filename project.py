import os

os.chdir(r"C:\Users\Aigerim\Desktop\Project")
 
print("Директория изменена")

list_dir =  os.listdir()
print("Список директорий")
for index, i in enumerate(list_dir):
    print(index, i)

f = open('test.txt', )
print(f.read())

print("Текущая деректория:", os.getcwd())

folder_name = input("Для смены директории наберите название папки / ")

try:
    os.chdir(f'C:\\Users\\Aigerim\\Desktop\\Project\\{folder_name}')
    print("Вы перешли на директорию:", os.getcwd())
except FileNotFoundError:
    print("Папка не найдена")

while True:
    command = int(input(
        'Выберите команду:\n 1.Создание папки/файла\n 2.Удаление папки/файла\n 3.Переименование папки/файла\n'
    ))

    if command==1:
        new_folder = input('Введите название папки ')
        os.mkdir(f'{new_folder}')
    elif command==2:
        delete_folder = input('Введите название папки ')
        os.remove(f'{delete_folder}')
    elif command==3:
        rename_folder = input('Введите название папки, которое хотите переименовать ')
        new_name = input('Введите новое название ')
        os.rename(f'{rename_folder}', f'{new_name}')





