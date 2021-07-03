from setuptools import setup
try:
    from pybind11.setup_helpers import Pybind11Extension
except:
    from setuptools import Extension as Pybind11Extension

setup(
    name='wavelib',
    version='1.0.3',
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
    install_requires=['numpy', 'pybind11'],
    extras_require={'test': ['pytest']},
    ext_modules=[Pybind11Extension('wavelib', ['wavelib.cc'])],
)