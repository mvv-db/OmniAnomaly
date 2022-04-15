from setuptools import setup

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="omni_anomaly",
    version="0.0.1",
    python_requires=">=3.6",
    author="Some cool dude",
    long_description="Some cool project",
    packages=["omni_anomaly"],
    install_requires=requirements,
)