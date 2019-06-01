from setuptools import setup, find_packages

setup(
    name='ordered_hash',
    version='0.0.1',
    description="Ordered Hash/Dictionary",
    author='Wael Farhan',
    author_email='wael34218@gmail.com',

    classifiers=[
        'Development Status :: Alpha',
        'Environment :: Console',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
    ],
    keywords='hash dictionary ordered_hash ordered_dictionary',
    packages=['ordered_hash'],
    install_requires=[],
    test_suite='nose2.collector.collector',
    extras_require={
        'test': ['nose2'],
    },
    include_package_data=True,
)
