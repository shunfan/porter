#coding=utf-8
from __future__ import with_statement
import os
import porter


test_porter = 'test_porter'
dir1 = os.path.join(test_porter, 'dir1')
dir2 = os.path.join(test_porter, 'dir2')
dir3 = os.path.join(test_porter, 'dir3')
dir3_dir4 = os.path.join(test_porter, 'dir3', 'dir4')
dir4 = os.path.join(test_porter, 'dir4')
f1 = os.path.join(test_porter, 'dir1', 'f1.txt')
f2 = os.path.join(test_porter, 'dir2', 'f2.txt')
f3 = os.path.join(test_porter, 'dir3', 'f3.txt')

def create(file_path):
    with open(file_path, 'w') as f:
        f.write('test file')


def test_mkdir():
    porter.mkdir(test_porter, force=True)
    porter.mkdir(test_porter, ignore=True)
    porter.mkdir(dir1)
    porter.mkdir(dir2)
    assert os.path.exists(test_porter) == True


def test_copy_file():
    create(f1)
    porter.copy(f1, f2)
    porter.copy(f1, f2, ignore=True)
    porter.copy(f1, f2, force=True)
    porter.copy_to(f1, dir2, ignore=True)
    porter.copy_to(f1, dir2, force=True)
    assert os.path.exists(f1) == True
    assert os.path.exists(f2) == True


def test_copy_directory():
    porter.copy(dir2, dir3)
    porter.copy(dir2, dir3, ignore=True)
    porter.copy(dir2, dir3, force=True)
    porter.copy_to(dir2, dir1)
    porter.copy_to(dir2, dir1, ignore=True)
    porter.copy_to(dir2, dir1, force=True)
    assert os.path.exists(os.path.join(dir1, 'dir2')) == True
    assert os.path.exists(dir2) == True


def test_move_file():
    porter.move(f2, f3)
    porter.move(f2, f3, ignore=True)
    create(f2)
    porter.move(f2, f3, force=True)
    create(f2)
    porter.move_to(f2, dir1)
    porter.move_to(f2, dir1, ignore=True)
    create(f2)
    porter.move_to(f2, dir1, force=True)
    assert os.path.exists(f1) == True
    assert os.path.exists(f2) == False


def test_move_directory():
    porter.move(dir2, dir3_dir4)
    porter.move(dir2, dir3_dir4, ignore=True)
    porter.mkdir(dir2)
    porter.move(dir2, dir3_dir4, force=True)
    porter.move_to(dir3_dir4, test_porter)
    porter.move_to(dir3_dir4, test_porter, ignore=True)
    porter.mkdir(dir3_dir4)
    porter.move_to(dir3_dir4, test_porter, force=True)
    assert os.path.exists(dir3_dir4) == False
    assert os.path.exists(dir4) == True
