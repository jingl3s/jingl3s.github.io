from pwn import *
import angr
context.log_level='INFO'

p = remote('::1', 8000)
# p = remote('9000:ff:1ce:ff:216:3eff:fe8c:4a0c', 8000)
p.recvuntil(b"Password: ")
print("sending password")
p.sendline(b"If things are not failing, you are not innovating enough")
intro = p.recvline().decode()

done = 0
while True:
    print("Waiting for binary")
    binary_base64 = p.recvline()
    if b"FLAG-" in binary_base64:
        print(binary_base64)
        sys.exit()
    print("Writing binary to disk")
    with open('prog', 'wb') as fd:
        fd.write(base64.b64decode(binary_base64))
    with open('/tmp/tmp.pt3TcpsgzA/prog', 'wb') as fd:
        fd.write(base64.b64decode(binary_base64))

    print("Starting analysis")
    project = angr.Project('./prog', selfmodifying_code=False, auto_load_libs=False)
    simfile = angr.SimFile('myconcretefile', content=b'/tmp/tmp.pt3TcpsgzA/prog')
    # init = project.factory.entry_state(add_options=angr.options.unicorn)
    init = project.factory.entry_state()
    init.options.add(angr.options.SYMBOL_FILL_UNCONSTRAINED_MEMORY)
    init.options.add(angr.options.SYMBOL_FILL_UNCONSTRAINED_REGISTERS)
    init.fs.insert(b'/proc/self/cmdline', simfile)

    cfg = project.analyses.CFGEmulated()
    sm = project.factory.simgr(init, veritesting=True)
    sm.explore(find=lambda s: b'Deactivated.' in s.posix.dumps(1))
    sm.run()

    correct_input = sm.found[0].posix.dumps(0) + b'\n'
    print(correct_input.decode())
    print(base64.b64encode(correct_input).decode())

    # p.interactive()
    p.sendline(base64.b64encode(correct_input).decode())
    msg = p.recvline()
    print(msg)
    done += 1
    print("Done:", done)
