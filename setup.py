#from setuptools import setup, find_packages
from setuptools import setup, find_packages
#from typing import list

hypen_e_dot="-e ."
def get_requirements(file_path):
    with open(file_path, 'r') as f:
        requirements=f.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        
        if hypen_e_dot in requirements:
            requirements.remove(hypen_e_dot)
        return requirements



setup(
name='MLPROJECT',
version='0.0.1',
packages=find_packages(),
author='Omkar',
author_email='naik.omkar283@gmail.com',
description='A Machine Learning Project',
install_requires=get_requirements('requirements.txt')
)