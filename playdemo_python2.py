import sys
import telnetlib
from time import sleep

HOST = "192.168.0.10"
PORT = 2121

tn = telnetlib.Telnet(HOST, PORT)


welcome = "CSGO Remote Console Online"
endl = "\n"


def run(command):
    tn.write(command + endl )


tn = telnetlib.Telnet(HOST, PORT)

tn.write("echo " + welcome + endl)
tn.read_until("Online")
print("Successfully Connected")

run("echo gg wp")

run("playdemo C:\Users\csgo2\Desktop\cloud9-vs-renegades-train.dem")

