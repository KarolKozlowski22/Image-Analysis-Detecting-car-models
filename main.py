from GUI import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from categorize import categorize
import os
from PyQt5.QtWidgets import QGraphicsScene

class MainWindow(Ui_MainWindow):
    def __init__(self):
        super(MainWindow).__init__()

    def setupUi(self, Dialog):
        super(MainWindow, self).setupUi(Dialog)
        if(os.path.exists('model1.h5')):
            self.label_TrainModel.setStyleSheet("color: green")
            self.label_TrainModel.setText("Model trained - accuracy: 75,19%")
        else:
            self.label_TrainModel.setStyleSheet("color: red")
            self.label_TrainModel.setText("Model not trained")
        self.button_LoadImage.clicked.connect(self._loadImage)
        self.button_Recogn.clicked.connect(self._recognizeImage)

    def _loadImage(self):
        file_dialog = QtWidgets.QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(None, "Select Image", "", "Image Files (*.png *.jpg *.jpeg)")
        if file_path:
            self.image = QtGui.QImage(file_path)
            self.path = file_path
            pixmap = QtGui.QPixmap.fromImage(self.image)
            scene = QGraphicsScene()
            self.graphicsView_Image.setScene(scene)
            self.graphicsView_Image.scene().addPixmap(pixmap)
            scene.update()

    def _recognizeImage(self):
        if 'image' not in self.__dict__:
            self.label_RecognOutput.setStyleSheet("color: red")
            self.label_RecognOutput.setText("No image loaded")
        elif not os.path.exists('model1.keras'):
            self.label_RecognOutput.setStyleSheet("color: red")
            self.label_RecognOutput.setText("Model not trained")
        else:
            output = categorize(self.path)
            if output == 'None':
                self.label_RecognOutput.setStyleSheet("color: red")
                self.label_RecognOutput.setText("No car model recognized")
            else:
                self.label_RecognOutput.setStyleSheet("color: green")
                self.label_RecognOutput.setText("Recognized car model: " + output)


# running GUI instance
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = MainWindow()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())