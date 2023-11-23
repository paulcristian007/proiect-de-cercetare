import random
from chromosome import Chromosome


class Population:
    def __init__(self, iterations, popSize, fct, plot):
        self.__popSize = popSize
        self.__iterations = iterations
        self.__fct = fct
        self.__plot = plot
        self.__population = []


    def createFirstGeneration(self):
        for _ in range(0, self.__popSize):
            self.__population.append(Chromosome(self.__fct.randomNeighbors(), self.__fct))

    def bestChromosome(self):
        pos = 0
        for i in range(1, self.__popSize):
            if self.__population[i].fitter(self.__population[pos]):
                pos = i

        return pos

    def worstChromosome(self):
        pos = 0
        for i in range(1, self.__popSize):
            if not(self.__population[i].fitter(self.__population[pos])):
                pos = i

        return pos

    def selection(self):
        # We generate randomly 2 individuals that will compete with each other
        x = self.__population[random.randint(0, self.__popSize - 1)]
        y = self.__population[random.randint(0, self.__popSize - 1)]

        # the fittest one will win the selection contest
        if x.fitter(y):
            return x
        return y


    def steadyState(self):
        chr1 = self.selection()
        chr2 = self.selection()

        offspring = chr1.crossover(chr2)
        offspring.mutation()
        worst = self.worstChromosome()
        if offspring.fitter(self.__population[worst]):
            self.__population[worst] = offspring

    def oneGeneration(self):
        newPop = []
        for _ in range(self.__popSize):
            p1 = self.selection()
            p2 = self.selection()
            off = p1.crossover(p2)
            off.mutation()
            newPop.append(off)
        self.__population = newPop


    def evolutionLoop(self):
        self.createFirstGeneration()
        bestScore = -1000.0
        bestChromosome = None
        for iteration in range(0, self.__iterations):
            self.oneGeneration()
            scores = []
            for chr in self.__population:
                score = chr.score()
                scoreStr = "{:.2f}".format(score)
                scores.append(scoreStr)
                if score > bestScore:
                    bestScore = score
                    bestChromosome = chr


            print(scores)

            if iteration % 10 == 0:
                self.__plot.plotNetwork(bestScore, bestChromosome.decode())

        self.__plot.plotNetwork(bestScore, bestChromosome.decode())
        print(bestChromosome.decode())
        return bestChromosome.decode()



