import random


class Chromosome:
    def __init__(self, DNA, fct):
        self.__fct = fct
        self.__n = len(DNA)
        self.__DNA = DNA

    def getDNA(self):
        return self.__DNA


    def score(self):
        return self.__fct.f(self.__DNA)

    def fitter(self, other):
        return self.score() > other.score()

    def decode(self):
        return self.__fct.getCommunities(self.__DNA)


    def mutation(self):
        i = random.randint(0, self.__n - 1)
        neighbors = self.__fct.getEdges(i)
        j = random.randint(0, len(neighbors) - 1)
        self.__DNA[i] = neighbors[j]

    def crossover(self, other):
        offspringDNA = []
        mask = [random.randint(0, 1)] * self.__n
        for i in range(0, self.__n):
            if not(mask[i]):
                offspringDNA.append(self.__DNA[i])
            else:
                offspringDNA.append(other.__DNA[i])

        offspring = Chromosome(offspringDNA, self.__fct)
        return offspring
