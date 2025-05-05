from ipyleaflet import Map as LeafletMap, basemaps, basemap_to_tiles, LayersControl, GeoJSON
import geopandas as gpd
import json

class IPyMap(LeafletMap):
    """
    A custom ipyleaflet.Map with easy methods for basemaps, layers, and vector data.
    """

    def add_basemap(self, basemap_name: str):
        """Add a basemap by name (e.g., 'OpenStreetMap', 'Esri.WorldImagery')"""
        parts = basemap_name.split(".")
        base = basemaps
        try:
            for part in parts:
                base = getattr(base, part)
            tile_layer = basemap_to_tiles(base)
            self.add_layer(tile_layer)
            return tile_layer
        except AttributeError:
            raise ValueError(f"Basemap '{basemap_name}' not found.")

    def add_layer_control(self):
        """Add a LayersControl widget to manage visibility of layers."""
        control = LayersControl(position='topright')
        self.add_control(control)
        return control

    def add_vector(self, data):
        """Add GeoPandas vector data (GeoJSON, shapefile, etc.)."""
        if isinstance(data, str):
            gdf = gpd.read_file(data)
        elif isinstance(data, gpd.GeoDataFrame):
            gdf = data
        else:
            raise TypeError("Input must be a filepath or GeoDataFrame")

        geojson = GeoJSON(data=json.loads(gdf.to_json()))
        self.add_layer(geojson)
        return geojson
