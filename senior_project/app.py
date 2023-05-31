from PyQt6.QtWidgets import (QApplication, QVBoxLayout, QWidget, 
                             QLabel, QHBoxLayout, QComboBox,
                             QPushButton, QTextEdit)
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import Qt
import sys
import controller
 
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(300, 400)
        self.setWindowTitle("The Harry Potter App")
        self.setWindowIcon(QIcon("icon.jpg"))
        self.uI()

    def uI(self):
        layout = QVBoxLayout()
        self.setLayout(layout)
 
        # Create our Widgets
        title_label = QLabel("Harry Potter Search Widget")
        title_label.setAlignment(Qt.AlignmentFlag.AlignTop)
        title_label.setFont(QFont("Playfair Display", 22))

        description = "Search the Potion or House by"
        description += " Name."
        description_label = QLabel(description)
        description_label.setFont(QFont("Playfair Display", 12))

        search_layout = QHBoxLayout()
        self.search_field = QComboBox()
        self.search_field.addItems(["Houses", "Elixirs", "Spells"])
        self.search_field.setFont(QFont("Playfair Display", 12))

        search_button = QPushButton("Search")
        search_button.setFont(QFont("Playfair Display", 12))
        search_button.clicked.connect(self.search)


        search_layout.addWidget(self.search_field)
        search_layout.addWidget(search_button)

        self.results_text = QTextEdit("Results. ")
        self.results_text.setFont(QFont("Playfair Display", 12))

        #Add all our widgets
        layout.addWidget(title_label)
        layout.addWidget(description_label)
        layout.addLayout(search_layout)
        layout.addWidget(self.results_text)

    def search(self):
        """get the search text and use it to make an API call to get
        the results for a search"""

        # get the user input
        search_text = self.search_field.currentText()

        # Make an API call
        search_results = controller.make_call(search_text)
        self.resize(300, 600)
        self.results_text.setText(search_results)
        self.results_text.toHtml()




def main():
    app = QApplication(sys.argv)
    window = Window()

    #app.setStyleSheet
    app.setStyleSheet("""
        QWidget {
            background-color: #fff7eb;
            color: #111111;
            padding: 10px;
        }
        QTextEdit {
            background-color: #eaece5;
        }
        QComboBox {
            background-color: #c0ded9;
        }
        QPushButton {
            background-color: #b2c2bf;
        }


    
    """)

    
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()