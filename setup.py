from setuptools import setup, find_packages

setup(
    name='sphinxcontrib-text-styles',
    version='0.1.0',
    description='Sphinx extension for custom text formatting roles',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Martin Priestley',
    author_email='martin@rainlabs.ai',
    url='https://github.com/RainUKLabs/sphinxcontrib-text-styles',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'sphinx>=3.0',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Sphinx :: Extension',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    keywords='sphinx extension formatting documentation',
    python_requires='>=3.7',
    entry_points={
        'sphinx.extensions': [
            'sphinxcontrib_text_styles = sphinxcontrib_text_styles.formatting:setup',
        ],
    },
)
