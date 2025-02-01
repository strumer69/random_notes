from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget, QPushButton, QLabel, QTextEdit, QMessageBox
import random
import os
import json

class NoteApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Random Notes App")
        self.notes_file = "notes.json"
        self.load_notes()
        self.used_notes = []

        # UI Elements
        self.layout = QVBoxLayout()

        self.note_display = QLabel("Click the button to read a random note!")
        self.note_display.setWordWrap(True)
        self.layout.addWidget(self.note_display)

        self.input_text = QTextEdit()
        self.layout.addWidget(self.input_text)

        save_button = QPushButton("Save Note")
        save_button.clicked.connect(self.save_note)
        self.layout.addWidget(save_button)

        random_note_button = QPushButton("Show Random Note")
        random_note_button.clicked.connect(self.show_random_note)
        self.layout.addWidget(random_note_button)

        self.setLayout(self.layout)

    def load_notes(self):
        """Load notes from file or initialize empty list."""
        if os.path.exists(self.notes_file):
            with open(self.notes_file, 'r') as file:
                self.notes = json.load(file)
        else:
            self.notes = []

    def save_notes_to_file(self):
        """Save notes to the file."""
        with open(self.notes_file, 'w') as file:
            json.dump(self.notes, file)

    def save_note(self):
        """Save the text input as a note."""
        new_note = self.input_text.toPlainText().strip()
        if new_note:
            self.notes.append(new_note)
            self.save_notes_to_file()
            self.input_text.clear()
            QMessageBox.information(self, "Note Saved", "Your note has been saved successfully.")
        else:
            QMessageBox.warning(self, "Empty Note", "Please write something before saving.")

    def show_random_note(self):
        """Show a random note without repeating until all are shown."""
        available_notes = [note for note in self.notes if note not in self.used_notes]

        if not available_notes:
            QMessageBox.information(self, "All Notes Displayed", "All notes have been displayed. Resetting notes.")
            self.used_notes = []
            available_notes = self.notes

        if available_notes:
            note = random.choice(available_notes)
            self.used_notes.append(note)
            self.note_display.setText(note)
        else:
            self.note_display.setText("No notes available.")

if __name__ == '__main__':
    app = QApplication([])
    window = NoteApp()
    window.show()
    app.exec_()

