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

            ssid_name = 'none'
            ip = 'none'

            try:
                ssid_name = m.group(1)
            except AttributeError as e:
                pass

            color = '#ff8888'

            if not ssid_name == 'none':
                out = subprocess.check_output(['ip','addr','show',self.interface])
                out = out.decode('utf-8')
                for line in out.split('\n'):
                    # TODO: checking ipv4 address only now, need to expand to ipv4 or ipv6
                    # also, this doesn't really check for a valid IP, just ANY IP
                    ipm = re.match(r'\s*inet (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/\d{2}\s+)', line)
                    if ipm:
                        ip = ipm.group(1)
                        break

            if not ssid_name == 'none' and not ip == 'none':
                color = '#7adf8f'
            
            return {
                'name': "wifi",
                'instance': self.interface,
                'full_text': ' ' + ssid_name,
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
