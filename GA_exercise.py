import numpy as np
import random


chr = np.ones((4, 8), dtype=np.int)

chr[0] = [6, 5, 4, 1, 3, 5, 3, 2]
chr[1] = [8, 7, 1, 2, 6, 6, 0, 1]
chr[2] = [2, 3, 9, 2, 1, 2, 8, 5]
chr[3] = [4, 1, 8, 5, 2, 0, 9, 4]

# print(chr[1])


def fitness(chri):

    fitness = chri[0] + chri[1] - chri[2] + chri[3] + chri[4] + chri[5] - chri[6] + chri[7]

    return fitness

def crossover(chr1, chr2, type):
    child1_gen = np.empty(len(chr1))
    child1_gen.fill(np.NaN)
    child2_gen = np.empty(len(chr2))
    child2_gen.fill(np.NaN)

    splice_len = np.floor(len(chr1) / 2)
    if type == 'p1':
        starting_gene = 0  # int(random.randrange(len(chr1) - splice_len))
        end_gene = int(starting_gene + splice_len)
    elif type == 'p2':
        starting_gene = 0  # int(random.randrange(len(chr1) - splice_len))
        end_gene = int(starting_gene + splice_len)
    elif type == 'pu':
        splice_len = np.floor(len(chr1) / 3.0 + 0.5)
        starting_gene = int(random.randrange(len(chr1) - splice_len))
        end_gene = int(starting_gene + splice_len)


    def transfer_rest(in1, in2, child_gen):

        # transfer across a piece from parent 2 to child 1
        # (or vice versa depending on the arguments' order)


        child_gen[starting_gene:end_gene] = in2[starting_gene:end_gene]

        # transfer the rest from the other parent
        # without internal repetitions

        k = end_gene - 1
        j = end_gene - 1

        while True:
            k += 1
            if k > len(in1) - 1:
                k -= len(in1)
            if k == starting_gene:
                break
            while in1[j] in child_gen:
                j += 1
                if j > len(in1) - 1:
                    j -= len(in1)
                if j == end_gene - 1:
                    break  # double stranded break!
            child_gen[k] = in1[j]

        return child_gen.astype(int)

    # apply function to both children's DNAs
    child1 = transfer_rest(chr1, chr2, child1_gen)
    child2 = transfer_rest(chr2, chr1, child2_gen)

    return [child1, child2]


fitnesses = np.zeros(4).astype(int)

# get all fitnesses of initial chromosomes
for i in range(0, (chr.shape[0])):
    print(fitness(chr[i]))
    fitnesses[i] = fitness(chr[i])

# order and store indexes bestfitnesses
bestFitnesses_index = np.argsort(fitnesses)
#print(bestFitnesses_index)

c1, c2 = crossover(chr[bestFitnesses_index[-1]], chr[bestFitnesses_index[-2]], 'p1')

c3, c4 = crossover(chr[bestFitnesses_index[-2]], chr[bestFitnesses_index[-3]], 'p2')

c5, c6 = crossover(chr[bestFitnesses_index[-1]], chr[bestFitnesses_index[-3]], 'pu')

print(c1, c2)

print(c3, c4)

print(c5, c6)

# get all fitnesses of children
for i in range(0, (chr.shape[0])):
    print(fitness(chr[i]))
    fitnesses[i] = fitness(chr[i])

#print(fitness(chr[bestFitnesses_index[-1]]), fitness(chr[bestFitnesses_index[-2]]))

print(fitness(c1), fitness(c2))
