from exam4 import *

#Define what the reads and k you want to test are
#Based on the chosen read and k, change the expected results throughout the test script
read = "ATTTGGATT"
k = 3

#testing if the input read is wrong -this script will only test for the letters of DNA: A, T, G, C
import re
import sys
#input_str = raw_input("Please provide some info: ")
if not re.match("^[c('A','T','G','C')]*$", read):
    print("Error! Only letters A,C,T,G allowed!")
    sys.exit()
    
def test_count_kmers_observed():
  '''
  This function is used to test the count kmers of size k function. 
  '''
  actual_result = len(count_kmers_observed(read, k)) #call on the function from the exam4.py script
  expected_result = 6 #put the expected result if you run the chosen read and k
  assert actual_result == expected_result #the actual result and expected should be the same
  

def test_count_kmers_possible():
  '''
  This function will test the count the number of all possible kmers function.
  '''
  actual_result = count_kmers_possible(read,k) #call on function from exam4.py
  expected_result = 7
  assert actual_result == expected_result

  
def test_create_panda():
  '''
  This function creates the pandas dataframe for the number of k, observed kmers, and possible kmers
  '''
  #actual_result = create_panda(read)
  expected_result = pd.DataFrame(list(zip([1,2,3,4,5,6,7,8,9], [3,5,6,6,5,4,3,2,1], [4,8,7,6,5,4,3,2,1])), columns = ['k','observed kmers','possible kmers'])
  expected_result.at['Total', 'observed kmers'] = expected_result['observed kmers'].sum() 
  expected_result.at['Total', 'possible kmers'] = expected_result['possible kmers'].sum() #this is the expected table 
  
  create_panda(read).eq(expected_result) #use this pandas way (.eq) to see if the tables are the same instead of assert


def test_calculate_LC():
  '''
  This function tests the function to calculate total linguistic complexity 
  '''
  actual_result = calculate_LC(read) #call on the function from exam4.py
  expected_result = 0.875
  assert actual_result == expected_result 
