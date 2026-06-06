# مبدل YOLO برای M3FD

تبدیل مجموعه دادهٔ چندспектري M3FD (نسخه ۲) به قالب YOLO با تقسیم خودکار test/val و تولید برچسب‌های تمیز.

![GitHub](https://img.shields.io/github/license/ArsinShaabani/M3FD-YOLO-Converter)
![GitHub stars](https://img.shields.io/github/stars/ArsinShaabani/M3FD-YOLO-Converter?style=social)
![GitHub forks](https://img.shields.io/github/forks/ArsinShaabani/M3FD-YOLO-Converter?style=social)

## ✨ ویژگی‌ها

- **پشتیبانی کامل از M3FD نسخهٔ ۲** - تمام annotations و modalities را مدیریت می‌کند
- **ورودی چندفرمت** - تصاویر PNG و JPG را به‌طورicoon پردازش می‌کند
- **تقسیم خودکار مجموعه داده** - تقسیم ۸۰/۲۰ test/val با تصادفی قابل بازتولید
- **خروجی آماده YOLO** - ساختار دایرکتوری استاندارد و فایل‌های برچسب تولید می‌کند
- **بدون تنظیم** - تنظیم کمینه لازم دارد، فقط به ریشه M3FD اشاره کنید
- **پلتفرم متقابل** - بر روی Windows، Linux و macOS کار می‌کند

## 📁 ساختار مورد نیاز مجموعه داده

مجموعه دادهٔ M3FD شما باید دقیقاً به صورت زیر سازماندهی شود:

```
M3FD/
├── Annotation/
│   ├── *.xml (annotations فرمت Pascal VOC)
├── Vis/
│   ├── *.png یا *.jpg (عکس‌های طیف مصنوعی visibles)
└── ir/
    ├── *.png یا *.jpg (عکس‌های طیف مادون قرمز)
```

## 🚀 نصب

1. **Clone مخزن**
    ```bash
    git clone https://github.com/ArsinShaabani/M3FD-YOLO-Converter
    cd M3FD-YOLO-Converter
    ```

2. **نصب وابسته‌ها** (توصیه می‌شود در محیط مجازی)
    ```bash
    pip install -r requirements.txt
    ```

3. **مسیر مجموعه داده را تنظیم کنید**
    فایل `scripts/xml2yolo_m3fd.py` را ویرایش و مقدار زیر را تنظیم کنید:
    ```python
    ROOT = r"C:\path\to\your\M3FD"  # به مسیر ریشه M3FD خودتان بروز کنید
    ```

## 🔧 استفاده

اسکریپت تبدیل را اجرا کنید:
```bash
python scripts/xml2yolo_m3fd.py
```

### ساختار خروجی
تبدیل‌کننده یک دایرکتوری `M3FD_yolo` با ساختار زیر ایجاد می‌کند:
```
M3FD_yolo/
├── images/
│   ├── train/   (۸۰٪ از عکس‌ها)
│   └── val/     (۲۰٪ از عکس‌ها)
└── labels/
    ├── train/   (فایل‌های .txt قالب YOLO)
    └── val/     (فایل‌های .txt قالب YOLO)
```

هر فایل برچسب حاوی مختصات نرمالisierten باکس‌های محصور در قالب YOLO است:
```
<class_id> <x_center> <y_center> <width> <height>
```
تمام مقادیر به نسبت [۰، ۱] نسبت به ابعاد تصویر نرمال‌شده‌اند.

## 📊 بصری‌سازی مجموعه داده

نمونهای تبدیل‌شده را با دفترچهٔ Jupyter見てی探索 کنید:
```bash
jupyter notebook notebooks/visualize_samples.ipynb
```
دفترچهٔ notebooks موارد زیر را نمایش می‌دهد:
- جفت‌های عکس VIS/IR به سمت هم
- باکس‌های محصور لایه‌دار شده
- آمار توزیع کلاس‌ها
- نمونه‌های افزایش داده

## 🏋️‍♂️ آموزش YOLOv8

مدل خود را با استفاده از کانفیگ تولید شده آموزش دهید:
```bash
yolo train model=yolov8n.pt data=configs/M3FD.yaml epochs=50 imgsz=640
```
فایل `configs/M3FD.yaml` به‌طور خودکار برای اشاره به مجموعه دادهٔ تبدیل‌شده شما تنظیم می‌شود.

## 📝 مجوز

این پروژه تحت مجوز MIT licencia است - برای جزئیات فایل [LICENSE](LICENSE) را ببینید.

## 🤝 مشارکت

مشارکت‌ها خوش‌آمد هستند! لطفاً بحرية یک Pull Request ارسال کنید.

1. Fork مخزن
2. شاخهٔ ویژگی خود را ایجاد کنید (`git checkout -b feature/AmazingFeature`)
3. تغییرات خود را 커밋 کنید (`git commit -m 'Add some AmazingFeature'`)
4. به شاخه خود Push کنید (`git push origin feature/AmazingFeature`)
5. یک Pull Request باز کنید

## 📧 تماس

Arsin Shaabani - [@ArsinShaabani](https://twitter.com/Arsin_Shaabani)

لینک پروژه: [https://github.com/ArsinShaabani/M3FD-YOLO-Converter](https://github.com/ArsinShaabani/M3FD-YOLO-Converter)

## 🙏 تشکر

- [مجموعه دادهٔ M3FD](https://github.com/zjhmale/M3FD) برای ارائه مجموعه دادهٔ چندспектري حرارتی
- [مجموعه دادهٔ M3FD در Kaggle](https://www.kaggle.com/datasets/nus1998/m3fd-dataset) برای دسترسی جایگزین به داده
- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics) برای چارچوب عالی تشخیص اشیا