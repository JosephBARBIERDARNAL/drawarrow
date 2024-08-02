from setuptools import setup, find_packages

setup(
    name="drawarrow",
    version="0.0.2",
    packages=find_packages(),
    description="Drawing arrows for matplotlib made easy.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Joseph Barbier",
    author_email="joseph.barbierdarnal@gmail.com",
    url="https://github.com/JosephBARBIERDARNAL/drawarrow/blob/main/README.md",
    install_requires=["matplotlib"],
)
