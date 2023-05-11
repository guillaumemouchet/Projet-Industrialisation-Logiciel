from setuptools import setup

setup(
    name="EzPwd",
    version="0.1.6", # TODO Change manually
    description="password address with flask",
    long_description=open("README.md").read(),
    author="benjamin.mouchet, guillaume.mouchet",
    package_dir={"EzPwd": "."},
    install_requires=open("Projet/requirements.txt").readlines(),
)


