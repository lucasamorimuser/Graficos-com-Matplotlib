# Elaboração de gráficos com Matpltlib

#### Trabalho voltado na geração de gráficos para visualização de dados de exportação de etanol no Brasil

### Linguagem e Ferramentas

Python - Linguagem para desenvolvimento dos comandos

- Matplotlib - Biblioteca Python para criação de gráficos

- Pandas - Manipulação de dados

VS Code - Ferramenta de edição de código

Excel - Armazenamento dos dados em arquivo no formato .CSV

### Roteiro

Importação das bibliotecas PANDAS e MATPLOTLIB

Importação da base de dados .CSV

Análise exploratória dos dados (AED) através dos métodos pandas INFO e DESCRIBE

Formatação de coluna como numérica usando o método PANDAS PD.TO_NUMERIC, e do tipo data usando PD.TO_DATETIME

Soma de receita nas operações de exportação usando ferramentas PANDAS GROUPBY e SUM, e elaboração de gráfico de barras horizontais (barh) com MATPLOTLIB

<div style = "display: inline_block"><br>
  <img align = "center" height = "400" width = "400" src="https://github.com/lucasamorimuser/icons_images/blob/main/receita_exportacao_total.png" />
</div>
<br><br>
Receita nas operações de exportação para etanol hidratado e anidro extraindo os dados por ano com DT.TO_PERIOD, agregando valores com GROUPBY e SUM. Elaboração de gráfico de linhas (plot) com MATPLOTLIB

<div style = "display: inline_block"><br>
  <img align = "center" height = "800" width = "800" src="https://github.com/lucasamorimuser/icons_images/blob/main/receita_exportacao_anual.png" />
</div>
<br><br>
Soma de volume exportado usando ferramentas PANDAS GROUPBY e SUM, e elaboração de gráfico de barras horizontais (barh) com MATPLOTLIB

<div style = "display: inline_block"><br>
  <img align = "center" height = "400" width = "400" src="https://github.com/lucasamorimuser/icons_images/blob/main/volume_exportado_total.png" />
</div>
<br><br>
Soma de exportação para etanol hidratado e anidro extraindo os dados por ano com DT.TO_PERIOD, agregando valores com GROUPBY e SUM. Elaboração de gráfico de linhas (plot) com MATPLOTLIB

<div style = "display: inline_block"><br>
  <img align = "center" height = "800" width = "800" src="https://github.com/lucasamorimuser/icons_images/blob/main/volume_exportado_anual.png" />
</div>

### Dados

Origem dos dados - https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/ie/etanol
