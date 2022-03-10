# Image-Converter
Program to change the size of the image and save it to new name and new type.

## Team members
1. Arnold Denzil [github](https://github.com/arnolddenzil)
2. Vrinda Lekshmi

## Team Id
Python / 591

## How it Works ?

   ### Usage 
   
-> To use the converter ,run the program in either of the two ways in the command line:    
    python {program name} load-image {image_location} {new_image_name} [options]    
                                        OR   
    typer {program name} run load-image {image_location} {new_image_name} [options]   
    
   ### Help 
   
-> To see help use 'typer image-converter.py run --help'    
-> To know how to use a command use 'typer image-converter.py run {command} --help'    

   ### Note 
   
-> Using typer would be much easier if you have typer-cli installed as it will provide you with autocompletion(just press tab key).   
-> The curly blackets'{}' should not be included when entering the command and the place should be completely replaced with what is specified inside the brackets.   
-> The {image_location} is expected to have the name of the image file if it is present in the same directory as the program or if it is present outside the program directory, it expectsthe full file path.   
-> The backslash symbol in location path(when copying the location from the image file property) should bereplaced with '/'.   
-> The {new_image_name} should also contain the file format that is required to save in.   

   ### Options  
   
-> To resize the image use '--width {width}' to change the width and '--height {height}' to change the height.   
-> Note that it is not necessary to mention both the width and height as it will keep the aspect ratio by default and the width and height entered will be used as the maximum widht and height.   
-> Inorder to manually set the width and height you must mention '--no-keep-aspect-ratio' option and must alsomention the height and width using '--width {width}' and '--height {height}' options.   
   
## Libraries used 

typer - 0.3.2   
typer-cli - 0.0.12   
Pillow - 9.0.1   

## How to configure 

Just install the above libraries using pip install command and you are set to go! 

## How to Run 

[In the command line]   
python {program name} load-image {image_location} {new_image_name} [options]   
                                   OR   
typer {program name} run load-image {image_location} {new_image_name} [options]   


