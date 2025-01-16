import sys
from PyQt5.QtWidgets import QApplication
from gui.main_window import MainWindow
from database.db_setup import initialize_database

def main():
    # Initialize the database
    initialize_database()

    # Create the PyQt5 application
    app = QApplication(sys.argv)

    # Create and show the main window
    window = MainWindow()
    window.show()

    # Start the application's event loop
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
