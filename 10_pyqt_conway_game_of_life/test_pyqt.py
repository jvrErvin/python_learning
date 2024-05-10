from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton

def foo():
    print("Hello World")

# Create the application instance
app = QApplication([])

# Create the main window
window = QMainWindow()
window.setWindowTitle("PyQt5 Installation Test")
window.setGeometry(500, 800, 500, 300)

# Add a label to the window
label = QLabel("Hello World", window)
label.move(50, 30)

# Add a button which closes the window when clicked
close_button = QPushButton("Close", window)
close_button.move(150, 30)
close_button.clicked.connect(window.close)

# Add a button which calls foo
foo_button = QPushButton("Foo", window)
foo_button.move(250, 30)
foo_button.clicked.connect(foo)

# Show the window
window.show()

# Run the application's event loop
app.exec_()
