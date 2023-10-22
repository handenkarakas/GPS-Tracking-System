import serial
import time

# Arduino üzerinde SIM808 ile bağlantı kurulan seri portun adı
ser = serial.Serial('COM4', 9600, timeout=1)

# GPS modülünü etkinleştirme komutu
ser.write(b'AT+CGPSPWR=1\r\n')
time.sleep(1)

# GPS verilerini almak için modülü ayarlama
ser.write(b'AT+CGPSINF=0\r\n')
time.sleep(1)

try:
    while True:
        response = ser.readline().decode('utf-8')
        if 'CGPSINF:' in response:
            # GPS verilerini işleyin
            gps_data = response.split(': ')[1].split(',')
            latitude = gps_data[1]
            longitude = gps_data[2]
            print(f"Enlem: {latitude}, Boylam: {longitude}")
        time.sleep(1)

except KeyboardInterrupt:
    ser.write(b'AT+CGPSPWR=0\r\n')  # GPS modülünü kapatma
    ser.close()
