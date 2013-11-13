from distutils.core import setup
from setuptools import find_packages

setup(
    name='django-extended-sessions',
    version='0.1.0-dev',
    author='Bouke Haarsma',
    author_email='bouke@webatoom.nl',
    packages=find_packages(exclude=('demo', 'tests',)),
    package_data={
        'extended_sessions': ['templates/extended_sessions/*.html'],
    },
    url='http://github.com/Bouke/django-extended-sessions',
    description='Extended sessions for django',
    license='MIT',
    long_description=open('README.rst').read(),
    install_requires=['Django>=1.5'],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Topic :: Security',
    ],
)
