#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import time
import json as JSON
pd.options.mode.chained_assignment = None


# ## Data Import

# In[2]:


dfile = pd.read_csv("dataset/Test Case Dataset.csv")
dfile


# ## Data Pre-Processing

# In[3]:


dfile = dfile.drop(["TEST STEPS","TEST DATA","EXPECTED RESULT", "ACTUAL RESULT", "PASS/FAIL"], axis=1)


# In[4]:


dummies = pd.get_dummies(dfile['PRECEDENCE'])
dfile = pd.concat([dfile, dummies], axis=1)


# In[5]:


PRE_CON_COUNT = [0]*dfile['TEST ID'].count()
dfile['PRE_CON_COUNT'] = PRE_CON_COUNT


# In[6]:


dfile['PRE-CONDITIONS'].unique()


# In[7]:


def childPCC(this):
    if this in dfile['PRE-CONDITIONS'].values:
        return len(dfile.loc[dfile['PRE-CONDITIONS'] == this,'TEST ID'])
    else:
        return 0


# In[8]:


for ids in dfile['TEST ID']:
    if ids in dfile['PRE-CONDITIONS'].values:
        dfile.loc[
            dfile['TEST ID'] == ids,'PRE_CON_COUNT'] = dfile.loc[dfile['PRE-CONDITIONS'] == ids,'TEST ID'].count()
    
        for sub in list(dfile.loc[dfile['PRE-CONDITIONS'] == ids,'TEST ID']):
                dfile.loc[ dfile['TEST ID'] == ids,'PRE_CON_COUNT' ] += childPCC(sub)


# In[9]:


dfile['PRE_CON_COUNT'].values


# In[10]:


dfile


# ## 'WEIGHTAGE' column

# In[11]:


weightage = [0]*dfile['TEST ID'].count()
dfile['WEIGHTAGE'] = weightage


# In[12]:


dfile.head()


# In[13]:


dfile['WEIGHTAGE'] = (dfile['H']*0.9 + 
                      dfile['M']*0.5 +
                      dfile['L']*0.1 +
                      (dfile['PRE_CON_COUNT'])) * (dfile['COMPLEXITY'])
dfile


# In[14]:


print( dfile['WEIGHTAGE'].max())


# ## Objective Function of the system

# In[15]:


def objectiveFn(arguments):
    x1, x2, x3, x4, x5 = arguments
    
    if x2 == x3:
        x3 = 0
    if x1 == x2 or x1 == x3:
        x2 = x3 = 0
    if x3 > x1 and x3 > x2:
        x1 = x2 = 0
    if x2 > x1 and x2 > x3:
        x1 = x3 = 0
    if x1 > x2 and x1 > x3:
        x2 = x3 = 0

    return (x1*0.9 + x2*0.5 + x3*0.1 + x4)*x5


# In[16]:


maximumIterations = 50


# ## Best values from Particle Swarm Optimization

# In[17]:


from algo.PSO import PSO

pso_before = time.time()

instance = PSO(func=objectiveFn,
               dim=5,
               pop=100,
               lb=[0, 0, 0, dfile['PRE_CON_COUNT'].min(), dfile['COMPLEXITY'].min()],
               ub=[1, 1, 1, dfile['PRE_CON_COUNT'].max(), dfile['COMPLEXITY'].max()],
               w=0.6, c1=0.7, c2=0.7
              )
pso_result = instance.run(max_iter=maximumIterations)

pso_time = time.time() - pso_before

print("Best values of x: ", pso_result.gbest_x )
print("Best values of f(x): ", pso_result.gbest_y )


# In[18]:


print("--- PSO took %f seconds ---" % pso_time)


# ## PSO result

# In[19]:


pso_dfile = dfile.copy()


# In[20]:


pso_dfile['DIFF'] = abs( pso_result.gbest_y - pso_dfile['WEIGHTAGE'] )
# pso_dfile['DIFF'] = abs(
#     pso_result.gbest_x[0] - pso_dfile['H']+
#     pso_result.gbest_x[1] - pso_dfile['M']+
#     pso_result.gbest_x[2] - pso_dfile['L']+
#     pso_result.gbest_x[3] - pso_dfile['PRE_CON_COUNT']+
#     pso_result.gbest_x[4] - pso_dfile['COMPLEXITY']
# )
pso_dfile.sort_values('DIFF', ascending=True, axis=0, inplace = True)


# In[21]:


pso_dfile = pso_dfile.drop(['H', 'L', 'M'], axis=1)
pso_dfile = pso_dfile.reset_index(drop=True)


# In[22]:


pso_dfile


# ## Best values from Genetic Algorithm

