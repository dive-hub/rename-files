import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QFileDialog, QLineEdit

class FileRenamer(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('File Renamer')
        self.setGeometry(100, 100, 300, 200)

        self.directory_label = QLabel('Select Directory:')
        self.directory_button = QPushButton('Browse')
        self.directory_button.clicked.connect(self.browse_directory)
        self.directory_line_edit = QLineEdit()

        self.start_number_label = QLabel('Start Number:')
        self.start_number_line_edit = QLineEdit()

        self.rename_button = QPushButton('Rename Files')
        self.rename_button.clicked.connect(self.rename_files)

        vbox = QVBoxLayout()
        vbox.addWidget(self.directory_label)
        vbox.addWidget(self.directory_line_edit)
        vbox.addWidget(self.directory_button)
        vbox.addWidget(self.start_number_label)
        vbox.addWidget(self.start_number_line_edit)
        vbox.addWidget(self.rename_button)

        self.setLayout(vbox)

    def browse_directory(self):
        directory = QFileDialog.getExistingDirectory(self, 'Select Directory')
        self.directory_line_edit.setText(directory)

    def rename_files(self):
        directory = self.directory_line_edit.text()
        start_number = int(self.start_number_line_edit.text())

        if not os.path.isdir(directory):
            print("Invalid directory")
            return

        files = os.listdir(directory)
        count = start_number

        for filename in files:
            old_filepath = os.path.join(directory, filename)
            new_filename = f"{str(count).zfill(4)}{os.path.splitext(filename)[1]}"
            new_filepath = os.path.join(directory, new_filename)

            # Check if the new filename already exists
            if os.path.exists(new_filepath):
                print(f"Skipping {filename} - {new_filename} already exists")
                continue

            os.rename(old_filepath, new_filepath)
            count += 1

        print("Files renamed successfully")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FileRenamer()
    ex.show()
    sys.exit(app.exec_())
