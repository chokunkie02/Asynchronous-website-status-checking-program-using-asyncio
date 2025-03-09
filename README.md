### ขั้นตอนการใช้งาน Git Clone เพื่อดาวน์โหลดโปรเจค

---

### 1. **เตรียมเครื่องมือ**
- ติดตั้ง Git บนเครื่องของคุณ (หากยังไม่ได้ติดตั้ง):
  - ดาวน์โหลด Git จาก [git-scm.com](https://git-scm.com/)
  - ติดตั้งตามขั้นตอนที่แนะนำ

- ตรวจสอบว่า Git ติดตั้งเรียบร้อยแล้ว:
  ```bash
  git --version
  ```

---

### 2. **ใช้ Git Clone เพื่อดาวน์โหลดโปรเจค**

#### คำสั่ง Git Clone
- เปิด Terminal หรือ Command Prompt
- รันคำสั่งต่อไปนี้เพื่อโคลนโปรเจคจาก GitHub:
  ```bash
  git clone https://github.com/chokunkie02/async-downloader.git
  ```

#### ผลลัพธ์ที่คาดหวัง
- Git จะดาวน์โหลดโปรเจคทั้งหมดลงในโฟลเดอร์ `async-downloader`:
  ```
  Cloning into 'async-downloader'...
  remote: Enumerating objects: 10, done.
  remote: Counting objects: 100% (10/10), done.
  remote: Compressing objects: 100% (8/8), done.
  remote: Total 10 (delta 1), reused 0 (delta 0), pack-reused 0
  Receiving objects: 100% (10/10), done.
  Resolving deltas: 100% (1/1), done.
  ```

---

### 3. **เข้าไปในโฟลเดอร์โปรเจค**

- ใช้คำสั่ง `cd` เพื่อเข้าไปในโฟลเดอร์โปรเจค:
  ```bash
  cd async-downloader
  ```

---

### 4. **ตรวจสอบไฟล์ในโปรเจค**

- ตรวจสอบไฟล์ที่ดาวน์โหลดมา:
  ```bash
  ls
  ```
- ผลลัพธ์ที่คาดหวัง:
  ```
  README.md
  async_downloader.py
  ```

---

### 5. **ติดตั้ง dependencies**

- ติดตั้งไลบรารีที่จำเป็น (`aiohttp`):
  ```bash
  pip install aiohttp
  ```

---

### 6. **รันโปรแกรม**

- รันโปรแกรมโดยใช้คำสั่ง:
  ```bash
  python async_downloader.py
  ```

---

### 7. **ผลลัพธ์ที่คาดหวัง**

- โปรแกรมจะแสดงผลลัพธ์การดาวน์โหลดหน้าเว็บแบบ asynchronous:
  ```
  Starting downloads...
  Read 3769 bytes from https://www.jython.org
  Read 274 bytes from http://olympus.realpython.org/dice
  ...
  Downloaded 160 sites in 1.72 seconds
  ```

---