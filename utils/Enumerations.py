from enum import IntEnum, Enum


class StrEnum(str, Enum):
    pass


class LightParameters(StrEnum):
    """ Enumeration that contains the possible /light parameters """
    INDEX, R, G, B, BRIGHT, TEMP, ON, REFRESH, STATE = "index r g b bright temp on refresh state".split()


class NotificationParameters(StrEnum):
    """ Enumeration that contains the possible /notification parameters """
    TITLE, APP, TEXT = "title app text".split()


class PowerStates(IntEnum):
    """ Enumeration that describes the state of the bulb
         0: OFF
         1: ON
        -1: Used to switch from OFF to ON o viceversa """
    ON, OFF, SWITCH = 1, 0, -1


class ColorModes(IntEnum):
    """ Enumeration that describes bulb color modes
        1: Color mode
        2: Temperature mode
        3: HSV color mode """
    COLOR_MODE, TEMP_MODE, HSV_MODE = 1, 2, 3