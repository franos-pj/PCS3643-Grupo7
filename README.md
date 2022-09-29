# Projeto de Monitoramento de voo

## Panorama Geral

Este é um projeto realizado na disciplina PCS3643 - Labortório de Engenharia de Software I pelo grupo 7, composto pelos seguintes integrantes:

* Francisco Cavalheiro Mariani - 11803701
* Lucas Palmiro de Freitas - 11803396
* Lucas von Ancken Garcia - 11257592

O projeto consiste em um sistema de monitoramento de voos, de acordo com este [Enunciado]().

## Guia de Instalação

Para executar este projeto em seu computador:

1. Crie um ambiente virtual pelo comando: 
```
python -m venv env
```

2. Ative o ambiente usando o comando: 
```
.\env\bin\Activate.ps1
```

3. Instale o django no ambiente criado por meio do seguinte comando:
```
pip install django
```

4. Finalmente, para executar o projeto, rode o comando:
```
pytohn manage.py runserver
```

5. Abra seu navegador a url `http://127.0.0.1:8000/admin/` para abrir a interface de administrador.

6. Abra a aba `http://127.0.0.1:8000/FIRST` para ver a página principal.