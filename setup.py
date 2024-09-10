from setuptools import setup, find_packages

setup(
    name='raksha_logger', 
    version='1.0.1',
    description='A custom logger with colored log levels and caller file information',
    author='Raksha',
    author_email='rakshakarnofficial@gmail.com',
    packages=['raksha_logger'],
    package_dir={'raksha_logger': 'raksha_logger'},
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)