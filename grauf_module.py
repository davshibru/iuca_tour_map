from collections import deque

from DrawConvas import *

# 'A': ['G', 'B', 'K'],
#          'B': ['A', 'C'],
#          'C': ['B', 'D'],
#          'D': ['C', 'E', 'K'],
#          'E': ['D', 'F'],
#          'F': ['E', 'I', 'L'],
#          'I': ['F', 'H'],
#          'H': ['G', 'I'],
#          'G': ['H', 'A'],
#          'K': ['A', 'F', 'D']

graph = {
    'f1':['f2', 'f3'],
    'f2':['f1', 'f4'],
    'f3':['f1', 'f4', 'f9'],
    'f4':['f3', 'f2', 'f5', 'f6'],
    'f5':['f4'],
    'f6':['f4','f7'],
    'f7':['f6', 'f8'],
    'f8':['f7', 's15'],
    'f9':['f3', 'f10'],
    'f10':['f9', 'f11', 'f12'],
    'f11':['f10'],
    'f12':['f10', 'f13'],
    'f13':['f12', 'f14', 'f20'],
    'f14':['f13', 'f15'],
    'f15':['f14'],
    'f20':['f13', 'f16', 'f17'],
    'f16':['f20'],
    'f17':['f20', 'f18'],
    'f18':['f17', 'f19'],
    'f19':['f18', 's1'],

    # second floor

    's1': ['f19', 's2'],
    's2': ['s1', 's3'],
    's3': ['s2', 's4', 's5'],
    's4': ['s3'],
    's5': ['s3', 's6', 's8'],
    's6': ['s5'],
    #'s7': ['s5', 's8', 's9'],
    's8': ['s5'],
    's9': ['s5', 's10', 's12', 's13'],
    's10': ['s9'],
    #'s11': ['s9', 's12', 's13'],
    's12': ['s9'],
    's13': ['s9', 's14', 's17', 's16'],
    's14': ['s13', 's15'],
    's15': ['s14', 'f8'],
    's16': ['s13'],
    's17': ['s13', 's18', 's19'],
    's18': ['s17'],
    's19': ['s17', 's20', 's21'],
    's20': ['s19'],
    's21': ['s19', 's22'],
    's22': ['s21']
         }

def bfs(start, goal, qraph):
    queue = deque([start])
    visited = {start: None}

    while queue:
        cur_node = queue.popleft()
        if cur_node == goal:
            break

        next_nodes = graph[cur_node]
        for next_node in next_nodes:
            if next_node not in visited:
                queue.append(next_node)
                visited[next_node] = cur_node

    return visited

start = 'f17'
goal = 's22'

def getPath(goal, start):

    viseted = bfs(start, goal, graph)
    cur_node = goal

    print(f'path from {goal} to {start}: \n {goal}', end='')

    way = []
    way.append(goal)

    while cur_node != start:
        cur_node = viseted[cur_node]
        way.append(cur_node)
        print(f' ---> {cur_node} ', end='')

    #print(f'\n{way}')

    draw_by_points(way)

