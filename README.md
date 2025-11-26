# 🧬 Algoritmo Genético para o Problema do Caixeiro Viajante (TSP)

Este projeto implementa um **Algoritmo Genético (Genetic Algorithm – GA)** para resolver o **Problema do Caixeiro Viajante (Traveling Salesman Problem – TSP)**.  
A solução foi desenvolvida em **Python**, utilizando uma estrutura modular organizada para facilitar manutenção, testes e extensões futuras.

---

## 📁 Estrutura do Projeto

```bash

tsp-genetic-algorithm/
│
├── datasets/ # Instâncias do TSP em CSV
│ ├── eil51.csv
│ ├── berlin52.csv
│ └── custom_dataset.csv
│
├── src/
│ ├── main.py # Arquivo principal de execução
│ │
│ ├── tsp/ # Modelagem do TSP
│ │ ├── city.py
│ │ ├── route.py
│ │ └── instance_loader.py
│ │
│ ├── ga/ # Implementação do Algoritmo Genético
│ │ ├── genetic_algorithm.py
│ │ ├── selection.py
│ │ ├── crossover.py
│ │ ├── mutation.py
│ │ └── init.py
│ │
│ └── visualization/ # Gráficos e resultados
│ ├── evolution_plot.py
│ └── plot_rout.py
│
└── requirements.txt # Dependências
```


---

## 🚀 Como Executar o Projeto

### 1️⃣ Instalar dependências(Precisa ter o python já instalado)

```bash
py install -r requirements.txt
```

### 2️⃣ Executar o algoritmo
```bash
python src/main.py --dataset logistica_brasil.csv
```
## 🧠 Como o Algoritmo Genético Funciona
<ul>
O GA segue os seguintes passos:

<li>Inicialização da população com rotas aleatórias</li>

<li>Seleção (tournament selection)</li>

<li>Crossover entre pares de indivíduos</li>

<li>Mutação controlada</li>

<li>Elitismo para manter o melhor indivíduo</li>

<li>Evolução por diversas gerações</li>

<li>Retorno da melhor rota encontrada</li>
</ul>

## 📊 Resultados Gerados

Ao final da execução, o código cria uma pasta:
```bash
results/
```
E dentro dela:
<ul>
<li>_map.png → gráfico da evolução da aptidão</li>

<li>_convergence.png → gráfico da melhor rota encontrada</li>
</ul>
Esses arquivos permitem visualizar:
<ul>
<li>A convergência do algoritmo ao longo das gerações</li>
<li>A rota final otimizada</li>
</ul>

## 🛠 Tecnologias Utilizada
<ul>
<li>Python 3</li>
<li>NumPy</li>
<li>Matplotlib</li>
<li>TQDM</li>
</ul>

## 📘 Referências
<ul>
<li>Traveling Salesman Problem – Gutin & Punnen</li>
<li>Genetic Algorithms – Goldberg</li>
<li>Documentação oficial do NumPy e Matplotlib</li>
</ul>

