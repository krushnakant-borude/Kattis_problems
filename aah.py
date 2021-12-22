import pandas as pd
import numpy as np




dic={
"smalllet":['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
, "Caplet":['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'], 
"otherlet":['@','g','(','|)','3','#','6','[-]','|','_|','|<','1','[]\/[]','[]\[]','0','|D','(,)','|Z','$',"']['",'|_|','\/','\/\/','}{','`/','2']

}

df=pd.DataFrame(dic)

print(df)

ab=input()

print(ab.replace())

for 