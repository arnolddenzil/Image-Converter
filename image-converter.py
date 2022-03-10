documentation = '''
       Help :-
    -> To see help use 'typer image-converter.py run --help'
    -> To know how to use a command use 'typer image-converter.py run {command} --help'
    ----------------------------------------------------------------------------------------------------------------
       Usage :-
    -> To use the converter ,run the program in either of the two ways in the command line: 
        python {program name} load-image {image_location} {new_image_name} [options]
                                            OR
        typer {program name} run load-image {image_location} {new_image_name} [options]
    ----------------------------------------------------------------------------------------------------------------
       Note:-
    -> Using typer would be much easier if you have typer-cli installed as it will provide you with 
       autocompletion(just press tab key).
    -> The curly blackets'{}' should not be included when entering the command and the place should be completely 
       replaced with what is specified inside the brackets.
    -> The {image_location} is expected to have the name of the image file if it is present in the same directory 
       as the program or if it is present outside the program directory, it expectsthe full file path.
    -> The backslash symbol in location path(when copying the location from the image file property) should be
       replaced with '/'.
    -> The {new_image_name} should also contain the file format that is required to save in.
    ----------------------------------------------------------------------------------------------------------------
       Options:-
    -> To resize the image use '--width {width}' to change the width and '--height {height}' to change the height
    -> Note that it is not necessary to mention both the width and height as it will keep the aspect ratio by 
       default and the width and height entered will be used as the maximum widht and height.
    -> Inorder to manually set the width and height you must mention '--no-keep-aspect-ratio' option and must also
       mention the height and width using '--width {width}' and '--height {height}' options.
                                x----------------------------------------------x
'''

from typing import Optional
import typer
from PIL import Image

app = typer.Typer()

@app.command()
def convert_img(location: str, new_name: str, keep_aspect_ratio: Optional[bool] = True, width: Optional[int] = None, height: Optional[int] = None):
    image = Image.open(location)
    image.show()
    typer.echo(image.size)

    if width != None or height != None:
        if keep_aspect_ratio:
            if width != None and height != None:
                image.thumbnail((width, height))
            elif width != None and height == None:
                image.thumbnail((width, 10000))
            else:
                image.thumbnail((10000, height))

        else:
            if width != None and height != None:
                image = image.resize((width, height))
            else:
                typer.echo("You must provide bot width and height if you are using '--no-keep-aspect-ratio'")
    typer.echo(image.size)
    image.save(new_name)
    image.show()

@app.command()
def description():
    typer.echo(documentation)