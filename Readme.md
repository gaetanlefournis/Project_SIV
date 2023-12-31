<!-- AUTHORS -->
<div align="center">

![By][by-shield] 

</div>

<!-- ABOUT THE PROJECT -->
## About The Project

This project consists in creating a virtual sudoku. The aim is to detect the hand of the user, then write click and the case we want to fill, then write the digit manually and finally detect this digit to write it in the case. At the end the algorithm must say if it's correct or not (optional part - this one is more based on AI)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- HOW TO INSTALL -->
## Installation (for Linux users)

Please make sure that "make" is installed :

```bash
sudo apt-get install make
```

Then do this command at the root of the project (after having cloned it): 

```bash
make install
```

It will create a virtual environment and install the dependencies in it.

Once it is done, enter the virtual environment : 

```bash
source venv/bin/activate
```

Now you can work on the project! 
Don't forget to enter the environment each time you want to work on it.
If you add some dependencies in the requirements.txt, be sure to do "make install" again to have them.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## In the code

In the file graphical_user_interface/constants.py, there is : 
- The number of the camera you use (0 if it's the integrated webcam of your computer, 1 or 2 otherwise)
- The size of the grid that can be changed (4 or 9)
- One grid per size (feel free to import other ones)


## How to use it 

When you run the main_project.py file, the grid appear. Just use one hand with the fingers up as a mouse. When you want to click, bend all your fingers. Then you can put them up again. The click will take place on the green point which is the centroid of the hand. You can decide to draw a digit by clicking on the button if the latter is active. To draw a digit, just click on the white interface by bending the fingers to start, then draw the digit with the fingers up, and to finish the digit click again by bending the fingers. You can now choose to validate the digit or to erase it. Be careful, don't take too much time too draw the digit otherwise the matrix with all pixels to draw will increase, and you may have a huge lose of FPS. 

ENJOY THE GAME! 


<!-- MARKDOWN LINKS & IMAGES -->

[by-shield]: https://img.shields.io/badge/by-Elsa_%26_getget-blue
