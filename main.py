import subprocess

connected = False

DEVICE_IP = "YOUR_DEVICE_IP"
output = subprocess.Popen(["ping", "-t 100", DEVICE_IP], stdout=subprocess.PIPE)

while not connected:
    line = output.stdout.readline()
    if not line:
        break
    connected_ip = line.decode("utf-8").split()[3].replace(":", "")
    if connected_ip == DEVICE_IP:
        subprocess.run(["say", "#navn har tilsluttet sig til netværket"])
        connected = True
    else:
        print("Venter på forbindelse..")