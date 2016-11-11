"""
Solve problem specified at : https://www.hackerrank.com/challenges/bfsshortreach
using Breadth First Search
"""
__author__ = "alye"


class Graph(object):

    """Represents a mathematical graph.

    Attributes:
        nodes({int : []}): Adjacency List style representation of the vertices
        starting_node(int): Starting Point for BFS
        results([]): A list of ints representing the distance of all nodes from 's' sorted by node number

    """

    def __init__(self, no_of_nodes):
        self.nodes = {x + 1: [] for x in xrange(0, no_of_nodes)}
        self.results = [-1 for x in xrange(0, no_of_nodes)]
        self.starting_node = None

    def add_link(self, start_node, end_node, is_directed=False):
        """Adds a link between two nodes in a graph if it doesn't already exist"""

        start_node_links = self.nodes[start_node]
        if end_node not in start_node_links:
            start_node_links.append(end_node)

        # Add reverse link for undirected graphs
        if not is_directed:
            self.add_link(end_node, start_node, is_directed=True)

    def set_start(self, starting_node):
        """Sets the starting point for searching the graph"""
        self.starting_node = starting_node
        # Set starting node's distance to itself
        self.results[starting_node - 1] = 0


def _perform_bfs(graph_object):
    visited_nodes = {graph_object.starting_node: None}
    level_no = 1
    current_level_nodes = graph_object.nodes[graph_object.starting_node]
    while current_level_nodes:
        next_level_nodes = []
        for node in current_level_nodes:
            # Visit current node, if not already visited
            if node not in visited_nodes:
                graph_object.results[node-1] = level_no * 6
                visited_nodes[node] = None
            # Add child-nodes to next level node list
            child_nodes = graph_object.nodes[node]
            for child_node in child_nodes:
                if child_node not in visited_nodes:
                    next_level_nodes.append(child_node)
        current_level_nodes = next_level_nodes
        level_no += 1


def main():
    no_of_queries = int(raw_input())
    graphs = []
    # load all graphs in memory
    for x in xrange(no_of_queries):
        no_of_nodes, no_of_edges = map(int, raw_input().split())
        graph = Graph(no_of_nodes)
        for y in xrange(no_of_edges):
            start_node, end_node = map(int, raw_input().split())
            graph.add_link(start_node, end_node)
        graph.starting_node = int(raw_input())
        graphs.append(graph)

    # compute distances via bfs and display results
    for graph in graphs:
        _perform_bfs(graph)
        # remove self-distance from results
        graph.results.pop(graph.starting_node - 1)
        print " ".join(map(str, graph.results))

if __name__ == "__main__":
    main()
