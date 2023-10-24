# Iris ML Deployment

## Overview

Este projeto demonstra como treinar e implantar um modelo de machine learning para previsões usando o conjunto de dados Iris. O modelo é treinado com Scikit-learn, e a previsão é servida por meio de uma API criada com FastAPI. Além disso, o projeto inclui um Dockerfile para facilitar a implantação do modelo em contêineres Docker. Também demonstra como testar o desempenho da API com o Locust.

## Tabela de Conteúdo

- [Objetivo](#objetivo)
- [Fluxo de Versionamento](#fluxo-de-versionamento)
- [Ferramentas](#ferramentas)
- [Getting Started](#getting-started)
- [Requisitos](#requisitos)
- [Usage](#usage)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Troubleshooting](#troubleshooting)
- [Contributions](#contributions)
- [License](#license)
- [Contato](#contato)
- [Acknowledgments](#acknowledgments)

## Objetivo

O objetivo deste projeto é criar uma pipeline de treinamento e implantação de um modelo de machine learning usando Scikit-learn, FastAPI e Docker. O modelo é treinado com base no conjunto de dados Iris e é capaz de fazer previsões sobre a espécie de uma flor com base nas características fornecidas.

## Fluxo de Versionamento

Este projeto segue um fluxo de versionamento baseado no Git. Cada grande alteração no projeto deve ser acompanhada por um novo commit com uma mensagem descritiva. Versões do modelo treinado e da API devem ser controladas com base em tags no Git.

## Ferramentas

- Scikit-learn: Biblioteca para machine learning em Python.
- FastAPI: Framework para criar APIs web rápidas com Python.
- Docker: Plataforma para criar, implantar e executar aplicativos em contêineres.
- Locust: Ferramenta para teste de carga.

## Getting Started

Siga estas instruções para configurar o ambiente de desenvolvimento e executar o projeto:

1. Clone o repositório:
```
git clone https://github.com/seu-usuario/iris-ml-deployment.git
cd iris-ml-deployment
```


2. Instale as dependências:
```
pip install -r requirements.txt
```


3. Treine o modelo:
```
python models/ml/train.py
```


4. Inicie a API:
```
uvicorn app:app --host 0.0.0.0 --port 8000
```

5. Acesse a documentação da API em seu navegador em http://localhost:8000/docs para fazer previsões.

## Requisitos

- Python 3.8+
- Scikit-learn
- FastAPI
- Docker (para implantação)
- Locust (opcional, para teste de carga)

## Usage

Após seguir as instruções em **[Getting Started](#getting-started)**, você pode acessar a documentação da API em http://localhost:8000/docs para fazer previsões sobre a espécie das flores de íris com base nas características fornecidas.

## Dockernization

Este projeto pode ser facilmente "dockernizado" para facilitar a implantação em contêineres Docker. A utilização de contêineres Docker ajuda a garantir a portabilidade e a independência das dependências do sistema, tornando a implantação mais fácil e consistente em diferentes ambientes.

Siga estas etapas para criar uma imagem Docker e executar a aplicação em um contêiner:

### 1. Construir uma imagem docker da aplicação

```
docker build -t iris-ml-build .
```

### 2. Executar o container

```
docker run -d -p 80:80 --name iris-api iris-ml-build 
```
O comando acima executa um contêiner Docker a partir da imagem que você construiu. Ele mapeia a porta 80 do contêiner para a porta 80 do host local.

### 3. Va para o localhost
```
http://localhost:80/docs
```
Agora, a aplicação estará em execução dentro do contêiner Docker. Você pode acessá-la em http://localhost:80/docs para fazer previsões por meio da API.


### 4. Try out the post /predict method
```
curl -X POST "http://localhost/v1/iris/predict" -H\
 "accept: application/json"\
 -H "Content-Type: application/json"\
 -d "{\"data\":[[4.8,3,1.4,0.3],[2,1,3.2,1.1]]}"
```

> Lembre-se de que você pode personalizar as portas e os nomes dos contêineres conforme necessário. Certifique-se de ter o Docker instalado e em execução em seu sistema antes de prosseguir.

Ao implantar em um ambiente de produção, você pode usar orquestradores de contêineres, como Kubernetes ou Docker Compose, para gerenciar a implantação e escalabilidade de contêineres. Certifique-se de configurar e ajustar seu ambiente de acordo com suas necessidades específicas.

## Testes

Este projeto inclui a capacidade de realizar testes automatizados usando a biblioteca Locust. Os testes de carga fornecidos podem ser usados para avaliar o desempenho da API e medir a capacidade de resposta em diferentes cenários de carga.

Siga estas etapas para executar os testes de carga:

1. Execute os Testes de Carga:

Navegue até o diretório de testes:


```
cd tests
```

2. Execute o Locust com o arquivo de teste específico:


```
locust -f load_test.py
```
Isso iniciará o servidor de teste do Locust em http://localhost:8089/. Você pode acessar o painel de controle do Locust em seu navegador.

3. Configure os Parâmetros de Teste:

* Acesse o painel de controle do Locust em http://localhost:8089/.
* Defina o número de usuários virtuais (virtual users) que você deseja simular e a taxa de spawn (quantos usuários por segundo serão iniciados).
* Clique no botão "Start Swarming" para iniciar os testes.

4. Execute os Testes de Carga:

Os usuários virtuais gerados pelo Locust irão acessar a API automaticamente de acordo com a configuração que você definiu. Eles enviarão solicitações de previsão à API e coletarão métricas de desempenho.

5. Analise os Resultados:

* Você pode monitorar o progresso dos testes e visualizar métricas de desempenho em tempo real no painel de controle do Locust.
* Ao encerrar os testes, você poderá acessar relatórios detalhados e gráficos para avaliar o desempenho da API.

Lembre-se de que os testes de carga com o Locust são uma maneira eficaz de avaliar o desempenho da sua aplicação e identificar possíveis gargalos. Certifique-se de ajustar os parâmetros dos testes de acordo com as necessidades e requisitos da sua aplicação.

## Estrutura do Projeto

O projeto tem a seguinte estrutura de diretórios:

```
.
├── deploy.sh
├── Dockerfile
├── main.py
├── models
│   ├── ml
│   │   ├── classifier.py
│   │   ├── iris_dt_v2.joblib
│   │   └── train.py
│   └── schemas
│       └── iris.py
├── README.md
├── requirements.txt
├── routes
│   ├── home.py
│   └── v1
│       └── iris_predict.py
├── saida.txt
└── tests
    ├── __init__.py
    ├── load_test.py
    ├── __pycache__
    └── test_response.py

11 directories, 16 files
```


## Troubleshooting

Se você encontrar problemas ou tiver dúvidas sobre o projeto, consulte a seção "Contributions" para obter informações sobre como relatar problemas ou fazer perguntas.

## Contributions

Contribuições são bem-vindas! Se você encontrar um problema ou tiver uma sugestão para melhorar o projeto, sinta-se à vontade para abrir uma issue ou criar uma solicitação pull.

## License

Este projeto está licenciado sob a [MIT License](LICENSE).

## Contato

Para entrar em contato, envie um e-mail para [seu-email@example.com](mailto:seu-email@example.com).

## Acknowledgments

Agradecimentos a todos os desenvolvedores e mantenedores das bibliotecas e ferramentas utilizadas neste projeto, bem como a toda a comunidade de código aberto que torna projetos como este possíveis.