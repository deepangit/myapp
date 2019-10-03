
from setuptools import setup, find_packages
from helloworld.core.version import get_version

VERSION = get_version()

f = open('README.md', 'r')
LONG_DESCRIPTION = f.read()
f.close()

setup(
    name='helloworld',
    version=VERSION,
    description='Hello World App using cememt',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='Deepan Chakrvarthy',
    author_email='deepan333@gmail.com',
    url='https://github.com/deepangit/swdp',
    license='unlicensed',
    packages=find_packages(exclude=['ez_setup', 'tests*']),
    package_data={'helloworld': ['templates/*']},
    include_package_data=True,
    entry_points="""
        [console_scripts]
        helloworld = helloworld.main:main
    """,
)
