# Classificação do Dataset Iris com KNN

Este projeto utiliza o algoritmo **K-Nearest Neighbors (KNN)** para classificação do famoso dataset **Iris**. O objetivo é prever a espécie da flor com base em medidas de comprimento e largura das sépalas e pétalas.

## 📌 Descrição
O dataset Iris contém 150 amostras divididas igualmente entre 3 espécies de flores:
- **Setosa**
- **Versicolor**
- **Virginica**

Cada amostra possui 4 atributos:
- **Sepal length** (comprimento da sépala)
- **Sepal width** (largura da sépala)
- **Petal length** (comprimento da pétala)
- **Petal width** (largura da pétala)

O modelo KNN é treinado para identificar a espécie de uma flor com base nesses atributos.

## 🛠 Tecnologias Utilizadas
- **Python**
- **Scikit-learn** (para implementação do KNN)
- **Pandas** (para manipulação do dataset)
- **Matplotlib & Seaborn** (para visualização de dados)
- **Jupyter Notebook** (para desenvolvimento e testes)

## 📂 Estrutura do Projeto
```
/
|-- Iris.ipynb  # Notebook contendo o código do projeto
|-- README.md   # Documentação do projeto
|-- requirements.txt  # Lista de dependências
```

## 🚀 Como Executar
1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/knn-iris.git
   ```

2. Acesse a pasta do projeto:
   ```bash
   cd knn-iris
   ```

3. Crie um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate  # Windows
   ```

4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

5. Execute o Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

6. Abra o arquivo `Iris.ipynb` e execute as células passo a passo.

## 📊 Resultados
- Visualização das distribuições das espécies.
- Treinamento e avaliação do modelo KNN.
- Testes de previsão com novos dados.

## 📝 Contribuição
Se quiser contribuir com melhorias, sinta-se à vontade para:
1. Fazer um fork do repositório.
2. Criar uma branch para suas modificações:
   ```bash
   git checkout -b minha-modificacao
   ```
3. Commitar suas mudanças:
   ```bash
   git commit -m "Melhoria no modelo KNN"
   ```
4. Enviar suas alterações para o repositório remoto:
   ```bash
   git push origin minha-modificacao
   ```
5. Abrir um Pull Request.

## 📜 Licença
Este projeto está sob a licença MIT. Sinta-se livre para usá-lo e modificá-lo como desejar.

---
Desenvolvido por Israel Alves 🚀

