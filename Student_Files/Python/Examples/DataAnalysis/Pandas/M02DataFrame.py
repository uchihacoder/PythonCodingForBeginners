import pandas as pd
data = { 'state': ['PA', 'NY', 'TX', 'FL' ], 'year': [ 2010, 2011, 2012, 2013],\
'pop': [ 18.2, 12.2, 9.2, 9.7 ] }
df = pd.DataFrame( data )
print( df)
print('-'*50)

data = { 'PA': {2010: 18.2, 2011: 12.2}, 'FL': {2008: 9.2, 2010: 9.7 } }
df = pd.DataFrame( data )
print( df)

print('-'*50)

data = { 'state': ['PA', 'NY', 'TX', 'FL' ], 'year': [ 2010, 2011, 2012, 2013],\
	'pop': [ 18.2, 12.2, 9.2, 9.7 ] }
df = pd.DataFrame( data )
print( df['state'])
print('-'*50)

data = { 'state': ['PA', 'NY', 'TX', 'FL' ], 'year': [ 2010, 2011, 2012, 2013],\
	'pop': [ 18.2, 12.2, 9.2, 9.7 ] }
df = pd.DataFrame( data )
df['other'] = [20, 30, 10, 25]
print( df)

import pandas as pd
data = { 'state': ['PA', 'NY', 'TX', 'FL' ], 'year': [ 2010, 2011, 2012, 2013],\
	'pop': [ 18.2, 12.2, 9.2, 9.7 ] }
df = pd.DataFrame( data )
#We can display the index, columns, and the underlying numpy data separately:
print(df.index)
print(df.columns)
print(df.values)
#We can also display a quick statistical
print(df.describe())