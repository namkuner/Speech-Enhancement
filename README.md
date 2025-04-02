# Speech Enhancement

Speech Enhancement là một dự án cải thiện chất lượng âm thanh bằng cách sử dụng ESP32 và server Python.

## 1. Yêu cầu phần cứng
- **ESP32**
- **Microphone I2S**
- **Loa (tùy chọn)**
- **Cáp USB để nạp code**

## 2. Yêu cầu phần mềm
- **Arduino IDE** (hoặc PlatformIO)
- **Python 3.x**
- Các thư viện cần thiết:
  - `numpy`
  - `scipy`
  - `sounddevice`
  - `flask`

## 3. Cài đặt ESP32
1. Cài đặt thư viện ESP32 trên Arduino IDE.
2. Thêm thư viện I2S và WiFi cho ESP32:
   - `ESP8266Audio`
   - `WiFi.h`
3. Flash code vào ESP32 thông qua Arduino IDE hoặc PlatformIO.

## 4. Cài đặt server Python
1. Clone repo:
   ```bash
   git clone https://github.com/namkuner/Speech-Enhancement.git
   cd Speech-Enhancement
   ```
2. Cài đặt môi trường Python:
   ```bash
   pip install -r requirements.txt
   ```
3. Chạy server:
   ```bash
   python server.py
   ```

## 5. Kết nối ESP32 với Server
- ESP32 sẽ gửi dữ liệu âm thanh thu được lên server thông qua giao thức HTTP hoặc WebSocket.
- Server sẽ xử lý dữ liệu và trả về kết quả đã cải thiện.

## 6. Kiểm tra hoạt động
1. Kết nối ESP32 với mạng WiFi.
2. Kiểm tra dữ liệu truyền lên server bằng cách xem log trên terminal.
3. Kiểm tra file đầu ra để xem âm thanh đã được cải thiện.

## 7. Troubleshooting
- Kiểm tra kết nối WiFi của ESP32.
- Đảm bảo server Python đang chạy.
- Kiểm tra cổng Serial Monitor trên Arduino IDE để debug lỗi ESP32.

## 8. Đóng góp
Nếu bạn có cải tiến hoặc phát hiện lỗi, vui lòng mở Pull Request hoặc Issue trên GitHub repo này.

---
Happy coding! 🚀