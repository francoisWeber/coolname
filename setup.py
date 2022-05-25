from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    long_description=long_description,
    packages=find_packages(),
    version_config=True,
)
