# Plano de Testes de Validação

## Introdução

Este documento tem como objetivo orientar a condução dos testes de validação a serem executados sobre o sistema de monitoramento de voos, sendo dirigido aos seguintes stakeholders: o gerente de projeto, os analistas de configuração e os analistas de qualidade, os quais executarão os casos de teste.

Para tanto, apresentam-se de forma detalhada os passos a serem seguidos, bem como os respectivos resultados esperados para cada caso de teste. Além disso, identificam-se os recursos tanto materiais quanto humanos necessários para a execução dos testes.

## Teste de Validação

Teste de Validação pode ser compreendido como um conjunto de ações que visam verificar se o sistema sobre o qual é aplicado está em conformidade com os requisitos previstos nas especificações dos seus casos de uso.

## Recursos Necessários

Os recursos materiais necessários para a execução do plano de testes apresentado neste documento são:

- Ambiente de teste:
  - Servidor local de teste
  - Banco de dados de teste
- Softwares do _stack_ escolhido:
  - Django
  - SQLite
  - Deployer (a ser escolhido)
- Exemplos de dados de voos do aeroporto cadastrados no banco de dados de teste.
- Simulação (física ou digital) de um painel de monitoramento.

Além disso, são necessários como recursos humanos analistas de qualidade, que executarão os casos de teste, inserindo entradas como usuários do sistema e verificando os resultados obtidos.

Esses analistas de qualidade devem, idealmente, ter a capacidade técnica para compreender e detalhar os erros encontrados; no entanto, não devem ter participado do projeto, de forma que não haja vieses indesejáveis durante os testes.

## Casos de Teste

