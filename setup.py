from setuptools import setup, find_packages

from pfood import meta

with open("README.md", "r") as readme:
    long_description = readme.read()

setup(
    name=meta.name,
    version=meta.version,
    author=meta.author,
    author_email=meta.email,
    description=meta.description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SamadiPour/foods",
    packages=find_packages(),
    package_data={
        "": ["../*.txt"],
    },
    entry_points={
        "console_scripts": ["pfood = pfood.__main__:main"],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Environment :: Console",
    ],
)
