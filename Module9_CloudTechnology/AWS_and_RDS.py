#%%
from sqlalchemy import create_engine
DATABASE_TYPE = 'postgresql'
DBAPI = 'psycopg2'
ENDPOINT = 'aicoredb.cughg1zxgq0r.eu-west-2.rds.amazonaws.com' # AWS endpoint
USER = 'postgres'
PASSWORD = 'Rainbowpancake5'
PORT = 5432
DATABASE = 'postgres'
engine = create_engine(f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{ENDPOINT}:{PORT}/{DATABASE}")
#%%
engine.connect()
#%%
from sklearn.datasets import load_iris
import pandas as pd
data = load_iris()
iris = pd.DataFrame(data['data'], columns=data['feature_names'])
iris.head()
#%%
iris.to_sql('iris_dataset', engine, if_exists='replace')
#%%
df = pd.read_sql_table('iris_dataset', engine)
#%%
df.head()