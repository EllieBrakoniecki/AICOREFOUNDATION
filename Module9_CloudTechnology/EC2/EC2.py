#%%
import pandas as pd

data = {'product_name': ['laptop', 'printer', 'tablet', 'desk', 'chair'],
        'price': [1200, 150, 300, 450, 200]
        }

df = pd.DataFrame(data)

print (df)

df.to_csv('test_csv.csv',mode='a',index=False, header=True)

# %%
# move key to .ssh directory
# chmod 400 aicorekey.pem
# scp -i </path/my-key-pair.pem> </path/my-file> ec2-user@ ec2-54-167-164-211.compute-1.amazonaws.com:.
# ssh -i aicorekey.pem ec2-user@ec2-13-40-50-176.eu-west-2.compute.amazonaws.com
# Note: ec2-user for linux, ubuntu for ubuntu
# %%

