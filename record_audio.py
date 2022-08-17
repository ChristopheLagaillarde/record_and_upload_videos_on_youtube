# Program : record audio
# Description : This function will record the internal audio
# Date : 07/08/22
# Author : Christophe Lagaillarde
# Version : 1.0

from datetime import datetime, timedelta
import queue
import sys
from sys import argv
import keyboard
import warnings

import pause
import sounddevice as sd
import soundfile as sf
import numpy  # Make sure NumPy is loaded before it is used in the callback
assert numpy  # avoid "imported but unused" message (W0611)


warnings.simplefilter('ignore')


def int_or_str(text):
    """Helper function for argument parsing."""
    try:
        return int(text)
    except ValueError:
        return text


def record_audio(file_name: str, time_record_start: datetime, device_id: int = 2, channels: int = 1,
                 samplerate: int = None) -> None:

    device_info = sd.query_devices(device_id, 'input')
    samplerate = int(device_info['default_samplerate'])
    q = queue.Queue()

    def callback(indata, frames, time, status):
        """This is called (from a separate thread) for each audio block."""
        if status:
            print(status, file=sys.stderr)
        q.put(indata.copy())

    # Make sure the file is opened before recording anything:
    with sf.SoundFile(file_name, mode='x', samplerate=samplerate,
                      channels=channels) as file:
        with sd.InputStream(samplerate=samplerate, device=device_id,
                            channels=channels, callback=callback):

            pause.until(time_record_start)

            while True and not keyboard.is_pressed('q'):
                file.write(q.get())

    return None


if __name__ == '__main__':
    record_audio(argv[1], datetime.now() + timedelta(seconds=10))





