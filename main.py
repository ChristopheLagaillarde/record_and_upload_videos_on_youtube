# Program : record and upload video on youtube
# Description : This program will record the screen and audio of the pc and then upload it to youtube
# Date : 07/08/22
# Author : Christophe Lagaillarde
# Version : 1.0
import logging
import os
from multiprocessing import Process

from append_audio_on_video import append_audio_on_video
from beep_audio_indicator import beep_audio_indicator
from beep_visual_indicator import beep_visual_indicator
from record_audio import record_audio
from record_screen import record_screen
import multiprocessing
from datetime import datetime, timedelta


logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')


def main() -> None:
    audio_image_lag_seconds: float
    title: str
    description: str
    keywords: str
    privacy_status: str

    record_screen_process: Process = multiprocessing.Process(target=record_screen, args=(datetime.now() +
                                                                                         timedelta(seconds=10),))
    record_audio_process: Process = multiprocessing.Process(target=record_audio, args=("recorded_sound_of_video.wav",
                                                            datetime.now() + timedelta(seconds=10)))
    beep_audio_indicator_process: Process = multiprocessing.Process(target=beep_audio_indicator,
                                                                    args=(datetime.now() + timedelta(seconds=10),))
    beep_visual_indicator_process: Process = multiprocessing.Process(target=beep_visual_indicator,
                                                                     args=(datetime.now() + timedelta(seconds=10),))

    record_audio_process.start()
    record_screen_process.start()
    beep_audio_indicator_process.start()
    beep_visual_indicator_process.start()

    logging.info('Recording started')

    record_screen_process.join()
    record_audio_process.join()
    logging.info('Recording endded')

    while True:
        try:
            audio_image_lag_seconds: float = float(input('Enter the number of second there is before the beep sound on'
                                                         ' the generated audio file: '))
            logging.info('Putting video and audio together')
            append_audio_on_video('recorded_sound_of_video.wav', 'recorded_screen_of_video.mp4',
                                  audio_image_lag_seconds)
            title = str(input('Enter the title of the video: '))
            description = str(input('Enter the description of the video: '))
            keywords = str(input('Enter the keywords of the video (separated by commas: '))
            privacy_status = str(input('Enter the privacy status of the video (public or private: '))
            break
        except ValueError:
            logging.error('Must be an integer')

    logging.info('Uploading video on youtube')
    os.system("python upload_video.py "
              "--file='final.mp4' "
              "--title='" + title
              + "' --description='" + description
              + "' --category='22' "
                "--keywords='" + keywords
              + "--privacyStatus='" + privacy_status)

    return None


if __name__ == '__main__':
    main()
