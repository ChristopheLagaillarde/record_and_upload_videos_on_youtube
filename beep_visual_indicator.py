# Program : beep visual indicator
# Description : this will display a "beep" message to help cordinate sound and image
# Date : 13/08/22
# Author : Christophe Lagaillarde
# Version : 1.0
from datetime import datetime

import pause


def beep_visual_indicator(time_record_start: datetime) -> None:
    pause.until(time_record_start)
    print('########################BEEP########################')

    return None
