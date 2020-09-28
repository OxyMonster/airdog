import subprocess
import optparse

is_accepted = False
parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest="interface", help="[+][+][+] by whiteRow [+][+][+]")
(options, arguments) = parser.parse_args()
interface = options.interface
password = input("Enter your sudo password: ")

def start_airmon_airodump():
    subprocess.call(f"sudo airmon-ng start {interface}", shell=True)
    subprocess.call(f"{password}", shell=True)
    print(interface)
    print(subprocess.call(f"sudo airodump-ng {interface}", shell=True))


if not interface:

    interface = input("interface >")
    print(f"[+] Changing mac address of {interface}")
    print(f"[+] Changing mode to monitor  of {interface}")
    print(f"[+] Getting LAN list  from {interface}")
    print("Do you wan to continue press y/n")
    is_accepted = input("")

    if is_accepted == "y":
        start_airmon_airodump()

    else:
        print("process exit =((")

else:
    start_airmon_airodump()




