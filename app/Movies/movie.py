import os
from flask_app import flask_app
from moviepy.editor import  *


class Movie:
    def __init__(self) -> None:
        self.filename = ''

    def __save_file(self, file, type="INPUT"):
        try:
            if type == "OUTPUT":
                if not os.path.exists(flask_app.config['OUTPUT_FOLDER']):
                    os.makedirs(flask_app.config['OUTPUT_FOLDER'])
                filename = os.path.join(
                    flask_app.config['OUTPUT_FOLDER'], "output.mp4")
                self.filename = filename
                file.write_videofile(filename)
                return
            if not os.path.exists(flask_app.config['INPUT_FOLDER']):
                os.makedirs(flask_app.config['INPUT_FOLDER'])
            filename = os.path.join(
                flask_app.config['INPUT_FOLDER'], file.filename)
            self.filename = filename
            file.save(filename)
        except BaseException as err:
            msg = f"Exception occured in save_files.{err}"
            print(msg)
            raise err

    def add_effects(self, file):
        try:
            self.__save_file(file=file)
            clip = VideoFileClip(filename=self.filename)
            final = clip.fx(vfx.speedx, 0.5)
            self.__save_file(file=final,type="OUTPUT")
            return self.filename
        except BaseException as err:
            msg = f"Exception occured in add_effects.{err}"
            print(msg)
            raise err
