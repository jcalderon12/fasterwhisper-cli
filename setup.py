from setuptools import setup, find_packages

# Read the contents of requirements.txt

def read_requirements_file():
    # opens requirements.txt and returns a List 
    # of str with the content of each line.
    # It is called on the install_requires argument of setup()
    pass


setup(
    name="fasterwhisper-cli",
    version="0.1.0",
    packages=find_packages(),
    install_requires=read_requirements_file(),
    entry_points={
        "console_scripts": [
            "fasterwhisper-cli=fasterwhisper_cli.main:main",
        ],
    },
    author="Jorge Calderon Gonzalez", 
    author_email="jcaldg00@estudiantes.unileon.es",
    description="A CLI tool for transcribing audio using faster-whisper",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
)

