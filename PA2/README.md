# Reconstructing image

Note: A.npy and C.npy files were removed before pushing to github. Will be added in Google Drive if required.  

## Problem 3
We have used CVXPY library to solve the convex optimization problem
* File **cvxpy_solver.py** takes A, y as input and give s, nu as output.
* s is used in Problem 4 to reconstruct the original image.
* nu is used in **verify.py** file to validate the results.

## Problem 4
File **construct_image.py** is used to get the original image from the input s.

## Problem 5
Image **pots.jpg** is present is present in Problem 5 directory.
* Image **pots.jpg** is splitted into 3 channels using split_3.py file.
* These images were used to create data
    * Data For Assignment_b/ - For blue channel
    * Data For Assignment_g/ - For green channel
    * Data For Assignment_r/ - For red channels
* In all these directories, convex optimisation was solved using the same approach as described above.
* Result from these directories i.e.,{x_r, x_g, x_b} were used to contruct the final image.
* In the ./combined_image directory, combine.py was used to get the final_image.jpg