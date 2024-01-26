from setuptools import setup, find_packages
from NCL import model

model.test_funk(2)

setup(
    name='nonparametricCausality',  # Replace with your package's name
    version='0.1',  # Replace with your package's version
    packages=find_packages(),
    #license='LICENSE',  # Replace with your license
    author='Asger Bak Morville',  # Replace with your name
    author_email='asgermorville@gmail.com',  # Replace with your email
    description='A Causal Inference library for nonparametric methods',  # Replace with a short description
    #long_description=open('README.md').read(),  # Include a long description from a README file
    #long_description_content_type='text/markdown',
    install_requires=[
        # List your project's dependencies here.
        # They will be installed by pip when your project is installed.
        # Example: 'requests >= 2.20.0'
    ],
    classifiers=[
        # Choose classifiers to describe your project.
        # See https://pypi.org/classifiers/ for a list of valid classifiers.
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Specify which version of Python your software requires.
)