#!/usr/bin/env python
# coding: utf-8

# In[1]:


from importlib import reload
from io import StringIO

from datetime import datetime 

from decimal import *
import pandas as pd

import datacompy_raj1 as datacompy
reload(datacompy)


# In[2]:


df1 = pd.DataFrame({
        'c1':  ['a','b'],
        'c2': [1,2],
        'c3': [Decimal(1),Decimal(2)]
       })

df2 = pd.DataFrame({
        'c1':  ['a','b'],
        'c2': [1,2],
        'c3': [Decimal(1),Decimal(2)]
       })

compareData = datacompy.Compare(
                    df1,
                    df2,
                    on_index = True
                )

assert compareData.matches() == True, "Expected true, exact match"


# In[3]:


df1 = pd.DataFrame({
        'c1':  ['a','b'],
        'c2': [1,2],
        'c3': [Decimal(1),Decimal(2)]
       })

df2 = pd.DataFrame({
        'c1':  ['a','b'],
        'c2': [1,2],
        'c3': [Decimal(1),Decimal(2)]
       })

compareData = datacompy.Compare(
                    df1,
                    df2,
                    join_columns = 'c1'
                )

assert compareData.matches() == True, "Expected true, exact match using join"


# In[4]:


data1 = """c1,c2,c3
A,c,1
b,d,2
"""
data2 = """c1,c2,c3
A,cc,1
b,dd,2
"""

df1 = pd.read_csv(StringIO(data1))
df2 = pd.read_csv(StringIO(data2))

compare = datacompy.Compare(
    df1,
    df2,
    on_index=True,
    df1_name='Original', #Optional, defaults to 'df1'
    df2_name='New' #Optional, defaults to 'df2'
    )

assert compare.matches() == False, 'Expect false, c2 is different'


# In[5]:


df1 = pd.DataFrame({
        'c1':  [None,'b']
       })

df2 = pd.DataFrame({
        'c1':  [None,'b']
       })

compareData = datacompy.Compare(
                    df1,
                    df2,
                    on_index = True
                )

assert compareData.matches() == True, "Expected true, none to none"


# In[6]:


df1 = pd.DataFrame({
        'c1':  ['','b']
       })

df2 = pd.DataFrame({
        'c1':  [None,'b']
       })

compareData = datacompy.Compare(
                    df1,
                    df2,
                    on_index = True
                )

assert compareData.matches() == True, "Expected true, empty to none"


# In[7]:


df1 = pd.DataFrame({
        'c1':  [None,'a','b'],
        'c2': [None,1,2],
        'c3': [None,Decimal(1),Decimal(2)]
       })

df2 = pd.DataFrame({
        'c1':  [None,'A','b'],
        'c2': [None,1,2],
        'c3': [None,Decimal(1),Decimal(2)]
       })

compareData = datacompy.Compare(
                    df1,
                    df2,
                    join_columns = 'c1',
                    ignore_case = False
                )

assert compareData.matches() == False, "Expected false, case difference"

df1 = pd.DataFrame({
        'c1':  ['a','b']
       })

df2 = pd.DataFrame({
        'c1':  ['a','B']
       })

compareData = datacompy.Compare(
                    df1,
                    df2,
                    join_columns = 'c1',
                    ignore_case = True
                )

assert compareData.matches() == True, "Expected True, ignore_case set to true"
# In[8]:


data1 = """acct_id,dollar_amt,name,float_fld,date_fld
10000001234,123.45,George Maharis,14530.1555,2017-01-01
10000001235,0.45,Michael Bluth,1,2017-01-01
10000001236,1345,George Bluth,,2017-01-01
10000001237,123456,Bob Loblaw,345.12,2017-01-01
10000001239,1.05,Lucille Bluth,,2017-01-01
"""

data2 = """acct_id,dollar_amt,name,float_fld
10000001234,123.4,George Michael Bluth,14530.155
10000001235,0.45,Michael Bluth,
10000001236,1345,George Bluth,1
10000001237,123456,Robert Loblaw,345.12
10000001238,1.05,Loose Seal Bluth,111
"""

df1 = pd.read_csv(StringIO(data1))
df2 = pd.read_csv(StringIO(data2))

compare = datacompy.Compare(
    df1,
    df2,
    join_columns='acct_id',  #You can also specify a list of columns
    abs_tol=0, #Optional, defaults to 0
    rel_tol=0, #Optional, defaults to 0
    df1_name='Original', #Optional, defaults to 'df1'
    df2_name='New' #Optional, defaults to 'df2'
    )

assert compare.matches(ignore_extra_columns=False) == False, 'Expect false'


# In[9]:


