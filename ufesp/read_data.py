#!/usr/bin/env python
# coding: utf-8


import pandas as pd
from pathlib import Path

# Paths
project_path = Path(__file__).parents[1].resolve()
data_path = project_path / 'ufesp' / 'data'
data_path.mkdir(exist_ok=True)









def get_table():
    df = pd.read_csv(
        data_path / 'ufesp.csv',
        parse_dates=['data_inicio', 'data_fim', 'ano_mes']
    )
    df.loc[:, 'ano_mes'] = pd.to_datetime(df['data_inicio']).dt.to_period('M')
    return df


def get_ufesp(dia):
    # Get Dataframe
    df = get_table()

    # json
    mask = (df['data_inicio'] <= dia) & (df['data_fim'] >= dia)
    return df.loc[mask].to_dict('records')[0]








if __name__ == '__main__':
    print(f'A pasta do projeto é: {project_path}')
    print(f'A pasta dos dados é: {data_path}')

    # 
    d = get_ufesp(dia='2021-11-15')
    print(d)
    print(d['valor'])
