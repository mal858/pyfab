from maxtask import maxtask
import trackpy as tp


class findtraps(maxtask):

    def __init__(self, **kwargs):
        super(findtraps, self).__init__(*kwargs)

    def dotask(self):
        f = tp.locate(self.frame, 11, topn=1)
        print(f)
