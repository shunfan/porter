#coding=utf-8
from __future__ import with_statement
import os
import porter


test_porter = 'test_porter'
mkdir = os.path.join(test_porter, 'test_mkdir')
dir1 = os.path.join(test_porter, 'dir1')
dir2 = os.path.join(test_porter, 'dir2')
dir2_dir1 = os.path.join(test_porter, 'dir2', 'dir1')
dir1_f1 = os.path.join(test_porter, 'dir1', 'f1.txt')
dir2_f1 = os.path.join(test_porter, 'dir2', 'f1.txt')
dir2_f2 = os.path.join(test_porter, 'dir2', 'f2.txt')

def create(file_path):
    with open(file_path, 'w') as f:
        f.write('test file')

def init():
    porter.mkdir(test_porter, force=True)
    porter.mkdir(dir1)
    porter.mkdir(dir2)
    create(dir1_f1)
    create(dir2_f2)


def test_mkdir():
    init()
    porter.mkdir(mkdir)
    porter.mkdir(mkdir, ignore=True)
    porter.mkdir(mkdir, force=True)
    assert os.path.exists(mkdir) == True


def test_copy():
    init()
    porter.copy(dir1_f1, dir2_f1)
    porter.copy(dir1_f1, dir2_f1, ignore=True)
    porter.copy(dir1_f1, dir2_f1, force=True)
    assert os.path.exists(dir1_f1) == True
    assert os.path.exists(dir2_f1) == True
    porter.copy(dir1, dir2_dir1)
    porter.copy(dir1, dir2_dir1, ignore=True)
    porter.copy(dir1, dir2_dir1, force=True)
    assert os.path.exists(dir1) == True
    assert os.path.exists(dir2_dir1) == True


def test_copy_to():
    init()
    porter.copy_to(dir1_f1, dir2)
    porter.copy_to(dir1_f1, dir2, ignore=True)
    porter.copy_to(dir1_f1, dir2, force=True)
    assert os.path.exists(dir1_f1) == True
    assert os.path.exists(dir2_f1) == True
    porter.copy_to(dir1, dir2)
    porter.copy_to(dir1, dir2, ignore=True)
    porter.copy_to(dir1, dir2, force=True)
    assert os.path.exists(dir1) == True
    assert os.path.exists(dir2_dir1) == True


def test_move():
    init()
    porter.move(dir1_f1, dir2_f1)
    porter.move(dir1_f1, dir2_f1, ignore=True)
    create(dir1_f1)
    porter.move(dir1_f1, dir2_f1, force=True)
    assert os.path.exists(dir1_f1) == False
    assert os.path.exists(dir2_f1) == True
    porter.move(dir1, dir2_dir1)
    porter.move(dir1, dir2_dir1, ignore=True)
    porter.mkdir(dir1)
    porter.move(dir1, dir2_dir1, force=True)
    assert os.path.exists(dir1) == False
    assert os.path.exists(dir2_dir1) == True


def test_move_to():
    init()
    porter.move_to(dir1_f1, dir2)
    porter.move_to(dir1_f1, dir2, ignore=True)
    create(dir1_f1)
    porter.move_to(dir1_f1, dir2, force=True)
    assert os.path.exists(dir1_f1) == False
    assert os.path.exists(dir2_f1) == True
    porter.move_to(dir1, dir2)
    porter.move_to(dir1, dir2, ignore=True)
    porter.mkdir(dir1)
    porter.move_to(dir1, dir2, force=True)
    assert os.path.exists(dir1) == False
    assert os.path.exists(dir2_dir1) == True
