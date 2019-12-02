import pandas as pd
s = pd.Series( [ 2, 4, 6, 8])
print(s)
print('-'*50)

s = pd.Series( [ 2, 4, 6, 8], index=[ 'f', 'a', 'c', 'e'] )
print( s['a'] )
print( s[ [ 'a', 'c' ] ] )
print('-'*50)

s = pd.Series( range(6), index=list( 'abcabc' ))
print( s['a'] )
print('-'*50)

s = pd.Series( [ 2, 4, 6, 8], index=[ 'f', 'a', 'c', 'e'] )
print( s[s > 4] ) 		# outputs 'c   6\ne   8'
print( s > 4)		# outputs 'f   False\na   False\nc   True\ne   True
print( s * 2)
print('-'*50)

sdata = { 'b': 100, 'c': 150, 'e': 200}
s = pd.Series( sdata, list('abcde'))
print(s * 2)
