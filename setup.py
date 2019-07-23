import os

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('setup/requirements.txt') as f:
    requirements = f.read().splitlines()


setuptools.setup(
    name='nuscenes-devkit',
    version='1.0.0',
    author="Holger Caesar, Oscar Beijbom, Qiang Xu, Varun Bankiti, Alex H. Lang, Sourabh Vora, Venice Erin Liong, "
           "Chris Li, Sergi Widjaja et al.",
    author_email="nuscenes@nutonomy.com",
    description="The official devkit of the nuScenes dataset (www.nuscenes.org).",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nutonomy/nuscenes-devkit",
    python_requires='>=3.5',
    install_requires=requirements,
    packages=['nuscenes', 'nuscenes.eval', 'nuscenes.utils'],
    package_dir={'': 'python-sdk'},
    classifiers=[
        "Programming Language :: Python :: 3.5",
        "Operating System :: OS Independent",
    ],
)


