# FacialVerificationProject
READ ME 

A webcam based basic facial verification program using OpenCV2, Numpy Dlib and Deep Face. 

Over the course of this repo's development I plan on adding a GUI using tkinter to make it more acessible.

The program functions by taking a picture of the user and then verifiying the frames captured. That being said it is imperative that no one else is in the frame before the OpenCV2 frame appears. 

Intially I had the program crop faces to ensure it verfifies the only one face in the captured frame but deep face auto-crops. So cropping the faces provided mix results. So to ensure that the program functions as intended make sure the background is clear of faces before intializing the program. When the Opencv2 frame pops up alternate faces can be introduced.

This can be cirumvented by deleting the extract_image function and using a different image of the intended face. Although, I find that the extract_image function is very convient for development.

Feel free to use this code in other applications, it was made with educational purposes in mind :). Also suggestions and constructive critism is STRONGLY ENCOURAGED. 
