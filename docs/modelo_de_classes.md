# Modelo de Classes

## Classes de controle:

- ControladorRegistroVoos (FlightRecordController)
- ControladorMonitoramento (MonitoringController)
- ControladorRelatorio (ReportController)

## Classes de fronteira:

- InterfaceOperadorVoo (FlightOperatorInterface)
- InterfacePiloto (PilotInterface)
- InterfaceFuncionarioCompanhia (AirlineEmployeeInterface)
- InterfaceTorreDeControle (ControlTowerInterface)
- InterfaceMonitoramento (MonitoringInterface)
- RelatorioGeral (GeneralReport)
- RelatorioEspecifico (SpecificReport)

## Classes de entidade:

- Voo (Flight)

## Diagramas de Classes:

### Cadastrar voo:

![Cadastrar voo](./images/diagrama_classes_cadastrar.png)

### Monitorar voos:

![Monitorar voos](./images/diagrama_classes_monitoramento.png)

### Gerar relatório administrativo:

![Gerar relatório administrativo](./images/diagrama_classes_relatorios.png)