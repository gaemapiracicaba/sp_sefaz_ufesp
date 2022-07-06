#!/usr/bin/env python
# coding: utf-8

import pandas as pd
from paths import data_path


def get_table():
    df = pd.read_csv(
        data_path / 'ufesp.csv',
        parse_dates=['data_inicio', 'data_fim', 'ano_mes']
    )
    df.loc[:, 'ano_mes'] = pd.to_datetime(df['data_inicio']).dt.to_period('M')
    print(df.head())
    return df


def get_ufesp(dia):
    #
    df = get_table()

    # json
    mask = (df['data_inicio'] <= dia) & (df['data_fim'] >= dia)
    return df.loc[mask].to_dict('records')[0]


if __name__ == '__main__':
    d = get_ufesp(dia='2021-11-15')
    print(d)
    print(d['valor'])
