import sys

class AppleSmcWidget(object):
    def __init__(self, applesmc_path='/sys/devices/platform/applesmc.768'):
        self.applesmc_path = applesmc_path

    def output(self):
        fan1_input = int(open('{dev}/{fan}'.\
                            format(dev=self.applesmc_path, fan='fan1_input')).read())
        fan2_input = int(open('{dev}/{fan}'.\
                            format(dev=self.applesmc_path, fan='fan2_input')).read())
        temp_input = int(open('{dev}/{temp}'.\
                                  format(dev=self.applesmc_path, temp='temp5_input')).read())

        temp = temp_input/1000
        color = '#3A993C'
        if temp > 68:
            color = '#94993A'
        if temp > 80:
            color = '#993A3A'

        return {
            'name': "applesmc",
            'full_text': ' {temp:.2g}°C'.format(temp=temp_input/1000) + ', ' + str(fan1_input) + ', ' + str(fan2_input),
            'color': color,
            'icon': 'mmbar/icons/temp.xbm',
            }

