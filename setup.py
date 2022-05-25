from setuptools import setup, find_packages

setup(
    name='flowcytopy',
    version='0.0.1',
    packages=find_packages(include=['flowcytopy', 'flowcytopy.*']),
    url='',
    install_requires=['pacmap', 'trimap', 'anndata'],
    license='',
    author='Ergün Tiryaki',
    author_email='erguntiryaki27@gmail.com',
    description='A package for alternative visualizations and analyses of cytometry data in python environment.'
)
