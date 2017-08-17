import sys
import telnetlib
from time import sleep
import subprocess

HOST = "192.168.0.10"
PORT = 2121
welcome = "CSGO Remote Console Online"
endl = "\n"

# Runs commands on the csgo console
# Sleeps after for rate limiting but does not block
def run(command):
    tn.write("echo Remote Command: " + command + endl)
    tn.write(command + endl)
    sleep(1.0)


# Start CS:GO
subprocess.Popen("C:\Program Files (x86)\Steam\steamapps\common\Counter-Strike Global Offensive\csgo.exe -netconport 2121 -console -novid")

# Wait for csgo to be ready (30 is being very safe)
print "Waiting for csgo to start up"
sleep(30)

# Initialize csgo telnet connection
tn = telnetlib.Telnet(HOST, PORT)
tn.write("echo " + welcome + endl)
tn.read_until("Online")
print("Successfully Connected")

# Do the work:

# Run a demo
run("playdemo C:\Users\csgo2\Desktop\cloud9-vs-renegades-train.dem")
# wait for demo to load and start playing
sleep(10)
run("demo_info")
run("demo_timescale 1.0") # can make go faster
run("demo_debug 1")
tn.read_until("Demo contents")

# Run 'demo_info' in a loop and check the output to see if we
# are still playing back a demo or if we are back to the menu
# Unfortunately there doesn't seem to be any text emited when
# the demo is finished, so poll for now
out_of_demo_count = 0
while True:
    run("demo_info")
    res = tn.expect(['Error', 'Demo contents'])
    if res[0] == 0:
        print "Not playing Demo"
        out_of_demo_count += 1
    else:
        print "Playing Demo"
    if out_of_demo_count > 3:
        run("exit")
        break
    sleep(1)
