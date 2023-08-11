from graph import Graph
from breadth_first_search import breadth_first_search

def main():
    g = Graph()
    g.add_node(1)
    g.add_node(2)
    g.add_node(3)
    g.add_node(4)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    print(breadth_first_search(g, 1))

if __name__ == "__main__":
    main()
