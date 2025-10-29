''' 
This file is an essenstial part of packaging and distributing python projexts. 
It is used by setuptools (or distutils in older python versions) to define the configuration of our project
such as its metadata, dependencied and more
'''

from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    '''
    This function will retrun list of requirements
    '''
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt', 'r') as file:
            # read lines from file
            lines = file.readlines()
            # Process each line
            for line in lines:
                requirement = line.strip()
                # Ignore the empty lines and -e .
                if requirement and requirement!= '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print('requirements.txt file is not found') 

    return requirement_lst

print(get_requirements())

setup(
    name="Network Security",
    version="0.0.1",
    author="Yogesh",
    author_email="yogesh050898@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)