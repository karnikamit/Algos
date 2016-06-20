# -*- coding: utf-8 -*-
__author__ = "karnikamit"
from os.path import isfile, join, isdir
from os import listdir
import re
files = []


def im_dir(dir_path):
    for p_file in listdir(dir_path):
        if isfile(join(dir_path, p_file)):
            if p_file != '__init__.py':
                name = im_file(join(dir_path, p_file))
                if name:
                    files.append(name[36:])
        elif isdir(join(dir_path, p_file)):
            im_dir(join(dir_path, p_file))


def im_file(file_path):
    filename = file_path.split('/')[-1]
    ext = filename.split('.')[-1]
    if ext == 'py':
        f_open = open(file_path)
        file_lines = f_open.readlines()
        f_open.close()
        for line in file_lines:
            if re.search(r'\bimport DateTime\b', line) and '#' not in line:
                return file_path
