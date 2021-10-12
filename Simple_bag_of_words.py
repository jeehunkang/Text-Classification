#!/usr/bin/env python
# coding: utf-8

# In[101]:


conda install tensorflow


# In[102]:


conda install keras


# In[103]:


from keras.preprocessing.text import Tokenizer 


# In[104]:


collection = [
'the cat sat',
'the cat sat in the hat',
'the cat with the hat'
]


# In[105]:


#step 1 

#Determining the Vocab 
tokenizer = Tokenizer()
tokenizer.fit_on_texts(collection)
print(f'vocabs: {list(tokenizer.word_index.keys())}')


# In[ ]:





# In[106]:


#step 2 
vectors = tokenizer.texts_to_matrix(collection, mode = 'count')
print(vectors)


# In[ ]:





# In[ ]:




