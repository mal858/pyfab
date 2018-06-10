# -*- coding: utf-8 -*-


class task(object):
    """task is a base class for operations on images in pyfab/jansen

    Registering a task with taskmanager().registerTask() places the
    task in a queue.  When the task reaches the head of the queue,
    taskmanager() calls initialize() to initialize the task.
    It then proceeds to feed video frames to the task
    as they become available.

    The task skips a number of frames set by delay (default: 0).
    It then feeds a number of frames to doprocess() set by
    nframes (default: 0).
    Finally, the task calls dotask() to perform its operation.

    When the task isDone(), taskmanager() unregisters the task
    and deletes it.

    Subclasses of task() should override
    initialize(), doprocess() and dotask()
    """

    def __init__(self,
                 parent=None,
                 delay=0,
                 nframes=0):
        self.parent = parent
        self.delay = delay
        self.nframes = nframes
        self.initialized = False
        self.done = False
        self.register = parent.tasks.registerTask

    def isDone(self):
        return self.done

    def initialize(self, frame):
        """Called when the taskmanager activates the task."""
        pass

    def doprocess(self, frame):
        """Operation performed on each video frame."""
        pass

    def dotask(self):
        """Operation performed to complete the task."""
        pass

    def process(self, frame):
        if not self.initialized:
            self.initialize(frame)
            self.initialized = True
        if self.delay > 0:
            self.delay -= 1
        elif self.nframes > 0:
            self.doprocess(frame)
            self.nframes -= 1
        else:
            self.dotask()
            print('TASK: ' + self.__class__.__name__ + ' done')
            self.done = True
