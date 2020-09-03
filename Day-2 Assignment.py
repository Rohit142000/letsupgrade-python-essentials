#!/usr/bin/env python
# coding: utf-8

# # List and its default functions

# In[59]:


lst=["RS",100,10.2]
lst


# In[60]:


lst.append("RN")
lst


# In[63]:


lst.reverse()
lst


# In[68]:


lst.count(10.2)


# In[70]:


lst.insert(2,"python")


# In[71]:


lst


# In[72]:


lst.pop(3)
lst


# # Dictionary and its default function

# In[74]:


dit={"name":"RN","number":123456789}
dit


# In[79]:


dit.items()


# In[80]:


dit.keys()


# In[81]:


dit.fromkeys(dit)


# In[85]:


dit.values()


# In[88]:


dit.popitem()


# # Sets and its default functions

# In[90]:


st={"RS",1,1,2,3,4,5,5}
st


# In[91]:


st.add("letsupgrade")


# In[92]:


st


# In[99]:


st.pop()


# In[101]:


st.issubset("RS")


# In[108]:


st={"a","b","c"}
st1={"b","c","g"}
st.difference(st1)


# In[110]:


st.clear()
st


# # Tuple and its default functions

# In[111]:


tup={"RS","@","letsupgrade.in"}
tup


# In[113]:


tup.add(210)
tup


# In[114]:


tup.remove(210)
tup


# In[117]:


tup.pop()


# In[120]:


tup={"rs","@","lets.in"}
tup1={"rn","@","lets.com"}
tup.difference(tup1)


# In[121]:


tup.clear()


# In[122]:


tup


# # Strings and its default function

# In[123]:


name="rs"
name


# In[124]:


type(name)


# In[127]:


name.capitalize()


# In[131]:


name.center(9)


# In[134]:


name.count("rs")


# In[144]:


name.find("r")


# In[146]:


name.index("rs")


# In[163]:


name.upper()


# In[164]:


name.isalpha()


# In[ ]:




