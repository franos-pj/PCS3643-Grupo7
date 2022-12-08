# Modelo de Casos de Uso

## Caso de Uso 1

**Nome:** Cadastrar voo

**Descrição:** Cadastrar, ler, atualizar e deletar as informações básicas de uma rota ou de um voo

**Evento iniciador:** seleção de cadastro de rota no sistema

**Atores:** Operador de voo

**Pré-condição:** não aplicável

**Sequência de eventos:**

1. Operador de voo seleciona a opção de cadastro de rota.
2. Sistema solicita código de voo, companhia aérea, aeroporto de origem, aeroporto de destino e horário previsto.
3. Operador de voo insere as informações solicitadas.
4. Sistema solicita a confirmação das informações de cadastro de rota.
5. Operador de voo confirma o cadastro da rota.
6. Sistema verifica se todas as informações foram inseridas e também a validade das mesmas (código de voo ainda não cadastrado, aeroporto de origem diferente de destino e um dos aeroportos como FLL).
7. Sistema armazena as informações inseridas da nova rota no banco de dados e exibe mensagem de sucesso ao operador de voo.
8. Operador de voo finaliza a operação de cadastro de rota.
9. Fim do caso de uso.

**Pós-condição:** informações da rota cadastradas no banco de dados do sistema

**Fluxos alternativos:**

1. Operador de voo seleciona opção de leitura das informações de uma rota (passo 1):
  * a. Sistema solicita o código de voo da rota.
  * b. Operador de voo seleciona um código de voo e solicita a busca da rota.
  * c. Sistema exibe as informações armazenadas correspondentes ao código do voo da rota.
  * d. Operador de voo finaliza a operação de leitura de rota.
  * e. Fim do fluxo alternativo.

2. Operador de voo seleciona opção de atualização das informações de uma rota (passo 1):
  * a. Sistema solicita o código de voo da rota.
  * b. Operador de voo seleciona um código de voo e solicita a busca da rota.
  * c. Sistema exibe as informações armazenadas correspondentes ao código do voo da rota.
  * d. Operador de voo seleciona opção de atualização da rota.
  * e. Sistema solicita a inserção das novas informações da rota.
  * f. Operador de voo insere novas informações da rota e solicita atualização.
  * g. Sistema solicita a confirmação da atualização das informações da rota.
  * h. Operador de voo confirma a atualização da rota.
  * i. Sistema verifica se todas as informações estão presentes e também a validade das mesmas.
  * j. Sistema armazena as informações atualizadas da rota no banco de dados, exibe mensagem de sucesso e também as informações atualizadas da rota ao operador de voo.
  * k. Operador de voo finaliza a operação de atualização de rota.
  * l. Fim do fluxo alternativo.

3. Operador de voo seleciona opção de exclusão de uma rota (passo 1):
  * a. Sistema solicita o código de voo da rota.
  * b. Operador de voo seleciona um código de voo e solicita a busca da rota.
  * c. Sistema exibe as informações armazenadas correspondentes ao código do voo da rota.
  * d. Operador de voo seleciona opção de exclusão da rota.
  * e. Sistema solicita a confirmação da exclusão da rota.
  * f. Operador de voo confirma a exclusão da rota.
  * g. Sistema exclui as informações da rota e dos voos associados a esta rota do banco de dados, e exibe mensagem de sucesso ao operador de voo.
  * k. Operador de voo finaliza a operação de exclusão de rota.
  * l. Fim do fluxo alternativo.

4. Operador de voo seleciona a opção de cadastro de um novo voo (Passo 1):
* a. Sistema solicita código de voo de rota já cadastrada e data prevista.
* b. Operador de voo seleciona um código de voo, insere uma data prevista e solicita o cadastro.
* c. Sistema solicita a confirmação das informações de cadastro de voo.
* d. Operador de voo confirma o cadastro do voo.
* e. Sistema verifica se todas as informações foram inseridas e também a validade das mesmas (código de voo já cadastrado e data prevista posterior a data atual).
* f. Sistema armazena as informações inseridas do novo voo no banco de dados e exibe mensagem de sucesso ao operador de voo.
* g. Operador de voo finaliza a operação de cadastro de voo.
* k. Fim do fluxo alternativo.

5. Operador de voo seleciona opção de leitura das informações de um voo (passo 1):
  * a. Sistema solicita o código de voo e data prevista do voo.
  * b. Operador de voo seleciona um código de voo, insere a data prevista e solicita a busca do voo.
  * c. Sistema exibe as informações armazenadas correspondentes ao código do voo e data prevista do voo.
  * d. Operador de voo finaliza a operação de leitura de voo.
  * e. Fim do fluxo alternativo.

6. Operador de voo seleciona opção de atualização das informações de um voo (passo 5):
  * a. Sistema solicita o código de voo e data prevista do voo.
  * b. Operador de voo seleciona um código de voo, insere a data prevista e solicita a busca do voo.
  * c. Sistema exibe as informações armazenadas correspondentes ao código do voo e data prevista do voo.
  * d. Operador de voo seleciona opção de atualização do voo.
  * e. Sistema solicita a inserção da nova data prevista do voo.
  * f. Operador de voo insere nova data prevista do voo e solicita atualização.
  * g. Sistema solicita a confirmação da atualização da data prevista do voo.
  * h. Operador de voo confirma a atualização do voo.
  * i. Sistema verifica se a informação da data prevista está presente e também a validade da mesma.
  * j. Sistema armazena a data prevista atualizada do voo no banco de dados, exibe mensagem de sucesso e também as informações atualizadas do voo ao operador de voo.
  * k. Operador de voo finaliza a operação de atualização de voo.
  * e. Fim do fluxo alternativo.

