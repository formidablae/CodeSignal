def solution(adj):
    lateral_nodes = []
    middle_nodes = []
    for node_ind in range(5):
        # nodes should not be connected to themselves
        if adj[node_ind][node_ind]:
            return False
        
        # node1 connected to node2 means node2 connected to node1
        for other_node_ind in range(node_ind + 1, 5):
            if adj[node_ind][other_node_ind] and not adj[other_node_ind][node_ind]:
                return False
            if not adj[node_ind][other_node_ind] and adj[other_node_ind][node_ind]:
                return False

        # define lateral and middle nodes
        if sum(adj[node_ind]) == 2:
            lateral_nodes.append(node_ind)
        elif sum(adj[node_ind]) == 4:
            middle_nodes.append(node_ind)
        else:
            return False

    # all nodes should be connected to 2 other nodes,
    # except one node should be connected to all other nodes
    if len(lateral_nodes) != 4:
        return False
    if len(middle_nodes) != 1:
        return False
    return True
