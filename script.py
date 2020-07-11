import numpy as np
from collections import OrderedDict

def calculate(list):
  # only accept 3*3 matrix = 9 elements
  if len(list) == 9:
    # convert into 3 * 3 matrix
    matrix = np.array(list).reshape(3,3)

    calculations = OrderedDict()

    keys = ['mean','variance', 'standard deviation',
    'max','min','sum']
    #create empty list for each keys
    for val in keys:
      calculations[val] = []
    # calculations : axis 0 ( columns ) , axis = 1 ( rows ), flattened
    calculations['mean'] = [matrix.mean(axis = 0), matrix.mean(axis = 1), np.mean(matrix)]
    calculations['variance'] = [matrix.var(axis = 0), matrix.var(axis = 1), np.var(matrix)]
    calculations['standard deviation'] = [matrix.std(axis = 0), matrix.std(axis = 1), np.std(matrix)]
    calculations['max'] = [matrix.max(axis = 0), matrix.max(axis = 1), np.max(matrix)]
    calculations['min'] = [matrix.min(axis = 0), matrix.min(axis = 1), np.min(matrix)]
    calculations['sum'] = [matrix.sum(axis = 0), matrix.sum(axis = 1), np.sum(matrix)]

    # convert the arrays in list to list
    for keys in calculations:
       calculations[keys] = [val.tolist()for val in calculations[keys]]
           
    return calculations
  else:
    # print error
    raise ValueError("List must contain nine numbers.")
