import random

import networkx as nx


class Graph:
    def __init__(self, graph):
        self._matrix = nx.to_numpy_array(graph)
        self._n = len(self._matrix)
        self._m = 0
        self._edges = self.addEdges()


    def getEdges(self, pos):
        return self._edges[pos]

    def addEdges(self):
        ans = []
        for i in range(0, self._n):
            curr = []
            for j in range(0, self._n):
                if int(self._matrix[i][j]) == 1:
                    curr.append(j)
                    self._m += 1

            ans.append(curr)

        self._m = int(self._m / 2)

        return ans


    def makeLinks(self, neighbors):
        links = []
        for _ in range(0, self._n):
            links.append([])

        for i in range(0, self._n):
            j = neighbors[i]
            if j not in links[i]:
                links[i].append(j)
            if i not in links[j]:
                links[j].append(i)
        return links


    def dfs(self, vis, node, links, community, communities):
        vis[node] = True
        communities[node] = community
        for target in links[node]:
            if not vis[target]:
                self.dfs(vis, target, links, community, communities)

    def getCommunities(self, neighbors):
        links = self.makeLinks(neighbors)
        community = 0
        vis = [False] * self._n
        communities = [-1] * self._n
        for i in range(0, self._n):
            if not vis[i]:
                community += 1
                self.dfs(vis, i, links, community, communities)

        return communities

    def randomNeighbors(self):
        neighbors = []
        for i in range(0, self._n):
            j = random.randint(0, len(self._edges[i]) - 1)
            neighbors.append(self._edges[i][j])
        return neighbors