| **Caso de Uso** | **Descrição** | **Passos (Entradas)** | **Resultados Esperados (saídas)** |
| --- | --- | --- | --- |
| 1. Cadastrar voo | 1.1 Inserção de código de voo ainda não cadastrado na ação de cadastro de um novo voo | Passo 1: selecione a opção de cadastro de voo | Resultado 1: interface para o operador de voo é exibida e o código de voo é solicitado |
| | | Passo 2: insira o código de voo ("AF0443") não cadastrado | Resultado 2: tela aparece, com opções para o tipo de ação (CRUD) a ser escolhida |
| | | Passo 3: selecione a ação de cadastro de um novo voo | Resultado 3: tela aparece, solicitando o preenchimento das informações básicas do voo |
| 1. Cadastrar voo | 1.2 Inserção de código de voo já cadastrado na ação de cadastro de um novo voo | Passo 1: selecione a opção de cadastro de voo | Resultado 1: interface para o operador de voo é exibida e o código de voo é solicitado |
| | | Passo 2: insira um código de voo já cadastrado ("AF0443") | Resultado 2: tela aparece, com opções para o tipo de ação (CRUD) a ser escolhida |
| | | Passo 3: selecione a ação de cadastro de um novo voo | Resultado 3: alarme é acionado e mensagem de erro é exibida |
| 1. Cadastrar voo | 1.3 Inserção de código de voo já cadastrado nas ações de leitura ou atualização ou exclusão de um voo | Passo 1: selecione a opção de cadastro de voo | Resultado 1: interface para o operador de voo é exibida e o código de voo é solicitado |
| | | Passo 2: insira um código de voo já cadastrado ("AF0443") | Resultado 2: tela aparece, com opções para o tipo de ação (CRUD) a ser escolhida |
| | | Passo 3: selecione a ação de leitura ou atualização ou exclusão de um voo | Resultado 3: tela correspondente à ação escolhida é apresentada |
| 1. Cadastrar voo | 1.4 Inserção de código de voo não cadastrado nas ações de leitura ou atualização ou exclusão de um voo | Passo 1: selecione a opção de cadastro de voo | Resultado 1: interface para o operador de voo é exibida e o código de voo é solicitado |
| | | Passo 2: insira um código de voo não cadastrado("LA 8070") | Resultado 2: tela aparece, com opções para o tipo de ação (CRUD) a ser escolhida |
| | | Passo 3: selecione a ação de leitura ou atualização ou exclusão de um voo | Resultado 3: alarme é acionado e mensagem de erro é exibida |
| 1. Cadastrar voo | 1.5 Cadastro de um novo voo com todas as informações básicas | Passo 1: realize caso de teste 1.1 | Resultado 1: as informações básicas do voo são solicitadas |
| | | Passo 2: insira as informações mínimas de voo com dados válidos('AirFrance', 'FLL - CDG', ''11/11/11', '11:11') | Resultado 2: informações inseridas são exibidas e a confirmação é solicitada |
| 1. Cadastrar voo | 1.6 Cadastro de um novo voo com informações básicas faltantes | Passo 1: realize caso de teste 1.1 | Resultado 1: as informações básicas do voo são solicitadas |
| | | Passo 2: não insira todas as informações básicas necessárias('@@', 'FLL - CDG', ''11/11/11', '11:11') | Resultado 2: alarme é acionado e mensagem de erro é exibida |
| 1. Cadastrar voo | 1.7 Leitura das informações de um voo | Passo 1: selecione a opção de cadastro de voo | Resultado 1: interface para o operador de voo é exibida e o código de voo é solicitado |
| | | Passo 2: insira um código de voo já cadastrado ("AF0443") | Resultado 2: tela aparece, com opções para o tipo de ação (CRUD) a ser escolhida |
| | | Passo 3: selecione a ação de leitura das informações de um voo | Resultado 3: Informações do voo são exibidas |
| 1. Cadastrar voo | 1.8 Atualização das informações de um voo com dados consistentes | Passo 1: selecione a opção de cadastro de voo | Resultado 1: interface para o operador de voo é exibida e o código de voo é solicitado |
| | | Passo 2: insira um código de voo já cadastrado ("AF0443") | Resultado 2: tela aparece, com opções para o tipo de ação (CRUD) a ser escolhida |
| | | Passo 3: selecione a ação de atualização das informações de um voo | Resultado 3: novas informações do voo são solicitadas |
| | | Passo 4: insira novas informações consistentes('AirFrance', 'FLL - CDG', ''11/11/12', '12:12') | Resultado 4: informações do voo são atualizadas |
| 1. Cadastrar voo | 1.9 Atualização das informações de um voo com dados inconsistentes | Passo 1: selecione a opção de cadastro de voo | Resultado 1: interface para o operador de voo é exibida e o código de voo é solicitado |
| | | Passo 2: insira um código de voo já cadastrado ("AF0443") | Resultado 2 tela aparece, com opções para o tipo de ação (CRUD) a ser escolhida |
| | | Passo 3: selecione a ação de atualização das informações de um voo | Resultado 3: novas informações do voo são solicitadas |
| | | Passo 4: insira novas informações inconsistentes ('AirFrance', 'FLL - CDG', ''32/02/12', '12:12') | Resultado 4: atualização das informações é cancelada, alarme é acionado e mensagem de erro é exibida |
| 1. Cadastrar voo | 1.10 Exclusão de um voo | Passo 1: selecione a opção de cadastro de voo | Resultado 1: interface para o operador de voo é exibida e o código de voo é solicitado |
| | | Passo 2: insira um código de voo já cadastrado ("AF0443") | Resultado 2: tela aparece, com opções para o tipo de ação (CRUD) a ser escolhida |
| | | Passo 3: selecione a ação de exclusão de um voo | Resultado 3: informações do voo são excluídas |
| 2. Monitorar voo | 2.1 Visualização de voo : inserção de um um código válido. | Passo 1: Escolha a opção de monitoramento de voo | Resultado 1: Painel de monitoramento dos voos é exibido |
| | | Passo 2: Insira um código de voo existente e selecione a ação de monitoramento ("AF0443") | Resultado 2: Informações do voo selecionado são exibidas. |
| 2. Monitorar voo | 2.2 Visualização de voo : inserção de um código inválido. | Passo 1: Escolha a opção de monitoramento de voo | Resultado 1: Painel de monitoramento dos voos é exibido |
| | | Passo 2: Insira um código de voo inexistente e selecione a ação de monitoramento ("LA 8070") | Resultado 2: Aviso com alarme é ativado, explicitando que o voo não existe |
| 2. Monitorar voo | 2.3 Atualização de voo : atualização com informações válidas. | Passo 1: Realize o caso de teste 2.1. | Resultado 1: Informações do voo selecionado são exibidas. |
| | | Passo 2: Selecione a ação de atualizar as informações do voo. | Resultado 2: Espaços para inserir novos dados do voo são exibidos |
| | | Passo 3: Insira novas informações, com conteúdo válido('em voo', '11/11/11', '11:16') | Resultado 3: Solicitação de confirmação para que as informações sejam atualizadas é exibida |
| | | Passo 4: Confirme o pedido de atualização da informação | Resultado 4: Aviso é acionado, notificando que as informações foram atualizadas |
| 2. Monitorar voo | 2.4 Atualização de voo : atualização com informações inválidas | Passo 1: Realize o caso de teste 2.1. | Resultado 1: Informações do voo selecionado são exibidas. |
| | | Passo 2: Selecione a opção de atualizar as informações do voo. | Resultado 2: Espaços para inserir novos dados do voo são exibidos |
| | | Passo 3: Insira novas informações, com conteúdo inválido | Resultado 3: Alarme é acionado e mensagem de erro é exibida. |
| 2. Monitorar voo | 2.5 Atualização do painel de monitoramento | Passo 1: Realize o caso de teste 2.3. | Resultado 1: Aviso é acionado, notificando que as informações foram atualizadas |
| | | Passo 2: Escolha a ação de monitoramento de voo | Resultado 1: Painel de monitoramento dos voos é exibido, com informações atualizadas |
| | | 3. Gerar relatório administrativo | Verificar se o comando de gerar relatório inicia a sequência de ações referente a esse processo | Passo 1: seleciona a opção de gerar relatório administrativo. | Resultado 1: A primeira etapa do fluxo para geração de relatório é mostrada: solicitação do período de análise |
| 3. Gerar relatório administrativo | Verificar se o sistema impede a inserção de dado inválido no campo de data início | Passo 1: Selecione a opção de gerar relatório administrativo | Resultado 1: Exibição das data de início e fim para preenchimento |
| | | Passo 2: Insira um dado inválido no campo para data de início e um dado válido no campo para data de fim ('xx yy' e '02/07/2022') | Resultado 2: Mensagem de erro é exibida, alarme é acionado |
| 3. Gerar relatório administrativo | Verificar se o sistema impede a inserção de dado inválido no campo de data fim | Passo 1: Selecione a opção de gerar relatório administrativo | Resultado 1: Exibição dos campos de data de início e de fim para preenchimento |
| | | Passo 2: Insira um dado válido no campo para data de início e um dado inválido no campo para data de fim ('02/07/2022' e ''xx yy') | Resultado 2: Mensagem de erro é exibida, alarme é acionado |
| 3. Gerar relatório administrativo | Verificar se o sistema impede a geração de relatório quando a data de início é posterior à data de fim | Passo 1: Selecione a opção de gerar relatório administrativo | Resultado 1: Exibição dos campos de data de início e de fim para preenchimento |
| | | Passo 2: Insira uma data de início posterior à data de fim (data de início = '17/07/2022' e data de fim = '02/07/2022') | Resultado 2: Mensagem de erro é exibida, alarme é acionado |
| 3. Gerar relatório administrativo | Verificar se o sistema impede a geração de relatório quando não há voos registrados para o período de análise informado | Passo 1: Selecione a opção de gerar relatório administrativo | Resultado 1: Exibição dos campos de data de início e de fim para preenchimento |
| | | Passo 2: Insira datas de início e fim válidas, mas que correspondem a um período de tempo para qual sabidamente não há voos registrados('01/01/1900' e '01/01/1901') | Resultado 2: Mensagem de erro é exibida, alarme é acionado |
| 3. Gerar relatório administrativo | Verificar se o sistema gera relatório com informações gerais sobre os voos quando o tipo de relatório geral é selecionado | Passo 1: Selecione a opção de gerar relatório administrativo | Resultado 1: Exibição dos campos de data de início e de fim para preenchimento |
| | | Passo 2: Insira datas de início e fim válidas, correspondendo a um período de tempo para o qual sabidamente há voos registrados('02/07/2022' e '17/07/2022') | Resultado 2: Solicitação para escolha do tipo de relatório a ser gerado (geral ou específico) |
| | | Passo 3: Selecione o tipo geral de relatório | Resultado 3: Exibição de um relatório contendo informações gerais sobre todos os voos registrados para o período de análise informado |
| 3. Gerar relatório administrativo | Verificar se o sistema gera relatório com informações específicas sobre os voos quando o tipo de relatório específico é selecionado | Passo 1: Selecione a opção de gerar relatório administrativo | Resultado 1: Exibição dos campos de data de início e de fim para preenchimento |
| | | Passo 2: Insira datas de início e fim válidas ('02/07/2022' e '17/07/2022'), correspondendo a um período de tempo para o qual sabidamente há voos registrados | Resultado 2: Solicitação para escolha do tipo de relatório a ser gerado (geral ou específico) |
| | | Passo 3: Selecione o tipo específico de relatório | Resultado 3: Exibição de um relatório contendo informações específicas sobre todos os voos registrados para o período de análise informado |