from pyvis.network import Network
import pandas as pd

got_net = Network(height="750px", width="100%", bgcolor="#222222", font_color="white")

# set the physics layout of the network
got_net.barnes_hut()
got_data = pd.read_csv("C:\\Users\\hqure\\Documents\\School folder\\BROCK U\\YEAR 5\\CHEM 3P20\\Presentation\\edges_final_network.csv")

sources = got_data['Source']
targets = got_data['Target']
weights = got_data['Weight']

edge_data = zip(sources, targets, weights)

for e in edge_data:
                src = e[0]
                dst = e[1]
                w = e[2]

                got_net.add_node(src, src, title=src)
                got_net.add_node(dst, dst, title=dst)
                got_net.add_edge(src, dst, value=w)

neighbor_map = got_net.get_adj_list()

# changing the colour of the nodes
def generate_color():
    random_number = random.randint(0,16777215)
    hex_number = str(hex(random_number))
    hex_number ='#'+ hex_number[2:]
    return hex_number

# To try to get the edges to take on the colour of the node they come from
def inherit_edge_colors(self, status):
        """
        Edges take on the color of the node they are coming from.

        :param status: True if edges should adopt color coming from.
        :type status: bool
        """
        self.options.edges.inherit_colors(status)

# add neighbor data to node hover data
for node in got_net.nodes:
                node["title"] += " Neighbors:<br>" + "<br>".join(neighbor_map[node["id"]])
                node["value"] = len(neighbor_map[node["id"]])
                node["color"] = "red"

got_net.show("gameofthrones.html")