data1 = """acct_id,dollar_amt,name,float_fld,date_fld
10000001234,123.45,George Maharis,14530.1555,2017-01-01
10000001235,0.45,Michael Bluth,1,2017-01-01
10000001236,1345,George Bluth,,2017-01-01
10000001237,123456,Bob Loblaw,345.12,2017-01-01
10000001239,1.05,Lucille Bluth,,2017-01-01
"""

data2 = """acct_id,dollar_amt,name,float_fld,date_fld
10000001234,123.45,George Maharis,14530.1555,2017-01-01
10000001235,0.45,Michael Bluth,1,2017-01-01
10000001236,1345,George Bluth,,2017-01-01
10000001237,123456,Bob Loblaw,345.12,2017-01-01
10000001239,1.05,Lucille Bluth,,2017-01-01
"""

df1 = pd.read_csv(StringIO(data1))
df2 = pd.read_csv(StringIO(data2))

compare = datacompy.Compare(
    df1,
    df2,
    join_columns='acct_id',  #You can also specify a list of columns
    abs_tol=0, #Optional, defaults to 0
    rel_tol=0, #Optional, defaults to 0
    df1_name='Original', #Optional, defaults to 'df1'
    df2_name='New' #Optional, defaults to 'df2'
    )
assert compare.matches(ignore_extra_columns=False) == True, 'Expect false'


# In[10]:


data1 = """acct_id,dollar_amt,name,float_fld,date_fld
10000001234,123.45,George Maharis,14530.1555,2017-01-01
10000001235,0.45,Michael Bluth,1,2017-01-01
10000001236,1345,George Bluth,,2017-01-01
10000001237,123456,Bob Loblaw,345.12,2017-01-01
10000001239,1.05,Lucille Bluth,,2017-01-01
"""

data2 = """acct_id,dollar_amt,name,float_fld,date_fld
10000001234,123.45,George Maharis,14530.1555,2017-01-01
10000001235,0.45,Michael Bluth,1,2017-01-01
10000001236,1345,George Bluths,,2017-01-01
10000001237,123456,Bob Loblaw,345.12,2017-01-01
10000001239,1.05,Lucille Bluth,,2017-01-01
"""

df1 = pd.read_csv(StringIO(data1))
df2 = pd.read_csv(StringIO(data2))

compare = datacompy.Compare(
    df1,
    df2,
    join_columns='acct_id',  #You can also specify a list of columns
    abs_tol=0, #Optional, defaults to 0
    rel_tol=0, #Optional, defaults to 0
    df1_name='Original', #Optional, defaults to 'df1'
    df2_name='New' #Optional, defaults to 'df2'
    )
assert compare.matches() == False, 'Expect false'


# In[11]:


df1 = pd.DataFrame({
        'c1':  ['a','d', '1','b',None,'']
       })

df2 = pd.DataFrame({
        'c1':  ['a','d','1','b','',None]
       })
compare = datacompy.Compare(
    df1,
    df2,
    join_columns='c1',  #You can also specify a list of columns
    )
assert compare.matches() == True, "Expected true"


# In[12]:


data1 = """acct_id,dollar_amt,name,float_fld,date_fld
10000001234,123.45,George Maharis,14530.1555,2017-01-01
"""

data2 = """acct_id,dollar_amt,name,float_fld,date_fld
10000001234,123.45,George maharis,14530.1555,2017-01-01
"""

df1 = pd.read_csv(StringIO(data1))
df2 = pd.read_csv(StringIO(data2))

compare = datacompy.Compare(
    df1,
    df2,
    join_columns='acct_id',  #You can also specify a list of columns
    abs_tol=0, #Optional, defaults to 0
    rel_tol=0, #Optional, defaults to 0
    df1_name='Original', #Optional, defaults to 'df1'
    df2_name='New', #Optional, defaults to 'df2',
    ignore_case=False
    )
assert compare.matches() == False, 'Expect False, different case'


# In[13]:


data1 = """acct_id,dollar_amt,name,float_fld,date_fld
10000001234,123.45,George Maharis,14530.1555,2017-01-01
"""

data2 = """acct_id,dollar_amt,name,float_fld,date_fld
10000001234,123.45,George maharis,14530.1555,2017-01-01
"""

df1 = pd.read_csv(StringIO(data1))
df2 = pd.read_csv(StringIO(data2))

compare = datacompy.Compare(
    df1,
    df2,
    join_columns='acct_id',  #You can also specify a list of columns
    abs_tol=0, #Optional, defaults to 0
    rel_tol=0, #Optional, defaults to 0
    df1_name='Original', #Optional, defaults to 'df1'
    df2_name='New', #Optional, defaults to 'df2',
    ignore_case=True
    )
assert compare.matches() == True, 'Expect True, different case w ignore_case'


# In[14]:


print('Complete', datetime.now())

