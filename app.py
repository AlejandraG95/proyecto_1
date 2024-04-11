from PySide6.QtWidgets import QApplication
from controllers.actualizarps_w import ActualizarpsWindow

if __name__== '__main__':
     app=QApplication()
     window= ActualizarpsWindow()
     window.show()
     app.exec()