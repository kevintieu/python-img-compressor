# python-img-compressor
Simple script for compressing images

The script will iterate through all subfolders of a specified path and scale every '.png' or '.jpg' file that is bigger than 1024x768 to 1024x768. If a folder contains photos that meet the credentials, a folder called 'temp' will be created and the newly scaled images will be saved in that folder. If the script comes across a corrupted image, it will create a folder called 'fail' and move the image into that folder. When finished, the script will show the total size of the raw images before being scaled, after being scaled, as well as the time elapsed.
