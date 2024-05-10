from setuptools import setup, find_packages

setup(
    name="PubChem_Prospector",
    version="0.1",
    packages=find_packages(),
    description="functions for bulk scraping pubchem annotations",
    author="demontrees",
    author_email="demontrees96@gmail.com",
    url="https://github.com/demontrees/PubChem_Prospector",
    install_requires=[
        'urllib3>=1.26.16'
    ]
)