# Projeto de Monitoramento de Voos

## Panorama Geral

Este é um projeto realizado na disciplina PCS3643 - Labortório de Engenharia de Software I pelo grupo 7, composto pelos seguintes integrantes:

* Francisco Cavalheiro Mariani - 11803701
* Lucas Palmiro de Freitas - 11803396
* Lucas von Ancken Garcia - 11257592

O projeto consiste em um sistema de monitoramento de voos, de acordo com este [Enunciado](./docs/enunciado.pdf).

O modelo de casos de uso e o modelo de classes elaborados para o projeto estão disponíveis em [Modelo de Casos de Uso](./docs/modelo_de_casos_de_uso.md) e [Modelo de Classes](./docs/modelo_de_classes.md).

Além disso, o plano de testes de validação elaborado para o projeto é apresentado em [Plano de Testes de Validação](./docs/plano_de_testes.md) e o diagrama entidade-relacionamento pode ser consultado em [Diagrama Entidade-Relacionamento](./docs/images/der.png).

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
```
.\env\bin\Activate.ps1
```
ou
```
.\env\scripts\Activate.ps1
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

1. Abra seu navegador na URL `http://127.0.0.1:8000`. No momento, as seguintes telas podem ser acessadas pela navegação da aplicação:

- `http://127.0.0.1:8000` - tela de login
- `http://127.0.0.1:8000/monitoring/dashboard` - interface de monitoramento de voos
- `http://127.0.0.1:8000/monitoring/flight-info` - tela com informações de um voo específico
- `http://127.0.0.1:8000/report` - interface para a escolha do relatório a ser gerado
- `http://127.0.0.1:8000/report/general` - tela de apresentação e download do relatório geral
- `http://127.0.0.1:8000/report/specific` - tela de apresentação e download do relatório específico