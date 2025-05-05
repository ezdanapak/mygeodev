from setuptools import setup, find_packages

setup(
    name='mygeodev',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'folium',
        'ipyleaflet',
        'geopandas'
    ],
    author='Giorgi Kapanadze',
    description='A Python mapping package using ipyleaflet and folium.',
    url='https://github.com/ezdanapak/mygeodev',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ]
)
