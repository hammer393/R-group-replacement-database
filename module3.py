from pyvis.network import Network

net = Network()

net.add_node(1, label='Alex')
net.add_node(2, label='Cathy')

net.show('nodes.html')

