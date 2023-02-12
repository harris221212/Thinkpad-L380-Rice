import pandas as pd
import sys
import re
import requests

def fixQuotes(x):
	x = x.replace("\"", "")
	return(str(x))

url = sys.argv[1]

df=pd.read_html(url, header=0)[1]


url = sys.argv[1]

page = requests.get(url)
table = pd.read_html(page.text.replace('<br />',' & '))
df = table[1]

df.head()

df['Song']=df['Song'].apply(lambda x: str(x.replace(",", "%comma%")) if isinstance(x, str) else x)
df['Song']=df['Song'].apply(lambda x: re.sub("\[.*\]", "", x) if isinstance(x, str) else x) 
df['Song']=df['Song'].apply(lambda x: str(x.replace("\"", "")) if isinstance(x, str) else x)
df['Song']=df['Song'].apply(lambda x: str(x.replace("%comma%", ",")) if isinstance(x, str) else x)
#df['Song']=df['Song'].apply(lambda x: print(x) if isinstance(x, str) else x)  
df['Song']=df['Song'].apply(lambda x: re.sub(" \(.*\)", "", x) if isinstance(x, str) else x) 


#df['Song'] = df['Song'].apply(fixQuotes)


df = df.drop(df.columns[[4]], axis=1)
df["Artist"] = sys.argv[2]

filename = sys.argv[2] + ".csv"
df.to_csv(filename, index=False)