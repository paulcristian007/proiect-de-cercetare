from function.modularity import Modularity
from function.myfunction1 import MyFunction1
from function.myfunction2 import MyFunction2
from plot import Plot
from graph import Graph
from repository import Repository
from population import Population


def main():
    repo = Repository('tests/test2.gml')
    p = Plot(repo)
    g = Graph(repo.getGraphGML())
    modularity = Modularity(p.getGraph())
    myfunction1 = MyFunction1(p.getGraph())
    myfunction2 = MyFunction2(p.getGraph())

    population = Population(1, 20, modularity, p)
    coms = population.evolutionLoop()
    print(modularity.calc(coms))

main()