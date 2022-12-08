# Plano de Testes de Validação

## Introdução

Este documento tem como objetivo orientar a condução dos testes de validação a serem executados sobre o sistema de monitoramento de voos, sendo dirigido aos seguintes stakeholders: o gerente de projeto, os analistas de configuração e os analistas de qualidade, os quais executarão os casos de teste.

Para tanto, apresentam-se de forma detalhada os passos a serem seguidos, bem como os respectivos resultados esperados para cada caso de teste. Além disso, identificam-se os recursos tanto materiais quanto humanos necessários para a execução dos testes.

## Teste de Validação

Teste de Validação pode ser compreendido como um conjunto de ações que visam verificar se o sistema sobre o qual é aplicado está em conformidade com os requisitos previstos nas especificações dos seus casos de uso.

## Recursos Necessários

Os principais recursos necessários para a execução da validação referenciada neste documento foram:

1. Código fonte da aplicação em fase de teste
  obs.: A validação foi executada a partir do código fonte da aplicação armazenado na branch develop do repositório do projeto: ttps://github.com/franos-pj/PCS3643-Grupo7

2. Ambiente de teste:
  * a. Servidor local de teste
  * b. Banco de dados contendo registros de teste: airportDB.sqlite3

  obs.: Para popular o banco de dados com os registros de testes utilizados na validação, é necessário executar o arquivo migration_scripts.py localizado no diretório ‘src/migrations’ do projeto. Isso pode ser feito com a execução, via terminal, do comando ‘python manage.py migrate' em ‘src’.

3. Softwares do stack escolhido:
  * a. Django
  * b. SQLite

4. Pacotes externos
  * a. Instalação do pacote django-axes
		
  obs.: O pacote django-axes é utilizado na implementação do controle de autenticação. Ressalta-se que sua instalação é necessária para a condução de todos os testes. Ela pode ser feita por meio da execução do comando ‘pip install django-axes’ via terminal

Além disso, em termos operacionais, foi necessária a participação direta de analistas de qualidade para a condução dos casos de teste. Eles foram responsáveis por executar as instruções, inserir as entradas indicadas e coletar os resultados. Para tanto, foram concedidos a eles credenciais de autenticação de cada um das categorias de acesso presentes no sistema. As credenciais de teste utilizadas nesse processo são listadas na tabela 1 apresentada a seguir.



Esses analistas de qualidade devem, idealmente, ter a capacidade técnica para compreender e detalhar os erros encontrados; no entanto, não devem ter participado do projeto, de forma que não haja vieses indesejáveis durante os testes.

## Casos de Teste

