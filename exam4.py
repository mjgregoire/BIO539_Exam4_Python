#!/usr/bin/env python3

#Example how to use: python3 exam4.py -read ATTTGGATT -k 3

import pandas as pd #import the dataframe builder

import argparse #import program to write user-friendly command-line interfaces
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
    counts = {} #Start with an empty dictionary
    num_kmers = len(read) - k + 1 #Calculate how many kmers of length k there are
    for i in range (num_kmers): #Loop through kmer start positions
        kmer= read[i:i+k] #Slice the string to get the kmer
        if kmer not in counts:  #Add the kmer to the dictionary if it's not there
            counts[kmer] = 0 #Increment the count for this kmer
        counts[kmer] +=1
    return counts
 
print(len(count_kmers_observed(read, k)))
  

# function to count possible kmers
#num_kmers = []
def count_kmers_possible(read, k):
  num_kmers = {}
  num_kmers1 = len(read) - k + 1
  num_kmers2 = 4**k
  num_kmers = min(num_kmers1,num_kmers2)
  return num_kmers
#print(len(count_kmers_observed(read,k)))



#### Question 2 #####
## function to create pandas df of possible and observed kmers ##

#get first column: number of ks
k_values = [] #make an empty list to append to
for i in range(1,len(read)+1): #loop through the length of the read
  #since len() doesn't include the last number in the range, add 1
  k_values.append(i) #append into the list
#print(k_values)


#get second column: observed kmers
observed_kmers = []
#loop through each value of k and get the observed kmers from the count_kmers_observed function
#this time you use i as the input so you can get each iteration of k from k_values, rather than using the variable k which comes from command line
for i in k_values:
  observed_kmers.append(len(count_kmers_observed(read, i)))
#print(observed_kmers)


#get third column: possible kmers
possible_kmers = []
for i in k_values:
  possible_kmers.append(count_kmers_possible(read, i))
#print(possible_kmers)
  
#create df
df = pd.DataFrame(list(zip(k_values, observed_kmers, possible_kmers)), columns = ['k','observed kmers','possible kmers'])
df.at['Total', 'observed kmers'] = df['observed kmers'].sum() #add total of observed kmers to dataframe
df.at['Total', 'possible kmers'] = df['possible kmers'].sum() #add total of possible kmers to dataframe
print (df)



#### Question 3 ####
#function to calculate total linguistic complexity (total observed/ total possible)
x = int(df.at['Total','observed kmers']) #isolate the total for observed kmers and assign it to a variable x
y = int(df.at['Total','possible kmers']) #isolate the total for possible kmers and assign it to a variable y

LC =  (x/y)
print(LC)

#4. Be sure that all your functions have appropriate docstrings.
#5. Use the main function in your script to read in your file and output results to files.
#6. Write a script to thoroughly test each of your functions.
#7. Include thorough comments for all of your code.
#8. Create a github repository including a README (in markdown) to submit your work.


