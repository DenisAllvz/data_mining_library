from setuptools import setup, find_packages

setup(
    name='data-mining-library',
    version='0.1.0',
    author='Daniel Duarte, Denilson Alves, Tiago Lima',
    author_email= 'denilsonideal@gmail.com',
    description='A library for data mining and analysis',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'matplotlib',
        'scikit-learn',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)