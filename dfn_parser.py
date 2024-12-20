"""
dfn_parser.py

Este módulo é responsável por processar arquivos DFN (Discrete Fracture Network).
Contém funções para:
- Ler e interpretar os dados de fraturas a partir de arquivos DFN.
- Verificar se os dados representam um sistema 2D ou 3D.
"""

def parse_dfn(file_path):
    """
    Lê um arquivo DFN e retorna um dicionário com as informações das fraturas.

    Args:
        file_path (str): Caminho para o arquivo DFN.

    Returns:
        dict: Dicionário onde a chave é o ID da fratura (part_id) e o valor
              é uma lista de tuplas contendo coordenadas (x, y, z), espessura
              (thickness) e permeabilidade (permeability).
    """
    fractures = {}
    with open(file_path, 'r') as file:
        for line in file.readlines()[1:]:  # Ignora a primeira linha (cabeçalho)
            parts = line.split()
            if len(parts) < 6:  # Ignora linhas com dados incompletos
                continue
            try:
                part_id = int(parts[0])
                x, y, z = map(float, parts[1:4])
                thickness, permeability = map(float, parts[4:6])
                if part_id not in fractures:
                    fractures[part_id] = []
                fractures[part_id].append((x, y, z, thickness, permeability))
            except ValueError:
                # Ignora linhas que não podem ser convertidas corretamente
                continue
    return fractures

def is_3d(fractures):
    """
    Verifica se os dados das fraturas representam um sistema 3D.

    Args:
        fractures (dict): Dicionário de fraturas retornado pela função parse_dfn.

    Returns:
        bool: True se as fraturas forem 3D, False se forem 2D.
    """
    z_values = {point[2] for points in fractures.values() for point in points}
    return len(z_values) > 1