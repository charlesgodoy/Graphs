
def earliest_ancestor(ancestors, starting_node, visited=None):
    y = [x[1] for x in ancestors]   # used to check if starting node is by finding nothing higher -> -1

    if visited is None:
        visited = set()

    if starting_node not in y and starting_node not in visited:
        return -1

    # find a y element that equals starting node, then get its x element, and make that x element new starting node, then repeat
    for i in ancestors:
        if i[1] is starting_node:
            node = i[0]
            visited.add(node)
            return earliest_ancestor(ancestors, node, visited)
    
    # print(x)
    # print(y)
    return starting_node