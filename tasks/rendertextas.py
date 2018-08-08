# -*- coding: utf-8 -*-
# MENU: Add trap/Render text ...

from .rendertext import rendertext
from PyQt4.QtGui import QInputDialog


class rendertextas(rendertext):
    """Render user-selected text as a pattern of traps"""

    def __init__(self, **kwargs):
        super(rendertextas, self).__init__(**kwargs)
        qtext, ok = QInputDialog.getText(self.parent,
                                         'Render Text',
                                         'Text:')
        if ok:
            self.text = str(qtext)
        else:
            self.text = 'hello'
