#/usr/bash
gdb -batch -ex 'file run' -ex 'disassemble main' > run.asm