# 1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
# |--my_project
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp
# Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?);
# как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена
# папок под конкретный проект; можно ли будет при этом расширять конфигурацию и хранить данные
# о вложенных папках и файлах (добавлять детали)?

import os
from os import path, getcwd, makedirs

main_create_dir = 'my_project'
create_dir = ['settings', 'mainapp', 'adminapp', 'authapp']
work_dir = getcwd()
print(work_dir)
chek_work_dir = path.exists(work_dir)
w_path = path.join(main_create_dir)
if not path.exists(w_path):
    makedirs(w_path)
for dir in create_dir:
    w_path_dir = path.join(main_create_dir, dir)
    if not path.exists(w_path_dir):
        makedirs(w_path_dir)

