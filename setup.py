from setuptools import setup, find_packages

VERSION = '1.0.0' 
DESCRIPTION = "This Python package, 'python_errorhandler', simplifies error handling in your code. You no longer need to write try-catch blocks for every function. Instead, you can import this package and use the included decorator with your functions.\
    The decorator allows you to specify a custom error message for better error handling and debugging."

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
        name="python_errorhandler", 
        version=VERSION,
        author="Nimesh Prajapati",
        author_email="prajapatin953@gmail.com",
        description=DESCRIPTION,
        long_description=long_description,
        long_description_content_type='text/markdown',
        packages=['python_errorhandler'],
        install_requires=[
        "Django",  
        "djangorestframework",
    ],
)