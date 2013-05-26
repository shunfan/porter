# coding=utf-8
from setuptools import setup, find_packages

from porter import __version__

setup(
    name='porter',
    version=__version__,
    author='Shunfan Du',
    author_email='i@perry.asia',
    description='Porter: Simple File Operations in Python',
    long_description=open('README.rst').read(),
    license='MIT',
    keywords='file directory operation',
    url='https://github.com/shunfan/porter',
    packages=find_packages(),
    include_package_data=True,
    install_requires=open("requirements.txt").readlines(),
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Utilities',
    ],
)
