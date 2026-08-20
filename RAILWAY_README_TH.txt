Railway startup (Admin Panel only)

ไฟล์เดิมของโปรเจกต์ถูกเก็บไว้ ไม่ได้แก้ main.py/addon.py/core/access_jwt
Railway จะเริ่มจาก railway_app.py ซึ่งเปิดเฉพาะหน้า Admin + SQLite เท่านั้น

Variables ที่ตั้งได้:
ADMIN_EMAIL       อีเมลล็อกอินแอดมิน
ADMIN_PASSWORD    รหัสผ่านแอดมิน
SECRET_KEY        ตั้งเป็นข้อความสุ่มยาว ๆ
DB_PATH           ถ้าใช้ Volume เช่น /data/bot_data.db

ถ้าไม่ตั้ง ADMIN_EMAIL/ADMIN_PASSWORD จะใช้ค่าดั้งเดิมใน admin_panel.py

Start command:
gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 4 --timeout 120 railway_app:app
