import os

import setuptools


own_dir = os.path.abspath(os.path.dirname(__file__))


def readme():
    with open(os.path.join(own_dir, 'README.md')) as f:
        for line in f.readlines():
            line = line.strip()
            yield line


setuptools.setup(
    name='dacite_ignore_case',
    version='0.0.2',
    description='Extends dacite.from_dict with a ignore case function',
    author='zkdev',
    author_email='dev@zeekay.dev',
    long_description = readme(),
    long_description_content_type = 'text/markdown',
    project_urls={
        'Bug Tracker': 'https://github.com/zkdev/dacite-ignore-case/issues',
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[
       'dacite',
    ],
    license='MIT',
    python_requires='>=3.9.*',
    package_dir={'': 'dacite_ignore_case'},
    packages=setuptools.find_packages(where='dacite_ignore_case'),
)
