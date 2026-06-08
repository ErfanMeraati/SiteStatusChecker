# Site Status Checker

**English** | [فارسی])

---

## English

A fast, concurrent CLI tool to check the online/offline status of multiple websites at once.

### Features
- Checks multiple URLs simultaneously (ThreadPoolExecutor)
- Shows status code, response time, server type, and content type
- Detects redirects
- Option to save results to a timestamped `.txt` file

### Usage

**Run the `.exe` directly:**
SiteStatusChecker.exe google.com github.com example.com

Or run without arguments to enter URLs manually.

Run with Python:

pip install requests

python SiteStatusChecker.py google.com github.com

Output Example
[OK] https://google.com | 200 | 143ms | gws | text/html

↳ Redirected to: https://www.google.com/

[OK] https://github.com | 200 | 210ms | GitHub.com | text/html

[FAIL] https://offline-site.com — Connection failed

فارسی
ابزاری سریع و همزمان برای بررسی وضعیت آنلاین/آفلاین بودن چندین وب‌سایت به‌طور همزمان.

ویژگی‌ها
بررسی همزمان چند URL با استفاده از ThreadPoolExecutor
نمایش کد وضعیت، زمان پاسخ، نوع سرور و نوع محتوا
تشخیص ریدایرکت
امکان ذخیره نتایج در فایل .txt با نام تاریخ‌دار
نحوه استفاده
اجرای مستقیم .exe:

SiteStatusChecker.exe google.com github.com example.com

یا بدون آرگومان اجرا کن تا URLها را دستی وارد کنی.

اجرا با پایتون:

pip install requests

python SiteStatusChecker.py google.com github.com

نمونه خروجی
[OK] https://google.com | 200 | 143ms | gws | text/html

↳ Redirected to: https://www.google.com/

[OK] https://github.com | 200 | 210ms | GitHub.com | text/html

[FAIL] https://offline-site.com — Connection failed

Day 1 of daily tools — 2026-06-08
