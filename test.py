#coding=utf-8
from __future__ import with_statement
import os
import porter


test_porter = 'test_porter'
dir1 = os.path.join(test_porter, 'dir1')
dir2 = os.path.join(test_porter, 'dir2')
f1 = os.path.join(test_porter, 'dir1', 'f1.txt')
f2 = os.path.join(test_porter, 'dir2', 'f2.txt')

def create(file_path):
    with open(file_path, 'w') as f:
        f.write('test file')


def test_mkdir():
    porter.mkdir(test_porter, force=True) # Force
    porter.mkdir(test_porter, ignore=True) # Ignore
    porter.mkdir(dir1)
    porter.mkdir(dir2)
    assert os.path.exists(test_porter) == True


def test_copy_file():
    create(f1)
    porter.copy(f1, f2)
    porter.copy(f1, f2, ignore=True) # Ignore
    porter.copy_to(f1, dir2, force=True) # Force
    assert os.path.exists(f1) == True
    assert os.path.exists(f2) == True


def test_copy_directory():
    porter.copy(dir2, dir1, ignore=True) # Ignore
    porter.copy_to(dir2, dir1, force=True) # Force
    assert os.path.exists(os.path.join(dir1, 'dir2')) == True
    assert os.path.exists(dir2) == True


def test_move_file():
    porter.move(f2, f1, ignore=True)
    porter.move_to(f2, dir1, force=True)
    assert os.path.exists(f1) == True
    assert os.path.exists(f2) == False


def test_move_directory():
    porter.move(os.path.join(dir1, 'dir2'), dir2, force=True)
    porter.move_to(os.path.join(dir1, 'dir2'), test_porter, force=True)
    assert os.path.exists(os.path.join(dir1, 'dir2')) == False
    assert os.path.exists(os.path.join(dir2)) == True
