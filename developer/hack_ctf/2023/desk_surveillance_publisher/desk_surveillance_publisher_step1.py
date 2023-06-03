import io
from os import read
import subprocess
import nclib
import base64

# nc = nclib.Netcat(("9000:ff:1ce:ff:216:3eff:fe8c:4a0c", 8000),udp=True, verbose=True, echo_hex=True)
# nc = nclib.Netcat(("9000:ff:1ce:ff:216:3eff:fe8c:4a0c", 8000),verbose=True, echo_hex=True)
nc = nclib.Netcat(("9000:ff:1ce:ff:216:3eff:fe8c:4a0c", 8000))
# nc.interact()
response = nc.recv()
# print(response)
nc.send("I have come for the shadow training\n".encode())
# response = nc.recv()
# print(response)
# nc.send("I have come for the shadow training\n".encode())
response = nc.recv(n=8000000)
response = nc.recv_until("\n")
print(response)

# with open('base64_file', 'wb') as output_file:
#   output_file.write(response)

# # subprocess.check_output(["echo", response.decode(), "|", "base64", "-d", ">", "run"])
# subprocess.run(["./to_bin.sh", response.decode()])

while True:
  bin_content = base64.decodebytes(response)
  # print(bin_content)
  with open('run', 'wb') as output_file:
    output_file.write(bin_content)

  # # subprocess.run(["ghidra-analyzeHeadless", ".", "desk", "-import", "run"])
  # # subprocess.run(["ghidra"])
  subprocess.run(["bash", "./desk_surveillance_publisher_step1_to_asm.sh"])

  with open("run.asm", "rb") as asm_code:
  # with open("Desk_Surveillance_Publisher/run.asm", "rb") as asm_code:
    asm_lines = asm_code.readlines()

  values = list()

  for asm_line in asm_lines:
    if b"add" in asm_line and b'To make' not in asm_line:
      add_value = asm_line
      add_value_n = int(asm_line.split()[-1].split(b',')[0][1:],16)
    elif b"cmp" in asm_line:
      cmp_value = asm_line
      cmp_value_n = int(asm_line.split()[-1].split(b',')[0][1:],16)
      val_in_progress = cmp_value_n - add_value_n
      if val_in_progress < 0:
        val_in_progress = val_in_progress & 0xffffffff
      values.append(str(val_in_progress))
    else:
      add_value_n = 0


  values_l=" ".join(values)

  print(values_l)


  value_b64 = base64.b64encode(values_l.encode())
  print(value_b64)

  # nc.interact()

  # asm_code = subprocess.check_output(["gdb", "-batch", "-ex", "'file run'", "-ex", "'disassemble main'"])
  # print(asm_code)

  # values=input("waiting values")
  nc.send(value_b64+ b'\n')
  response = nc.recv_until("\n")
  print(response)
  response = nc.recv_until("\n")
  print(response)
