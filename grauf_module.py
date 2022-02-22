from collections import deque
from heapq import *
from DrawConvas import *


graph_with_weights = {

    # веса графа посчитаны на основе пикселей из словаря в файле "DrawConvas"

    # ground floor

    'g1': [(2000, 'f47'), (700, 'g2')],
    'g2': [(700, 'g1'), (400, 'g3')],
    'g3': [(400, 'g2'), (250, 'g4'), (282, 'g5')],
    'g4': [(250, 'g3')],
    'g5': [(282, 'g3')],

    'g6': [(2000, 'f31'), (800, 'g7')],
    'g7': [(800, 'g6'), (200, 'g8'), (650, 'g9')],
    'g8': [(200, 'g7')],
    'g9': [(650, 'g7'), (200, 'g10'), (200, 'g12')],
    'g10': [(200, 'g9'), (200, 'g11'), (550, 'g13')],
    'g11': [(200, 'g10')],
    'g12': [(200, 'g9')],
    'g13': [(550, 'g10'), (300, 'g14'), (800, 'g15')],
    'g14': [(300, 'g13')],
    'g15': [(800, 'g13'), (200, 'g16'), (650, 'g17')],
    'g16': [(200, 'g15')],
    'g17': [(650, 'g15'), (300, 'g18'), (700, 'g19')],
    'g18': [(300,'g17')],
    'g19': [(700, 'g17'), (200, 'g20'), (300, 'g21'), (300, 'g22')],
    'g20': [(200, 'g19')],
    'g21': [(300, 'g19')],
    'g22': [(300, 'g19'), (300, 'g23'), (300, 'g24')],
    'g23': [(300, 'g22')],
    'g24': [(300, 'g22'), (300, 'g25'), (500, 'g26')],
    'g25': [(300, 'g24')],
    'g26': [(500, 'g24')],



    # first floor


    'f0': [(522, 'f1'), (2000, 'g1')],
    'f1': [(522, 'f0'), (509, 'f47'), (700, 'f2')],
    'f2': [(700, 'f1'), (281, 'f3'), (120, 'f4')],
    'f3': [(281, 'f2')],
    'f4': [(120, 'f2'), (200, 'f48'), (380, 'f5')],
    'f5': [(380, 'f4'), (250, 'f6'), (250, 'f7')],
    'f6': [(250, 'f5')],
    'f7': [(250, 'f5'), (250, 'f8'), (1350, 'f9')],
    'f8': [(250, 'f7')],
    'f9': [(1350, 'f7'), (250, 'f10'), (100, 'f11')],
    'f10': [(250, 'f9')],
    'f11': [(100, 'f9'), (250, 'f12'), (900, 'f13')],
    'f12': [(250, 'f11')],
    'f13': [(900, 'f11'), (250, 'f14'), (250, 'f17'), (550, 'f18')],
    'f14': [(250, 'f13'), (250, 'f15')],
    'f15': [(250, 'f14'), (450, 'f16')],
    'f16': [(450, 'f15')],
    'f17': [(250, 'f13')],
    'f18': [(550, 'f13'), (900, 'f19')],
    'f19': [(900, 'f18'), (626, 'f20'), (900, 'f21'), (670, 'f23')],
    'f20': [(626, 'f19')],
    'f21': [(900, 'f19'), (300, 'f22'), (707, 'f25'), (602, 'f26')],
    'f22': [(300, 'f21'), (300, 'f23'), (806, 'f24'), (694, 'f26')],
    'f23': [(670, 'f19'), (300, 'f22'), (447, 'f24')],
    'f24': [(447, 'f23'), (806, 'f22'), (672, 'f26')],
    'f25': [(707, 'f21'), (460, 'f26'), (509, 'f27')],
    'f26': [(602, 'f21'), (694, 'f22'), (672, 'f24'), (460, 'f25'), (1029, 'f32')],
    'f27': [(509, 'f25'), (600, 'f28'), (700, 'f29')],
    'f28': [(600, 'f27')],
    'f29': [(700, 'f27'), (608, 'f30'), (632,'f31')],
    'f30': [(608, 'f29'), (2000, 's27')],
    'f31': [(632, 'f29'), (2000, 'g6')],
    'f32': [(1029, 'f26'), (710, 'f33'), (2050, 'f36')],
    'f33': [(710, 'f32'), (282, 'f34'), (1201, 'f35')],
    'f34': [(282, 'f33'), (1030, 'f35')],
    'f35': [(1201, 'f33'), (1030, 'f34')],
    'f36': [(2050, 'f32'), (800, 'f37')],
    'f37': [(800, 'f36'), (250, 'f38')],
    'f38': [(250, 'f37'), (150, 'f39'), (600, 'f40')],
    'f39': [(150, 'f38')],
    'f40': [(600, 'f38'), (200, 'f41'), (400, 'f42')],
    'f41': [(200, 'f40')],
    'f42': [(400, 'f40'), (200, 'f43'), (200, 'f44')],
    'f43': [(200, 'f42')],
    'f44': [(200, 'f42'), (550, 'f45'), (500, 'f46')],
    'f45': [(550, 'f44')],
    'f46': [(500, 'f44')],
    'f47': [(509, 'f1'), (2000, 's1')],
    'f48': [(200, 'f4')],


    # second floor

    's0': [(2000, 'f47'), (712, 's1')],
    's1': [(715, 's0'), (700, 's2'), (715, 's50')],
    's2': [(700, 's1'), (251, 's3'), (370, 's4')],
    's3': [(251, 's2')],
    's4': [(370, 's2'), (250, 's5'), (230, 's6')],
    's5': [(250, 's4')],
    's6': [(230, 's4'), (200, 's7'), (250, 's10')],
    's7': [(200, 's6'), (403, 's8')],
    's8': [(403, 's7'), (600, 's9')],
    's9': [(600, 's8')],
    's10': [(250, 's6'), (250,'s11'), (900, 's12')],
    's11': [(250, 's10')],
    's12': [(900, 's10'), (250, 's13'), (450, 's14')],
    's13': [(250, 's12')],
    's14': [(450, 's12'), (254, 's15'), (206, 's16'), (650, 's17')],
    's15': [(254, 's14')],
    's16': [(206, 's14')],
    's17': [(650, 's14'), (250, 's18'), (100, 's19')],
    's18': [(250, 's17')],
    's19': [(100, 's17'), (200, 's20'), (500, 's21')],
    's20': [(200, 's19')],
    's21': [(500, 's19'), (250, 's22'), (100, 's23')],
    's22': [(250, 's21')],
    's23': [(100, 's21'), (200, 's24'), (1550, 's25')],
    's24': [(200, 's23')],
    's25': [(1550, 's23'), (800, 's26'), (200, 's28'), (700, 's29')],
    's26': [(800, 's25'), (776, 's27'), (559, 's51')],
    's27': [(776, 's26'), (2000, 'f30')],
    's28': [(200, 's25')],
    's29': [(700, 's25'), (200, 's30'), (150, 's31')],
    's30': [(200, 's29')],
    's31': [(150, 's29'), (250, 's32'), (450, 's33')],
    's32': [(250, 's31')],
    's33': [(450, 's31'), (316, 's34'), (200, 's35'), (750, 's36')],
    's34': [(316, 's33')],
    's35': [(200, 's33')],
    's36': [(750, 's33'), (300, 's37'), (200, 's38'), (750, 's39')],
    's37': [(300, 's36')],
    's38': [(200, 's38')],
    's39': [(750, 's36'), (301, 's40'), (200, 's41'), (750, 's42')],
    's40': [(301, 's39')],
    's41': [(200, 's39')],
    's42': [(750, 's39'), (200, 's43'), (300, 's44'), (450, 's45')],
    's43': [(200, 's42')],
    's44': [(300, 's42')],
    's45': [(450, 's42'), (300, 's46'), (250, 's49')],
    's46': [(300, 's45')],
    's47': [(316, 's49')],
    's48': [(223, 's49')],
    's49': [(250, 's45'), (316, 's47'), (223, 's48')],
    's50': [(715, 's1'), (2000, 't1')],
    's51': [(559, 's26'), (2000, 't28')],

    # third floor

    't1': [(2000, 's50'), (707, 't2')],
    't2': [(707, 't1'), (502, 't3')],
    't3': [(502, 't2'), (251, 't4'), (370, 't5')],
    't4': [(251, 't3')],
    't5': [(370, 't3'), (250, 't6'), (230, 't7')],
    't6': [(250, 't5')],
    't7': [(230, 't5'), (200, 't8'), (250, 't9')],
    't8': [(200, 't7')],
    't9': [(250, 't7'), (250, 't10'), (800, 't11')],
    't10': [(250, 't9')],
    't11': [(800, 't9'), (200, 't12'), (250, 't13'), (550, 't14')],
    't12': [(200, 't11')],
    't13': [(250, 't11')],
    't14': [(550, 't11'), (206, 't15'), (254, 't16'), (650, 't17')],
    't15': [(206, 't14')],
    't16': [(254, 't14')],
    't17': [(650, 't14'), (200, 't18'), (250, 't19'), (600, 't20')],
    't18': [(200, 't17')],
    't19': [(250, 't17')],
    't20': [(600, 't17'), (250, 't21'), (100, 't22')],
    't21': [(250, 't20')],
    't22': [(100, 't20'), (200, 't24'), (200, 't25')],
    't24': [(200, 't22')],
    't25': [(200, 't22'), (200, 't26'), (800, 't27'), (700, 't29')],
    't26': [(200, 't25')],
    't27': [(800, 't25'), (776, 't28')],
    't28': [(776, 't27'), (2000, 's51')],
    't29': [(700, 't25'), (200, 't30'), (150, 't31')],
    't30': [(200, 't29')],
    't31': [(150, 't29'), (250, 't32'), (450, 't33')],
    't32': [(250, 't31')],
    't33': [(450, 't31'), (304, 't34'), (200, 't35'), (750, 't36')],
    't34': [(304, 't33')],
    't35': [(200, 't33')],
    't36': [(750, 't33'), (200, 't37'), (750, 't38')],
    't37': [(200, 't36')],
    't38': [(750, 't36'), (301, 't39'), (200, 't40'), (750, 't41')],
    't39': [(301, 't38')],
    't40': [(200, 't38')],
    't41': [(750, 't38'), (200, 't42'), (450, 't43')],
    't42': [(200, 't41')],
    't43': [(450, 't41'), (300, 't44'), (250, 't45')],
    't44': [(300, 't43')],
    't45': [(250, 't43'), (316, 't46')],
    't46': [(316, 't45')]
}

def dijkstra(start, goal, graph):
    queue = []
    heappush(queue, (0, start))
    cost_visited = {start: 0}
    visited = {start: None}

    while queue:
        cur_cost, cur_node = heappop(queue)
        if cur_node == goal:
            break

        next_nodes = graph[cur_node]
        for next_node in next_nodes:
            neigh_cost, neigh_node = next_node
            new_cost = cost_visited[cur_node] + neigh_cost

            if neigh_node not in cost_visited or new_cost < cost_visited[neigh_node]:
                heappush(queue, (new_cost, neigh_node))
                cost_visited[neigh_node] = new_cost
                visited[neigh_node] = cur_node
    return visited




def getPath(goal, start):

    viseted = dijkstra(start, goal, graph_with_weights)
    cur_node = goal

    way = []
    way.append(goal)

    while cur_node != start:
        cur_node = viseted[cur_node]
        way.append(cur_node)
        print(f' ---> {cur_node} ', end='')

    draw_by_points(way)

