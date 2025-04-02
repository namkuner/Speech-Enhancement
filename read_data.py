import socket
import pyaudio
import struct
import wave

# Cấu hình mạng
HOST = "0.0.0.0"  # Lắng nghe trên tất cả các IP
PORT = 3000

# Cấu hình âm thanh
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 8000
CHUNK = 8000

# Khởi tạo socket TCP server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print("Đang chờ ESP32 kết nối...")
conn, addr = server_socket.accept()
print(f"Kết nối từ {addr}")

# Khởi tạo PyAudio
p = pyaudio.PyAudio()
stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, output=True, frames_per_buffer=CHUNK)

wav_file = wave.open("output.wav", "wb")
wav_file.setnchannels(CHANNELS)
wav_file.setsampwidth(p.get_sample_size(FORMAT))
wav_file.setframerate(RATE)
try:
    while True:
        data = conn.recv(CHUNK * 2)  # Nhận dữ liệu từ ESP32
        print("data",data)
        print("data",len(data))
        print("data",type(data))
        numbers = list(struct.unpack(f"{len(data) // 2}h", data))
        print("numbers",numbers)  # In ra danh sách số nguyên
        print("numbers",len(numbers))
        print("numbers",type(numbers))

        if not data:
            break
        stream.write(data)  # Phát âm thanh
        wav_file.writeframes(data)
except KeyboardInterrupt:
    print("\nDừng server.")
finally:

    # Đóng file WAV
    wav_file.close()

    stream.stop_stream()
    stream.close()
    p.terminate()
    conn.close()
    server_socket.close()