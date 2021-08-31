from setuptools import setup

__version__ = '0.0.1'

with open("README.md") as f:
    long_description = f.read()

setup(
    name='bridgedbpy',
    version=__version__,
    url='https://github.com/ecell/bridgedbpy',
    license='MIT',
    py_modules=['bridgedbpy'],
    python_requires='>=3.7',
    author='Kozo Nishida',
    author_email='kozo.nishida@gmail.com',
    install_requires=['requests'],
    description='Python wrapper for the BridgeDB webservices',
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=['License :: OSI Approved :: MIT License',]
)
