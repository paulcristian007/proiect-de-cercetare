from graph import Graph


class MyFunction2(Graph):
    def __init__(self, graph):
        super().__init__(graph)

    def f(self, neighbors):
        communities = self.getCommunities(neighbors)
        cntNodes = [0] * self._n

        for i in range(0, self._n):
            cntNodes[communities[i]] += 1

        score = 0
        for i in range(0, self._n):
            innerEdges = 1
            outerEdges = 0
            for j in self._edges[i]:
                if communities[i] == communities[j]:
                    innerEdges += 1
                else:
                    outerEdges += 1

            nodeScore = innerEdges / cntNodes[communities[i]] - outerEdges / len(self._edges[i])

            ratio = 1 / self._n
            score += nodeScore * ratio

        return score

