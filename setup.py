"""This is the setup file for the ML project. 
It is used to install the necessary dependencies and package the project."""

from typing import List
from setuptools import setup, find_packages

HYPHEN_DOT_E = '-e .'
def get_requirements(file_path:str) -> List[str]:
    """This function will return the list of requirements"""
    requirements= []
    with open(file_path, 'r', encoding='utf-8') as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        if HYPHEN_DOT_E in requirements:
            requirements.remove(HYPHEN_DOT_E)
    return requirements

setup(
    name="mlproject",
    version="1.0.0",
    author="Arghajit",
    author_email="reddevil20@zohomail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    description="A machine learning project setup",
    )
