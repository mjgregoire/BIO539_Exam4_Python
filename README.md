# Exam4_Python

This script (exam4.py) is used to assess the number of substrings of length k, or k-mers, that are observed and possible for a sequence (termed "read"). It can also determine the linguistic complexity of the kmer, or the number of kmers that are observed for all possible kmer lengths divided bythe total possible kmers. For simplicity, this script will only test for the letters of DNA: A, T, G, C.

This script is run in the command line as follows:
python3 exam4.py -read ATTTGGATT -k 3

The user needs to define what sequence or "read" they want to analyze as well as what length of k as arguments on the command line. Each time the user wants to analzye a new read or k the command must be re-typed into the command line and the results will be appended to the existing output files.

The script will give two output files, one for the linguistic complexity of the entered read and k, and one with a dataframe of all the observed and possible kmers for the entered read and k. 

The script contains a function to count the observed kmers of size k, the possible kmers of size k, a resulting table of the observed and possible kmers, as well as the linguistic complexity of the entered sequence and k. 

I have added example output files ("linguistic_complexity.txt", "dataframe.csv") to this repository for the following reads and ks:

* -read ATTTGGATT -k 3
* -read CGGTACGAT -k 2
* -read CAGGGCTAT -k 6
* -read TCGTAGGAC -k 1

The script has been tested with py.test (test_exam4.py) and each of the functions passed. 
