import pandas as pd
import numpy as np

df =pd.read_csv('filename', header=0, skipinitialspace=True, dtype=str) 

df = df[df.urls.notnull()]
row_index = df[df['urls'].isnull()].index.tolist()
df.drop(df.index[row_index], axis=0, inplace = True)
df.reset_index(drop = True, inplace= True)
df.drop_duplicates()
df.reset_index(drop = True, inplace= True)


df['urls'] = pd.DataFrame([x.split('(')[1]for x in df['urls'].tolist()])
df['urls'] = pd.DataFrame([x.split(')')[0]for x in df['urls'].tolist()])
df['OrgId'] = pd.DataFrame([x.split(',')[0]for x in df['urls'].tolist()])
df['LDIBookId'] = pd.DataFrame([x.split(',')[1]for x in df['urls'].tolist()])
df['LDIOrgId'] = pd.DataFrame([x.split(',')[2]for x in df['urls'].tolist()])
df['LDISecId'] = pd.DataFrame([x.split(',')[3]for x in df['urls'].tolist()])
df['FromRecent'] = pd.DataFrame([x.split(',')[4]for x in df['urls'].tolist()])
df['Save'] = pd.DataFrame([x.split(',')[5]for x in df['urls'].tolist()])
df['Position'] = pd.DataFrame([x.split(',')[6]for x in df['urls'].tolist()])


df['url_address'] = "https://lo.bvdep.com/OrgDocument.asp?OrgId=" + df['OrgId'] + "&LDIBookId=" + df['LDIBookId'] \
					+ "&LDIOrgId=" + df['LDIOrgId'] + "&LDISecId=" + df['LDISecId'] \
					+ "&FromRecent=1&Save=0&hidebio=1&page=-1&fulllisting=1"

df['url_address'].str.strip()

df.to_csv('filename',index=False)

print df.head(5)
print type(df['url_address'])


