from setuptools import setup, find_packages

with open('README.rst', encoding='UTF-8') as f:
    readme = f.read()

setup(
    name='hr',
    version='0.1.0',
    description='Unknown but looks like an hr project',
    long_description=readme,
    author='Raminder Singh',
    author_email='raminderis@live.com',
    install_requires=[],
    packages=find_packages('src'),
    package_dir={'': 'src'}
)
