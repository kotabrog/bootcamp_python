from setuptools import setup

packages = [
    'ai42',
    'ai42.logging',
]


setup(
    name='ai42',
    version='1.0.0',
    packages=packages,
    package_dir={"": "src"},
)
