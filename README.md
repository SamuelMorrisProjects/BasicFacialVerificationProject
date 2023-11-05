# FacialVerificationProject
READ ME 

A webcam based basic facial verification program using OpenCV2, Numpy Dlib and Deep Face. Feel Free to reach out to me on www.linkedin.com/in/samuel-morris-8b5356298 or GitHub reguarding about the project.

I plan on adding threading to optimize processing. Please also take into consideration that this project is still in development.

The program starts on running of the FacialVer.py file 
The program functions by taking a picture of the user and then verifies the frames captured matches the intial picture. That being said it is imperative that no one else is in the frame before the OpenCV2 frame appears.

Over the course of this repo's development I plan on adding a GUI using tkinter to make it more acessible. 
Intially, I had the program crop faces to ensure it verfifies only one face in the captured frame, but deep face auto-crops. So cropping the faces using OpenCv2 provided mixed results. So to ensure that the program functions as intended make sure the background is clear of faces before intializing the program. When the Opencv2 frame pops up alternate faces can be introduced.

This can be cirumvented by deleting the extract_image function and using a different image of the intended face. Although, I find that the extract_image function is very convient for development.
Feel free to use this code in other applications, it was made with educational purposes in mind :). Both for my education and others. Also suggestions and constructive critism is STRONGLY ENCOURAGED. 
