# Análise da Topologia das Fraturas em DFN

Este projeto tem como objetivo realizar a análise da topologia de fraturas representadas em arquivos DFN (Discrete Fracture Network). A aplicação identifica e classifica interseções de fraturas, exporta os resultados para arquivos e fornece uma interface gráfica interativa para visualização e controle do processo.

## Funcionalidades
- Carregamento de arquivos DFN:
- Suporte a arquivos com extensões .dat, .in, e .txt.
- Leitura de informações sobre fraturas, incluindo coordenadas e propriedades físicas.
- Classificação de nós:
- Identificação e classificação de interseções de fraturas como tipos X, Y ou I.
- Exportação de resultados:
- Geração de arquivos de saída no formato .txt contendo a análise topológica das fraturas.
- Visualização interativa:
- Exibição de imagens relacionadas ao processamento diretamente na interface gráfica.
- Interface gráfica amigável:
- Implementação em PyQt5 para facilitar a interação com o usuário.

## Estrutura do Projeto
**`main.py`**:
- Ponto de entrada do programa, gerencia a interação entre os módulos.

**`gui.py`**:
- Implementa a interface gráfica usando PyQt5.

**`dfn_parser.py`**:
- Realiza a leitura e processamento dos arquivos DFN.

**`topology_analyzer.py`**:
- Responsável por analisar a topologia das fraturas.

**`results_exporter.py`**:
- Exporta os resultados da análise para arquivos .txt.

## Como Usar
1. Clone o repositório:
```bash
git clone https://github.com/brunomcmm/Analise_da_topologia_das_fraturas_em_DFN.git
```

2. Instale as dependências:
```bash
pip install PyQt5
```

3. Execute o programa:
```bash
python main.py
```

### Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request com melhorias ou novas funcionalidades.