import networkx as nx
import matplotlib.pyplot as plt

class NetworkAssociationModel:
    def __init__(self):
        self.graph = nx.Graph()

    def add_node(self, node):
        self.graph.add_node(node)

    def add_edge(self, node1, node2):
        self.graph.add_edge(node1, node2)

    def visualize(self):
        nx.draw(self.graph, with_labels=True)
        plt.show()
