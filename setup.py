"""
pybitcoin
==============

"""

from setuptools import setup, find_packages

setup(
    name='onename',
    version='0.2.0',
    url='https://github.com/onenameio/onename-python',
    license='MIT',
    author='Halfmoon Labs, Inc.',
    author_email='hello@onename.com',
    description=("Onename API python client"),
    keywords='onename api identity blockchain',
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
        'requests>=2.7.0',
        'pybitcoin>=0.9.1'
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
