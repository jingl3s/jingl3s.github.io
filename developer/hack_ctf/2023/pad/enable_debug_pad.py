import serial

with serial.Serial() as ser:
    ser.baudrate = 115200
    ser.port = '/dev/ttyUSB0'
    ser.timeout = 0.5
    ser.open()
    ser.write(b'\n')
    answer = ser.read_until(b'>').decode()
    counter = 1
    while counter < 30000:
    # if True:
        print(f"Current Iteration: {counter}")
        ser.write(f"debug enable {counter}\n".encode())
        answer = ser.read_until(b':').decode()
        answer2 = ser.readline().decode()
        if "not enabled" not in answer:
          print(answer)
          answer = ser.readline().decode()
          print(answer)
        else:
          answer = ser.readline().decode()

        #   answer = ser.readline().decode()
        #   print(answer)
        counter += 1

