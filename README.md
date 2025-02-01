# Random Notes App

## Overview
The **Random Notes App** is a simple desktop application built using PyQt5. It allows users to write, save, and display notes randomly. The app ensures that all saved notes are shown without repetition until each note has been displayed at least once.

## Features
- Save custom text notes.
- Display a random saved note.
- Avoids repeating notes until all have been shown.
- Simple and user-friendly interface.

## Requirements
- Python 3.x
- PyQt5

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```bash
   cd random-notes-app
   ```

3. Install dependencies:
   ```bash
   pip install PyQt5
   ```

## Usage
1. Run the application:
   ```bash
   python random_notes_app.py
   ```

2. Write and save notes using the input text field.
3. Click **"Show Random Note"** to display a random saved note.
4. Notes will not repeat until all have been shown at least once.

## File Structure
- `random_notes_app.py`: Main application file.
- `notes.json`: Stores saved notes.

## Future Enhancements
- Add support for categorizing notes.
- Provide export/import functionality for notes.
- Improve UI design with more customization options.

## License
This project is open-source and available under the [MIT License](LICENSE).

## Contributions
Feel free to fork this repository and submit pull requests for improvements.

