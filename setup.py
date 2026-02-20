from setuptools import find_packages, setup
from typing import List


HYPEN_E_DOT = '-e .'
def get_requirements(file_path: str) -> List[str]:
    '''
    return the filtered list of requirements from the provided file
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = [line.strip() for line in file_obj if line.strip()]
    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name = 'mlproject',
    version = '0.0.1',
    author = 'om',
    author_email = 'ombante56@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')

)