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

file_name = "fdpractice.txt"
file_handle = os.open(file_name, os.O_RDWR | os.O_CREAT)
file_object_TextIO = os.fdopen(file_handle, "w+")
file_object_TextIO.write("Some string to write to this file")
file_object_TextIO.flush()

pid = 1
#MacOS
#pid = os.fork()

if pid == 0:
    print(f"\nChild Process ID: {os.getpid()}")
    os.lseek(file_handle, 0, 0)
    print(f"\nFile Contents: {os.read(file_handle, 100).decode()}")
    os.close(file_handle)
    sys.exit(0)
else:
    print(f"\nParent Process ID: {os.getpid()}, Child Process ID: {pid}")
    print("Wait for child")
    os.wait(pid, 0)
    print("Child done")
    file_object_TextIO.close()
sys.exit(0)