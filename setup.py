from setuptools import setup, find_packages
import os

version = '2.2'

setup(name='collective.js.multizoom',
      version=version,
      description="collective.js.multizoom",
      long_description=open("README.rst").read() + "\n" +
                       open("CHANGES.rst").read(),
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='multizoom',
      author='Martronic SA',
      author_email='martronic@martronic.ch',
      url='http://www.dynamicdrive.com/dynamicindex4/featuredzoomer.htm',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective', 'collective.js'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
