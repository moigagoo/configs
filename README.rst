*********************************
Configs: Configuration for Humans
*********************************

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

``Configs`` work with Python 2.7+ (including 3).

The repo is at `github.com/moigagoo/configs <https://github.com/moigagoo/configs>`_.

Read the full documentation at `configs.rtfd.org <http://configs.rtfd.org>`_.

.. image::  figs.jpg
    :align: center
    :width: 200


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
Load a config file::

    >>> import configs
    >>> c = configs.load('sample.conf')
    >>> c['general']
    {'foo': 'baz'}


Tests
=====

Run the tests with:

.. code-block:: bash

    $ python test_configs.py
