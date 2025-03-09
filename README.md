```markdown
# โครงการ: โปรแกรมตรวจสอบสถานะเว็บไซต์แบบ asynchronous ด้วย `asyncio`

## คำอธิบายโปรแกรม
โปรแกรมนี้เป็นตัวอย่างการใช้งาน `asyncio` ใน Python เพื่อตรวจสอบสถานะ HTTP ของเว็บไซต์หลายแห่งแบบ asynchronous โดยโปรแกรมจะส่งคำขอ HTTP พร้อมกันหลายคำขอและแสดงสถานะ HTTP response code (เช่น 200, 404) ของแต่ละเว็บไซต์

## ไฟล์ในโครงการ
- `main.py`: โค้ดหลักของโปรแกรม
- `README.md`: คำอธิบายโครงการ

## การติดตั้งและรันโปรแกรม

### ขั้นตอนการติดตั้ง
1. ติดตั้ง Python 3.7 หรือสูงกว่า
2. ติดตั้งไลบรารี `aiohttp`:
   ```bash
   pip install aiohttp
   ```

### ขั้นตอนการรันโปรแกรม
1. โคลนโปรเจคจาก Git repository:
   ```bash
   git clone https://github.com/chokunkie02/Asynchronous-website-status-checking-program-using-asyncio.git
   cd Asynchronous-website-status-checking-program-using-asyncio
   ```
2. รันโปรแกรม:
   ```bash
   python main.py
   ```

## ผลลัพธ์ที่คาดหวัง
โปรแกรมจะแสดงสถานะ HTTP response code ของแต่ละเว็บไซต์ เช่น:
```
Status of https://www.google.com: 200
Status of https://www.github.com: 200
Status of https://www.example.com: 200
Error checking https://www.invalid-website-12345.com: Cannot connect to host...
```

## รายละเอียดโค้ด
### ฟังก์ชัน `check_website_status`
- ฟังก์ชันนี้ใช้ `aiohttp` เพื่อส่งคำขอ GET ไปยัง URL ที่กำหนด
- หากสำเร็จ จะแสดงสถานะ HTTP response code (เช่น 200, 404)
- หากเกิดข้อผิดพลาด (เช่น เว็บไซต์ไม่สามารถเข้าถึงได้) จะแสดงข้อความ error

### ฟังก์ชัน `main`
- ฟังก์ชันหลักที่สร้าง `aiohttp.ClientSession` และ task สำหรับตรวจสอบสถานะเว็บไซต์หลายแห่งพร้อมกัน
- ใช้ `asyncio.gather` เพื่อรัน task พร้อมกัน

### การรันโปรแกรม
- ใช้ `asyncio.run(main(urls))` เพื่อรันฟังก์ชันหลัก `main`

## การส่งงาน
- ส่งโค้ดในรูปแบบ Git repository
- ไฟล์ README.md ควรมีคำอธิบายโครงการและวิธีการรันโปรแกรม

## หมายเหตุ
- สามารถเพิ่มหรือแก้ไขรายการเว็บไซต์ในตัวแปร `urls` เพื่อทดสอบกับเว็บไซต์อื่นๆ ได้
- หากต้องการทดสอบกับเว็บไซต์จำนวนมาก สามารถใช้ลิสต์ URL จากไฟล์หรือ API ได้

---
