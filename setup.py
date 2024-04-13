from setuptools import setup, find_packages

setup(
    name='Oulipo Variations',
    version='0.0.1',
    packages=find_packages(),
    url='https://github.com/kaizengrowth/oulipo_package',
    author='Kaitlin Cort',
    author_email='kaitlin.zhang@owasp.org',
    description='Test python library with 4 functions to generate variations of Oulipo text transformer logic',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        'pandas',
        'spacy>=3.0'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.7',
)
