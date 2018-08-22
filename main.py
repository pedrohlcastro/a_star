from queue import PriorityQueue

Graph = {}
CITY = 1
WEIGHT = 0

def add_item_graph(origin, destiny):
    for city, cost in destiny:
        if origin in Graph:
            no = (cost, city)
            Graph[origin].append(no)
        else:
            Graph[origin] = []
            no = (cost, city)
            Graph[origin].append(no)

def init_graph():
    add_item_graph('oradea', [('zerind', 71), ('sibiu', 151)])
    add_item_graph('zerind', [('oradea', 71), ('arad', 75)])
    add_item_graph('arad', [('timisoara', 118), ('sibiu', 140), ('zerind', 75)])
    add_item_graph('timisoara', [('arad', 118), ('lugoj', 111)])
    add_item_graph('lugoj', [('timisoara', 111), ('mehadia', 70)])
    add_item_graph('mehadia', [('lugoj', 70), ('dobreta', 75)])
    add_item_graph('dobreta', [('mehadia', 75), ('craiova', 120)])
    add_item_graph('craiova', [('dobreta', 120), ('rimnicuvilcea', 146),('pitesti', 138)])
    add_item_graph('rimnicuvilcea', [('sibiu', 80), ('craiova', 146),('pitesti', 97)])
    add_item_graph('sibiu', [('oradea', 151), ('rimnicuvilcea', 80),('fagaras', 99),('arad', 140)])
    add_item_graph('fagaras', [('sibiu', 99),('bucharest', 211)])
    add_item_graph('pitesti', [('bucharest', 101),('rimnicuvilcea', 97),('craiova', 138)])
    add_item_graph('bucharest', [('fagaras', 211), ('giurgiu', 90), ('pitesti', 101), ('urziceni', 85)])
    add_item_graph('giurgiu', [('bucharest', 90)])
    add_item_graph('urziceni', [('bucharest', 85), ('vaslui', 142), ('hirsova', 98)])
    add_item_graph('hirsova', [('eforie', 86), ('urziceni', 98)])
    add_item_graph('eforie', [('hirsova', 86)])
    add_item_graph('vaslui', [('urziceni', 142), ('iasi', 92)])
    add_item_graph('iasi', [('neamt', 87), ('vaslui', 92)])
    add_item_graph('neamt', [('iasi', 87)])

def h(start, end):
    straight_line_dist = {
        'bucharest': 0,
        'arad': 366,
        'craiova': 160,
        'dobreta': 242,
        'eforie': 161,
        'fagaras': 176,
        'giurgiu': 77,
        'hirsova': 151,
        'iasi': 226,
        'lugoj': 244,
        'mehadia': 241,
        'neamt': 234,
        'oradea': 380,
        'pitesti': 101,
        'rimnicuvilcea': 193,
        'sibiu': 253,
        'timisoara': 329,
        'urziceni': 80,
        'vaslui': 199,
        'zerind': 374
    }
    return straight_line_dist[start]

def a_star(start, end):
    nodes_to_go = PriorityQueue()
    nodes_to_go.put( (h(start, end),start) )
    vistided_cities = {}

    while not nodes_to_go.empty():
        current_node = nodes_to_go.get() # return min(cost in current_node )
        # print(str(current_node[CITY]))
        #avoid loop -> never back to a visited city
        while vistided_cities.get(current_node[CITY], False):
            current_node = nodes_to_go.get()
            # print(str(current_node[CITY]))
        print(str(current_node[CITY]) + '-> ', end=' ')
        vistided_cities[current_node[CITY]] = True

        # check stop condition
        if current_node[CITY] == end:
            break

        for neighbor in Graph[current_node[CITY]]:
            neighbor_cost = neighbor[WEIGHT] + h(neighbor[CITY], end)
            nodes_to_go.put((neighbor_cost, neighbor[CITY]))
            # print('ADD:' + str(neighbor[CITY]) + str(neighbor_cost))


if __name__ == '__main__':
    init_graph()
    a_star('arad', 'bucharest')