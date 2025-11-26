import pandas as pd
import os
from typing import List
from .city import City

class InstanceLoader:
    """
    Responsável por carregar instâncias de problemas TSP a partir de arquivos.
    """
    def __init__(self, file_path: str):
        self.file_path = file_path

    def load_cities(self) -> List[City]:
        """
        Lê o arquivo CSV e retorna uma lista de objetos City.
        
        Espera-se que o CSV tenha formato compatível (ex: id, x, y)
        ou apenas as coordenadas.
        """
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"Arquivo não encontrado: {self.file_path}")

        try:
            # Lê o CSV usando pandas
            # Assume que o CSV pode ter cabeçalho ou não.
            # Se tiver cabeçalho padrão (id, x, y), o pandas identifica.
            # Espaços em branco são removidos dos nomes das colunas.
            df = pd.read_csv(self.file_path, skipinitialspace=True)
            
            cities = []
            
            # Itera sobre as linhas do DataFrame
            # Verifica se as colunas necessárias existem pelo nome ou por índice
            # Prioridade: colunas nomeadas 'x', 'y'
            
            cols = [c.lower() for c in df.columns]
            
            if 'x' in cols and 'y' in cols:
                # Mapeamento pelo nome da coluna
                for idx, row in df.iterrows():
                    # Tenta obter ID, se não existir usa o índice do loop + 1
                    city_id = row['id'] if 'id' in cols else (idx + 1)
                    cities.append(City(
                        index=int(city_id),
                        x=float(row['x']),
                        y=float(row['y'])
                    ))
            else:
                # Fallback: assume ordem posicional (id, x, y) ou (x, y)
                num_cols = df.shape[1]
                for idx, row in df.iterrows():
                    if num_cols >= 3:
                        # Assume col 0: id, col 1: x, col 2: y
                        cities.append(City(
                            index=int(row.iloc[0]),
                            x=float(row.iloc[1]),
                            y=float(row.iloc[2])
                        ))
                    elif num_cols == 2:
                        # Assume col 0: x, col 1: y (Gera ID sequencial)
                        cities.append(City(
                            index=idx + 1,
                            x=float(row.iloc[0]),
                            y=float(row.iloc[1])
                        ))
                    else:
                        raise ValueError("Formato de colunas do CSV desconhecido.")
                        
            return cities

        except Exception as e:
            raise RuntimeError(f"Erro ao processar arquivo {self.file_path}: {e}")