import os
from setuptools import setup

def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()


setup(
    name="auto-ml",
    version="0.0.1",
    author="Takahiro Hagino",
    author_email="haginota@gmail.com",
    description=("Automated Data Preprocessing for Machine Learning.",
                 "Optimized for Pandas DataFrame."),
    license="Apache Software License",
    keywords="automl preprocessing",
    url="https://github.com/haginot/auto-prep",
    packages=['autoprep', 'tests'],
    long_description=read('README.md'),
    classifiers=[]
)
