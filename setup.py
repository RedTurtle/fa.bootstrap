from setuptools import setup, find_packages
import os

version = '0.1'

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = (
    read('README.txt')
    + '\n' +
    read('CHANGES.txt'))

setup(name='fa.bootstrap',
      version=version,
      description="pyramid_formalchemy twitter bootstrap integration",
      long_description=long_description,
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='pyramid pyramid_formalchemy twitter bootstrap redturtle',
      author='RedTurtle Developers',
      author_email='svilplone@redturtle.it',
      url='https://github.com/RedTurtle/fa.bootstrap',
      license='GPL',
      packages=find_packages(),
      namespace_packages=['fa'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'js.bootstrap',
          ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
