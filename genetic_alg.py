from random import randint, choice, uniform, shuffle
from datetime import datetime
from pprint import pprint 

def create_individus(n_population, n_genes):
  res = []
  for index in range(n_population):
    res.append([randint(0, 1) for gene in range(n_genes)])
  return res

def get_fitness_score(individu):
  return sum(individu)

def parent_selections(sample):
  '''
  Random 50% selection
  '''
  trigger = int(len(sample)/2)
  sort = sorted(sample, key=get_fitness_score, reverse=True)
  if len(sort[0:trigger])%2==0:
    return sort[0:trigger]
  else:
    return sort[0:trigger+1]

def mutate(individu):
  for index_g, gene in enumerate(individu):
    if uniform(0.0, 1.0)<=0.15:
      individu[index_g] = 1 if individu[index_g]==0 else 0
  return individu

def crossover(sample, n):
  new_sample = sample.copy()
  shuffle(new_sample)
  length = len(new_sample[0])
  for index in range(0, len(new_sample), 2):
    in1 = new_sample[index]
    in2 = new_sample[index+1]
    new_sample.append(mutate(in1[0:length] + in2[length:]))
    new_sample.append(mutate(in2[0:length] + in1[length:]))
  return new_sample



if __name__ == '__main__':
  start = datetime.now()
  i = 0
  POPULATION = 20
  GENE_LENGTH = 16
  individus = create_individus(POPULATION, GENE_LENGTH)
  max_fitness = get_fitness_score(max(individus, key=get_fitness_score))
  while i < 15:# max_fitness<GENE_LENGTH:
    print("Step {} : fitness score : {}/{} -------------".format(i, max_fitness, GENE_LENGTH))
    for ind in individus:
      print(ind, " : ", get_fitness_score(ind))
    individus = crossover(parent_selections(individus), POPULATION)
    max_fitness = get_fitness_score(max(individus, key=get_fitness_score))
    i+=1
  print("Step {} : fitness score : {}/{} -------------".format(i, max_fitness, GENE_LENGTH))
  for ind in individus:
    print(ind, " : ", get_fitness_score(ind))
  print('It takes {} seconds.'.format((datetime.now() - start).seconds))