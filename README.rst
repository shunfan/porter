Porter
------

.. image:: https://travis-ci.org/shunfan/porter.png?branch=master
    :target: https://travis-ci.org/shunfan/porter

.. image:: https://coveralls.io/repos/shunfan/porter/badge.png?branch=master
    :target: https://coveralls.io/r/shunfan/porter?branch=master

Porter provides simple file operations.

License
-------

MIT.

Installation
------------

Using pip::

    pip install porter

File management
---------------

Import porter::

    import porter

Create a folder::

    porter.mkdir('/foo/bar')
    # The new directory 'bar' will be created.

Rename a file/directory::

    porter.rename('/foo/bar.txt', 'file.txt')
    >>> '/foo/file.txt'

    porter.rename('/foo/bar', 'folder')
    >>> '/foo/folder'

Remove a file/directory::

    porter.remove('/foo/bar')

Copy a file/directory::

    # Two ways same result
    porter.copy('/foo/bar.txt', '/foo1/bar.txt')
    porter.copy_to('/foo/bar.txt', '/foo1')

Move a file/directory::

    # Two ways same result
    porter.move('/foo/bar', '/foo1/bar')
    >>> '/foo1/bar'

    porter.move_to('/foo/bar', '/foo1')
    >>> '/foo1/bar'

Ignore and force::

    porter.mkdir('/foo/bar', ignore=True)
    # If '/foo/bar' exists, porter will not create the folder and no error will occur.
    # Ignore option can ONLY ignore the error of the existing destination file/directory.

    porter.move('/foo/bar', '/foo1/bar', force=True)
    # If '/foo1/bar' exists, porter will move the directory anyway.

Ignore and force are both available in 'mkdir', 'copy', 'copy_to', 'move', 'move_to' functions.

Archive::

    porter.archive('/foo/bar')
    >>> '/foo/bar.tar'

    porter.archive('/foo/bar', 'archive', 'zip')
    >>> '/foo/archive.zip'

    porter.archive_to('/foo/bar', '/foo/bar1', 'archive')
    >>> '/foo/bar1/archive.tar'

All supported archive types: 'gztar', 'bztar', 'tar', 'zip'

class ``TargetFile``::

    bar = porter.TargetFile('/foo/bar.txt')

    bar.src
    >>> '/foo/bar.txt'

    bar.name
    >>> 'bar'

    bar.ext
    >>> 'txt'

    bar.move_to('foo1')

    bar.src
    >>> '/foo1/bar.txt'

    bar.remove()
    # Then it will be removed.

class ``TargetDirectory``::

    """
    The structure of the directory:
    - foo
      - bar
        - dir1
          - f1.txt
        - dir2
          - f2.txt
    - foo1
    """

    bar = porter.TargetDirectory('/foo/bar')

    bar.src
    >>> '/foo/bar'

    bar.list()
    >>> {'dir1': {'f1.txt': None}, 'dir2': {'f2.txt': None}}

    bar.files()
    >>> ['f1.txt', 'f2.txt']

    bar.directories()
    >>> ['dir1', 'dir2']

    bar.move_to('foo1')

    bar.src
    >>> '/foo1/bar'

    bar.empty()
    # All of the files in it will be removed

    bar.remove()
    # Then it will be removed.
