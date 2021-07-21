import numpy as np
from numpy.lib.function_base import _quantile_is_valid, quantile
from scipy.sparse.csgraph import dijkstra
from scipy.sparse import csr_matrix

import sys
input = sys.stdin.readline
n,q = map(int, input().split())

ab = [list(map(int, input().split())) for _ in range(n-1)]
cd = [list(map(int, input().split())) for _ in range(q)]

route_list = [[0]*n]*n
route_list = np.array(route_list)

for i in ab:
    route_list[i[0]-1][i[1]-1] = 1
    route_list[i[1]-1][i[0]-1] = 1

# pass_route = (shortest_path(route_list))
pass_route = dijkstra(csr_matrix(route_list))


for j in cd:
    if pass_route[j[0]-1][j[1]-1]%2 == 1:
        print("Road")
    else:
        print("Town")
