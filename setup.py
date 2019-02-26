from setuptools import find_packages, setup

setup(
    name='django-crispy-bulma',
    version='0.1.2',
    description='Django application to add \'django-crispy-forms\' layout objects for Bulma.io',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author='Python Discord',
    author_email='staff@pythondiscord.com',
    url='https://github.com/python-discord/django-crispy-bulma',
    license='MIT',
    packages=find_packages(),
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 2.0",
        "Framework :: Django :: 2.1",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=[
        'Django>=2.0',
        'django-crispy-forms==1.7.2'
    ],
    extras_require={
        "dev": [
            "flake8",
            "flake8-bugbear",
            "flake8-import-order",
            "flake8-tidy-imports",
            "flake8-todo",
            "flake8-string-format",
            "pdoc",
            "pre-commit",
            "PyGithub",
            "wheel",
        ]
    },
    include_package_data=True,
    zip_safe=False
)
