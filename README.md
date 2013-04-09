*********************************
configs: Configuration for Humans
*********************************

Parsing INI-format configurations with the standard library configparser is painful.

**configs** provides an easy and clean API for configuration file parsing.

It supports values without section, automatically converts numeric values, automatically handles sections with listed values as lists.

Configurations are easy as they should be in Python!

Requirements
============

python3

Installation
============

    pip install configs

Usage
=====

    import configs

    conf = configs.load('sample.conf')

    print(conf['root'])     #Items with no section specified

    print(conf['general']['qwe'])

    print(conf)             #Prints all sections

    for i in conf['list']:  #Sections are iterable
        print(i * 2)        #Numeric values are automatically converted

    for i in conf['general']: #Key-value sections are iterable, too!
        print(i)

    for i in conf['mixed']: #Even mixed sections are iterable: lists first, dicts next
        print(i)
