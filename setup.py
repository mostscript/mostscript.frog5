from setuptools import setup, find_packages

version = '0.1.dev0'

setup(
    name='mostscript.frog5',
    version=version,
    description='Policy product for ShrubFrog QI on Plone 5',
    long_description=(
        open('README.rst').read() + '\n' +
        open('CHANGES.rst').read()
        ),
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Plone',
        ],
    keywords='',
    author='Sean Upton',
    author_email='sean@mostscript.com',
    url='http://github.com/mostscript',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['mostscript'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'Products.GenericSetup',
        'plone.app.dexterity',
        'plone.api',
        'collective.teamwork',
        'collective.talkflow',
        'collective.documentviewer',
        'wildcard.media',
        'uu.formlibrary',
        # -*- Extra requirements: -*-
    ],
    extras_require={
        'test': ['plone.app.testing'],
    },
    entry_points='''
    # -*- Entry points: -*-
    [z3c.autoinclude.plugin]
    target = plone
    ''',
    )
