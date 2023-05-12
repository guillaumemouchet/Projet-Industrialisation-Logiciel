from setuptools import setup

setup(
    name="EzPwd Back",
    version="0.1.6", # TODO Change manually
    description="password address with flask",
    long_description=open("README.md").read(),
    author="benjamin.mouchet, guillaume.mouchet",
    package_dir={"EzPwd_Back": "Projet/logger/."},
    install_requires=open("Projet/logger/requirements.txt").readlines(),
)


