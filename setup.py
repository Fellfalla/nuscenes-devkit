#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='nuscenes-devkit',
      version='1.0',
      description='Development Kit for nuScenes dataset',
      author='nuTonomy',
      author_email='nuScenes@nuTonomy.com',
      url='https://www.nuscenes.org/',
      packages=find_packages('python_sdk'),
      package_dir={'':'python_sdk'},   # tell distutils packages are under python_sdk
      install_requires=[
                # 'jupyter==1.0.0',
                # 'matplotlib==2.2.3',
                'numpy==1.14.5',
                'opencv-python==3.4.2.17',
                'Pillow>=5.2.0',
                'pyquaternion>=0.9.2',
                # 'scikit-learn==0.19.2',
                'tqdm>=4.25.0',
      ]
     )


