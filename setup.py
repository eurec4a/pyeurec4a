import setuptools
import versioneer


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="eurec4a",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    author="Tobias Kölling",
    author_email="tobias.koelling@mpimet.mpg.de",
    description="common utilities for analysing data from the EUREC4A field campaign",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/eurec4a/pyeurec4a",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
    install_requires=[
        "requests",
        "pyyaml",
        "intake!=0.6.1",  # due to lacking jinja2 dependency
        "aiohttp",  # required by intake to access catalogs via http
    ],
)
