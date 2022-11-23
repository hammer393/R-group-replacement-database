from pyvis.network import Network
import pandas as pd

got_net = Network(height="750px", width="100%", bgcolor="#222222", font_color="white")

# set the physics layout of the network
got_net.barnes_hut()
got_data = pd.read_csv("C:\\Users\\hqure\\Documents\\School folder\\BROCK U\\YEAR 5\\CHEM 3P20\\Presentation\\edges_final_network.csv")

sources = got_data['from']
targets = got_data['to']
weights = got_data['weight']

edge_data = zip(sources, targets, weights)

for e in edge_data:
                src = e[0]
                dst = e[1]
                w = e[2]

                got_net.add_node(src, src, title=src)
                got_net.add_node(dst, dst, title=dst)
                got_net.add_edge(src, dst, value=w)

neighbor_map = got_net.get_adj_list()

got_net.show("Rgroup.html")
