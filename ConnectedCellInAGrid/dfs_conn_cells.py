class ConnectedGraph(object):
    def __init__(self, grid):
        self._no_of_rows = len(grid)
        self._no_of_columns = len(grid[0])
        self._grid = grid
        self.nodes = {}
        self._fill_graph()

    def _fill_graph(self):
        for i in range(self._no_of_rows):
            for j in range(self._no_of_columns):
                if self._grid[i][j] == 1:
                    self._add_neighbours(i, j)

    def _add_neighbours(self, i, j):
        my_no = self._get_node_number(i, j)
        if my_no not in self.nodes:
            self.nodes[my_no] = []
        for row_index in range(i - 1, i + 2):
            for column_index in range(j - 1, j + 2):
                if row_index == i and column_index == j:
                    continue
                try:
                    if self._grid[row_index][column_index] == 1 and min(row_index, column_index) >= 0:
                        dest_node = self._get_node_number(row_index, column_index)
                        self._add_link(my_no, dest_node)
                except IndexError:
                    pass

    def _add_link(self, start_node, dest_node, is_directed=False):
        # Add start node to graph, if it doesn't already exist
        if start_node not in self.nodes:
            self.nodes[start_node] = []

        # Add link to start node
        current_links = self.nodes[start_node]
        if dest_node not in current_links:
            self.nodes[start_node].append(dest_node)

        # Add reverse link if undirected graph
        if not is_directed:
            self._add_link(dest_node, start_node, is_directed=True)

    def _get_node_number(self, row_index, column_index):
        """Returns the unique identifier for the given node"""
        node_number = row_index * self._no_of_columns + column_index + 1
        return node_number


def get_depth(graph, entry_node, visited_nodes={}):
    my_depth = 1
    visited_nodes[entry_node] = None
    for adj_node in graph.nodes[entry_node]:
        if adj_node not in visited_nodes:
            my_depth += get_depth(graph, adj_node, visited_nodes)
    return my_depth


def get_biggest_region(grid):
    """Traverses through all possible connected cells to calculate maximum depth"""
    graph = ConnectedGraph(grid)
    depth = []
    visited_nodes = {}

    # Iterate through all possible connection sequences
    for start_node in graph.nodes.keys():
        if start_node not in visited_nodes:
            depth.append(get_depth(graph, start_node, visited_nodes))
    return 0 if not depth else max(depth)


def main():
    """Performs basic input-output tasks"""
    import sys
    sys.stdin = open("input.txt", 'r')
    n = int(raw_input().strip())
    m = int(raw_input().strip())
    grid = []
    for grid_i in xrange(n):
        grid_temp = map(int, raw_input().strip().split(' '))
        grid.append(grid_temp)
    print get_biggest_region(grid)


if __name__ == "__main__":
    main()
