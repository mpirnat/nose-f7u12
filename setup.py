from setuptools import setup

setup(
    name='nose-f7u12',
    version='0.2',

    description='f7u12 output plugin for the nose testing framework',
    long_description=open('./README').read(),
    author='Mike Pirnat',
    author_email='mpirnat@gmail.com',
    license='MIT',
    url='https://github.com/mpirnat/nose-f7u12',

    packages=['f7u12'],
    entry_points={
        'nose.plugins': [
            'f7u12 = f7u12:F7U12',
        ]
    },
    classifiers = [
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python :: 2'
    ],
)
