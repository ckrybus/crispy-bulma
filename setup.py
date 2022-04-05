#!/usr/bin/env python

from setuptools import find_packages, setup

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = ["Django>=2.2", "django-crispy-forms>=1.9.0"]
test_requirements = [
    "pytest>=3",
]

setup(
    name="crispy-bulma",
    version="0.3.0",
    description="Bulma template pack for django-crispy-forms",
    long_description=readme + "\n\n" + history,
    long_description_content_type="text/markdown",
    author="Christoph Krybus",
    author_email="chris@ckrybus.com",
    url="https://github.com/ckrybus/crispy-bulma",
    license="MIT license",
    packages=find_packages(include=["crispy_bulma", "crispy_bulma.*"]),
    classifiers=[
        "Development Status :: 3 - Alpha",
        # "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 3.0",
        "Framework :: Django :: 3.1",
        "Framework :: Django :: 3.2",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=requirements,
    python_requires=">=3.6",
    include_package_data=True,
    zip_safe=False,
    test_suite="tests",
    tests_require=test_requirements,
)
