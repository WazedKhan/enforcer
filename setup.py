from setuptools import setup, find_packages

setup(
    name="src",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    python_requires=">=3.7",
    description="A lightweight decorator for enforcing type hints at runtime.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/WazedKhan/enforcer",
    author="Wajed Khan",
    author_email="wajed.abdul.khan@gamil.com",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
