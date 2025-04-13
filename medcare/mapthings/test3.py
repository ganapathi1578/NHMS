import osmnx as ox
import networkx as nx

def shortest_route_graphml(coord1, coord2):
    G = ox.load_graphml(r"C:\Users\GANAPATHI\Desktop\NIT\project\ymhhacakthon\medcare\mapthings\mizoram_graph.graphml")
    if coord1 and coord2:
        node1 = ox.distance.nearest_nodes(G, coord1[1], coord1[0])  # (lon, lat) -> (lat, lon)
        node2 = ox.distance.nearest_nodes(G, coord2[1], coord2[0])
        distance_m = nx.shortest_path_length(G, node1, node2, weight='length')
        return distance_m / 1000
    else:
        return 0

coord1 = (23.732369, 92.716494)  # (lat, lon)
coord2 = (23.718835, 92.717611)

distance = shortest_route_graphml(coord1, coord2)
print(distance, "km")
