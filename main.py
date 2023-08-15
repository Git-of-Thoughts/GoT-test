from network_association_model import NetworkAssociationModel

def main():
    model = NetworkAssociationModel()

    # Add nodes
    model.add_node('A')
    model.add_node('B')
    model.add_node('C')

    # Add edges
    model.add_edge('A', 'B')
    model.add_edge('B', 'C')
    model.add_edge('A', 'C')

    # Visualize the graph
    model.visualize()

if __name__ == "__main__":
    main()
