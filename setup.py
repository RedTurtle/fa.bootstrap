from setuptools import setup, find_packages
import os

version = '0.3'

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
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
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
          'pyramid_formalchemy>=0.4.2dev',
          'fa.jquery',
          'js.jquery_tablesorter',
          'js.bootstrap>=1.4',
          'WebOb',
          ],
      entry_points="""
      [fanstatic.libraries]
      fa_bootstrap = fa.bootstrap.fanstatic_resources:fa_bootstrap_library
      [paste.paster_create_template]
      pyramid_fa_bootstrap = fa.bootstrap.scaffolds:PyramidFormAlchemyBootstrapTemplate
      """
      )
