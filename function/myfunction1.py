from graph import Graph


class MyFunction1(Graph): 
    def __init__(self, graph):
        super().__init__(graph)

    def f(self, neighbors):
        communities = super().getCommunities(neighbors)
        cntNodes = [0] * len(communities)                # How many nodes does every community contain
        cntEdges = [0] * len(communities)                # How many edges connects any 2 nodes in the same community

        # for every node, increment the NODE counter for the community it belongs to
        for i in range(0, self._n):
            cntNodes[communities[i]] += 1

        # for every edge that has both vertices in the same community,
        # increment the EDGE counter for the community they belong to
        totalEdges = 0
        for i in range(0, self._n):
            for j in self._edges[i]:
                if i < j and communities[i] == communities[j]:
                    cntEdges[communities[i]] += 1
                    totalEdges += 1

        ans = 0
        for i in range(0, len(communities)):
            if cntNodes[i] > 1:
                ans += cntEdges[i] / (cntNodes[i] * (cntNodes[i] - 1) / 2)
        ans /= len(communities)
        ans *= totalEdges / self._m


        return ans

