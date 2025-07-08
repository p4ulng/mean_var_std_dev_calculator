import numpy as np

def calculate(input_list):
   if len(input_list) != 9:
      raise ValueError("List must contain nine numbers.")
      
   matrix=[]
   helper=[]
   for i in input_list:
    helper.append(i)
    if len(helper)==3:
        matrix.append(helper)
        helper=[]
   matrix = np.array(matrix)
   calculations={
        'mean':[matrix.mean(axis=0).tolist(),matrix.mean(axis=1).tolist(),matrix.mean().tolist()]
         ,'variance':[matrix.var(axis=0).tolist(),matrix.var(axis=1).tolist(),matrix.var().tolist()]
         ,'standard deviation':[matrix.std(axis=0).tolist(),matrix.std(axis=1).tolist(),matrix.std().tolist()]
         ,'max':[matrix.max(axis=0).tolist(),matrix.max(axis=1).tolist(),matrix.max().tolist()]
         ,'min':[matrix.min(axis=0).tolist(),matrix.min(axis=1).tolist(),matrix.min().tolist()]
         ,'sum':[matrix.sum(axis=0).tolist(),matrix.sum(axis=1).tolist(),matrix.sum().tolist()]
    }

   return calculations

print(calculate([0,1,2,3,4,5,6,7,8]))