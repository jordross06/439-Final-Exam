#!/usr/bin/env python
# coding: utf-8

# In[99]:


# upload strings to
import pandas as pd
df = pd.read_csv("sampledna.txt.txt")
some_list = df.values.tolist()
# Function to calculate the number of possible combinations of substrings given k
# k = number of substrings that you want 
def calc_poss_substring(string, k):
    return(len(string) - k +1)


# In[100]:


poss_kmers = calc_poss_substring(some_list, 5)
poss_kmers


# In[102]:


# Creates a function that calculates the observed kmers in the list
def calc_obs_kmers(string, k):
    count = []
    # Calculate how many kmers of length k there are
    num_kmers = len(string) - k + 1
    # Loop over the kmer start positions
    for i in range(num_kmers):
        # Slice the string to get the kmer
        kmer = string[i:i+k]
        # Add the kmer to the dictionary if it's not there
        if kmer not in count:
            count[kmer] = 0
        # Increment the count for this kmer
        count[kmer] += 1
    # Return the final counts
    return count


# In[104]:


obs_kmers = count_kmers(some_list,2)
obs_kmers


# In[105]:


# Creates a function to input the possible and observed kmers into a data frame
    data = {'Possible':[possible], 'Observed':[observed]}
    df = pd.DataFrame(data)
    print(df)
    return


# In[106]:


kmers_df = df_table(poss_kmers, len(obs_kmers))
kmers_df


# In[107]:


# Creates a function that calculates the linguistic complexity
def ling_complex(df):
    df1 = sum(df(axis = 1))
    df2 = sum(df(axis = 2))
    ling = df1/df2
    return ling


# In[108]:


ling_complex(kmers_df)


# In[ ]:




