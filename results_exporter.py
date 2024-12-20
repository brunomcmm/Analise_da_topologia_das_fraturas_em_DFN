"""
results_exporter.py

Este módulo é responsável pela exportação dos resultados e pela geração de visualizações.
Contém funções para:
- Exportar os resultados da análise topológica em arquivos `.txt`.
- Gerar e salvar uma visualização 2D (projeção no plano XY) como imagem.
"""

import matplotlib.pyplot as plt

def export_results(topology, output_file):
    """
    Exporta os resultados da análise topológica para um arquivo de texto.

    Args:
        topology (list): Lista de dicionários contendo as informações das fraturas 
                         retornadas pela função analyze_topology.
        output_file (str): Caminho do arquivo onde os resultados serão salvos.
    """
    with open(output_file, 'w') as file:
        for entry in topology:
            file.write(f"Part ID: {entry['part_id']}\n")
            file.write(f"Type: {entry['type']}\n")
            file.write("Nodes:\n")
            for node in entry['nodes']:
                file.write(f"  {node}\n")
            file.write("\n")

def plot_top_view(projected_fractures, output_path="temp_top_view.png"):
    """
    Gera uma visualização 2D (projeção no plano XY) e salva como imagem.

    Args:
        projected_fractures (dict): Dicionário com as fraturas projetadas no plano 2D,
                                    retornado pela função top_view_projection.
        output_path (str): Caminho do arquivo onde a imagem será salva.
    """
    import matplotlib.pyplot as plt

    plt.figure(figsize=(6, 4))
    for part_id, points in projected_fractures.items():
        if points:  # Verifica se há pontos para plotar
            x_coords, y_coords = zip(*points)
            plt.plot(x_coords, y_coords)
    plt.title("Corte de Topo - Visualização 2D")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.savefig(output_path)  # Salva a imagem
    plt.close()  # Fecha a figura