7. Operador de voo seleciona opção de exclusão de um voo (passo 5):
  * a. Sistema solicita o código de voo e data prevista do voo.
  * b. Operador de voo seleciona um código de voo, insere a data prevista e solicita a busca do voo.
  * c. Sistema exibe as informações armazenadas correspondentes ao código do voo e data prevista do voo.
  * d. Operador de voo seleciona opção de exclusão do voo.
  * e. Sistema solicita a confirmação da exclusão do voo.
  * f. Operador de voo confirma a exclusão do voo.
  * g. Sistema exclui as informações do voo do banco de dados e exibe mensagem de sucesso ao operador de voo.
  * k. Operador de voo finaliza a operação de exclusão de voo.
  * l. Fim do fluxo alternativo.

**Exceções:**

1. Há informações ausentes ou inválidas de rota (passo 6 ou Fluxo Alternativo 2 - passo i):
  * a. Sistema exibe mensagem de erro ao operador de voo.
  * b. Sistema cancela cadastro ou atualização da rota.
  * c. Fim do fluxo da exceção.
2. Nenhum código de voo de rota é selecionado (Fluxo Alternativo 1, 2 ou 3 - passo b):
  * a. Sistema exibe mensagem de erro ao operador de voo.
  * b. Fim do fluxo da exceção.
3. Há informações ausentes ou inválidas de voo (Fluxo Alternativo 4 - passo e ou Fluxo Alternativo 6 - passo i):
  * a. Sistema exibe mensagem de erro ao operador de voo.
  * b. Sistema cancela cadastro ou atualização do voo.
  * c. Fim do fluxo da exceção.
4. Nenhum código de voo de rota e/ou nenhuma data prevista é(são) selecionado(s) (Fluxo Alternativo 5, 6 ou 7 - passo b):
  * a. Sistema exibe mensagem de erro ao operador de voo.
  * b. Fim do fluxo da exceção.

## Caso de Uso 2

**Nome:** Monitorar voos

**Descrição:** Visualizar e atualizar as informações do voo (_status_ de voo e horários de chegada e partida reais)

**Evento iniciador:** redirecionamento para dashboard de monitoramento de voos após login (piloto, torre de controle, ou companhia aérea)

**Atores:** Funcionários das empresas aéreas, piloto do voo e torre de controle

**Pré-condição:** não aplicável

**Sequência de eventos:**

1. Sistema exibe o dashboard de monitoramento, com todos os voos no sistema
2. Usuário seleciona o voo que deseja editar no dashboard
3. Sistema exibe informações referentes ao voo, e solicita a inserção do _status_ atualizado e/ou dos horários reais do voo (chegada ou partida).
4. Usuário atualiza _status_ do voo ou insere horários reais do voo.
5. Sistema exibe as informações atualizadas e solicita confirmação.
6. Usuário confirma a atualização das informações.
7. Sistema verifica a consistência do _status_ atualizado e/ou dos horários reais inseridos e armazena as informações atualizadas no banco de dados.
8. Sistema exibe mensagem de sucesso, notificando que os dados do voo foram atualizados.
9. Fim do caso de uso.


**Pós-condição:** informações de _status_ e/ou de horários reais do voo atualizadas no banco de dados do sistema e exibidas no painel de monitoramento.

**Fluxos alternativos:**

1. Usuário apenas visualiza as informações do voo (passo 3):
  * a. Sistema exibe informações referentes ao voo.
  * b. Usuário finaliza a operação de visualização do voo.
  * c. Fim do fluxo alternativo.

**Exceções:**

1. Usuário não tem permissão para acessar aquele voo naquele momento (passo 2):
  * a. Sistema exibe mensagem de erro ao usuário.
  * b. Fim do fluxo da exceção.
2. _Status_ de voo ou horários reais inválidos (passo 7):
  * a. Sistema exibe mensagem de erro ao usuário.
  * b. Sistema cancela atualização do voo.
  * c. Fim do fluxo da exceção.

## Caso de Uso 3

**Nome:** Gerar relatório administrativo

**Descrição:** Buscar dados históricos sobre os voos realizados no aeroporto durante um período de tempo selecionado, e gerar um relatório administrativo reunindo de forma estruturada tais informações. O relatório deve abranger informações referentes ao desempenho dos voos de cada companhia aérea (tempos de atraso) e dados gerais sobre a movimentação do aeroporto (número de voos realizados por rota e por companhia aérea).

**Evento iniciador:** redirecionamento para a tela de geração de relatórios após login (gerente de operações)

**Ator(es):** Gerente de Operação

**Pré-condição:** não aplicável

**Sequência de eventos:**

1. Sistema exibe a tela de geração de relatórios, e solicita o período de análise para o relatório, assim como o tipo (geral do aeroporto ou específico à nível de voo).
2. Gerente de Operação insere a data de início e a data de fim da análise, e o tipo de relatório a ser gerado (geral).
3. Sistema verifica a consistência do período de tempo fornecido, a existência de voos no período selecionado, e busca as informações históricas.
4. Sistema gera relatório com informações gerais dos voos do aeroporto.
5. Fim do caso de uso.


**Pós-condição:** relatório administrativo gerado

**Fluxos alternativos:**

1. Usuário seleciona a opção de gerar relatório específico à nível de voo (passo 2):
  * a. Sistema gera relatório com informações específicas dos voos do aeroporto.
  * b. Fim do fluxo alternativo.

**Exceções:**

1. Período de tempo informado para análise apresenta data de início posterior a data de fim ou não há voos no período selecionado (passo 3):
  * a. Sistema exibe mensagem de erro ao operador de voo.
  * b. Fim do fluxo da exceção.

## Diagrama de Caso de Usos:

![Diagrama de Casos de Uso](./images/diagrama_casos_de_uso.png)