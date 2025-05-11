#!/usr/bin/env python

from setuptools import setup

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()


setup(
    name="crispy-bulma",
    version="0.11.0",
    description="Bulma template pack for django-crispy-forms",
    long_description=readme + "\n\n" + history,
    author="Christoph Krybus",
    author_email="chris@ckrybus.com",
    keywords=["forms", "django", "crispy", "bulma"],
    url="https://github.com/ckrybus/crispy-bulma",
    license="MIT",
    packages=["crispy_bulma"],
    install_requires=["Django>=4.2", "django-crispy-forms>=2.0"],
    extras_require={"test": ["pytest", "pytest-django"]},
    tests_require=["crispy-bulma[test]"],
    python_requires=">=3.8",
    project_urls={
        "Documentation": "https://crispy-bulma.readthedocs.io/en/latest/",
        "Source": "https://github.com/ckrybus/crispy-bulma",
        "Changelog": "https://github.com/ckrybus/crispy-bulma/blob/main/HISTORY.rst",
    },
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 4.2",
        "Framework :: Django :: 5.0",
        "Framework :: Django :: 5.1",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
