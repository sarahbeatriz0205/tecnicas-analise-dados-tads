# Fundamentos da Estatística Descritiva
- **Estatística Descritiva:** Foco deste módulo. Envolve resumir e descrever as principais características de um conjunto de dados (ex: média, mediana, histogramas).
- **Probabilidade:** O estudo da incerteza e dos eventos prováveis.
- **Estatística Inferencial:** O processo de usar dados de uma amostra para fazer conclusões (inferências) sobre uma população maior. É a base para a criação de modelos preditivos.

## Vocabulário essencial
- **População (ou Universo):** A coleção completa de todos os indivíduos ou itens de interesse. É representada por N. (Ex: Todos os alunos do IFRN).
- **Amostra:** Um subconjunto representativo da população. É representada por n. (Ex: 500 alunos selecionados aleatoriamente do IFRN). Analisamos amostras porque geralmente é inviável (em custo ou tempo) analisar toda a população.
- **Censo:** Um procedimento especial onde os dados são coletados de toda a população (ex: Censo Demográfico do IBGE).
- **Variável (ou Atributo):** Uma característica que está sendo medida ou observada. Nas planilhas, as colunas são as variáveis (ex: 'idade', 'sexo', 'nota').
- **Dados (ou Instâncias):** Os valores observados para cada variável. Nas planilhas, as linhas são as instâncias (ex: os dados de um aluno específico).
- **Parâmetros:** Valores que descrevem uma população (ex: a média de idade de todos os alunos).

**Estatísticas:** Valores calculados a partir de uma amostra (ex: a média de idade dos 500 alunos da amostra), usados para estimar os parâmetros da população.

## Variáveis e Dados nas Planilhas
| Variável (Coluna / Atributo) | Dados / Instâncias (Linha) |
| ---------------------------- | -------------------------  |
| Uma característica que está sendo medida ou observada. Nas planilhas, as colunas são as variáveis. Exemplos: idade, sexo, nota, descrição |  Os valores observados para cada variável. Nas planilhas, as linhas são as instâncias — os dados de um aluno específico, por exemplo|

## Tipos de variáveis

<img width="1034" height="399" alt="image" src="https://github.com/user-attachments/assets/ca46037a-14ea-4537-83f3-c0116b760d2f" />

### Qualitativas (Categóricas)
Descrevem uma qualidade ou categoria.
- **Nominal:** Categorias que não possuem uma ordem intrínseca (não depende de nada para existir, existe por si)
> Exemplos: 'sexo' (masculino, feminino), 'raça', 'cor_do_carro' (vermelho, azul).

- **Subtipo (Binária):** Uma variável nominal com apenas duas categorias (ex: 'Sim/Não', 'Verdadeiro/Falso', 'Evadiu/Não Evadiu').

- **Ordinal:** Categorias que possuem uma relação de ordem ou hierarquia clara.
> Exemplos: 'escolaridade' (fundamental, médio, superior), 'nível_satisfação' (baixo, médio, alto), 'tamanho' (P, M, G).

### Qualitativas (Numéricas)
Descrevem uma quantidade ou medida numérica.
- **Discreta:** Valores resultantes de uma contagem (geralmente números inteiros). Não se pode ter "meio" valor.
> Exemplos: 'quantidade_de_filhos' (0, 1, 2), 'numero_de_faltas'.

- **Contínua:** Valores resultantes de uma medição (números reais, podem ser fracionados).
> Exemplos: 'temperatura' (27.5 °C), 'peso' (70.3 kg), 'altura' (1.75m).

## Medidas de Tendência Central e Assimetria
- **Média Aritmética:** A soma de todos os valores dividida pelo número de observações.
> [!TIP]
> Pró: É a medida mais comum e usa todos os dados no seu cálculo.

> [!CAUTION]
> Contra: É uma medida "volátil", pois é extremamente sensível a valores extremos, ou outliers (valores muito fora da curva). Um único erro de digitação (ex: 1000 em vez de 10) pode distorcer completamente a média.

- **Mediana:** O valor central que divide o conjunto de dados (após ordenados) exatamente ao meio (50% dos dados estão abaixo, 50% estão acima).
> [!TIP]
> Pró: É uma medida "robusta". Ela não é afetada por outliers, sendo uma representante muito melhor do "centro" em dados de baixa qualidade ou muito assimétricos (ex: média salarial, que é melhor representada pela mediana do que pela média, que é puxada para cima pelos super-ricos).

> [!CAUTION]
> Contra: Ignora a magnitude dos valores, focando apenas na posição.

- **Moda:** O valor que ocorre com a maior frequência no conjunto de dados.
> [!TIP]
> Pró: Também é uma medida robusta e é a única medida de tendência central que pode ser usada em dados qualitativos (ex: a "moda" da variável 'raça' é 'parda').





