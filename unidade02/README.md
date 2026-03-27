# Coleta e Manipulação de Dados com Pandas
- **Pandas:** biblioteca padrão para ciência de dados
- Baseada no **NumPy**
- Suporta dados tabulares (planilhas, csv, json)
- Suporta tipos variados, como string, float, int, boolean e categóricos (os categóricos ele entende como "object")

## Métodos
- **pd.read_csv():** Lê arquivos ```.csv```
- **pd.read_excel():** Lê arquivos ```.xls``` e ```.xlsx```
- **pd.read_json():** Lê arquivos ```.json```
- **pd.read_sql():** Consulta diretamente um banco de dados
- **pd.read_parquet():** Lê dados compactados, colunar binário

## O Conceito de Series no Pandas
- **Dataframe:** Conjunto de Series, conjunto de colunas
- Array unidimensional, pois é apenas uma coluna do Dataframe
- **Serie:** Coluna individual com dados homogêneos (os dados devem ser de um mesmo tipo
<div>
  <img width="839" height="546" alt="image" src="https://github.com/user-attachments/assets/15065d91-6f6c-4c3c-a354-596ada3291ae" /><br>
  <figcaption>Exemplo de Series</figcaption>
</div>

