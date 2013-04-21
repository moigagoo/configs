from distutils.core import setup

import configs

setup(
    name=configs.__title__,
    version=configs.__version__,
    author=configs.__author__,
    description='Configuration for humans',
    long_description=open('README.rst').read(),
    author_email='moigagoo@myopera.com',
    url='https://bitbucket.org/moigagoo/configs',
    packages=['configs'],
    package_dir={'configs': 'configs'},
    package_data={'configs': ['*.conf']},
    include_package_data = True,
    license=configs.__license__,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3'])
)
