# Unidade Fiscal do Estado de São Paulo (UFESP)

<br>

A Unidade Fiscal do Estado de São Paulo (UFESP) é utilizada, dentre outras funções, para estabelecer as multas ambientais do Estado de São Paulo. É definida pela Secretaria da Fazenda do Estado de São Paulo ([SEFAZ](https://portal.fazenda.sp.gov.br/))

Com objetivo de obter os dados, para cálculos de multas, inicialmente vi o código apresentado em [Medium: Web Scraping: aquisição de dados em páginas web com Python](https://medium.com/data-hackers/web-scraping-aquisi%C3%A7%C3%A3o-de-dados-em-p%C3%A1ginas-web-com-python-ec6e33e9e452), porém optei por fazer d'outro jeito a aquisição dos dados.

Optei por utilizar o [*site* oficial](https://legislacao.fazenda.sp.gov.br/Paginas/ValoresDaUFESP.aspx) da SEFAZ com as informações. Fiz a partir de 1997 apenas.

<br>

----

### Como Instalar?

```python
# Instala
!pip3 install ufesp --upgrade
```

<br>

----

### Como Usar?

```python
import ufesp

# Pega Tabela
df_ufesp = ufesp.get_table()

# Pega Valor para um dado dia
get_ufesp(dia='2021-11-15')
```

<br>

----

### Útlima Atualização?

O código foi escrito em julho de 2022 e será necessário atualizar uma vez ao ano.
