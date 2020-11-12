from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    readme = fh.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name="problems",
    version="0.0.1",
    py_modules=["problems"],
    description="Palindromes and Bishops problems",
    url="https://github.com/carlosjimz87/pyrepo.git",
    author="Carlos Jimenez",
    author_email="carlosjimz87@gmail.com",
    packages=find_packages(),
    python_requires='>=3.6',
    long_description=readme,
    long_description_content_type="text/markdown",
    license=license,
    tests_require=['pytest'],
    classifiers=[
        "Programming Language :: Python :: 3.0",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    extras_require={
        "dev": [
            "pytest>=3.7",
        ],
    },


)
