log
===

Pythonic logging with a familiar API


Motivation
----------

Logging in Python has always been unnecessarily hard to approach. The
builtin :code:`logging` module basically follows old Java style
guidelines which has led to a hard-to-read documentation, which in
turn has given us a basic tutorial, an advanced tutorial AND the
'Logging Cookbook'. It is probably the most documented library on
docs.python.org, while still being extremely hard to grasp for a
relatively simple concept.


Installation
------------

log is available on PyPI:

.. code:: bash

    $ pip install --upgrade log


Usage
-----
:code:`log` aims to be easy to approach, highly flexible while still
providing a familiar api for veterans.


Basic
~~~~~

.. code:: python
    >>> import log
    >>> log.info("I\'m a logger!")
    2017-07-02 19:08:58 - __main__ - I\'m a logger!

Simple as that.


Levels
~~~~~~

:code:`log` comes with five functions of different levels like :code:`logging`:

.. code:: python
    log.critical
    log.error
    log.warning
    log.info
    log.debug


Configuration
~~~~~~~~~~~~~

While :code:`log` tries to deliver a desirable config, you might not
be sattisfied. All configuration is placed in the :code:`dict`
:code:`log.config`.

It is recommended to change it like this, because that is how Armin
Ronacher does it:

.. code:: python
    log.config.update(dict(
        print_level='ERROR',
        file=open('log.txt'),
    ))

