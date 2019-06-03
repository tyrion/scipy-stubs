from setuptools import setup
import glob
import os


def find_stubs(package):
    BASE_PATH = os.path.dirname(__file__)
    CWD = os.getcwd()
    try:
        os.chdir(os.path.join(BASE_PATH, package))
        return {package: glob.glob("**/*.pyi", recursive=True)}
    finally:
        os.chdir(CWD)


setup(
    name="scipy-stubs",
    maintainer="Germano Gabbianelli",
    maintainer_email="gemano.gabbianelli@contentwise.tv",
    description="PEP 561 type stubs for scipy",
    url="https://www.scipy.org/",
    version="2019.4.0",
    packages=["scipy-stubs"],
    install_requires=["scipy"],
    package_data=find_stubs("scipy-stubs"),
)
