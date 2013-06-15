"""Porter: Simple File Operations in Python

* https://github.com/shunfan/porter
* MIT License
* Copyright (c) 2013 Shunfan Du, i@perry.asia

"""
import os
import shutil


__all__ = ['TargetFile', 'TargetDirectory', 'mkdir', 'rename', 'remove', \
           'copy', 'copy_to', 'move', 'move_to', 'archive', 'archive_to', \
           'FileExistsError', 'FileNotFoundError', 'FileTypeError']
__version__ = '0.1.0'


class TargetFile(object):
    def __init__(self, src):
        if not os.path.isfile(src):
            raise FileTypeError("'%s' is not a file." % src)
        self._src = src

    @property
    def src(self):
        return self._src

    def move_to(self, dst, ignore=False, force=False):
        move_to(self.src, dst, ignore, force)
        self._src = os.path.join(dst, os.path.basename(self.src))

    def remove(self):
        remove(self.src)


class TargetDirectory(object):
    def __init__(self, src):
        if not os.path.isdir(src):
            raise FileTypeError("'%s' is not a directory." % src)
        self._src = src

    @property
    def src(self):
        return self._src

    @property
    def branch(self):
        branch = []
        for f in os.listdir(self.src):
            path = os.path.join(self.src, f)
            if os.path.isfile(path):
                f = TargetFile(path)
            elif os.path.isdir(path):
                f = TargetDirectory(path)
            branch.append(f)
        return branch

    def list(self):
        structure = {}
        for branch in self.branch:
            if isinstance(branch, TargetFile):
                structure[os.path.basename(branch.src)] = None
            elif isinstance(branch, TargetDirectory):
                structure[os.path.basename(branch.src)] = branch.list()
        return structure

    def move_to(self, dst, ignore=False, force=False):
        move_to(self.src, dst, ignore, force)
        self._src = os.path.join(dst, os.path.basename(self.src))

    def empty(self):
        remove(self.src)
        mkdir(self.src)

    def remove(self):
        remove(self.src)


class FileExistsError(EnvironmentError):
    pass


class FileNotFoundError(EnvironmentError):
    pass


class FileTypeError(EnvironmentError):
    pass


def mkdir(directory, ignore=False, force=False):
    """
    Create a directory.
    """
    if os.path.exists(directory):
        if not ignore and not force:
            try:
                os.makedirs(directory)
            except OSError:
                raise FileExistsError("'%s' is exist." % directory)
        elif force:
            remove(directory)
            os.makedirs(directory)
    else:
        os.makedirs(directory)


def rename(src, name, ignore=False, force=False):
    """
    Rename a file or a directory
    """
    parent_dir = os.path.abspath(os.path.join(src, os.pardir))
    return move(src, os.path.join(parent_dir, name), ignore, force)


def remove(src):
    """
    Remove a file or a directory.
    """
    if os.path.isfile(src):
        os.remove(src)
    elif os.path.isdir(src):
        shutil.rmtree(src)


def copy(src, dst, ignore=False, force=False):
    """
    Copy a file or directory to a future destination.
    Possibilities:
        - copy a file to a future destination.
        - copy a directory to a future destination.
    """
    if not os.path.exists(src):
        raise FileNotFoundError("'%s' is not found." % src)

    if os.path.isfile(src):
        if os.path.exists(dst):
            if not ignore and not force:
                raise FileExistsError("'%s' is exist." % dst)
            elif force:
                shutil.copyfile(src, dst)
        else:
            shutil.copyfile(src, dst)
    elif os.path.isdir(src):
        if os.path.exists(dst):
            if not ignore and not force:
                try:
                    shutil.copytree(src, dst)
                except OSError:
                    raise FileExistsError("'%s' is exist." % dst)
            elif force:
                remove(dst)
                shutil.copytree(src, dst)
        else:
            shutil.copytree(src, dst)


def copy_to(src, dst, ignore=False, force=False):
    copy(src, os.path.join(dst, os.path.basename(src)), ignore, force)


def move(src, dst, ignore=False, force=False):
    """
    Move a file or directory to a future destination.
    Possibilities:
        - move a file to a future destination.
        - move a directory to a future destination.
    """
    copy(src, dst, ignore, force)
    remove(src)
    return dst


def move_to(src, dst, ignore=False, force=False):
    return move(src, os.path.join(dst, os.path.basename(src)), ignore, force)


def archive(src, name=None, format='tar'):
    """
    Archive types:
        - gztar: gzip'ed tar-file
        - bztar: bzip2'ed tar-file
        - tar: uncompressed tar file
        - zip: ZIP file
    Warning:
        - Archive will overwrite file with the same name forcely
    """
    parent_dir = os.path.abspath(os.path.join(src, os.pardir))
    if not name:
        dst = os.path.join(parent_dir, os.path.basename(src))
    else:
        dst = os.path.join(parent_dir, name)
    try:
        return shutil.make_archive(dst, format, src)
    except OSError:
        raise FileTypeError("'%s' is not a directory." % src)


def archive_to(src, dst, name=None, format='tar'):
    return move_to(archive(src, name, format), dst)
