from utils.Enumerations import PowerStates, ColorModes
from yeelight import Bulb, discover_bulbs


class BulbArray:

    bulbs = []

    def __init__(self, timeout=2):
        """ Initializer. Searches for bulbs """
        self.discover_bulbs(timeout)  # Discovering bulbs

    def get_properties(self, bulb_index=-1):
        """ Returns a dictionary with the state of a bulb
            i.e.: power, bright, ct, rgb, hue, sat, color_mode, flowing ... """

        def int_to_rgb(integer):
            """ Converts an integer read from the bulb and returns its RGB value """
            hexadecimal = hex(int(integer))
            hexadecimal = hexadecimal.split("x")[1].zfill(6)
            r = int("0x" + hexadecimal[-7:-4], 16)
            g = int("0x" + hexadecimal[-4:-2], 16)
            b = int("0x" + hexadecimal[-2::], 16)
            return r, g, b

        bulb_index=int(bulb_index)
        properties = self.bulbs[bulb_index].get_properties()
        properties["rgb"] = (int_to_rgb(properties["rgb"]))
        return properties

    def set_brightness(self, brightness, bulb_index=-1):
        """ Changes the brightness of a bulb.
            Brightness value goes from 1 to 100. """

        # TODO: Throw an error if value not in range

        bulb_index = int(bulb_index) if bulb_index is not None else -1
        brightness = int(brightness)
        if bulb_index == -1:
            for bulb in self.bulbs:
                bulb.set_brightness(brightness, effect="smooth", duration=1000)
        elif bulb_index <= len(self.bulbs):
            self.bulbs[bulb_index].set_brightness(brightness, effect="smooth", duration=1000)

    def set_color_temp(self, color_temp, bulb_index=-1):
        """ Changes the bulb white temperature
            Temperature value goes from 1700 to 6500K """

        # TODO: Throw an error if value not in range

        color_temp = int(color_temp)
        color_temp = max(1700, color_temp)
        color_temp = min(6500, color_temp)
        if bulb_index == -1:
            for bulb in self.bulbs:
                bulb.set_color_temp(color_temp, effect="smooth", duration=1000)
        elif bulb_index <= len(self.bulbs):
            self.bulbs[bulb_index].set_color_temp(color_temp, effect="smooth", duration=1000)

    def set_rgb(self, r=None, g=None, b=None, bulb_index=-1):
        """ Changes the color given RGB values
            If an RGB value is not given, its value will not change """

        # TODO: Throw an error if value not in range

        bulb_index = int(bulb_index)
        r, g, b = map(lambda x: int(x) if x is not None else None, (r, g, b))
        r0, g0, b0 = self.get_properties().get("rgb", (None, None, None))
        r = r0 if r is None else min(r, 255)
        g = g0 if g is None else min(g, 255)
        b = b0 if b is None else min(b, 255)

        if bulb_index == -1:
            for pereta in self.bulbs:
                pereta.set_rgb(r, g, b, effect="smooth", duration=1000)
        elif bulb_index <= len(self.bulbs):
            self.bulbs[bulb_index].set_rgb(r, g, b, effect="smooth", duration=1000)

    def power(self, on_off, bulb_index=-1):
        """ power a bulb (or all) depending on param on_off """

        # TODO: Throw an error if value not in range

        on_off = int(on_off)
        if bulb_index == -1:
            for bulb in self.bulbs:
                if on_off == PowerStates.ON:
                    bulb.turn_on(effect="smooth", duration=1000)
                if on_off == PowerStates.OFF:
                    bulb.turn_off(effect="smooth", duration=1000)
                if on_off == PowerStates.SWITCH:
                    bulb.toggle(effect="smooth", duration=1000)
        elif bulb_index <= len(self.bulbs):
            if on_off == PowerStates.ON:
                self.bulbs[bulb_index].turn_on(effect="smooth", duration=1000)
            if on_off == PowerStates.OFF:
                self.bulbs[bulb_index].turn_off(effect="smooth", duration=1000)
            if on_off == PowerStates.SWITCH:
                self.bulbs[bulb_index].toggle(effect="smooth", duration=1000)

    def discover_bulbs(self, timeout):
        print("Discovering bulbs...")
        self.bulbs = []
        while len(self.bulbs) < 1:
            bulbs_discovered = discover_bulbs(timeout)
            for pereta_descoberta in bulbs_discovered:
                ip, port = (pereta_descoberta["ip"], pereta_descoberta["port"])
                bulb = Bulb(ip, port=port)
                if bulb:
                    self.bulbs.append(bulb)

        print("{x} bulbs found".format(x=len(self.bulbs)))