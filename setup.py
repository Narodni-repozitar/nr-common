# -*- coding: utf-8 -*-


"""NUSL common data types"""

import os

from setuptools import find_packages, setup

readme = open('README.md').read()

tests_require = [
    'pytest',
    'pytest-cov',
    'oarepo[tests]'
]

extras_require = {
    'docs': [
        'Sphinx>=1.5.1',
    ],
    'tests': tests_require,
    'all': []
}

for reqs in extras_require.values():
    extras_require['all'].extend(reqs)

setup_requires = [
    'pytest-runner>=2.6.2',
]

install_requires = [
    'pycountry>=19.0.0',
    'arrow',
    'isbnlib>=3.10.3,<4.0.0',
    'python-stdnum>=1.14, <2.0',
    'IDUtils>=1.1.8, <2.0.0',
    'oarepo-invenio-model>=2.0.0, <3.0.0',
    'oarepo-multilingual>=2.0.0, <3.0.0',
    'oarepo-taxonomies>=2.5.0, <3.0.0'
]

packages = find_packages()

# Get the version string. Cannot be done with import!
g = {}
with open(os.path.join('invenio_nusl_common', 'version.py'), 'rt') as fp:
    exec(fp.read(), g)
    version = g['__version__']

setup(
    name='invenio-nusl-common',
    version=version,
    description=__doc__,
    long_description=readme,
    keywords='NUSL Invenio',
    license='MIT',
    author='Daniel Kopecký',
    author_email='Daniel.Kopecky@techlib.cz',
    url='',
    packages=packages,
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    entry_points={
        'invenio_jsonschemas.schemas': [
            'invenio_nusl_common = invenio_nusl_common.jsonschemas'
        ],
        'invenio_pidstore.minters': [
            'nusl = invenio_nusl_common.minters:nusl_id_minter',
        ],
        'invenio_pidstore.fetchers': [
            'nusl = invenio_nusl_common.fetchers:nusl_id_fetcher',
        ],
        'invenio_db.alembic': [
            'nusl = invenio_nusl_common:alembic',
        ],
        "oarepo_mapping_includes": [
            "invenio_nusl_common = invenio_nusl_common.mapping_includes"
        ]
    },
    extras_require=extras_require,
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Development Status :: 3 - Planning',
    ],
)
