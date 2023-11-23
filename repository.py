import networkx as nx


class Repository:
    def __init__(self, filepath):
        self.__graphGML = nx.read_gml(filepath, label='id')

    def getGraphGML(self):
        return self.__graphGML
    