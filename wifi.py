import re
import subprocess


class WifiWidget(object):
    def __init__(self, interface='wlan0'):
        self.interface = interface

    def output(self):
        try:
            out = subprocess.check_output(['iwgetid'])
            out = out.decode('utf-8')
            m = re.match(r'{interface}\s+ESSID:"(.+?)"\n'.format(
                interface=self.interface), out)
            
            color = '#ff8888'
            out = subprocess.check_output(['wpa_cli','status'])
            out = out.decode('utf-8')
            ip = 'none'
            for line in out.split('\n'):
                #print("checking: {0}".format(line))
                ipm = re.match(r'ip_address=(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$)', line)
                if ipm:
                    ip = ipm.group(1)
                    color = '#7adf8f'
                    break
            
            return {
                'name': "wifi",
                'instance': self.interface,
                'full_text': ' ' + m.group(1),
                'color': color,
                'icon': 'mmbar/icons/wifi_03.xbm',
            }
        except subprocess.CalledProcessError:
            return {
                'name': "wifi",
                'instance': self.interface,
                'full_text': ' ',
                'color': '#3f3f3f',
                'icon': 'mmbar/icons/wifi_off_03.xbm',
            }
            pass
