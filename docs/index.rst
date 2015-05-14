*********************************
Configs: Configuration for Humans
*********************************

.. toctree::
    :maxdepth: 2
    :hidden:

    apidocs/index

.. image:: https://pypip.in/v/configs/badge.png
    :target: https://pypi.python.org/pypi/configs/
    :alt: Latest Version

.. image:: https://pypip.in/d/configs/badge.png
    :target: https://pypi.python.org/pypi/configs/
    :alt: Downloads

.. image:: https://pypip.in/wheel/configs/badge.png
    :target: https://pypi.python.org/pypi/configs/
    :alt: Wheel Status

Parsing INI configs must be easy, as are the INI files.

**Configs** provides a simple API for getting data from INI config files.

Loading data from a config is as easy as ``configs.load('my.conf')``.

``Configs`` work with Python 2.7+ and 3.

The repo is at `bitbucket.org/moigagoo/configs <https://bitbucket.org/moigagoo/configs>`_.

Features
========

*   Root-level params support
*   Numeric and boolean values are converted automatically
*   Sections with only key-value items are parsed as dicts
*   Sections with only flag items (keys with no value) are parsed as lists
*   Mixed content sections are parsed as tuples of a dict and a list, which can be accessed individually
*   Sections are iterable (even the mixed ones; list first, dict second)
*   Comments support

Installation
============

Install configs with pip:

.. code-block:: bash

    $ pip install configs

Usage
=====

.. sidebar:: Note

    In order to support URL values (e.g. ``http://example.com``), colons cannot be used as the assignment sign. Use only the equal sign: **=**.

    This will fail::

        wrong_assignment: wrong_value

    This will work::

        pretty = nice

Sample config file (``sample.conf``):

.. literalinclude:: ../configs/sample.conf

Load the file::

    >>> import configs

    >>> c = configs.load('sample.conf')

Get all values::

    >>> c
    {'list_section': [7.1, 42, ('foo', 123)], 'root': {'path': 'some_path', 'hosts': ('example.com', 'http://bing.com', 'ssh.com:23', 'www.qwe.asd')}, 'mixed': (['flag'], {'boolean': False, 'prop': 'val', 'list': (12.3, 'eggs')})}
Get root section::

    >>> c['root']
    {'path': 'some_path', 'hosts': ('example.com', 'http://bing.com', 'ssh.com:23', 'www.qwe.asd')}

Get individial value::

    >>> c['root']['path']
    some_path

You can omit `[root]`::

    >>> c['path']
    some_path

List section values are accesses by index::

    >>> c['list_section'][1]
    42

Numeric values are parsed as numbers::

    >>> c['list_section'][1] + 3
    45

    >>> c['list_section'][0] * 2
    14.2

Iterate over a section::

    >>> for key in c['root']:
        print(key, c['root'][key])
    path some_path
    hosts ('example.com', 'http://bing.com', 'ssh.com:23', 'www.qwe.asd')

    >>> for value in c['list_section']:
        print(value)
    7.1
    42

    >>> for mix in c['mixed']:
        print(mix)
    flag
    prop

    >>> c['mixed'].dict_props
    {'prop': 'val'}

    >>> c['mixed'].list_props
    flag

Fallback Config
---------------

.. deprecated:: 3.0.1

.. note::

	Fallback support was removed because it was used about 0 times.

.. versionadded:: 1.4

It is possible to define a fallback configuration when loading a config.

If the loaded config does not have some values defined in the fallback config, the default values will be used.

Fallback config file (``default.conf``):

.. literalinclude:: ../configs/default.conf

Use the optional ``fallback_file`` parameter of the :func:`load <configs.api.load>` method::

    >>> fc = configs.load('sample.conf', fallback_file='default.conf')

    >>> fc
    {'list_section': [1, 2.2, 3, 7.1, 42], 'new_section': {'new_key': 'new_value'}, 'root': {'url': 'http://example.com', 'top_level': 'value', 'path': 'some_path'}, 'general': {'spam': 'eggs', 'foo': 'baz'}, 'mixed': (['flag'], {'prop': 'val'})}

    >>> fc['general']['spam']
    eggs

The `defaults` Dict
-------------------

.. deprecated:: 3.0.1

.. warning::

	This functionality was buggy and unstable. Also, real life proved it (as well as the fallback file support) quite unnecessary.

.. versionadded:: 2.0.5

You can pass a dict of default values to be loaded into the `root` section in the `defaults` param of the :func:`load <configs.api.load>` method::

    >> dc = configs.load('sample.conf', defaults={'defaul_key': 'default_value'})

    >>> dc
    {'list_section': [1, 2.2, 3, 7.1, 42], 'new_section': {'new_key': 'new_value'}, 'root': {'url': 'http://example.com', 'top_level': 'value', 'path': 'some_path', 'defaul_key': 'default_value'}, 'general': {'spam': 'eggs', 'foo': 'baz'}, 'mixed': (['flag'], {'prop': 'val'})}

    >>> fc['defaul_key']
    default_value

.. versionadded:: 2.0.1

Boolean values are converted automatically.

Use the special ``True`` and ``False`` values to declare boolean type (case matters!)::

    this_is_a_boolean_value = True
    this_is_a_string = true
    this_is_a_number = 1

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
