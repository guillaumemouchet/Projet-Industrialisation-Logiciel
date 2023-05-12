from setuptools import setup

setup(
    name="EzPwd Front",
    version="0.1.5", # TODO Change manually
    description="password address with flask",
    long_description=open("README.md").read(),
    author="benjamin.mouchet, guillaume.mouchet",
    package_dir={"EzPwd_front": "."},
    install_requires=open("Projet/requirements.txt").readlines(),
)


