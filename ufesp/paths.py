#!/usr/bin/env python
# coding: utf-8

from pathlib import Path

project_path = Path(__file__).parents[1].resolve()

data_path = project_path / 'ufesp' / 'data'
data_path.mkdir(exist_ok=True)

if __name__ == '__main__':
    print(f'A pasta do projeto é: {project_path}')
    print(f'A pasta dos dados é: {data_path}')
