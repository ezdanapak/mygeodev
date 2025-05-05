from setuptools import setup, find_packages

setup(
    name='mygeodev',
    version='0.1.0',
    author='Giorgi Kapanadze',
    author_email='kapan.gio777@gmail.com',
    description='A Python package for interactive maps using ipyleaflet and folium.',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "ipyleaflet",
        "folium",
        "geopandas",
        "shapely",
        "pandas",
        "branca",
        "jupyter",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
