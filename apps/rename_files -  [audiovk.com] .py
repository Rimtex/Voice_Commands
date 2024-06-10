import os

def rename_files_in_directory(directory, substring_to_remove):
    # Получаем список файлов в указанной директории
    files = os.listdir(directory)
    
    for filename in files:
        # Проверяем, содержится ли подстрока в имени файла
        if substring_to_remove in filename:
            # Создаем новое имя, удаляя подстроку
            new_filename = filename.replace(substring_to_remove, "")
            # Получаем полный путь старого и нового файла
            old_file_path = os.path.join(directory, filename)
            new_file_path = os.path.join(directory, new_filename)
            # Переименовываем файл
            os.rename(old_file_path, new_file_path)
            print(f'Renamed: {filename} -> {new_filename}')

# Задаем путь к папке и подстроку для удаления
directory_path = "E:\Muzic\Trance Best"
substring_to_remove = " [audiovk.com]"

# Переименовываем файлы
rename_files_in_directory(directory_path, substring_to_remove)
