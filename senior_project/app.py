from PyQt6.QtWidgets import (QApplication, QVBoxLayout, QWidget, 
                             QLabel, QHBoxLayout, QLineEdit,
                             QPushButton, QTextEdit)
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import Qt
import sys
 
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
        self.search_field = QLineEdit()
        self.search_field.setFont(QFont("Playfair Display", 12))
        self.search_field.setPlaceholderText("Name of Potion or House")

        search_button = QPushButton("Search")
        search_button.setFont(QFont("Playfair Display", 12))


        search_layout.addWidget(self.search_field)
        search_layout.addWidget(search_button)

        results_text = QTextEdit("Results. ")
        results_text.setFont(QFont("Playfair Display", 12))

        #Add all our widgets
        layout.addWidget(title_label)
        layout.addWidget(description_label)
        layout.addLayout(search_layout)
        layout.addWidget(results_text)

def search(self):
    """get the search text and use it to make an API call to get
    the results for a search"""

    # get the user input
   





def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()