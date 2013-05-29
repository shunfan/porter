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

    porter.mkdir('/foo/bar') # The directory 'bar' will be created within empty file.

Remove a file/directory::

    porter.remove('/foo/bar')

Copy a file/directory::

    # Two ways same result
    porter.copy('/foo/bar.txt', '/foo1/bar.txt')
    porter.copy_to('/foo/bar.txt', '/foo1')

Move a file/directory::

    # Two ways same result
    porter.move('/foo/bar', '/foo1/bar')
    porter.move_to('/foo/bar', '/foo1')

Ignore and force::

    porter.mkdir('/foo/bar', ignore=Ture) # If '/foo/bar' exists, porter will not create the folder and no error will occur.
    porter.move('/foo/bar', '/foo1/bar', force=True) # If '/foo1/bar' exists, porter will move the directory anyway.

Ignore and force are both available in 'mkdir', 'copy', 'copy_to', 'move', 'move_to' functions.

Archive::

    porter.archive('/foo/bar') # retrun the archive .tar file '/foo/bar.tar'
    porter.archive('/foo/bar', 'archive', 'zip') # return the archive file '/foo/archive.zip'
    porter.archive_to('/foo/bar', '/foo/bar1', 'archive') # return '/foo/bar1/archive.tar'

All supported archive types: 'gztar', 'bztar', 'tar', 'zip'
