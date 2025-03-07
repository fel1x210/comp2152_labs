import platform
import socket
import sys
import os

print(f"\nMachine type: {platform.machine()}")
print(f"\nProcessor type: {platform.architecture()}")

socket.setdefaulttimeout(50)
print(f"\nDefault TImeout for Socket: {socket.getdefaulttimeout()}")

print(f"\nOS type: {os.name}")
print(f"\nOS name type: {platform.system()}")
print(f"\nCurrent PID type: {os.getpid()}")