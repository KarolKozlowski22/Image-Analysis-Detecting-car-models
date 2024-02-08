# Image-Analysis-Detecting-car-models

## About project
The project carried out during the Image Analysis course in the 5th semester of Applied Computer Science at AGH.

## Short description
The program, written in Python, is designed to allow the user to load a car logo image using a GUI, and then, using machine learning, recognize and categorize the image into one of the groups. Initially, the program will support the following brands: Mercedes, Volkswagen, Skoda, Lexus and None.

Link to dataset and model: https://drive.google.com/drive/folders/1ENMmsX_74hF0vcwBLtJv53shgnVJ9E_L?usp=sharing

## Contributors
Figurska Marta, Makieła Małgorzata, Konopka Bartosz, Kozłowski Karol


### Additional Information: Dockerization of the Application

The application has been Dockerized, which is a bit tricky because it involves dockerizing an application with the PyQt5 module. This means we need to run the GUI in the container. Below is a user manual for Windows users:

#### User Manual for Windows

1. **Download and Install an X Server, such as Xming**:
   - Download Xming from its [official website](https://sourceforge.net/projects/xming/).
   - Install it on your Windows machine.
   - Run Xming in "Disable access control" mode for easier setup (be aware of security implications).

2. **Build the Docker Image**:
   - Open a terminal and navigate to the project directory.
   - Build the Docker image using the command:
     ```bash
     docker build -t <image_name> .
     ```
     Replace `<image_name>` with your preferred name for the Docker image.

3. **Run the Docker Container**:
   - To run the Docker container, use the command:
     ```bash
     docker run -it --rm -e DISPLAY=host.docker.internal:0.0 -e QT_DEBUG_PLUGINS=1 --name ao_container <image_name>
     ```
     Make sure to replace `<image_name>` with the name you used to build the image.
   - This command sets up the environment to display the PyQt5 GUI through the X server running on your Windows host.