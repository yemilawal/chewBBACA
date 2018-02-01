try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import chewBBACA

setup(
  name = 'chewBBACA',
  packages = ['chewBBACA'],
  version = '2.0',
  description = 'A complete suite for gene-by-gene schema creation and strain identification',
  author = 'Mickael Silva, João Carriço',
  author_email = 'mickaelsilva@medicina.ulisboa.pt, jcarrico@medicina.ulisboa.pt',
  url = 'https://github.com/B-UMMI/chewBBACA', 
  download_url = 'https://github.com/B-UMMI/chewBBACA/archive/v2.0_pypi.tar.gz', 
  keywords = ['cgMLST', 'bacterial typing'],
  classifiers = ['Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'],
  install_requires=['numpy>=1.13.1','scipy>=0.13.3','biopython>=1.70','plotly>=1.12.9','SPARQLWrapper>=1.8.0'],
)