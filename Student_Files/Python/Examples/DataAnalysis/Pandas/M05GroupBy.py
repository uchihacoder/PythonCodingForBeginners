import pandas as pd
import numpy as numpy
df = pd.DataFrame({
'A' : ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
'B' : ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
'C' : numpy.random.randn(8),
'D' : numpy.random.randn(8)})

print(df.groupby('A').sum())
print('-'*50)
print(df.groupby(['A','B']).sum())