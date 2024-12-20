"""
gui.py

Este módulo implementa a interface gráfica da aplicação utilizando PyQt5.
Contém a classe `MainWindow`, que é responsável por:
- Exibir uma interface gráfica para selecionar arquivos DFN.
- Mostrar logs do progresso das operações.
- Gerar e exibir visualizações 2D das fraturas.
"""

from PyQt5.QtWidgets import (
    QMainWindow, QPushButton, QLabel, QFileDialog, QVBoxLayout, QHBoxLayout, QWidget, QTextEdit
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from dfn_parser import parse_dfn
from topology_analyzer import top_view_projection
from results_exporter import plot_top_view

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Análise de Fraturas")
        self.setGeometry(100, 100, 1050, 400)
        self.setFixedSize(1050, 420)
        
        # Layout principal horizontal
        self.main_layout = QHBoxLayout()
        
        # Layout para controles (lado esquerdo)
        self.left_layout = QVBoxLayout()
        
        # Título
        self.label = QLabel("Selecione um arquivo DFN para análise")
        self.label.setFixedHeight(30)
        self.left_layout.addWidget(self.label)
        
        # Botão para selecionar o arquivo
        self.select_button = QPushButton("Selecionar Arquivo DFN")
        self.select_button.setFixedHeight(30)
        self.select_button.clicked.connect(self.select_file)
        self.left_layout.addWidget(self.select_button)
        
        # Botão para gerar o preview
        self.preview_button = QPushButton("Gerar Preview")
        self.preview_button.setFixedHeight(30)
        self.preview_button.clicked.connect(self.generate_preview)
        self.left_layout.addWidget(self.preview_button)
        
        # Botão para processar o arquivo
        self.process_button = QPushButton("Processar Arquivo")
        self.process_button.setFixedHeight(30)
        self.process_button.clicked.connect(self.process_file)
        self.left_layout.addWidget(self.process_button)
        
        # Janela de texto para progresso
        self.text_log = QTextEdit()
        self.text_log.setReadOnly(True)
        self.text_log.setFixedSize(380, 275)
        self.left_layout.addWidget(self.text_log)
        
        # Adicionando o layout esquerdo ao principal
        left_widget = QWidget()
        left_widget.setFixedWidth(400)
        left_widget.setLayout(self.left_layout)
        self.main_layout.addWidget(left_widget)
        
        # Espaço para imagem (lado direito)
        self.image_label = QLabel("Espaço reservado para imagem")
        self.image_label.setFixedSize(590, 400)
        self.image_label.setStyleSheet("border: 1px solid black;")
        self.image_label.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(self.image_label)
        
        # Container principal
        container = QWidget()
        container.setLayout(self.main_layout)
        self.setCentralWidget(container)

    def log(self, message):
        """
        Adiciona uma mensagem ao log de progresso, com separação visual entre etapas.
        """
        if not self.text_log.toPlainText().endswith("\n\n"):
            self.text_log.append("")  # Adiciona uma linha em branco entre mensagens
        self.text_log.append(message)

    def select_file(self):
        """Método chamado ao clicar no botão 'Selecionar Arquivo DFN'."""
        file_dialog = QFileDialog()
        self.file_path, _ = file_dialog.getOpenFileName(
            self, 
            "Selecione o arquivo DFN", 
            "", 
            "Arquivos DFN (*.dat *.in *.txt *.DAT *.IN *.TXT)"
        )
        if self.file_path:
            self.label.setText(f"Arquivo selecionado: {self.file_path}")
            self.log(f"Arquivo selecionado: {self.file_path}")
        else:
            self.log("Nenhum arquivo selecionado.")

    def generate_preview(self):
        """Gera uma visualização de prévia (preview) do arquivo selecionado."""
        if hasattr(self, 'file_path'):
            try:
                self.log("Gerando preview...")
                fractures = parse_dfn(self.file_path)
                
                # Informar a quantidade de fraturas
                num_fractures = len(fractures)
                self.log(f"O arquivo DFN contém {num_fractures} fraturas.")
                
                # Gerar a projeção 2D
                projected_fractures = top_view_projection(fractures, z_value=0.0)
                plot_top_view(projected_fractures, output_path="preview.png")
                
                # Atualizar a imagem na interface
                pixmap = QPixmap("preview.png")
                if not pixmap.isNull():
                    self.image_label.setPixmap(pixmap)
                    self.log("Preview gerado com sucesso.")
                else:
                    self.log("Erro ao carregar a imagem de preview.")
            except Exception as e:
                self.log(f"Erro ao gerar preview: {e}")
        else:
            self.log("Nenhum arquivo selecionado. Por favor, selecione um arquivo primeiro.")

    def process_file(self):
        """Processa o arquivo DFN e gera visualizações."""
        if hasattr(self, 'file_path'):
            self.log("Iniciando o processamento do arquivo DFN...")
            # Processamento completo pode ser implementado aqui
        else:
            self.log("Nenhum arquivo selecionado. Por favor, selecione um arquivo primeiro.")