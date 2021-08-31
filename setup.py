import setuptools

# Nasty but effective way to set __version__
__version__=None
exec(open("bridgedbpy/_version.py").read())

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='bridgedbpy',
    version=__version__,
    author="Kozo Nishida",
    author_email="kozo.nishida@gmail.com",
    maintainer="Kozo Nishida",
    maintainer_email="kozo.nishida@gmail.com",
    description="Code for using BridgeDb identifier mapping framework from within Python",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/kozo2/bridgedbpy',
    license='AGPL-3',
    keywords=['wikipathways', 'bioinformatics'],
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=['requests', 'pandas'],
    classifiers=[
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Mathematics'
    ],
    python_requires='>=3.7',
    test_suite='tests',
)
