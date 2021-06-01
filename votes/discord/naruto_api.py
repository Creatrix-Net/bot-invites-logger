from os.path import join
from pathlib import Path
from random import choice,shuffle

from .color import Color
from .embeds import Embed


def naruto_api():
    e=Embed(title='Arigato! <:smilenaruto:848961696047300649>',color=Color.random(),)
    imageslistdir = Path(__file__).resolve(
                strict=True).parent / join('images_list.txt')
    filepointer = open(imageslistdir)
    imageslist = filepointer.readlines()
    shuffle(imageslist)
    choice_image = choice(imageslist)
    if choice_image.split('.')[-1] != 'mp4':
        e.set_image(url=choice_image.strip('\n'))
        return (e.to_dict(), False)
    else:
        return (e.to_dict(), choice_image)