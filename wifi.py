import re
import subprocess


class WifiWidget(object):
    def __init__(self, interface='wlan0'):
        self.interface = interface

    def output(self):
        ssid_name = 'none'
        ip = 'none'
        color = '#ff8888'
        icon = 'mmbar/icons/wifi_03.xbm'

        try:
            out = subprocess.check_output(['iwgetid'])
            out = out.decode('utf-8')
            m = re.match(r'{interface}\s+ESSID:"(.+?)"\n'.format(
                interface=self.interface), out)

            try:
                ssid_name = m.group(1)
            except AttributeError as e:
                pass
        except (subprocess.CalledProcessError, FileNotFoundError):
            color = '#3f3f3f'
            icon = 'mmbar/icons/wifi_off_03.xbm'

        if not ssid_name == 'none':
            try:
                out = subprocess.check_output(['ip','addr','show',self.interface])
                out = out.decode('utf-8')
                for line in out.split('\n'):
                    # TODO: checking ipv4 address only now, need to expand to ipv4 or ipv6
                    # also, this doesn't really check for a valid IP, just ANY IP
                    ipm = re.match(r'\s*inet (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/\d{2}\s+)', line)
                    if ipm:
                        ip = ipm.group(1)
                        break
            except subprocess.CalledProcessError:
                # ip addr show could fail if interface wasn't
                # available, but previous subprocess call should have
                # already determined that
                pass
            except AttributeError:
                # call to `ip addr show interface` succeeded but regex did not match
                pass

        if not ssid_name == 'none' and not ip == 'none':
            color = '#7adf8f'
            

        return {
            'name': "wifi",
            'instance': self.interface,
            'full_text': ' ' + ssid_name,
            'color': color,
            'icon': icon,
        }
        pass
