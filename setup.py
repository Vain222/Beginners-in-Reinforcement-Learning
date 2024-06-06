from setuptools import setup, find_packages

def parse_requirements(filename):
    with open(filename, 'r') as f:
        lines = f.read().splitlines()
    return lines

def readme():
    with open('README.md', 'r') as f:
        return f.read()

setup(
    name='BIRL',
    version='1.0.0',
    description='Beginners-in-Reinforcement-Learning',
    long_description=readme(),
    long_description_content_type='text/markdown',
    author='LHL',
    author_email='2807419248@qq.com',
    packages=find_packages(include=['BIRL.*']),
    package_data={
        '': ['*.py'],
    },
    keywords='timm',
    include_package_data=True,
    url='https://github.com/Vain222/Beginners-in-Reinforcement-Learning.git',
    license='Apache License 2.0',
    install_requires=parse_requirements('requirements.txt'),
    zip_safe=False
)