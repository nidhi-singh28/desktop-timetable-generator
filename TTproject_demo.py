# TTproject_demo.py

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QComboBox, QFileDialog
import sys
import pandas as pd

class TimetableApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Desktop Timetable Generator")
        self.setGeometry(100, 100, 600, 400)

        self.label = QLabel("Select Semester & Section", self)
        self.label.move(50, 50)

        self.combo = QComboBox(self)
        self.combo.addItems(["Semester 3", "Semester 5", "Semester 7"])
        self.combo.move(50, 90)

        self.generate_btn = QPushButton("Generate Timetable", self)
        self.generate_btn.move(50, 140)
        self.generate_btn.clicked.connect(self.generate_timetable)

    def generate_timetable(self):
        # Placeholder function for Genetic Algorithm-based generation
        print("Timetable generated (logic hidden in demo version)")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TimetableApp()
    window.show()
    sys.exit(app.exec_())
