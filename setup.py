from setuptools import setup, find_packages

exec(open('pylintconfig/version.py').read())

with open('readme.md', 'r') as f:
    readme = f.read()

setup(
    name='pylintconfig',
    version=__version__,
    packages=find_packages(),
    long_description=readme,
    long_description_content_type='text/markdown',
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        pylintconfig=pylintconfig.pylintconfig:pylintconfig
    ''',
)
