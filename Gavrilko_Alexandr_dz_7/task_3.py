# 3. Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
# Написать скрипт, который собирает все шаблоны в одну папку templates, например:
# |--my_project
#    ...
#   |--templates
#    |   |--mainapp
#    |   |  |--base.html
#    |   |  |--index.html
#    |   |--authapp
#    |      |--base.html
#    |      |--index.html
# Примечание: исходные файлы необходимо оставить; обратите внимание,
# что html-файлы расположены в родительских папках (они играют роль пространств имён);
# предусмотреть возможные исключительные ситуации; это реальная задача, которая решена, например,
# во фреймворке django.


from os import path, getcwd, makedirs, walk
from shutil import copy, SameFileError

main_create_dir = 'my_project'
template_dir = 'templates'
create_dir = ['settings', 'mainapp', 'adminapp', 'authapp']
files = ['base.html', 'detail.html']
work_dir = getcwd()
chek_work_dir = path.exists(work_dir)
w_path = path.join(main_create_dir)
if not path.exists(w_path):
    makedirs(w_path)
    print(f'Create {w_path} - ok')
for dir in create_dir:
    w_path_dir = path.join(main_create_dir, dir)
    if not path.exists(w_path_dir):
        makedirs(w_path_dir)
        print(f'Create {w_path_dir} - ok')
        dir_file = path.join(work_dir, main_create_dir, dir)
        for file in files:
            if dir == 'mainapp' or dir == 'authapp':
                dir_files = path.join(dir_file, file)
                with open(dir_files, 'w', encoding='utf-8') as f:
                    print(f'{main_create_dir}/{dir}/{file} - ok')

template_path = path.join(work_dir, main_create_dir, template_dir)
if not path.exists(template_path):
    makedirs(template_path)
    print(f'Create {main_create_dir}/{template_dir}/ - ok')
for root, dirs, files in walk(path.join(work_dir, main_create_dir)):
    if files:
        dir_name = root.split('/')[-1]
        dir = path.join(template_path, dir_name)
        if not path.exists(dir):
            makedirs(dir)
            print(f'Create {main_create_dir}/{template_dir}/{dir_name} - ok')
        for file in files:
            try:
                copy(path.join(root, file), dir)
            except SameFileError:
                print(f'Directory - {dir.split("/")[-2]} not copy')
                continue
            print(f'Create file {  dir_name}/{file} copy - ok')
print(f'My collectstatic - finish!')


