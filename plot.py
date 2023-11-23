import matplotlib.pyplot as plt
import networkx as nx
import repository


class Plot:
    def __init__(self, repo):
        self.__graph = repo.getGraphGML()
        self.__layout = nx.spring_layout(self.__graph)

    def getGraph(self):
        return self.__graph

    def plotNetwork(self, score, communities):
        nx.draw_networkx_nodes(self.__graph, pos=self.__layout, node_size=100, node_color=communities, alpha=0.7)
        nx.draw_networkx_edges(self.__graph, pos=self.__layout, edge_color="black", alpha=0.8)

        # Show the plot
        plt.title(score)
        plt.figure(figsize=(32, 32))  # image is 8 x 8 inches
        plt.axis("off")
        plt.show()


