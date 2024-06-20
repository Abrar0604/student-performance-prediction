from setuptools import find_packages, setup
from typing import List

H = "-e ."
def get_requirements(file_path: str) -> List[str]:
    # This function will return a list of requirements
    requirements = []
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.strip() for req in requirements]
        if H in requirements:
            requirements.remove(H)
    return requirements

setup(
    name='student-performance',
    version='0.0.1',
    author="Abrar",
    author_email="abrar2004myself@gmail.com",
    packages=find_packages()
)