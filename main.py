# функція відкриває шляш з файлу
# після чого забирає шлях з яким працюємо
# або пише введіть шлях який записує у файл
# а нашо ваще бавитися зі шляхами якщо можна запускати прогу в папці яку треба відсортувати ?
import re
import os
import shutil

def read_file(filename: str) -> str:
    with open(filename) as file:
        return file.readline()

def write_file(filename: str, path: str) -> None:
    with open(filename, 'w') as file:
        file.write(path)


def search_type_file(all_files: list, endswithtext: str) -> list[str]:
    result = []
    for file in all_files:
        if file.endswith(endswithtext):
            result.append(file)
    return result


def create_dir(type_file: str) -> str:
    if not os.path.isdir(type_file[1:]):
        os.mkdir(type_file[1:])
    return type_file[1:]

def create_dirs(namesdir: list):
    for name in namesdir:
        create_dir(name)


# переміщення 1 файла в 1 категорію
def move_files_category(namesfile: list[str], dir: str) -> None:
    if os.path.exists(dir):
        for name in namesfile:
            if name != 'main.py' and name != 'main.exe' and name != '':
                shutil.move(name, dir)
                print(f'File moved: {name}')

# додати функцію для пошуку форматів файлів ?
def search_types() -> list[str]:
    typeses = []
    all_files = os.listdir()
    for t in all_files:
        filename, file_extension = os.path.splitext(t)
        if file_extension != '':
            typeses.append(file_extension)
    return typeses


def sort_file(type_file: str):
    all_files = os.listdir()
    search = search_type_file(all_files, type_file)
    move_files_category(search, create_dir(type_file))

    # перенести файл в папку txt
    # о тримати назви файлів які рівні *.txt
    # файл по черзі перемістити в папку txt

def sort_files():
    list = search_types()
    for type in list:
        sort_file(type)

# що робити з дублями назф файли різні назви однакові ?
if __name__ == "__main__":
    try:
        # print(read_file('path.txt'))
        # write_file('text.txt', 'тут шлях')
        # print(os.listdir())

        sort_files()
    except Exception as exc:
        print(exc)
