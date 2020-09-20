from DFS import DFS


class IDS(DFS):
    depth = 0

    def process_accessible_nodes(self, current_node, accessible_nodes):
        if len(self.path) != self.depth + 1:  # Add new nodes to the frontier if they are inside max. depth
            accessible_nodes = self.remove_visited_nodes(accessible_nodes)
            self.add_new_nodes_to_frontier(accessible_nodes)

    def execute(self, mode):
        self.depth = -1
        print("\n", self.name, "\n_________________________________________________________________________\n")
        end = False
        while not end and self.depth != len(self.maze) * len(self.maze[0]):  # Continue until reach a goal state
            if len(self.frontier) == 0:  # Terminates when frontier is empty
                self.initialize()
                self.depth += 1
            end = self.progress(mode)
        if not end:
            print("CANNOT REACH A GOAL STATE")
        print("DEPTH:", self.depth, "\nEXPANDED NODES:", self.visited)
