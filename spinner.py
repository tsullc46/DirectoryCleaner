import itertools
import threading
import sys
import time

class Spinner:
    def __init__(self, delay=0.1):
        self.spinner = itertools.cycle(['-', '/', '|', '\\'])
        self.delay = delay
        self.done = False

    def spin(self):
        while not self.done:
            sys.stdout.write(next(self.spinner))  # write the next character
            sys.stdout.flush()                    # flush stdout buffer (actual character display)
            sys.stdout.write('\b')                # erase the last written char
            time.sleep(self.delay)

    def start(self):
        self.done = False
        threading.Thread(target=self.spin).start()

    def stop(self):
        self.done = True
        time.sleep(self.delay * 2)  # Ensure the spinner has time to finish
