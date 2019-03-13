from setuptools import setup, find_packages


with open('README.md', 'r') as f:
    long_description = f.read()


setup(
    name='jhTAlib',
    version='20190313.0',
    author='Joost Hoeks',
    author_email='joosthoeks@gmail.com',
    description='Technical Analysis Library Time-Series',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/joosthoeks/jhTAlib',
    packages=find_packages(),
    classifiers=[
    'Programming Language :: Python :: 3',
    'License :: OSI Approved :: GNU General Public Licence v3',
    'Operating System :: OS Independent',
    ],
)

