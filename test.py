def search_files_by_extension(all_files: list, file_extension: str) -> list[str]:
    result = []
    for file in all_files:
        if file.endswith(file_extension):
            result.append(file)
    return result
import os

if os.path.exists("D:\Загальне\вайберс\png\91.png"):
    print('its File true')

import datetime

datetime_now = datetime.datetime.now().strftime("%Y_%m_%d_%H-%M-%S")
print(datetime_now)