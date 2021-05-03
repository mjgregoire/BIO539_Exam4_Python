from exam4 import *

read = "ATTTGGATT"
k = 3

def test_count_kmers_observed():
  '''
  This function is used to test the count kmers of size k function. 
  '''
  actual_result = count_kmers_observed(read,k) 
  expected_result = 6
  assert actual_result == expected_result
  

def test_count_kmers_possible():
  '''
  This function will test the count the number of all possible kmers function.
  '''
  actual_result = count_kmers_possible(read,k)
  expected_result = 7
  assert actual_result == expected_result

  
def test_create_panda():
  '''
  This function creates the pandas dataframe for the number of k, observed kmers, and possible kmers
  '''
  actual_result = create_panda(read)
  expected_result = ({'k': [1,2,3,4,5,6,7,8,9],'observed kmers': [3,5,6,6,5,4,3,2,1,35], 'possible kmers':[4,8,7,6,5,4,3,2,1,40]})
  assert actual_result == expected_result



def test_calculate_LC():
  '''
  This function tests the function to calculate total linguistic complexity 
  '''
  actual_result = calculate_LC(read)
  expected_result = 0.875
  assert actual_result == expected_result
 
