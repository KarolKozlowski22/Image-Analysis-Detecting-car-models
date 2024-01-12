from GUI import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from train import train
from categorize import categorize
import os
from PyQt5.QtWidgets import QGraphicsScene

class MainWindow(Ui_MainWindow):
    def __init__(self):
        super(MainWindow).__init__()

    def setupUi(self, Dialog):
        super(MainWindow, self).setupUi(Dialog)
        if(os.path.exists('ex.txt')):
            self.label_TrainModel.setStyleSheet("color: green")
            self.label_TrainModel.setText("Model already trained")
        else:
            self.label_TrainModel.setStyleSheet("color: red")
            self.label_TrainModel.setText("Model not trained")
        self.button_TrainModel.clicked.connect(self._trainModel)
        self.button_LoadImage.clicked.connect(self._loadImage)
        self.button_Recogn.clicked.connect(self._recognizeImage)

    def _trainModel(self):
        if(os.path.exists('ex.txt')):
            self.label_TrainModel.setStyleSheet("color: green")
            self.label_TrainModel.setText("Model already trained - you do not have to train model, to trian it delete model file")
        else:
            train()
            self.label_TrainModel.setStyleSheet("color: yellow")
            self.label_TrainModel.setText("Model training in progress")

    def _loadImage(self):
        file_dialog = QtWidgets.QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(None, "Select Image", "", "Image Files (*.png *.jpg *.jpeg)")
        if file_path:
            self.image = QtGui.QImage(file_path)
            pixmap = QtGui.QPixmap.fromImage(self.image)
            scene = QGraphicsScene()
            self.graphicsView_Image.setScene(scene)
            self.graphicsView_Image.scene().addPixmap(pixmap)
            scene.update()

    def _recognizeImage(self):
        if 'image' not in self.__dict__:
            self.label_RecognOutput.setStyleSheet("color: red")
            self.label_RecognOutput.setText("No image loaded")
        else:
            output = categorize(self.image)
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