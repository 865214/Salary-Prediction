from setuptools import setup, find_packages


def read_requirements(filepath):
    requirements = []
    with open(filepath) as fileobj:
        requirements = fileobj.readlines()
        requirements = [req.replace("\n", " ").strip() for req in requirements]
    return requirements

setup(
    name = "Salary Prediction",
    version = "0.0.1",
    author = "Zoheb Kazi",
    author_email="kazizoheb59@gmail.com",
    packages=find_packages(),
    install_requires=read_requirements("requirements.txt")
)