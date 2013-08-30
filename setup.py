# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages
from version import get_version

version = get_version()

setup(name='gs.skin.blue',
    version=version,
    description="Blue GroupServer skin.",
    long_description=open("README.txt").read() + "\n" +
                      open(os.path.join("docs", "HISTORY.txt")).read(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        "Environment :: Web Environment",
        "Framework :: Zope2",
        "Intended Audience :: Developers",
        'License :: OSI Approved :: Zope Public License',
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux"
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
      ],
    keywords='skin groupserver blue css',
    author='Michael JasonSmith',
    author_email='mpj17@onlinegroups.net',
    url='http://www.onlinegroups.net/',
    license='ZPL 2.1',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['gs', 'gs.skin'],
    include_package_data=True,
    zip_safe=True,
    install_requires=[
        'setuptools',
        'zope.app.rotterdam',
        'zope.browserresource',
        'zope.publisher',
        'gs.content.css',  # We depend on the core CSS
    ],
    entry_points="""
    # -*- Entry points: -*-
    """,)
