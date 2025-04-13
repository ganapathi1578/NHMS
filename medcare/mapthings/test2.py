import osmnx as ox
import networkx as nx
import os

# Define file paths
SHAPEFILE_PATH = r"C:\Users\GANAPATHI\Desktop\NIT\project\ymhhacakthon\medcare\mapthings\gis_osm_roads_free_1.shp"
GRAPHML_PATH = r"C:\Users\GANAPATHI\Desktop\NIT\project\ymhhacakthon\medcare\mapthings\mizoram_graph.graphml"

def build_and_save_graph(shapefile_path, graphml_path):
    """
    Build a graph from a shapefile and save it as a GraphML file.
    """
    # Load the graph from the shapefile
    G = ox.graph_from_place("Mizoram, India", network_type="drive")
    # Save the graph to a GraphML file
    ox.save_graphml(G, graphml_path)
    print(f"Graph saved to {graphml_path}")

import osmnx as ox
import networkx as nx
import pyproj

def load_graph(place):
    """
    Loads a graph from OSM for a given location.
    """
    G = ox.graph_from_place(place, network_type="drive")
    
    # Ensure CRS is set
    if "crs" not in G.graph:
        G.graph["crs"] = pyproj.CRS.from_epsg(4326)  # Assign default WGS 84
    
    return G

def check_projection(G):
    """
    Checks if the graph's CRS is projected.
    """
    crs = G.graph.get("crs", None)
    
    if crs is None:
        print("CRS is missing from the graph.")
        return False
    
    is_proj = ox.projection.is_projected(crs)
    print(f"Is the CRS projected? {is_proj}")
    return is_proj

def ensure_projected(G):
    """
    Ensures the graph is projected for accurate distance calculations.
    """
    if not check_projection(G):
        print("Reprojecting the graph...")
        G_proj = ox.project_graph(G)  # Automatically converts to UTM projection
        print(f"New Projected CRS: {G_proj.graph['crs']}")
        return G_proj
    return G

def find_distance(G, start, end):
    """
    Finds the shortest path distance between two nodes in meters.
    """
    G = ensure_projected(G)  # Ensure graph is projected

    # Compute shortest path length
    distance = nx.shortest_path_length(G, source=start, target=end, weight="length")
    print(f"Distance between {start} and {end}: {distance} meters")
    return distance

# Example Usage
place = "M"
G = load_graph(place)

# Get two random nodes for testing
nodes = list(G.nodes)
start, end = nodes[0], nodes[-1]

# Compute distance
find_distance(G, start, end)
