import os
from setuptools import setup

def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()


setup(
    name="autoprep",
    version="0.0.1",
    author="Hagino Takahiro",
    author_email="haginota@gmail.com",
    description=("Automated Data Pre-processing for Machine Learning.",
                 "Optimized for Pandas DataFrame."),
    license="Apache Software License",
    keywords="automl preprocessing",
    url="https://github.com/haginot/auto-prep",
    packages=['autoprep'],
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
    classifiers=[]
)
