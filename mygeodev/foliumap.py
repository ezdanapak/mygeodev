import folium
import geopandas as gpd
from folium import TileLayer, LayerControl, GeoJson

class FoliumMap(folium.Map):
    """
    A custom folium.Map with simple methods for adding basemaps and vector layers.
    """

    def add_basemap(self, basemap_name: str):
        """Add a basemap by name (e.g., 'OpenStreetMap', 'Esri WorldImagery')"""
        known_tiles = {
            "OpenStreetMap": "OpenStreetMap",
            "Stamen Terrain": "Stamen Terrain",
            "Stamen Toner": "Stamen Toner",
            "CartoDB positron": "CartoDB positron",
            "Esri WorldImagery": "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}"
        }

        if basemap_name not in known_tiles:
            raise ValueError(f"Unknown basemap '{basemap_name}'.")

        tile = known_tiles[basemap_name]
        layer = TileLayer(
            tiles=tile,
            attr=basemap_name,
            name=basemap_name,
            overlay=False,
            control=True
        )
        layer.add_to(self)
        return layer

    def add_layer_control(self):
        """Add a LayerControl widget to manage layers."""
        control = LayerControl()
        control.add_to(self)
        return control

    def add_vector(self, data):
        """Add GeoPandas vector data."""
        if isinstance(data, str):
            gdf = gpd.read_file(data)
        elif isinstance(data, gpd.GeoDataFrame):
            gdf = data
        else:
            raise TypeError("Input must be a filepath or GeoDataFrame")

        layer = GeoJson(gdf.__geo_interface__)
        layer.add_to(self)
        return layer
