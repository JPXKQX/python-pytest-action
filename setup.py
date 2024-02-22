from setuptools import find_packages
from setuptools import setup

setup(
    name="pkg_name",
    description="Testing GitHub action of pytests",
    install_requires=["torch"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.10",
    ],
    packages=find_packages(),
)