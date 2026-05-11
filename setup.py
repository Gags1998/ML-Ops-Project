from setuptools import setup, find_packages 
from typing import List

def get_requirements() -> List[str]:
    requirements_list = []
    try:
        with open('requirements.txt') as f:
            lines = f.readlines()
            for line in lines:
                requirements=line.strip()
                if requirements !='-e .' and not requirements.startswith('-r'):
                    requirements_list.append(requirements)
    except FileNotFoundError:
        print("Error: requirements.txt not found")
    return requirements_list
        
setup(
    name='Network_Security',
    version='0.0.1',
    packages=find_packages(),
    install_requires=get_requirements(),
    description='A package for Network Security project',
    author='Gagan N',
    author_email='gagan.kishan98@gmail.com'
    )