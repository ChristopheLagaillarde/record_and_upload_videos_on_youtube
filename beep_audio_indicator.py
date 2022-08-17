# Program : beep audio indicator
# Description : this will emit a "beep" sound to help cordinate sound and image
# Date : 13/08/22
# Author : Christophe Lagaillarde
# Version : 1.0
from datetime import datetime

import pause
import winsound
from numba import jit


@jit
def beep_audio_indicator(time_record_start: datetime) -> None:
    pause.until(time_record_start)
    winsound.Beep(2500, 1000)

    return None
