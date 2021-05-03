#!/usr/bin/env python3

#this script will tell you all the observed kmers and possible kmers
#Example how to use: python3 exam4.py -read ATTTGGATT -k 3
#run the script in the command line and change the read and k to get different results

import pandas as pd #import the dataframe builder

import argparse #import program to write user-friendly command-line interfaces

#putting the arguments section into a block to prevent the code from being run if file is imported into another as a module
if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('-read') #after -read you can put the read value when you run the program
  parser.add_argument('-k') #after -k you can put the k value when you run the program
  args = parser.parse_args() 
  read = args.read #the read value will come from what the user enters
  k = int(args.k) #the k value as an integer will be what the user enters

  
#different method of how to input the info into the command line:
#read = input("Enter read: ")
#k= int(input("Enter k: "))


#### Question 1 ####
# function to count observed kmers (COUNT KMERS OF SIZE K) 
def count_kmers_observed(read, k):
  '''
  This function is used to count kmers of size k. It will tell you the number of observed kmers
  '''
  counts = {} #Start with an empty dictionary
  num_kmers = len(read) - k + 1 #Calculate how many kmers of length k there are
  for i in range (num_kmers): #Loop through kmer start positions
      kmer= read[i:i+k] #Slice the string to get the kmer
      if kmer not in counts:  #Add the kmer to the dictionary if it's not there
          counts[kmer] = 0 #Increment the count for this kmer
      counts[kmer] +=1
  return counts
 
#print(len(count_kmers_observed(read, k))), print("is the kmers of size k")

  

# function to count possible kmers
#num_kmers = []
def count_kmers_possible(read, k):
  '''
  This function will count the number of all possible kmers
  '''
  num_kmers = {}
  num_kmers1 = len(read) - k + 1
  num_kmers2 = 4**k
  num_kmers = min(num_kmers1,num_kmers2)
  return num_kmers



#### Question 2 #####
## function to create pandas df of possible and observed kmers ##

def create_panda(read):
  '''
  This function creates the pandas dataframe for the number of k, observed kmers, and possible kmers
  '''
  k_values = [] #get first column: number of ks, make an empty list to append to
  for i in range(1,len(read)+1): #loop through the length of the read, since len() doesn't include the last number in the range, add 1
    k_values.append(i)
  observed_kmers = [] #get second column: observed kmers, empty list
  for i in k_values: #loop through each value of k and get the observed kmers from the count_kmers_observed function
    observed_kmers.append(len(count_kmers_observed(read, i)))
  possible_kmers = [] #get third column: possible kmers
  for i in k_values:
    possible_kmers.append(count_kmers_possible(read, i))
  df = pd.DataFrame(list(zip(k_values, observed_kmers, possible_kmers)), columns = ['k','observed kmers','possible kmers'])
  df.at['Total', 'observed kmers'] = df['observed kmers'].sum() #add total observed kmer value
  df.at['Total', 'possible kmers'] = df['possible kmers'].sum() #add total possible kmer value
  return df
#create_panda(read)

#### Question 3 ####
#function to calculate total linguistic complexity (total observed/ total possible)
def calculate_LC(read):
  '''
  This function calculates the total linguistic complexity which is the total observed kmers divided by the total posssible kmers
  '''
  k_values = [] 
  for i in range(1,len(read)+1): 
    k_values.append(i) 
  observed_kmers = [] 
  for i in k_values: 
    observed_kmers.append(len(count_kmers_observed(read, i)))
  possible_kmers = [] 
  for i in k_values:
    possible_kmers.append(count_kmers_possible(read, i))
  df = pd.DataFrame(list(zip(k_values, observed_kmers, possible_kmers)), columns = ['k','observed kmers','possible kmers'])
  df.at['Total', 'observed kmers'] = df['observed kmers'].sum()
  df.at['Total', 'possible kmers'] = df['possible kmers'].sum()
  x = int(df.at['Total','observed kmers']) #isolate the total for observed kmers and assign it to a variable x
  y = int(df.at['Total','possible kmers']) #isolate the total for possible kmers and assign it to a variable y
  LC =  (x/y)
  #print(LC), print("is the linguistic complexity") 
  return LC
#calculate_LC(read)


#### Question 4 Be sure that all your functions have appropriate docstrings ####

#### Question 5 ####
#Use the main function in your script to read in your file and output results to files
#putting the main function into a block to prevent from being run if file is imported into another as a module
#this needs to be separate from the first if __name__== '__main__' section because this needs the arguments from the first to run throughout the script
if __name__ == '__main__':
  def main():
    '''
    This function is used to save the output from the input that is typed on the command line. 
    It saves the output into two files, one for linguistic complexity and one for the dataframe.
    '''
    with open("linguistic_complexity.txt",'a+') as f: #open file and use append and read mode
      f.seek(0) #move cursor to start of file
      data= f.read() #scan through the file to see if there is information there
      if len(data) >0 : #if file is not empty then append '\n' or at the end
        f.write("\n")
      LingC = calculate_LC(read)
      f.write(str(LingC)) #append the LingC (LC) value
      f.close()
    panda = create_panda(read)
    panda.to_csv('dataframe.csv', mode ='a+') #open and append to pandas dataframe
    
  main()


#### Question 6 ####
#Script to thoroughly test each of your functions: test_exam4.py

#### Question 7 --Comments  included thorughout code ####

#### Question 8 --github repository created with README ####
