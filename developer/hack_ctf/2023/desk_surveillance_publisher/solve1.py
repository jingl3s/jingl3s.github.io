from pwn import *

import angr
import base64
import claripy
import sys

context.log_level='DEBUG'
local = False

if len(sys.argv) > 1:
    local = True

if not local:
    p = remote('::1', 8000)
    # p = remote('9000:ff:1ce:ff:216:3eff:fe8c:4a0c', 8000)
    p.recvuntil(b"Password: ")
    p.sendline(b"I have come for the shadow training")
    intro = p.recvline().decode()

while True:
    if not local:
        binary_base64 = p.recvline()
        if b"FLAG-" in binary_base64:
            print(binary_base64)
            sys.exit()
        with open('prog', 'wb') as fd:
            fd.write(base64.b64decode(binary_base64))

    project = angr.Project('./prog', selfmodifying_code=False, auto_load_libs=True)

    input_chars = [claripy.BVS('input_%d' % i, 8) for i in range(60)]
    output_chars = [claripy.BVS('out_%d' % i, 8) for i in range(16)]
    err_chars = [claripy.BVS('err_%d' % i, 8) for i in range(100)]
    _input = claripy.Concat(*input_chars)
    _output = claripy.Concat(*output_chars)
    _err = claripy.Concat(*err_chars)
    stdin = angr.SimFile('/dev/stdin', content=_input, size=60)
    stdout = angr.SimFile('/dev/stdout', content=_output, size=16)
    stderr = angr.SimFile('/dev/stderr', content=_err, size=100)

# init = project.factory.entry_state(args=['/tmp/prog'], add_options=angr.sim_options.unicorn)
    init = project.factory.entry_state()
    sm = project.factory.simulation_manager(init)
    sm.explore(find=lambda s: b'Deactivated.' in s.posix.dumps(1))
    sm.run()

    correct_input = sm.found[0].posix.dumps(0) + b'\n'
    print(correct_input.decode())
    print(base64.b64encode(correct_input).decode())

    if not local:
        # p.interactive()
        p.sendline(base64.b64encode(correct_input).decode())
        msg = p.recvline()
        print(msg)
