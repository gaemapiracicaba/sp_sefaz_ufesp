#!/usr/bin/env python
# coding: utf-8

import pandas as pd
from pathlib import Path
from datetime import datetime


def get_table():
    # Paths
    project_path = Path(__file__).parents[1].resolve()
    data_path = project_path / 'ufesp' / 'data'
    data_path.mkdir(exist_ok=True)

    # ddd
    df = pd.read_csv(
        data_path / 'ufesp.csv',
        parse_dates=['data_inicio', 'data_fim', 'ano_mes'],
        decimal=','
    )
    df.loc[:, 'ano_mes'] = pd.to_datetime(df['data_inicio']).dt.to_period('M')
    return df


def get_ufesp_from_date(date):
    # Get Dataframe
    df = get_table()

    # Json
    mask = (df['data_inicio'] <= date) & (df['data_fim'] >= date)
    return df.loc[mask].to_dict('records')[0]


def get_ufesp_from_year(year):
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
    dados = get_ufesp_from_date(date='2020-11-15')
    print(dados['valor'])

    # Com dia (datetime)
    a = '2021-11-15'
    b = datetime.strptime(a, '%Y-%m-%d')
    dados = get_ufesp_from_date(date=b)
    print(dados['valor'])

    # Com Ano
    dados = get_ufesp_from_year(2022)
    print(dados['valor'])
