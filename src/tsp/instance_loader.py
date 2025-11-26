import pandas as pd
import os
from typing import List
from .city import City

class InstanceLoader:
    """
    Carregador Inteligente: Detecta automaticamente se o dataset
    é Geográfico (Lat/Lon) ou Euclidiano (X/Y).
    """
    def __init__(self, file_path: str):
        self.file_path = file_path

    def load_cities(self) -> List[City]:
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"Arquivo não encontrado: {self.file_path}")

        try:
            df = pd.read_csv(self.file_path, skipinitialspace=True)
            # Normaliza colunas
            df.columns = [c.lower().strip() for c in df.columns]
            cols = df.columns
            
            cities = []
            
            # DETECÇÃO DE MODO
            is_geo = False
            if 'lat' in cols or 'latitude' in cols:
                is_geo = True
                col_c1 = 'lat' if 'lat' in cols else 'latitude'
                col_c2 = 'lon' if 'lon' in cols else ('lng' if 'lng' in cols else 'longitude')
            elif 'x' in cols:
                is_geo = False
                col_c1 = 'x'
                col_c2 = 'y'
            else:
                # Fallback para datasets sem cabeçalho padrão
                # Assume X, Y se houver 3 colunas e nenhuma for lat
                is_geo = False
                df.rename(columns={df.columns[1]: 'x', df.columns[2]: 'y'}, inplace=True)
                col_c1, col_c2 = 'x', 'y'

            print(f"   -> Modo detectado: {'🌍 Geográfico (GPS)' if is_geo else '📐 Euclidiano (Plano)'}")

            for idx, row in df.iterrows():
                # Identificar Nome
                if 'name' in cols: name = str(row['name'])
                elif 'city' in cols: name = str(row['city'])
                elif 'id' in cols: name = str(row['id'])
                else: name = f"Ponto_{idx + 1}"

                cities.append(City(
                    name=name,
                    c1=float(row[col_c1]),
                    c2=float(row[col_c2]),
                    is_geo=is_geo
                ))
                        
            return cities

        except Exception as e:
            raise RuntimeError(f"Erro ao processar arquivo {self.file_path}: {e}")