import os
import socket
import platform

print("=" * 50)
print("SYSTEM INFORMATION & NETWORK ASSET SCANNER")
print("=" * 50)

print("\n[ SYSTEM INFORMATION ]")
print("Hostname:", socket.gethostname())
print("Operating System:", platform.system())
print("OS Release:", platform.release())
print("Kernel:", platform.version())
print("Architecture:", platform.machine())
print("Python Version:", platform.python_version())

print("\n[ NETWORK INFORMATION ]")
print("IP Address:", socket.gethostbyname(socket.gethostname()))

print("\n[ NETWORK INTERFACES ]")
os.system("ip -br addr")

print("\n[ DEFAULT GATEWAY ]")
os.system("ip route | grep default")

print("\n[ DNS CONFIGURATION ]")
os.system("cat /etc/resolv.conf | grep nameserver")

print("\n[ LISTENING PORTS ]")
os.system("ss -tuln")

print("\n" + "=" * 50)
print("SCAN COMPLETED")
print("=" * 50)
