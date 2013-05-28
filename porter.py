"""Porter: Simple File Operations in Python

* https://github.com/shunfan/porter
* MIT License
* Copyright (c) 2013 Shunfan Du, i@perry.asia

"""
import os
import shutil


__all__ = ['mkdir', 'copy', 'copy_to', 'move', 'move_to', \
          'archive', 'archive_to', 'FileExistsError', \
          'FileNotFoundError', 'FileTypeError']
__version__ = '0.0.5'


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
            shutil.rmtree(directory)
            os.makedirs(directory)
    else:
        os.makedirs(directory)


def copy(src, dst, ignore=False, force=False):
    """
    Copy a file or directory to a future destination.
    Possibilities:
        - copy a file to a future destination.
        - copy a directory to a future destination.
    """
    if not os.path.exists(src) and not ignore:
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
                shutil.rmtree(dst)
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
    if os.path.isfile(src):
        os.remove(src)
    elif os.path.isdir(src):
        shutil.rmtree(src)


def move_to(src, dst, ignore=False, force=False):
    move(src, os.path.join(dst, os.path.basename(src)), ignore, force)


def archive(src, name=None, format='tar'):
    """
    Archive types:
        - gztar: gzip'ed tar-file
        - bztar: bzip2'ed tar-file
        - tar: uncompressed tar file
        - zip: ZIP file
    """
    parent_dir = os.path.abspath(os.path.join(src, os.pardir))
    if not name:
        dst = os.path.join(parent_dir, os.path.basename(src))
    else:
        dst = os.path.join(parent_dir, name)
    try:
        return shutil.make_archive(dst, format, src)
    except OSError:
        raise FileTypeError("'%s' is not directory." % src)


def archive_to(src, dst, name=None, format='tar'):
    move_to(archive(src, name, format), dst)
