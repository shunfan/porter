#coding=utf-8
from __future__ import with_statement
import os

from porter import TargetFile, mkdir, rename, remove, copy, copy_to, \
                   move, move_to, archive, archive_to, FileExistsError, \
                   FileNotFoundError, FileTypeError
from pytest import raises


test_porter = 'test_porter'
dir_mkdir = os.path.join(test_porter, 'dir_mkdir')
dir1 = os.path.join(test_porter, 'dir1')
dir1_tar = os.path.join(test_porter, 'dir1.tar')
dir1_archive_tar = os.path.join(test_porter, 'archive.tar')
dir2 = os.path.join(test_porter, 'dir2')
dir2_dir1_tar = os.path.join(test_porter, 'dir2', 'dir1.tar')
dir2_archive_tar = os.path.join(test_porter, 'dir2', 'archive.tar')
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


class TestTargetFile:
    def test_init(self):
        init()
        target_file = TargetFile(dir1_f1)
        assert isinstance(target_file, TargetFile) == True

    def test_move_to(self):
        init()
        target_file = TargetFile(dir1_f1)
        target_file.move_to(dir2)
        assert os.path.exists(dir1_f1) == False
        assert os.path.exists(dir2_f1) == True
        assert target_file.src == dir2_f1

    def test_remove(self):
        init()
        target_file = TargetFile(dir1_f1)
        target_file.remove()
        assert os.path.exists(dir1_f1) == False


class TestRename:
    def test_file(self):
        init()
        rename(dir2_f2, 'f1.txt')
        assert os.path.exists(dir2_f2) == False
        assert os.path.exists(dir2_f1) == True

    def test_directory(self):
        init()
        rename(dir1, dir2, force=True)
        assert os.path.exists(dir1) == False
        assert os.path.exists(dir2) == True


class TestRemove:
    def test_file(self):
        init()
        remove(dir1_f1)
        assert os.path.exists(dir1_f1) == False

    def test_directory(self):
        init()
        remove(dir1)
        assert os.path.exists(dir1) == False


class TestCopy:
    def test_file(self):
        init()
        copy(dir1_f1, dir2_f1)
        copy(dir1_f1, dir2_f1, ignore=True)
        copy(dir1_f1, dir2_f1, force=True)
        assert os.path.exists(dir1_f1) == True
        assert os.path.exists(dir2_f1) == True

    def test_directory(self):
        init()
        copy(dir1, dir2_dir1)
        copy(dir1, dir2_dir1, ignore=True)
        copy(dir1, dir2_dir1, force=True)
        assert os.path.exists(dir1) == True
        assert os.path.exists(dir2_dir1) == True


class TestCopyTo:
    def test_file(self):
        init()
        copy_to(dir1_f1, dir2)
        copy_to(dir1_f1, dir2, ignore=True)
        copy_to(dir1_f1, dir2, force=True)
        assert os.path.exists(dir1_f1) == True
        assert os.path.exists(dir2_f1) == True

    def test_directory(self):
        init()
        copy_to(dir1, dir2)
        copy_to(dir1, dir2, ignore=True)
        copy_to(dir1, dir2, force=True)
        assert os.path.exists(dir1) == True
        assert os.path.exists(dir2_dir1) == True


class TestMove:
    def test_file(self):
        init()
        move(dir1_f1, dir2_f1)
        move(dir1_f1, dir2_f1, ignore=True)
        create(dir1_f1)
        move(dir1_f1, dir2_f1, force=True)
        assert os.path.exists(dir1_f1) == False
        assert os.path.exists(dir2_f1) == True

    def test_directory(self):
        init()
        move(dir1, dir2_dir1)
        move(dir1, dir2_dir1, ignore=True)
        mkdir(dir1)
        move(dir1, dir2_dir1, force=True)
        assert os.path.exists(dir1) == False
        assert os.path.exists(dir2_dir1) == True


class TestMoveTo:
    def test_file(self):
        init()
        move_to(dir1_f1, dir2)
        move_to(dir1_f1, dir2, ignore=True)
        create(dir1_f1)
        move_to(dir1_f1, dir2, force=True)
        assert os.path.exists(dir1_f1) == False
        assert os.path.exists(dir2_f1) == True
    def test_directory(self):
        init()
        move_to(dir1, dir2)
        move_to(dir1, dir2, ignore=True)
        mkdir(dir1)
        move_to(dir1, dir2, force=True)
        assert os.path.exists(dir1) == False
        assert os.path.exists(dir2_dir1) == True


class TestArchive:
    def test_directory(self):
        init()
        archive(dir1)
        archive(dir1, 'archive')
        assert os.path.exists(dir1) == True
        assert os.path.exists(dir1_tar) == True
        assert os.path.exists(dir1_archive_tar) == True


class TestArchiveTo:
    def test_directory(self):
        init()
        archive_to(dir1, dir2)
        archive_to(dir1, dir2, 'archive')
        assert os.path.exists(dir1) == True
        assert os.path.exists(dir2_dir1_tar) == True
        assert os.path.exists(dir2_archive_tar) == True


class TestError:
    def test_FileExistsError(self):
        init()
        with raises(FileExistsError):
            mkdir(test_porter)
        init()
        with raises(FileExistsError):
            copy(dir1_f1, dir2_f2)
        init()
        with raises(FileExistsError):
            copy(dir1, dir2)

    def test_FileNotFoundError(self):
        init()
        with raises(FileNotFoundError):
            move('none', 'none')

    def test_FileTypeError(self):
        init()
        with raises(FileTypeError):
            archive(dir1_f1)
