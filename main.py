# потрібно додати візуал і захист від дибіла


import os
import shutil


def search_files_by_extension(all_files: list, file_extension: str) -> list[str]:
    result = []
    for file in all_files:
        if file.endswith(file_extension):
            result.append(file)
    return result


def create_dir(file_extension: str, input_path: str) -> str:
    if not os.path.isdir(f'{input_path}\\{file_extension[1:]}'):
        os.mkdir(f'{input_path}\\{file_extension[1:]}')
    return file_extension[1:]


def move_files_category(list_of_files: list[str], folder: str, input_path: str) -> None:
    if os.path.exists(f'{input_path}\\{folder}'):
        for one_file in list_of_files:
            if one_file != 'main.py' and one_file != 'main.exe' and one_file != '':
                shutil.move(f'{input_path}\\{one_file}', f'{input_path}\\{folder}')
                print(f'File moved: {one_file}')


def search_file_extensions(input_path: str) -> list[str]:
    file_extension_list = []
    all_files = os.listdir(input_path)
    for t in all_files:
        filename, file_extension = os.path.splitext(f'{input_path}\\{t}')
        if file_extension != '':
            file_extension_list.append(file_extension)
    return file_extension_list


def sort_file(extension: str, input_path: str):
    all_files = os.listdir(input_path)
    move_files_category(search_files_by_extension(all_files, extension), create_dir(extension, input_path), input_path)


def sort_files(input_path: str):
    list_extensions = search_file_extensions(input_path)
    for file_extension in list_extensions:
        sort_file(file_extension, input_path)


# що робити з дублями назф файли різні назви однакові ?
if __name__ == "__main__":
    try:
        input_user_path = input('Please enter the full path to the folder: ')
        if os.path.exists(input_user_path):
            sort_files(input_user_path)
        else:
            print('Folder not found try again please!')

    except Exception as exc:
        print(exc)
