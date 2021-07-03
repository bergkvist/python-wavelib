from setuptools import setup, Extension
import pybind11

setup(
    name='wavelib',
    version='1.0.1',
    author='Tobias Bergkvist',
    author_email='tobias@bergkv.ist',
    description='Signal processing utilities for Python/Numpy written in C++',
    url='https://github.com/bergkvist/python-wavelib',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: C++'
    ],
    install_requires=['numpy'],
    extras_require={'test': ['pytest']},
    ext_modules=[
        Extension(
            'wavelib',
            ['wavelib.cc'],
            language='c++',
            include_dirs=[pybind11.get_include()]
        )
    ],
)