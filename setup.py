from setuptools import setup, find_packages


setup(name='nocd',
      version='0.1.0',
      description='Community detection with GNNs',
      author='Oleksandr Shchur',
      author_email='shchur@in.tum.de',
      packages=find_packages('.'),
      zip_safe=False)
