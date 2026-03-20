import kagglehub
import pandas as pd
# uma alternativa pra eu ver o nome do arquivo -> import os > print(os.listdir(path))

path = kagglehub.dataset_download("bhushandivekar/video-game-sales-and-industry-data-1980-2024") # aqui ele baixa uma pasta com os dados
df = pd.read_csv(path + "/Video_Games_Sales_Cleaned.csv")
df.head()
df.info()
df.describe()