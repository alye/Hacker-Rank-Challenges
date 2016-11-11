class ConnectedGraph(object):
    def __init__(self, grid):
        self._no_of_rows = len(grid)
        self._no_of_columns = len(grid[0])
        self._grid = grid
        no_of_nodes = self._no_of_rows * self._no_of_columns
        self.nodes = {}
        self.fill_graph()

    def fill_graph(self):
        for i in range(self._no_of_rows):
            for j in range(self._no_of_columns):
                # print ("i : {}\tj : {}\tgrid_value: {}".format(i, j, self._grid[i][j]))
                if self._grid[i][j] == 1:
                    # print "Adding"
                    self._add_neighbours(i, j)

    def _add_neighbours(self, i, j):
        my_no = self._get_node_number(i, j)
        if my_no not in self.nodes:
            self.nodes[my_no] = []
        for row_index in range(i-1, i+2):
            for column_index in range(j-1, j+2):
                # print ("i : {}\tj : {}".format(row_index, column_index))
                if row_index == i and column_index == j:
                    continue
                try:
                    # # print ("Entered")
                    if self._grid[row_index][column_index] == 1 and min(row_index, column_index) >= 0:
                        # print ("Added neighbour: i = {}\tj = {}".format(row_index, column_index))
                        dest_node = self._get_node_number(row_index ,column_index)
                        self._add_link(my_no, dest_node)
                except IndexError:
                    # print "Index Exceeded"
                    pass

    def _add_link(self, start_node, dest_node, is_directed=False):
        # start_node = self._get_node_number(start[0], start[1])
        # dest_node = self._get_node_number(dest[0], dest[1])
        # print ("Start node : {}\tDest Node: {}".format(start_node, dest_node))
        # Add start node to graph, if it doesn't already exist
        if start_node not in self.nodes:
            self.nodes[start_node] = []

        # Add link to start node
        current_links = self.nodes[start_node]
        if dest_node not in current_links:
            self.nodes[start_node].append(dest_node)
            # print ("Added link : ({}, {})".format(start_node, dest_node))

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
    graph = ConnectedGraph(grid)
    depth = []
    my_depth = 0
    
    # Iterate through all nodes
    for start_node in graph.nodes.keys():
        my_depth += 1
        depth.append(get_depth(graph, start_node))
    return 0 if not depth else max(depth)


def main():    
    n = int(raw_input().strip())
    m = int(raw_input().strip())
    grid = []
    for grid_i in xrange(n):
        grid_temp = map(int, raw_input().strip().split(' '))
        grid.append(grid_temp)
    print get_biggest_region(grid)

if __name__ == "__main__":
    main()