| **Caso de Uso** | **Descrição** | **Passos (Entradas)** | **Resultados Esperados (saídas)** |
| --- | --- | --- | --- |
| 1. Cadastrar voo | 1.1 Cadastro de uma rota com dados válidos | Passo 1: Faça login como operador de voo: **Nome do usuário:** michelet.chavez **Senha:** PCS3643 | Resultado 1:Tela "Registros de Rotas e de Voos" é exibida |
| | | Passo 2:Clique no botão " **Selecionar**" de "Rotas" e, em seguida, clique no botão " **Cadastrar**" de "Cadastro de Rota" | Resultado 2:Tela "Cadastro de uma nova rota" é exibida |
| | | Passo 3:Preencha: **Código** : AF123 **Companhia** : Air France **Origem** : FLL **Destino** : CDG **Horário Previsto** : 11:00 AMClique no botão " **Cadastrar**" | Resultado 3: Modal de "Confirmação das informações de cadastro" é exibido com as informações de rota preenchidas |
| | | Passo 4:Clique no botão " **Confirmar**" | Resultado 4:Modal com mensagem de sucesso é exibido |
| | | Passo 5:Clique no botão " **Ok**" | Resultado 5:Tela "Cadastro de uma nova rota" é exibida novamente com inputs vazios |
| 1. Cadastrar voo | 1.2 Tentativa de cadastro de uma rota com dados inválidos | Passo 1: Faça login como operador de voo: **Nome do usuário:** michelet.chavez **Senha:** PCS3643 | Resultado 1:Tela "Registros de Rotas e de Voos" é exibida |
| | | Passo 2:Clique no botão " **Selecionar**" de "Rotas" e, em seguida, clique no botão " **Cadastrar**" de "Cadastro de Rota" | Resultado 2:Tela "Cadastro de uma nova rota" é exibida |
| | | Passo 3:Preencha: **Código** : LH123 **Companhia** : Lufthansa **Origem** : MUC **Destino** : MUC **Horário Previsto** : 03:00 PMClique no botão " **Cadastrar**" | Resultado 3: Modal de "Confirmação das informações de cadastro" é exibido com as informações de rota preenchidas |
| | | Passo 4:Clique no botão " **Confirmar**" | Resultado 4:Modal com mensagem de erro é exibido (mesmo aeroporto de origem e destino) |
| | | Passo 5:Clique no botão " **Ok**" | Resultado 5:Tela "Cadastro de uma nova rota" é exibida novamente com inputs vazios |
| 1. Cadastrar voo | 1.3 Tentativa de cadastro de uma rota já cadastrada | Passo 1: Faça login como operador de voo: **Nome do usuário:** michelet.chavez **Senha:** PCS3643 | Resultado 1:Tela "Registros de Rotas e de Voos" é exibida |
| | | Passo 2:Clique no botão " **Selecionar**" de "Rotas" e, em seguida, clique no botão " **Cadastrar**" de "Cadastro de Rota" | Resultado 2:Tela "Cadastro de uma nova rota" é exibida |
| | | Passo 3:Preencha: **Código** : AF123 **Companhia** : Air France **Origem** : CDG **Destino** : FLL **Horário Previsto** : 06:00 PMClique no botão " **Cadastrar**" | Resultado 3: Modal de "Confirmação das informações de cadastro" é exibido com as informações de rota preenchidas |
| | | Passo 4:Clique no botão " **Confirmar**" | Resultado 4:Modal com mensagem de erro é exibido (código de voo de rota já cadastrada) |
| | | Passo 5:Clique no botão " **Ok**" | Resultado 5:Tela "Cadastro de uma nova rota" é exibida novamente com inputs vazios |
| 1. Cadastrar voo | 1.4 Leitura das informações de uma rota cadastrada | Passo 1: Faça login como operador de voo: **Nome do usuário:** michelet.chavez **Senha:** PCS3643 | Resultado 1:Tela "Registros de Rotas e de Voos" é exibida |
| | | Passo 2:Clique no botão " **Selecionar**" de "Rotas" e, em seguida, insira em "Informações de Rota": **Código de Voo** : AF123Clique no botão " **Buscar**" | Resultado 2:Tela "Informações da rota" é exibida com as informações correspondente à rota buscada |
| 1. Cadastrar voo | 1.5 Tentativa de leitura das informações de uma rota ainda não cadastrada | Passo 1: Faça login como operador de voo: **Nome do usuário:** michelet.chavez **Senha:** PCS3643 | Resultado 1:Tela "Registros de Rotas e de Voos" é exibida |
| | | Passo 2:Clique no botão " **Selecionar**" de "Rotas" e, em seguida, insira em "Informações de Rota": **Código de Voo** : LH123Clique no botão " **Buscar**" | Resultado 2:Modal com mensagem de erro é exibido (código de voo inserido é de rota ainda não cadastrada) |
| | | Passo 3:Clique no botão " **Ok**" | Resultado 7:Tela "Registros da Rotas" é exibida |
| 1. Cadastrar voo | 1.6 Atualização das informações de uma rota cadastrada | Passo 1: Faça login como operador de voo: **Nome do usuário:** michelet.chavez **Senha:** PCS3643 | Resultado 1:Tela "Registros de Rotas e de Voos" é exibida |
| | | Passo 2:Clique no botão " **Selecionar**" de "Rotas" e, em seguida, insira em "Informações de Rota": **Código de Voo** : AF123Clique no botão " **Buscar**" | Resultado 2:Tela "Informações da rota" é exibida com as informações correspondente à rota buscada |
| | | Passo 3:Clique no botão " **Atualizar**" | Resultado 3:Campos para inserção das novas informações são exibidos |
| | | Passo 4:Apague e preencha: **Companhia** : Lufthansa **Origem** : FRA **Destino** : FLL **Horário Previsto** : 05:00 AMClique no botão " **Atualizar**" | Resultado 4:Modal de "Confirme atualização" com mensagem "Você deseja mesmo atualizar as informações de rota?" é exibido |
| | | Passo 5:Clique no botão " **Sim, atualizar!**" | Resultado 5:Modal com mensagem de sucesso é exibido |
| | | Passo 6:Clique no botão " **Ok**" | Resultado 6:Tela "Informações da rota" é exibida com as novas informações inseridas |
| 1. Cadastrar voo | 1.7 Tentativa de atualização de uma rota com dados inválidos | Passo 1: Faça login como operador de voo: **Nome do usuário:** michelet.chavez **Senha:** PCS3643 | Resultado 1:Tela "Registros de Rotas e de Voos" é exibida |
| | | Passo 2:Clique no botão " **Selecionar**" de "Rotas" e, em seguida, insira em "Informações de Rota": **Código de Voo** : AF123Clique no botão " **Buscar**" | Resultado 2:Tela "Informações da rota" é exibida com as informações correspondente à rota buscada |
| | | Passo 3:Clique no botão " **Atualizar**" | Resultado 3:Campos para inserção das novas informações são exibidos |
| | | Passo 4:Apague e preencha: **Companhia** : Air France **Origem** : FLL **Destino** : FLL **Horário Previsto** : 07:00 AMClique no botão " **Atualizar**" | Resultado 4:Modal de "Confirme atualização" com mensagem "Você deseja mesmo atualizar as informações de rota?" é exibido |
| | | Passo 5:Clique no botão " **Sim, atualizar!**" | Resultado 5:Modal com mensagem de erro é exibido (mesmo aeroporto de origem e destino) |
| | | Passo 6:Clique no botão " **Ok**" | Resultado 6:Tela "Informações da rota" é exibida com as informações originais |
| 1. Cadastrar voo | 1.8 Cadastro de um novo voo com dados válidos | Passo 1: Faça login como operador de voo: **Nome do usuário:** michelet.chavez **Senha:** PCS3643 | Resultado 1:Tela "Registros de Rotas e de Voos" é exibida |
| | | Passo 2:Clique no botão " **Selecionar**" de "Voos" e, em seguida, clique no botão " **Cadastrar**" de "Cadastro de Voos" | Resultado 2:Tela "Cadastro de um novo voo" é exibida |
| | | Passo 3:Selecione: **Código** : AF123 **Data Prevista** : 15/01/2023 | Resultado 3: Modal de "Confirmação das informações de cadastro" é exibido com as informações de voo preenchidas |
| | | Passo 4:Clique no botão " **Confirmar**" | Resultado 4:Modal com mensagem de sucesso é exibido |
| | | Passo 5:Clique no botão **Ok** | Resultado 5:Tela "Cadastro de um novo voo" é exibida novamente com inputs vazios |
| 1. Cadastrar voo | 1.9 Tentativa de cadastro de um voo com dados inválidos | Passo 1: Faça login como operador de voo: **Nome do usuário:** michelet.chavez **Senha:** PCS3643 | Resultado 1:Tela "Registros de Rotas e de Voos" é exibida |
| | | Passo 2:Clique no botão " **Selecionar**" de "Voos" e, em seguida, clique no botão " **Cadastrar**" de "Cadastro de Voos" | Resultado 2:Tela "Cadastro de um novo voo" é exibida |
| | | Passo 3: Não selecione nenhuma informação | Resultado 3: Modal de "Confirmação das informações de cadastro" é exibido sem informações de voo preenchidas |
| | | Passo 4:Clique no botão " **Confirmar**" | Resultado 4:Modal com mensagem de erro é exibido (nenhuma informação) |
| | | Passo 5:Clique no botão **Ok** | Resultado 5:Tela "Cadastro de um novo voo" é exibida novamente |
| 1. Cadastrar voo | 1.10 Tentativa de cadastro de um voo já cadastrado | Passo 1: Faça login como operador de voo: **Nome do usuário:** michelet.chavez **Senha:** PCS3643 | Resultado 1:Tela "Registros de Rotas e de Voos" é exibida |
| | | Passo 2:Clique no botão " **Selecionar**" de "Voos" e, em seguida, clique no botão " **Cadastrar**" de "Cadastro de Voos" | Resultado 2:Tela "Cadastro de um novo voo" é exibida |
| | | Passo 3:Selecione: **Código** : AF123 **Data Prevista** : 15/01/2023 | Resultado 3: Modal de "Confirmação das informações de cadastro" é exibido com as informações de voo preenchidas |
| | | Passo 4:Clique no botão " **Confirmar**" | Resultado 4:Modal com mensagem de erro é exibido (voo já cadastrado) |
| | | Passo 5:Clique no botão **Ok** | Resultado 5:Tela "Cadastro de um novo voo" é exibida novamente com inputs vazios |
| 1. Cadastrar voo | 1.11 Leitura das informações de um voo já cadastrado | Passo 1: Faça login como operador de voo: **Nome do usuário:** michelet.chavez **Senha:** PCS3643 | Resultado 1:Tela "Registros de Rotas e de Voos" é exibida |
| | | Passo 2:Clique no botão " **Selecionar**" de "Voos" e, em seguida, insira em "Informações de Voo": **Código de Voo** : AF123 **Data Prevista** : 15/01/2023Clique no botão " **Buscar**" | Resultado 2:Tela "Informações de voo" é exibida com as informações correspondente ao voo buscado |
| 1. Cadastrar voo | 1.12 Tentativa de leitura das informações de um voo ainda não cadastrado | Passo 1: Faça login como operador de voo: **Nome do usuário:** michelet.chavez **Senha:** PCS3643 | Resultado 1:Tela "Registros de Rotas e de Voos" é exibida |
| | | Passo 2:Clique no botão " **Selecionar**" de "Voos" e, em seguida, insira em "Informações de Voo": **Código de Voo** : LH123 **Data Prevista** : 18/01/2023Clique no botão " **Buscar**" | Resultado 2:Modal com mensagem de erro é exibido (voo não cadastrado) |
| | | Passo 5:Clique no botão **Ok** | Resultado 5:Tela "Registro de voos" é exibida |
| 1. Cadastrar voo | 1.13 Atualização das informações de um voo cadastrado | Passo 1: Faça login como operador de voo: **Nome do usuário:** michelet.chavez **Senha:** PCS3643 | Resultado 1:Tela "Registros de Rotas e de Voos" é exibida |
| | | Passo 2:Clique no botão " **Selecionar**" de "Voos" e, em seguida, insira em "Informações de Voo": **Código de Voo** : AF123 **Data Prevista** : 15/01/2023Clique no botão " **Buscar**" | Resultado 2:Tela "Informações de voo" é exibida com as informações correspondente ao voo buscado |
| | | Passo 3:Clique no botão " **Atualizar**" | Resultado 3:Campo para inserção da nova data prevista é exibido |
| | | Passo 4:Selecione: **Data Prevista** : 16/01/2023Clique no botão " **Atualizar**" | Resultado 4:Modal de "Confirme atualização" com mensagem "Você deseja mesmo atualizar a data prevista do voo?" é exibido |
| | | Passo 5:Clique no botão " **Sim, atualizar!**" | Resultado 5:Modal com mensagem de sucesso é exibido |
| | | Passo 6:Clique no botão " **Ok**" | Resultado 6:Tela "Informações de voo" é exibida com a nova informação inserida |
| 1. Cadastrar voo | 1.14 Tentativa de atualização de um voo com dado inválido | Passo 1: Faça login como operador de voo: **Nome do usuário:** michelet.chavez **Senha:** PCS3643 | Resultado 1:Tela "Registros de Rotas e de Voos" é exibida |
| | | Passo 2:Clique no botão " **Selecionar**" de "Voos" e, em seguida, insira em "Informações de Voo": **Código de Voo** : AF123 **Data Prevista** : 16/01/2023Clique no botão " **Buscar**" | Resultado 2:Tela "Informações de voo" é exibida com as informações correspondente ao voo buscado |
| | | Passo 3:Clique no botão " **Atualizar**" | Resultado 3:Campo para inserção da nova data prevista é exibido |
| | | Passo 4:Não selecione nenhuma data prevista e clique no botão " **Atualizar**" | Resultado 4:Modal de "Confirme atualização" com mensagem "Você deseja mesmo atualizar a data prevista do voo?" é exibido |
| | | Passo 5:Clique no botão " **Sim, atualizar!**" | Resultado 5:Modal com mensagem de erro é exibido (nova data prevista não foi definida) |
| | | Passo 6:Clique no botão " **Ok**" | Resultado 6:Tela "Informações de voo" é exibida com as informações originais |
| 1. Cadastrar voo | 1.15 Exclusão de uma rota com seus voos associados | Passo 1: Faça login como operador de voo: **Nome do usuário:** michelet.chavez **Senha:** PCS3643 | Resultado 1:Tela "Registros de Rotas e de Voos" é exibida |
| | | Passo 2:Clique no botão " **Selecionar**" de "Rotas" e, em seguida, insira em "Informações de Rota": **Código de Voo** : AF123Clique no botão " **Buscar**" | Resultado 2:Tela "Informações da rota" é exibida com as informações correspondente à rota buscada |
| | | Passo 3:Clique no botão " **Excluir**" | Resultado 4:Modal de "Confirme exclusão" com mensagem "Você deseja mesmo excluir essa rota?" é exibido |
| | | Passo 4:Clique no botão " **Excluir**" | Resultado 5:Modal com mensagem de sucesso é exibido |
| | | Passo 5:Clique no botão " **Ok**" | Resultado 6:Tela "Registros de Rotas" é exibida novamente |
| | | Passo 6:Clique no botão "Voltar para Registros de Voos", em seguida, clique no botão "Voltar para Registro de Rotas e de Voos" | Resultado 6:Tela "Registros de Rotas e de Voos" é exibida novamente |
| | | Passo 7:Clique no botão " **Selecionar**" de "Voos" e, em seguida, insira em "Informações de Voo": **Código de Voo** : AF123 **Data Prevista** : 16/01/2023Clique no botão " **Buscar**" | Resultado 7:Modal com mensagem de erro é exibido (voo excluído) |
| | | Passo 8:Clique no botão **Ok** | Resultado 8:Tela "Registro de voos" é exibida |
| 2. Monitorar voo | **2.1 Visualização de voo** : quando o usuário tem permissão para tal | Passo 1: Faça login como um usuário piloto ( **francisco.mariani, SR71** ) | Resultado 1: Dashboard de monitoramento dos voos é exibido |
| | | Passo 2: Clique no card do código de voo a ser monitorado ( **AA122, Dez. 1** ) | Resultado 2: Tela com informações do voo é exibida |
| 2. Monitorar voo | **2.2 Visualização de voo** : visualização de um voo quando o usuário não tem permissão para tal | Passo 1: Faça login como um usuário piloto ( **francisco.mariani, SR71** ) | Resultado 1: Dashboard de monitoramento dos voos é exibido |
| | | Passo 2: Clique no card do código de voo a ser monitorado ( **UA679, Dez. 1** ) | Resultado 2: Tela de erro é exibida |
| 2. Monitorar voo | **2.3a Atualização do status de voo partindo** : atualização do status de voo de não iniciado para embarcando | Passo 1: Faça login como um usuário companhia aérea ( **lucas.garcia, B52** ) | Resultado 1: Dashboard de monitoramento dos voos é exibido |
| | | Passo 2: Clique no card do código de voo a ser atualizado ( **LH679, Dez. 1** ) | Resultado 2: Tela com informações do voo é exibida |
| | | Passo 3: Mude o dropdown do status de voo para 'embarcando'. Pressione em **'Atualizar'**. | Resultado 3: Modal de confirmação para que as informações sejam atualizadas é exibido |
| | | Passo 4: Confirme o pedido de atualização da informação: ' **Sim, atualizar!**' | Resultado 4: Aviso é acionado, notificando que as informações foram atualizadas |
| | | Passo 5: Volte para o painel de monitoramento de voo | Resultado 5: O voo é exibido com o status atualizado no painel |
| 2. Monitorar voo | **2.3b Atualização do status de voo partindo** : atualização do status de voo de embarcando para programado | Passo 1: Faça login como um usuário companhia aérea ( **lucas.garcia, B52** ) | Resultado 1: Dashboard de monitoramento dos voos é exibido |
| | | Passo 2: Clique no card do código de voo a ser atualizado ( **LH679, Dez. 1** ) | Resultado 2: Tela com informações do voo é exibida |
| | | Passo 3: Mude o dropdown do status de voo para programado. Pressione em **'Atualizar'**. | Resultado 3: Modal de confirmação para que as informações sejam atualizadas é exibido |
| | | Passo 4: Confirme o pedido de atualização da informação: ' **Sim, atualizar!**' | Resultado 4: Aviso é acionado, notificando que as informações foram atualizadas |
| | | Passo 5: Volte para o painel de monitoramento de voo | Resultado 5: O voo é exibido com o status atualizado no painel |
| 2. Monitorar voo | **2.3c Atualização do status de voo partindo** : atualização do status de voo de programado para taxiando | Passo 1: Faça login como um usuário torre de controle ( **lucas.palmiro, A380** ) | Resultado 1: Dashboard de monitoramento dos voos é exibido |
| | | Passo 2: Clique no card do código de voo a ser atualizado ( **LH679, Dez. 1** ) | Resultado 2: Tela com informações do voo é exibida |
| | | Passo 3: Mude o dropdown do status de voo para taxiando. Pressione em **'Atualizar'**. | Resultado 3: Modal de confirmação para que as informações sejam atualizadas é exibido |
| | | Passo 4: Confirme o pedido de atualização da informação: ' **Sim, atualizar!**' | Resultado 4: Aviso é acionado, notificando que as informações foram atualizadas |
| | | Passo 5: Volte para o painel de monitoramento de voo | Resultado 5: O voo é exibido com o status atualizado no painel |
| 2. Monitorar voo | **2.3d Atualização do status de voo partindo** : atualização do status de voo de taxiando para pronto | Passo 1: Faça login como um usuário piloto ( **francisco.mariani, SR71** ) | Resultado 1: Dashboard de monitoramento dos voos é exibido |
| | | Passo 2: Clique no card do código de voo a ser atualizado ( **LH679, Dez. 1** ) | Resultado 2: Tela com informações do voo é exibida |
| | | Passo 3: Mude o dropdown do status de voo para pronto. Pressione em **'Atualizar'**. | Resultado 3: Modal de confirmação para que as informações sejam atualizadas é exibido |
| | | Passo 4: Confirme o pedido de atualização da informação: ' **Sim, atualizar!**' | Resultado 4: Aviso é acionado, notificando que as informações foram atualizadas |
| | | Passo 5: Volte para o painel de monitoramento de voo | Resultado 5: O voo é exibido com o status atualizado no painel |
| 2. Monitorar voo | **2.3e Atualização do status de voo partindo** : atualização do status de voo de pronto para autorizado | Passo 1: Faça login como um usuário torre de controle ( **lucas.palmiro, A380** ) | Resultado 1: Dashboard de monitoramento dos voos é exibido |
| | | Passo 2: Clique no card do código de voo a ser atualizado ( **LH679, Dez. 1** ) | Resultado 2: Tela com informações do voo é exibida |
| | | Passo 3: Mude o dropdown do status de voo para autorizado. Pressione em **'Atualizar'**. | Resultado 3: Modal de confirmação para que as informações sejam atualizadas é exibido |
| | | Passo 4: Confirme o pedido de atualização da informação: ' **Sim, atualizar!**' | Resultado 4: Aviso é acionado, notificando que as informações foram atualizadas |
| | | Passo 5: Volte para o painel de monitoramento de voo | Resultado 5: O voo é exibido com o status atualizado no painel |
| 2. Monitorar voo | **2.3f Atualização do status de voo partindo** : atualização do status de voo de autorizado para em voo | Passo 1: Faça login como um usuário piloto ( **francisco.mariani, SR71** ) | Resultado 1: Dashboard de monitoramento dos voos é exibido |
| | | Passo 2: Clique no card do código de voo a ser atualizado ( **LH679, Dez. 1** ) | Resultado 2: Tela com informações do voo é exibida |
| | | Passo 3: Mude o dropdown do status de voo para em voo. Pressione em **'Atualizar'**. | Resultado 3: Modal de confirmação para que as informações sejam atualizadas é exibido |
| | | Passo 4: Confirme o pedido de atualização da informação: ' **Sim, atualizar!**' | Resultado 4: Aviso é acionado, notificando que as informações foram atualizadas |
| | | Passo 5: Volte para o painel de monitoramento de voo | Resultado 5: O voo é exibido com o status atualizado no painel |
| 2. Monitorar voo | **2.3g Atualização do status de voo partindo** : atualização do status de voo de em voo para decolagem bem sucedida | Passo 1: Faça login como um usuário companhia aérea ( **lucas.palmiro, A380** ) | Resultado 1: Dashboard de monitoramento dos voos é exibido |
| | | Passo 2: Clique no card do código de voo a ser atualizado ( **LH679, Dez. 1** ) | Resultado 2: Tela com informações do voo é exibida |
| | | Passo 3: Mude o dropdown do status de voo para **decolagem bem sucedida**. Preencha a data real como **12/01/2022** , e a hora real como **11:40 PM**.Pressione em **'Atualizar'**. | Resultado 3: Modal de confirmação para que as informações sejam atualizadas é exibido |
| | | Passo 4: Confirme o pedido de atualização da informação: ' **Sim, atualizar!**' | Resultado 4: Aviso é acionado, notificando que as informações foram atualizadas |
| | | Passo 5: Clique em OK | Resultado 4: Dashboard de monitoramento dos voos é exibido, com as novas informações do voo. |
| | | Passo 6: Volte para o painel de monitoramento de voo | Resultado 6: O voo é exibido com o status atualizado no painel |
| 2. Monitorar voo | **2.4a Atualização do status de voo chegando** : atualização do status de voo de previsto para em voo | Passo 1: Faça login como um usuário torre de controle ( **lucas.palmiro, A380** ) | Resultado 1: Dashboard de monitoramento dos voos é exibido |
| | | Passo 2: Clique no card do código de voo a ser atualizado ( **AF679, Dez. 1** ) | Resultado 2: Tela com informações do voo é exibida |
| | | Passo 3: Mude o dropdown do status de voo para em voo. Pressione em **'Atualizar'**. | Resultado 3: Modal de confirmação para que as informações sejam atualizadas é exibido |
| | | Passo 4: Confirme o pedido de atualização da informação: ' **Sim, atualizar!**' | Resultado 4: Aviso é acionado, notificando que as informações foram atualizadas |
| | | Passo 5: Volte para o painel de monitoramento de voo | Resultado 5: O voo é exibido com o status atualizado no painel |
| 2. Monitorar voo | **2.4b Atualização do status de voo chegando** : atualização do status de voo de em voo para aterissado | Passo 1: Faça login como um usuário torre de controle ( **lucas.palmiro, A380** ) | Resultado 1: Dashboard de monitoramento dos voos é exibido |
| | | Passo 2: Clique no card do código de voo a ser atualizado ( **AF679, Dez. 1** ) | Resultado 2: Tela com informações do voo é exibida
| | | Passo 3: Mude o dropdown do status de voo para aterrisado. Pressione em **'Atualizar'**. | Resultado 3: Modal de confirmação para que as informações sejam atualizadas é exibido
| | | Passo 4: Confirme o pedido de atualização da informação: ' **Sim, atualizar!**' | Resultado 4: Aviso é acionado, notificando que as informações foram atualizadas
| | | Passo 5: Volte para o painel de monitoramento de voo | Resultado 5: O voo é exibido com o status atualizado no painel
| 2. Monitorar voo | **2.5 Atualização inválida da data e hora de voo** : tentativa de atualização da data e hora do voo quando o usuário tem permissão para tal, porém escolhendo uma hora de partida real anterior à programada. | Passo 1: Faça login como um usuário companhia aérea ( **lucas.palmiro, A380** ) | Resultado 1: Dashboard de monitoramento dos voos é exibido |
| | | Passo 2: Clique no card do código de voo a ser atualizado ( **BA246, Dez. 1** ) | Resultado 2: Tela com informações do voo é exibida |
| | | Passo 3: Mude o dropdown do status de voo para **'embarcando'**. Preencha a data real como **09/08/2022** , e a hora real como **07:00 AM**.Pressione em **'Atualizar'**. | Resultado 3: Modal de confirmação para que as informações sejam atualizadas é exibido |
| | | Passo 4: Confirme o pedido de atualização da informação: ' **Sim, atualizar!**' | Resultado 4: Aviso é acionado, notificando erro no campo 'hora real'
| 3. Gerar relatório administrativo | **3.1 Acesso ao fluxo de geração de relatório** Verificação se o comando de gerar relatório inicia a sequência de ações referente ao processo de geração de relatórios administrativos | Passo 1: Faça login como um gerente de operação ( **kechi.hirama, PCS3643** ) | Resultado 1:Tela "Geração de Relatórios" é exibida. |
| 3. Gerar relatório administrativo | **3.2. Inserção de período de análise inválido** Verificação se o sistema impede a geração de relatório quando a data de início é posterior à data de fim | Passo 1: Faça login como um gerente de operação ( **kechi.hirama, PCS3643** ) | Resultado 1:Tela "Geração de Relatórios" é exibida.
| | | Passo 2: Selecione uma opção data de fim anterior à data de início (data de início = '17/12/2022' e data de fim = '02/12/2022') | Resultado 2: O Sistema não permite a tentativa de seleção de data feita, movendo a opção de data de início para a data de fim recém escolhida
| 3. Gerar relatório administrativo | **3.3 Inserção de período de análise sem nenhum registro de voo finalizado (relatório geral)**Verificação se o sistema impede a geração de relatório geral quando não há registros de voos concluídos ('cancelado', 'decolagem finalizada', 'aterrissado') para o período de análise informado | Passo 1: Faça login como um gerente de operação ( **kechi.hirama, PCS3643** ) | Resultado 1:Tela "Geração de Relatórios" é exibida.
| | | Passo 2: Selecione datas de início e fim, mas que correspondem a um período de tempo para o qual sabidamente não há voos registrados como concluídos.(04/08/2022 e 05/08/2022) | Resultado 2: Tela "Geração de Relatórios" é atualizada, com o _input_ de seleção de período de análise atualizado para '04/08/2022 - 05/08/2022'
| | | Passo 3: Selecione o tipo geral de relatório | Resultado 3: Mensagem de erro é exibida informando que não há voos registrados como concluídos para o período selecionado. |
| 3. Gerar relatório administrativo | **3.4 Inserção de período de análise sem nenhum registro de voo finalizado (relatório específico)**Verificação se o sistema impede a geração de relatório específico quando não há não há registros de voos finalizados (status 'cancelado', 'decolagem finalizada', 'aterrissado') para o período de análise informado | Passo 1: Faça login como um gerente de operação ( **kechi.hirama, PCS3643** ) | Resultado 1:Tela "Geração de Relatórios" é exibida.
| | | Passo 2: Selecione datas de início e fim, mas que correspondem a um período de tempo para o qual sabidamente não há voos registrados como concluídos.(04/08/2022 e 05/08/2022) | Resultado 2:Tela "Geração de Relatórios" é atualizada, com o _input_ de seleção de período de análise atualizado para '04/08/2022 - 05/08/2022' |
| | | Passo 3: Selecione o tipo específico de relatório | Resultado 3: Mensagem de erro é exibida informando que não há voos registrados como concluídos para o período selecionado. |
| 3. Gerar relatório administrativo | **3.5 Inserção de período de análise com registros de voos finalizados (relatório específico)**Verificação se o sistema gera relatório com informações específicas sobre os voos finalizados (status 'cancelado', 'decolagem finalizada' ou 'aterrissado') quando o tipo de relatório específico é selecionado | Passo 1: Faça login como um gerente de operação ( **kechi.hirama, PCS3643** ) | Resultado 1:Tela "Geração de Relatórios" é exibida.
| | | Passo 2: Selecione datas de início e fim que correspondem a um período de tempo para o qual sabidamente há voos registrados como concluídos ou cancelados(07/11/2022 e 03/12/2022) | Resultado 2: Tela "Geração de Relatórios" é atualizada, , com o _input_ de seleção de período de análise atualizado para '07/11/2022 - 03/12/2022'
| | | Passo 3: Selecione o tipo específico de relatório | Resultado 3:Exibição de um relatório contendo informações específicas sobre todos os voos finalizados (status 'cancelado', 'decolagem finalizada' ou 'aterrissado') para o período de análise informado |
| 3. Gerar relatório administrativo | **3.6 Inserção de período de análise com registros de voos finalizados (relatório geral)**Verificação se o sistema gera relatório com informações gerais sobre os voos finalizados (status 'cancelado', 'decolagem finalizada' ou 'aterrissado') quando o tipo de relatório geral é selecionado | Passo 1: Faça login como um gerente de operação ( **kechi.hirama, PCS3643** ) | Resultado 1:Tela "Geração de Relatórios" é exibida.
| | | Passo 2: Selecione datas de início e fim que correspondem a um período de tempo para o qual sabidamente há voos registrados como concluídos ou cancelados(07/11/2022 e 03/12/2022) | Resultado 2: Tela "Geração de Relatórios" é atualizada, com o _input_ de seleção de período de análise atualizado para '07/11/2022 - 03/12/2022'
| | | Passo 3: Selecione o tipo geral de relatório | Resultado 3:Exibição de um relatório contendo informações gerais sobre todos os voos finalizados (status 'cancelado', 'decolagem finalizada' ou 'aterrissado') para cada companhia aérea no período selecionado