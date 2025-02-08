from machine import Pin, I2C
import dht
import ssd1306
import time

# Inisialisasi sensor DHT11 di GPIO 4
dht11 = dht.DHT11(Pin(4))

# Inisialisasi I2C untuk OLED (SCL=22, SDA=21)
i2c = I2C(0, scl=Pin(22), sda=Pin(21))

# Inisialisasi OLED 128x64
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

while True:
    try:
        dht11.measure()  # Membaca suhu & kelembaban
        suhu = dht11.temperature()  # Suhu dalam °C
        kelembaban = dht11.humidity()  # Kelembaban dalam %

        # Menampilkan data di Serial Monitor
        print(f"Suhu: {suhu}°C, Kelembaban: {kelembaban}%")

        # Membersihkan layar OLED sebelum menampilkan data baru
        oled.fill(0)

        # Menampilkan teks di OLED
        oled.text("Ardan Santi", 0, 5)
        oled.text(f"Suhu : {suhu} C", 0, 25)
        oled.text(f"Kelembaban: {kelembaban}%", 0, 45)

        # Menampilkan di OLED
        oled.show()

    except Exception as e:
        print("Error membaca sensor!", e)

    # Tunggu 2 detik sebelum membaca ulang
    time.sleep(3)
