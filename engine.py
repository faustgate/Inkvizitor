# We only need to import this module
import os
import send2trash
 
# The top argument for walk. The
# Python27/Lib/site-packages folder in my case


class Engine(object):
    def __init__(self):
        self.topdir = '/var/run/media/sergey.puronen/One Touch 4 Mini/Music/DEAD CAN DANCE (1982-2013) (mp3 128-320)/'
        # The arg argument for walk, and subsequently ext for step
        self.exten = '.mp3'
        self.recycle = None
        self.songs = []
        self.excepts = []

    def _step(self, arg, dirname, names):

        for name in names:
            full_file_name = os.path.join(dirname, name)
            if os.path.isdir(full_file_name):
                continue
            _, exten = os.path.splitext(full_file_name)
            if full_file_name not in self.songs and exten not in self.excepts:
                if self.recycle:
                    send2trash.send2trash(full_file_name)
                else:
                    os.remove(full_file_name)
                print full_file_name

    def _get_list(self, list_name):
        if list_name != '':
            with open(list_name, 'r') as play_list:
                listt = play_list.read()
        else:
            listt = []
        return listt

    def start(self, start_dir, list_of_targets, list_of_exceptions='',
              recursive=True, rem_to_recycle=True):
        # Start the walk

        self.songs = self._get_list(list_of_targets)
        self.excepts = self._get_list(list_of_exceptions)
        self.recycle = rem_to_recycle
        if recursive:
            os.path.walk(start_dir, self._step, None)
        else:
            os.listdir(start_dir)