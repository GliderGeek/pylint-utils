from setuptools import setup, find_packages

exec(open('pylintrc/version.py').read())

setup(
    name='pylintrc',
    version=__version__,
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        pylintrc=pylintrc.pylintrc:pylintrc
    ''',
)
