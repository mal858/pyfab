from PIL import Image, ImageDraw, ImageFont
import numpy as np
from numpy.random import normal
from task import task
from PyQt4.QtGui import QVector3D
import os


class rendertext(task):

    def __init__(self,
                 text='hello',
                 spacing = 20,
                 fuzz=0.05,
                 **kwargs):
        super(rendertext, self).__init__(**kwargs)
        dir, _ = os.path.split(__file__)
        font = os.path.join(dir, 'Ubuntu-R.ttf')
        self.font = ImageFont.truetype(font)
        self.text = text
        self.spacing = spacing
        self.fuzz = fuzz

    def dotask(self):
        sz = self.font.getsize(self.text)
        img = Image.new('L', sz, 0)
        draw = ImageDraw.Draw(img)
        draw.text((0, 0), self.text, font=self.font, fill=255)
        bmp = np.array(img) > 128
        bmp = bmp[::-1]
        y, x = np.nonzero(bmp)
        x = x - np.mean(x) + normal(scale=self.fuzz, size=len(x))
        y = y - np.mean(y) + normal(scale=self.fuzz, size=len(y))
        x = x * self.spacing + 320
        y = y * self.spacing + 240
        p = list(map(lambda x, y: QVector3D(x, y, 0), x, y))
        self.parent.pattern.createTraps(p)
