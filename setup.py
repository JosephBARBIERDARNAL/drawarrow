from setuptools import setup

setup(
    name="drawarrow",
    version="0.1.0",
    packages=["drawarrow"],
    description="Drawing arrows for matplotlib made easy.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Joseph Barbier",
    author_email="joseph.barbierdarnal@gmail.com",
    url="https://github.com/JosephBARBIERDARNAL/drawarrow/",
    install_requires=["matplotlib"],
)
