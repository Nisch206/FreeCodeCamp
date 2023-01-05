import numpy as np

def calculate(list):
  if len(list) <9:
      raise ValueError('List must contain nine numbers.')
  else:
      # initializing dictionary:
      calculations = {'mean' : '', 'variance' : '', 'standard deviation' : '', 'max' : '', 'min' : '', 'sum' : ''}  
  
      # Values for flattened matrix
      storage = np.array([list[0:3], list[3:6], list[6:9]])
      s_min = storage.min()
      s_max = storage.max()
      s_sum = storage.sum()
      s_mean = storage.mean()
      s_var = storage.var()
      s_std = storage.std()
  
      # values across the rows
      s_min_row = storage.min(0)
      s_max_row = storage.max(0)
      s_sum_row = storage.sum(0)
      s_mean_row = storage.mean(0)
      s_var_row = storage.var(0)
      s_std_row = storage.std(0)
  
       # values across the column
      s_min_col = storage.min(1)
      s_max_col = storage.max(1)
      s_sum_col = storage.sum(1)
      s_mean_col = storage.mean(1)
      s_var_col = storage.var(1)
      s_std_col = storage.std(1)
  
      # update dictionary
      # .tolist() converts numpy array to python list
      calculations.update({"min": [s_min_row.tolist(), s_min_col.tolist(), s_min]})
      calculations.update({"max": [s_max_row.tolist(), s_max_col.tolist(), s_max]})
      calculations.update({"sum": [s_sum_row.tolist(), s_sum_col.tolist(), s_sum]})
      calculations.update({"mean": [s_mean_row.tolist(), s_mean_col.tolist(), s_mean]})
      calculations.update({"variance": [s_var_row.tolist(), s_var_col.tolist(), s_var]})
      calculations.update({"standard deviation": [s_std_row.tolist(), s_std_col.tolist(), s_std]})




  return calculations