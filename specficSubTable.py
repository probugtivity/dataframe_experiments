import pandas as pd
import numpy as np

df = pd.DataFrame({'colA' : ['Debug'  ,'Debug', 'Prod', 'Prod'], 'colB' : [1,2,3,4], 'colC' : 
[5,6,7,8], 'colD' : [11,12,123,14], 'colE' : [9,10,11,12], 'colF' : [4,3,2,1]})

specificDF = df.loc[(df['colA'] == 'Prod') | (df['colA'] == 'Debug'),'colB':'colF']
