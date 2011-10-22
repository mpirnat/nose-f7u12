from setuptools import setup

setup(
    name='nose-f7u12',
    version='0.1',
    download_url='TBD',

    description='f7u12 output plugin for the nose testing framework',
    author='Mike Pirnat',
    author_email='mpirnat@gmail.com',
    license='MIT',

    url='TBD',

    long_description="""
Implements PEP712 for the Nose testing framework; after 7 failing tests,
replaces all 'F' character output with 'U's for the remainder of the test run.
See
http://www.revsys.com/blog/2011/oct/20/pep712-proposal-make-unittest2-more-accurate/
""",
    packages=['nose-f7u12'],
    entry_points={
        'nose.plugins': [
            'f7u12 = f7u12:F7U12',
        ]
    }
)