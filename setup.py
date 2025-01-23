from setuptools import setup, find_packages

setup(
    name='HousePricePrediction',
    version='0.1',
    packages=find_packages,
    install_requires=[
        'pandas',
        'numpy',
        'scikit-learn',
        'mlflow',
        'dataclasses',
        'pathlib',
        'urllib3'
    ],
)