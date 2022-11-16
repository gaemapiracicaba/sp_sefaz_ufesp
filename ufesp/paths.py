"""
Pastas
"""

from pathlib import Path


# Paths
project_path = Path(__file__).parents[1].resolve()
package_path = project_path / 'ufesp'


data_path = package_path / 'data'
data_path.mkdir(exist_ok=True)

if __name__ == '__main__':
    print(project_path)
