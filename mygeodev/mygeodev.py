from ipyleaflet import Map as LeafletMap, basemaps, basemap_to_tiles, LayersControl, GeoJSON
import geopandas as gpd
import json

class Map(LeafletMap):
    """
    A customized interactive map class that extends ipyleaflet.Map.

    This class provides convenient methods for:
    - Adding popular basemaps by name
    - Displaying GeoPandas-compatible vector data
    - Managing visible layers through a layer control widget

    Use this class in Jupyter notebooks or JupyterLab to create
    dynamic and interactive maps for geospatial data visualization.
    """

    def add_basemap(self, basemap_name: str):
        """
        Add a basemap layer to the map using a named source from ipyleaflet.basemaps.

        Parameters:
        ----------
        basemap_name : str
            The name of the basemap, as defined in ipyleaflet.basemaps.
            Examples include:
                - "OpenStreetMap"
                - "Esri.WorldImagery"
                - "OpenTopoMap"

        Returns:
        -------
        ipyleaflet.TileLayer
            The basemap tile layer added to the map.

        Raises:
        ------
        ValueError:
            If the specified basemap name is not found.
        """
        parts = basemap_name.split(".")
        base = basemaps
        try:
            for part in parts:
                base = getattr(base, part)
            tile_layer = basemap_to_tiles(base)
            self.add_layer(tile_layer)
            return tile_layer
        except AttributeError:
            raise ValueError(f"Basemap '{basemap_name}' not found in ipyleaflet.basemaps.")

    def add_layer_control(self):
        """
        Add a layer control widget to the map.

        This control allows users to toggle the visibility of different
        layers (basemaps, vector layers, etc.) added to the map.

        Returns:
        -------
        ipyleaflet.LayersControl
            The layer control widget added to the map.
        """
        control = LayersControl(position='topright')
        self.add_control(control)
        return control

    def add_vector(self, data):
        """
        Add vector data (e.g., Shapefile, GeoJSON) to the map.

        Supports direct loading from file paths or existing GeoDataFrames.

        Parameters:
        ----------
        data : str or geopandas.GeoDataFrame
            Path to a supported vector data file (e.g., '.geojson', '.shp'), 
            or a GeoDataFrame object.

        Returns:
        -------
        ipyleaflet.GeoJSON
            The GeoJSON layer added to the map.

        Raises:
        ------
        TypeError:
            If the data is neither a string path nor a GeoDataFrame.
        """
        if isinstance(data, str):
            gdf = gpd.read_file(data)
        elif isinstance(data, gpd.GeoDataFrame):
            gdf = data
        else:
            raise TypeError("Data must be a file path or a GeoDataFrame")

        geo_json_data = json.loads(gdf.to_json())
        geo_json_layer = GeoJSON(data=geo_json_data, name="Vector Layer")
        self.add_layer(geo_json_layer)
        return geo_json_layer
