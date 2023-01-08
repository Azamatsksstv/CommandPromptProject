import os

# начальная директория с диска E:/ можно поменять на диск C
pathway = ["E:/"]
url_pathway = "".join(pathway)
os.chdir(url_pathway)

while True:
    action = input("choose action (dir, cd , cd.. , mkdir , rmdir, rename, open, 0): ")
    # print(action)
    if action == "0":
        break

    #  команду “dir” для показа всех существующих директорий в находящейся папке
    elif action == "dir":
        for i in os.listdir():
            print(i)

    # переход между директориями
    elif action == "cd":
        try:
            dir_url = input("Dir name: ")  # вводится директория для перехода
            if len(pathway) > 1:
                dir_url = "/" + dir_url
            pathway.append(dir_url)
            url_pathway = "".join(pathway)
            os.chdir(url_pathway)
        except Exception:
            print("Не найдена директория")

    # переход назад в директории
    elif action == "cd..":
        pathway = pathway[:-1]
        url_pathway = "".join(pathway)
        os.chdir(url_pathway)

    # создание папки
    elif action == "mkdir":  # вводится имя папки для создания
        name_of_dir = input("Dir name: ")
        os.mkdir(name_of_dir)

    # удаление папки
    elif action == "rmdir":
        name_of_dir = input("Dir name: ")  # вводится имя папки для удаления
        os.rmdir(name_of_dir)

    # переименование папки
    elif action == "rename":
        name_of_dir = input("Dir name: ")  # вводится имя папки для переименования
        new_name_of_dir = input("New Dir name: ")  # вводится новое имя папки для переименования
        os.rename(name_of_dir, new_name_of_dir)

    #  просмотр файлов как .txt, .md
    elif action == "open":
        name_of_file = input("File name: ")  # вводится имя файла для просмотра
        try:
            file = open(name_of_file)
            print(file.read())
            file.close()
        except Exception:
            print("incorrect file name")

