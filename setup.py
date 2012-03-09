from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='collective.memberdatatables',
      version=version,
      description="Override current Plone screens that manage users to use datatables",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='plone datatables member',
      author='JeanMichel FRANCOIS',
      author_email='toutpt@gmail.com',
      url='https://github.com/collective/collective.memberdatatables',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'collective.js.datatables',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
