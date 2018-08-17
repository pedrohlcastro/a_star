# f(n) = g(n) + h(n)
Graph = {}

# bh: [{name:betim, peso:peso}, contagem]


# {

# }
def add_item_graph(origin, destiny):
    for city, cost in destiny:
        if origin in Graph:
            no = {}
            no['name'] = city
            no['weight'] = cost
            Graph[origin].append(no)
        else:
            Graph[origin] = []
            no = {}
            no['name'] = city
            no['weight'] = cost
            Graph[origin].append(no)

def init_graph():
    add_item_graph('oradea', [('zerind', 71), ('sibiu', 151)])
    add_item_graph('zerind', [('oradea', 71), ('arad', 75)])
    add_item_graph('arad', [('timisoara', 118), ('sibiu', 140), ('zerind', 75)])
    add_item_graph('timisoara', [('arad', 118), ('lugoj', 111)])
    add_item_graph('lugoj', [('timisoara', 111), ('mehadia', 70)])
    add_item_graph('mehadia', [('lugoj', 70), ('dobreta', 75)])
    add_item_graph('dobreta', [('mehadia', 75), ('craiova', 120)])
    add_item_graph('craiova', [('dobreta', 120), ('rimncuvilcea', 146),('pitesti', 138)])
    add_item_graph('rimncuvilcea', [('sibiu', 80), ('craiova', 146),('pitesti', 97)])
    add_item_graph('sibiu', [('oradea', 151), ('rimncuvilcea', 80),('fagaras', 99),('arad', 140)])
    add_item_graph('fagaras', [('sibiu', 99),('buhcarest', 211)])
    add_item_graph('pitesti', [('buhcarest', 101),('rimncuvilcea', 97),('craiova', 138)])
    print(Graph)


if __name__ == '__main__':
    init_graph()