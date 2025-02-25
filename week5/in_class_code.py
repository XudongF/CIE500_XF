# %%

import geopandas as gpd
import networkx as nx
import momepy
import matplotlib.pyplot as plt

river_data = gpd.read_file(
    "/Users/xudongfan/Documents/Courses/CIE500-UrbanNetworks/CIE500_XF/week5/rivernetwork/networkoregon.shp"
)

river_data.plot()

river_data_exploded = river_data.explode(ignore_index=True, index_parts=False)[
    ["geometry"]
]

river_data_exploded.plot()
river_data_exploded["length"] = river_data_exploded.geometry.length

print(river_data_exploded.head())

G = momepy.gdf_to_nx(
    river_data_exploded,
    approach="primal",
    multigraph=False,
    directed=False,
    length="length",
)

G.remove_edges_from(nx.selfloop_edges(G))

pos = {node: node for node in G.nodes()}

fig, ax = plt.subplots(figsize=(8, 8))
nx.draw_networkx(
    G,
    pos=pos,
    width=2,
    with_labels=False,
    node_color="lightblue",
    edge_color="gray",
    node_size=1,
)
ax.axis("off")  # remove the frame of the generated figure
plt.show()
