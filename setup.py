from setuptools import setup, find_packages
from setuptools.extension import Extension

sources = [
    'src/common.c',
    'src/rdrand.c',
    'src/main.c'
]

extra_args = [
    '-mrdrnd'
]

module = Extension('_rdrand',
                   sources=sources,
                   extra_compile_args=extra_args)

setup(
    name="rdrand",
    version="1.3",
    description="Intel® - Digital Random Number Generator (DRNG) [Bull Mountain] interface for Python.",
    author="Murilo Augusto",
    ext_modules=[module],
    packages=find_packages(),
)

