# Projeto de Monitoramento de Voos

## Panorama Geral

Este é um projeto realizado na disciplina PCS3643 - Labortório de Engenharia de Software I pelo grupo 7, composto pelos seguintes integrantes:

* Francisco Cavalheiro Mariani - 11803701
* Lucas Palmiro de Freitas - 11803396
* Lucas von Ancken Garcia - 11257592

O projeto consiste em um sistema de monitoramento de voos, de acordo com este [Enunciado](./docs/enunciado.pdf).

O modelo de casos de uso e o modelo de classes elaborados para o projeto estão disponíveis em [Modelo de Casos de Uso](./docs/modelo_de_casos_de_uso.md) e [Modelo de Classes](./docs/modelo_de_classes.md).

O plano de testes de validação elaborado para o projeto é apresentado em [Plano de Testes de Validação](./docs/plano_de_testes.md) e o diagrama entidade-relacionamento pode ser consultado em [Diagrama Entidade-Relacionamento](./docs/images/der.png).

Os diagramas de navegação de telas podem ser visualizados em [Diagramas de Navegação de Telas](./docs/navegacao_telas.md).

## Guia de Instalação

Para executar este projeto em seu computador:

1. Clone o repositório, digitando no seu terminal o comando:
``` 
git clone https://github.com/franos-pj/PCS3643-Grupo7
```

1. Crie um ambiente virtual pelo comando: 
```
cd PCS3643-Grupo7
python -m venv env
```

2. Ative o ambiente usando o comando: 

**Windows**
```
.\env\scripts\Activate.ps1
```

**Linux**
```
source env/bin/activate
```


3. Instale o django no ambiente criado por meio do seguinte comando:
```
pip install django
```

4. Crie as migrações pelo comando:
```
cd src
python manage.py makemigrations
```

5. Execute as migrações (criar o banco de dados) por meio do comando:
```
python manage.py migrate
```

6. Execute os testes pelo comando:
```
python manage.py test
```

7. Para executar o projeto, rode o comando:
```
python manage.py runserver
```

8. Abra seu navegador a url `http://127.0.0.1:8000` e abra uma das seguintes abas:

- `http://127.0.0.1:8000` - Tela de Autenticação
- `http://127.0.0.1:8000/routes-and-flights` - Tela do Operador de Voo
- `http://127.0.0.1:8000/routes-and-flights/routes-records` - Tela de Rotas
- `http://127.0.0.1:8000/routes-and-flights/routes-records/info` - Tela de Visualização de Rota
- `http://127.0.0.1:8000/routes-and-flights/routes-records/register` - Tela de Cadastro de Rota
- `http://127.0.0.1:8000/routes-and-flights/flights-records` - Tela de Voos
- `http://127.0.0.1:8000/routes-and-flights/flights-records/flights-record-info` - Tela de Visualização de Voo
- `http://127.0.0.1:8000/routes-and-flights/flights-records/register` - Tela de Cadastro de Voo
- `http://127.0.0.1:8000/monitoring/dashboard` - Tela do Painel de Monitoramento de Voos
- `http://127.0.0.1:8000/monitoring/flight-info` - Tela de Atualização de Voo
- `http://127.0.0.1:8000/report` - Tela de Geração de Relatório
- `http://127.0.0.1:8000/report/general` - Tela de Visualização de Relatório Geral
- `http://127.0.0.1:8000/report/specific` - Tela de Visualização de Relatório Específico