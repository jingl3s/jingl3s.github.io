import serial
import operator
ops = {
    "+": operator.add,
    "-": operator.sub,
    "%": operator.mod,
    "*": operator.mul,
    "/": operator.truediv,
}

with serial.Serial() as ser:
    ser.baudrate = 115200
    ser.port = '/dev/ttyUSB0'
    ser.timeout = 0.5
    ser.open()
    ser.write(b'\n')
    answer = ser.read_until(b'>').decode()
    ser.write(b'math\n')
    limit = 10000
    while limit > 0:
        print(f"Current Iteration: {limit}")
        args = ser.read_until(b'=').decode().split()
        print(args)
        gauche = int(args[-4])
        op = args[-3]
        droite = int(args[-2])
        equals = f"{ops[op](gauche, droite)}\n" 
        ser.write(equals.encode())
        limit -= 1
