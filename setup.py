from setuptools import setup, find_packages

setup(
    name='crispy-forms-bulma',
    version='1.1.4',
    description='Django application to add \'django-crispy-forms\' layout objects for Bulma.io',
    long_description=open('README.md').read(),
    author='Jure Hotujec',
    author_email='jure.hotujec@gmail.com',
    url='http://pypi.python.org/pypi/crispy-forms-bulma',
    license='MIT',
    packages=find_packages(),
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 1.8",
        "Framework :: Django :: 1.9",
        "Framework :: Django :: 1.10",
        "Framework :: Django :: 1.11",
        "Framework :: Django :: 2.0",
        "Framework :: Django :: 2.1",
        "Framework :: Django :: 2.11",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=[
        'Django>=1.8',
        'django-crispy-forms >= 1.6.1'
    ],
    include_package_data=True,
    zip_safe=False
)
