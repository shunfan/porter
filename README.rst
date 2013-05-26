Porter
------

Porter is a simple file operations in Python.

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

Copy a file/directory::

    # Two ways same result
    porter.copy('/foo/bar.txt', '/foo1/bar.txt')
    porter.copy_to('/foo/bar.txt', '/foo1')

Move a file/directory::

    # Two ways same result
    porter.move('/foo/bar', '/foo1/bar')
    porter.move_to('/foo/bar', '/foo1')

Ignore and force::

    porter.mkdir('/foo/bar', ignore=Ture) # If '/foo/bar' exists, porter will not create the folder and no error will occur
    porter.move('/foo/bar', '/foo1/bar', force=True) # If '/foo1/bar' exists, porter will remove the former directory first, then start to move the directory

Ignore and force are both available in 'mkdir', 'copy', 'copy_to', 'move', 'move_to' functions.
