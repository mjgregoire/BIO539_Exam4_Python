from exam4 import *

def test_count_kmers_observed(read, k):
  '''
  This function is used to test the count kmers of size k function. 
  '''
  read = "ATTTGGATT"
  k = 3
  actual_result = num_kmers = len(read) - k + 1 
  for i in range (num_kmers):
      kmer= read[i:i+k] 
      if kmer not in counts:  
          counts[kmer] = 0 
      counts[kmer] +=1
  return counts
  expected_result = 6
  assert actual_result == expected_result
  

def test_count_kmers_possible(read, k):
  '''
  This function will test the count the number of all possible kmers function.
  '''
  read = "ATTTGGATT"
  k = 3
  actual_result = min(num_kmers1, num_kmers2)
  expected_result = 7
  assert actual_result == expected_result

  
def test_create_panda(read):
  '''
  This function creates the pandas dataframe for the number of k, observed kmers, and possible kmers
  '''
  read = "ATTTGGATT"
  k = 3
  actual_result_kvalues = k_values = []
  for i in range(1,len(read)+1): 
    k_values.append(i)
  actual_result_observed_kmers = [] 
  for i in k_values: 
    observed_kmers.append(len(count_kmers_observed(read, i)))
  actual_result_possible_kmers = [] 
  for i in k_values:
    possible_kmers.append(count_kmers_possible(read, i))
  actual_result_df1 = pd.DataFrame(list(zip(k_values, observed_kmers, possible_kmers)), columns = ['k','observed kmers','possible kmers'])
  actual_total_df_observed = df.at['Total', 'observed kmers'] = df['observed kmers'].sum() #add total observed kmer value
  actual_result_df = df.at['Total', 'possible kmers'] = df['possible kmers'].sum() #add total possible kmer value
  expected_result_df = ({'k': [1,2,3,4,5,6,7,8,9],'observed kmers': [3,5,6,6,5,4,3,2,1,35], 'possible kmers':[4,8,7,6,5,4,3,2,1,40]})
  assert actual_result_df == expected_result_df



def test_calculate_LC(read):
  '''
  This function tests the function to calculate total linguistic complexity 
  '''
  read = "ATTTGGATT"
  k = 3
  actual_x = int(df.at['Total','observed kmers']) 
  actual_y = int(df.at['Total','possible kmers']) 
  actual_LC = (x/y)
  expected_LC = 0.875
  assert actual_LC == expected_LC
 

def test_main():
  '''
  This tests saving the output from the input that is typed on the command line 
  '''
  actual_ling_c_txt = "linguistic_complexity.txt"
  expected_ling_c_txt = "linguistic_complexity.txt"
  actual_panda = 'dataframe.csv'
  expected_panda = 'dataframe.csv'
  assert actual_ling_c_txt == expected_ling_c_txt
  assert actual_panda == expected_panda
    
