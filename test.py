def search_files_by_extension(all_files: list, file_extension: str) -> list[str]:
    result = []
    for file in all_files:
        if file.endswith(file_extension):
            result.append(file)
    return result


