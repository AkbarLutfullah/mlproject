from setuptools import find_packages, setup
from typing import List

# use of this constant runs setup.py automatically once change in requirements.txt
HYPHEN_E_DOT = "-e ."


def get_requirements(file_path: str) -> List[str]:
    """
    returns list of requirements
    :param file_path: path to requirements.txt
    :return: list of current requirements
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author='Akbar',
    author_email='akbar.lutfullah@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
