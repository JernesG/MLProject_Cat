from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    """
    This function is used to install the required libs
    """
    requirements = []
    with open(file_path) as obj_file:
        requirements = obj_file.readlines()
        requirements = [req.replace("\n"," ") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='MLproject_Cat',
    version='0.0.1',
    author= 'Jernes',
    author_email= 'jernes2000@gmail.com',
    packages= find_packages(),
    install_requirements = get_requirements('requirements.txt')
)