import geopandas as gpd
from numpy import short
import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt
import sklearn

def find_distance(start_coord,end_coord):
    shapefile_path = r"C:\Users\GANAPATHI\Desktop\NIT\project\ymhhacakthon\medcare\mapthings\gis_osm_roads_free_1.shp"  # Change this path
    gdf = gpd.read_file(shapefile_path)
    
    nodes_gdf, edges_gdf = ox.graph_to_gdfs(ox.graph_from_place("Mizoram, India", network_type="drive"))

    graph = ox.graph_from_gdfs(nodes_gdf, edges_gdf)
    start_coord = (23.732369, 92.716494)  # Example start Civil Hospital
    end_coord = (23.718835, 92.717611)   # Example end Aizawl Hospital & Research Center
    start_node = ox.distance.nearest_nodes(graph, X=start_coord[1], Y=start_coord[0])
    end_node = ox.distance.nearest_nodes(graph, X=end_coord[1], Y=end_coord[0])
    shortest_path = nx.astar_path(graph, start_node, end_node, weight='length')
    print(shortest_path)
    edge_lengths = []
    for u, v, data in graph.edges(data=True):
        if (u, v) in zip(shortest_path[:-1], shortest_path[1:]):
            edge_lengths.append(data.get("length", 0))

    distance = sum(edge_lengths) / 1000

    print(f"Total distance: {distance} km")
    print(f"Shortest Road Distance: {distance:.2f} km")
    return distance
# Example usage
if __name__ == "__main__":
    start = (23.7363, 92.7147)  # (lat, lon)
    end = (23.7271, 92.7179)

    distance = find_distance(start, end)
    if distance:
        print(f"Shortest distance: {distance:.2f} km")
    else:
        print("Calculation failed")
