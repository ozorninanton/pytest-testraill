from setuptools import setup


def read_file(fname):
    with open(fname) as f:
        return f.read()


setup(
    name='pytest-testraill',
    description='pytest plugin for creating TestRail runs and adding results',
    long_description=read_file('README.rst'),
    version='0.0.1',
    author='Anton Ozornin',
    author_email='ozorninanton@mail.ru',
    url='https://github.com/ozorninanton/pytest-testraill',
    packages=[
        'pytest_testrail',
    ],
    package_dir={'pytest_testraill': 'pytest_testraill'},
    install_requires=[
        'pytest>=3.6',
        'requests>=2.20.0',
    ],
    include_package_data=True,
    entry_points={'pytest11': ['pytest-testraill = pytest_testrail.conftest']},
)
