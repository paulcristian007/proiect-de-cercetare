from graph import Graph


class Modularity(Graph):
    def __init__(self, graph):
        super().__init__(graph)


    def f(self, neighbors):
        sum = 0
        communities = super().getCommunities(neighbors)
        for i in range(0, self._n):
            for j in range(0, self._n):
                value = int(self._matrix[i][j]) - len(self._edges[i]) * len(self._edges[j]) / (2 * self._m)
                if communities[i] != communities[j]:
                    value = 0
                sum += value

        return sum / (2 * self._m)

    def calc(self, communities):
        sum = 0
        for i in range(0, self._n):
            for j in range(0, self._n):
                value = int(self._matrix[i][j]) - len(self._edges[i]) * len(self._edges[j]) / (2 * self._m)
                if communities[i] != communities[j]:
                    value = 0
                sum += value

        return sum / (2 * self._m)
