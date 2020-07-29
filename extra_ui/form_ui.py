#!/usr/bin/env python3

# Filename: form_ui.py

"""Simple membership form built using Python and PyQt5."""

import sys

# Import QApplication and the required widgets from PyQt5.QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLineEdit, QPushButton, QVBoxLayout, QFormLayout, QLabel
from PyQt5.QtCore import Qt
from functools import partial

__version__ = '0.1'
__author__ = 'Janric B. Malate'
ERROR_MSG = 'ERROR'

# Create a subclass of QMainWindow to setup the form's GUI
class FormUI(QMainWindow):
    """PyCalc's View (GUI)."""
    def __init__(self):
        """View initializer."""
        super().__init__()
        # Set some main window's properties
        self.setWindowTitle('OFWTMC MEMBERSHIP SYSTEM')
        self.setFixedSize(600, 600)
        # Set the central widget and the general layout
        self.generalLayout = QVBoxLayout()
        # Set the central widget
        self._centralWidget = QWidget(self)
        self._centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget(self._centralWidget)
        # Create the display and the buttons
        self._createFormLayout()

    def _createFormLayout(self):
        """Create the display."""
        self.formWidget = QWidget()
        formLayout = QFormLayout()
        # Create the display widget
        formLayout.addRow(QLabel("MEMBERSHIP APPLICATION FORM"))
        formLayout.addRow('OFW Abroad:', QLineEdit())
        formLayout.addRow('Address:', QLineEdit())
        formLayout.addRow(QLabel("Benefeciaries:"))
        formLayout.addRow('Name:', QLineEdit())
        formLayout.addRow('Address:', QLineEdit())
        formLayout.addRow('Place of Birth:', QLineEdit())
        formLayout.addRow('Provincial Address:', QLineEdit())
        formLayout.addRow('Occupation:', QLineEdit())
        formLayout.addRow('Religion:', QLineEdit())
        formLayout.addRow('Contact No:', QLineEdit())
        formLayout.addRow('Date of Birth:', QLineEdit())
        formLayout.addRow('Age:', QLineEdit())
        formLayout.addRow('Sex:', QLineEdit())
        formLayout.addRow('Civil Status:', QLineEdit())
        formLayout.addRow('Citizenship:', QLineEdit())
        formLayout.addRow('TIN:', QLineEdit())
        formLayout.addRow('SSS No.:', QLineEdit())
        formLayout.addRow('Name of Husband/Wife:', QLineEdit())
        formLayout.addRow('Place of Birth:', QLineEdit())
        formLayout.addRow('Date of Birth:', QLineEdit())
        formLayout.addRow('Occupation:', QLineEdit())
        formLayout.addRow('Age:', QLineEdit())
        self.formWidget.setLayout(formLayout)
        # Set some display's properties
        # Add the display to the general layout
        self.generalLayout.addWidget(self.formWidget)


# Create a Controller class to connect the GUI and the model

# Client code
def main():
    """Main function."""
    # Create an instance of QApplication
    formApp = QApplication(sys.argv)
    # Show the calculator's GUI
    view = FormUI()
    view.show()
    # Create instances of the model and the controller
    # Create instances of the model and the controller
    # Execute the calculator's main loop
    sys.exit(formApp.exec_())

if __name__ == '__main__':
    main()