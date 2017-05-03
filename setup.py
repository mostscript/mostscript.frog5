from setuptools import setup, find_packages

version = '0.1.dev0'

setup(
    name='upiq.qits',
    version=version,
    description='Policy product for QI TeamSpace on Plone 5',
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
    author_email='sean.upton@hsc.utah.edu',
    url='http://github.com/upiq',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['upiq'],
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

