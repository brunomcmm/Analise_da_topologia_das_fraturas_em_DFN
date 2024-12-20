"""
main.py

Este módulo é o ponto de entrada do programa. Ele inicializa a aplicação PyQt5
e exibe a interface gráfica principal definida no módulo `gui.py`. Antes de iniciar,
a tela do terminal é limpa.
"""

import os
import sys
from gui import MainWindow
from PyQt5.QtWidgets import QApplication

# Função para limpar a tela
def clear_terminal():
    """Limpa a tela do terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    clear_terminal()  # Limpa a tela antes de iniciar
    print("Iniciando o programa...\n")  # Mensagem inicial
    
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())