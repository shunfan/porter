#coding=utf-8
from __future__ import with_statement
import os

from porter import mkdir, copy, copy_to, move, move_to, FileExistsError, FileNotFoundError
from pytest import raises


test_porter = 'test_porter'
dir_mkdir = os.path.join(test_porter, 'dir_mkdir')
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
    mkdir(test_porter, force=True)
    mkdir(dir1)
    mkdir(dir2)
    create(dir1_f1)
    create(dir2_f2)


def test_mkdir():
    init()
    mkdir(dir_mkdir)
    mkdir(dir_mkdir, ignore=True)
    mkdir(dir_mkdir, force=True)
    assert os.path.exists(dir_mkdir) == True


def test_copy():
    init()
    copy(dir1_f1, dir2_f1)
    copy(dir1_f1, dir2_f1, ignore=True)
    copy(dir1_f1, dir2_f1, force=True)
    assert os.path.exists(dir1_f1) == True
    assert os.path.exists(dir2_f1) == True
    copy(dir1, dir2_dir1)
    copy(dir1, dir2_dir1, ignore=True)
    copy(dir1, dir2_dir1, force=True)
    assert os.path.exists(dir1) == True
    assert os.path.exists(dir2_dir1) == True


def test_copy_to():
    init()
    copy_to(dir1_f1, dir2)
    copy_to(dir1_f1, dir2, ignore=True)
    copy_to(dir1_f1, dir2, force=True)
    assert os.path.exists(dir1_f1) == True
    assert os.path.exists(dir2_f1) == True
    copy_to(dir1, dir2)
    copy_to(dir1, dir2, ignore=True)
    copy_to(dir1, dir2, force=True)
    assert os.path.exists(dir1) == True
    assert os.path.exists(dir2_dir1) == True


def test_move():
    init()
    move(dir1_f1, dir2_f1)
    move(dir1_f1, dir2_f1, ignore=True)
    create(dir1_f1)
    move(dir1_f1, dir2_f1, force=True)
    assert os.path.exists(dir1_f1) == False
    assert os.path.exists(dir2_f1) == True
    move(dir1, dir2_dir1)
    move(dir1, dir2_dir1, ignore=True)
    mkdir(dir1)
    move(dir1, dir2_dir1, force=True)
    assert os.path.exists(dir1) == False
    assert os.path.exists(dir2_dir1) == True


def test_move_to():
    init()
    move_to(dir1_f1, dir2)
    move_to(dir1_f1, dir2, ignore=True)
    create(dir1_f1)
    move_to(dir1_f1, dir2, force=True)
    assert os.path.exists(dir1_f1) == False
    assert os.path.exists(dir2_f1) == True
    move_to(dir1, dir2)
    move_to(dir1, dir2, ignore=True)
    mkdir(dir1)
    move_to(dir1, dir2, force=True)
    assert os.path.exists(dir1) == False
    assert os.path.exists(dir2_dir1) == True


def test_FileExistsError():
    init()
    with raises(FileExistsError):
        mkdir(test_porter)


def test_FileNotFoundError():
    init()
    with raises(FileNotFoundError):
        move('none', 'none')
