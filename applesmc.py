import sys

class AppleSmcWidget(object):
    def __init__(self, applesmc_path='/sys/devices/platform/applesmc.768'):
        self.applesmc_path = applesmc_path

    def output(self):
        temp = int(900)
        fan1_input = 'unknown'
        fan2_input = 'unknown'
        try: 
            fan1_input = int(open('{dev}/{fan}'.\
                                      format(dev=self.applesmc_path, fan='fan1_input')).read())
            fan2_input = int(open('{dev}/{fan}'.\
                                      format(dev=self.applesmc_path, fan='fan2_input')).read())
        except OSError as e:
            sys.stderr.write("fan input: {0}\n".format(e))

        try:
            temp_input = int(open('{dev}/{temp}'.\
                                      format(dev=self.applesmc_path, temp='temp5_input')).read())
            temp = temp_input/1000
        except OSError as e:
            sys.stderr.write("temp input: {0}\n".format(e))

        color = '#3A993C'
        if temp > 68:
            color = '#94993A'
        if temp > 80:
            color = '#993A3A'

        return {
            'name': "applesmc",
            'full_text': ' {temp:.2g}°C'.format(temp=temp) + ', ' + str(fan1_input) + ', ' + str(fan2_input),
            'color': color,
            'icon': 'mmbar/icons/temp.xbm',
            }