# In[23]:


from algo.GA import GeneticAlgorithm

ga_before = time.time()

ga = GeneticAlgorithm(
    fitness_function=objectiveFn,
    pop_size=100,
    genome_length=5,
    lb=[0, 0, 0, dfile['PRE_CON_COUNT'].min(), dfile['COMPLEXITY'].min()],
    ub=[1, 1, 1, dfile['PRE_CON_COUNT'].max(), dfile['COMPLEXITY'].max()]
)
ga.generate_binary_population()
ga.number_of_pairs = 4
ga.selective_pressure = 1.4
ga.mutation_rate = 0.2
ga.run(maximumIterations)

ga_time = time.time() - ga_before

best_genome, best_fitness = ga.get_best_genome()
print("Best values for x: ", best_genome )
print("Best value for f(x):", best_fitness )


# In[24]:


print("--- GA took %f seconds ---" % ga_time)


# ## GA result

# In[25]:


ga_dfile = dfile.copy()


# In[26]:


ga_dfile['DIFF'] = abs( best_fitness - ga_dfile['WEIGHTAGE'] )
# ga_dfile['DIFF'] = abs(
#     best_genome[0] - ga_dfile['H']+
#     best_genome[1] - ga_dfile['M']+
#     best_genome[2] - ga_dfile['L']+
#     best_genome[3] - ga_dfile['PRE_CON_COUNT']+
#     best_genome[4] - ga_dfile['COMPLEXITY']
# )
ga_dfile.sort_values('DIFF', ascending=True, axis=0, inplace = True)


# In[27]:


ga_dfile = ga_dfile.drop(['H', 'L', 'M'], axis=1)
ga_dfile = ga_dfile.reset_index(drop=True)


# In[28]:


ga_dfile


# ## Comparative Study

# In[29]:


equality = 1
for i in range( pso_dfile['TEST ID'].count() ):
    if pso_dfile['TEST ID'][i] != ga_dfile['TEST ID'][i]:
        print(pso_dfile['TEST ID'][i]," is different from ", ga_dfile['TEST ID'][i]," at row ",i)
        equality = 0
        break


# In[30]:


customer_rank = pd.read_csv("dataset/Test Customer Ranking.csv")


# In[31]:


pso_accuracy= 0; pso_error = 0;

pso_accuracy= pso_dfile.loc[ pso_dfile['TEST ID']==customer_rank['TEST ID'], 'TEST ID' ].count()
pso_accuracy= (pso_accuracy/pso_dfile['TEST ID'].count())*100

pso_error = 100 - pso_accuracy

print("PSO accuracy: ", pso_accuracy, "%" )
print("PSO error: ", pso_error, "%" )


# In[32]:


ga_accuracy = 0; gaError = 0;

ga_accuracy = ga_dfile.loc[ ga_dfile['TEST ID']==customer_rank['TEST ID'], 'TEST ID' ].count()
ga_accuracy = (ga_accuracy/ga_dfile['TEST ID'].count())*100

ga_error = 100 - ga_accuracy

print("GA accuracy: ", ga_accuracy, "%" )
print("GA error: ", ga_error, "%" )


# In[33]:


print("PSO execution time: ",pso_time)
print("GA execution time: ", ga_time)


# ## Export results

# In[34]:


pso_dfile.to_csv('result/PSO Result.csv', index=False, encoding='utf-8')
ga_dfile.to_csv('result/GA Result.csv', index=False, encoding='utf-8')

pso_dfile.to_csv('result/PSO Result.tsv', sep="\t",index=False, encoding='utf-8')
ga_dfile.to_csv('result/GA Result.tsv', sep="\t",index=False, encoding='utf-8')


# In[35]:


result = {
    "PSO":{
        "x" : pso_result.gbest_x.tolist(),
        "fx" : int(pso_result.gbest_y),
        "xaxis" : list(pso_result.xaxis),
        "yaxis" : list(pso_result.yaxis),
        "time" : float(pso_time),
        "accuracy" : pso_accuracy
    },
    "GA":{
        "x" : best_genome.tolist(),
        "fx" : int(best_fitness),
        "xaxis" : list(ga.xaxis),
        "yaxis" : list(ga.yaxis),
        "time" : float(ga_time),
        "accuracy" : ga_accuracy
    },
    "Equality": equality,
    "maximumIterations": maximumIterations
}
result_json = JSON.dumps( result )

File = open('result/result.json', 'w')
File.write( result_json )


# In[36]:


File.close()


# ## Export to python script file

# In[37]:


# Convert to python3 script file

get_ipython().system('jupyter nbconvert --to script "Test Case Opt"')

