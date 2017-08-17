import sys
import telnetlib
from time import sleep

HOST = "192.168.0.10"
PORT = 2121

tn = telnetlib.Telnet(HOST, PORT)


welcome = "CSGO Remote Console Online"
endl = "\n"


def run(command):
    tn.write("echo " + command + endl)
    tn.write(command + endl)
    sleep(1.0)


tn = telnetlib.Telnet(HOST, PORT)

tn.write("echo " + welcome + endl)
tn.read_until("Online")
print("Successfully Connected")


run("demo_timescale 4.0")
run("playdemo really_short.dem; exit")

