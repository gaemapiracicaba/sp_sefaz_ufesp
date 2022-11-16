"""
Funções
nov.22
"""

from datetime import datetime
from pathlib import Path
import pandas as pd


def get_table():
    """
    _summary_

    :return: _description_
    :rtype: _type_
    """
    # Paths
    project_path = Path(__file__).parents[1].resolve()
    data_path = project_path / 'ufesp' / 'data'
    data_path.mkdir(exist_ok=True)

    # ddd
    df = pd.read_csv(
        data_path / 'ufesp.csv',
        parse_dates=['data_inicio', 'data_fim', 'ano_mes'],
        decimal=',',
    )
    df.loc[:, 'ano_mes'] = pd.to_datetime(df['data_inicio']).dt.to_period('M')
    return df


def get_ufesp_from_date(date):
    """
    _summary_

    :param date: _description_
    :type date: _type_
    :return: _description_
    :rtype: _type_
    """
    # Get Dataframe
    df = get_table()

    # Json
    mask = (df['data_inicio'] <= date) & (df['data_fim'] >= date)
    return df.loc[mask].to_dict('records')[0]


def get_ufesp_from_year(year):
    """
    _summary_

    :param year: _description_
    :type year: _type_
    :return: _description_
    :rtype: _type_
    """
    # Adjust Year
    year = int(year)

    # Get Dataframe
    df = get_table()

    # Create Year Columns
    df['data_inicio_year'] = pd.DatetimeIndex(df['data_inicio']).year
    df['data_fim_year'] = pd.DatetimeIndex(df['data_fim']).year

    # Json
    mask = (df['data_inicio_year'] <= year) & (df['data_fim_year'] >= year)
    return df.loc[mask].to_dict('records')[0]


if __name__ == '__main__':
    # Com dia (string)
    my_date_string = '2021-11-15'
    dados = get_ufesp_from_date(date=my_date_string)
    print(dados['valor'])

    # Com dia (datetime)
    my_date = datetime.strptime(my_date_string, '%Y-%m-%d')
    dados = get_ufesp_from_date(date=my_date)
    print(dados['valor'])

    # Com Ano
    my_year = 2022
    dados = get_ufesp_from_year(my_year)
    print(dados['valor'])
