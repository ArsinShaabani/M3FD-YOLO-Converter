# xml2yolo_m3fd.py
# Converts M3FD (version 2) dataset to YOLO format
# Supports PNG and JPG


import os
import shutil
import xml.etree.ElementTree as ET
import random

# مسیر دیتاست نسخه 2
ROOT = r"C:\Users\Mohammadreza\Desktop\deep_learning\nav_yolo_m3fd\data\M3FD"

ANNOT = os.path.join(ROOT, "Annotation")
VIS = os.path.join(ROOT, "VIS")

# مسیر خروجی YOLO
OUT = r"C:\Users\Mohammadreza\Desktop\deep_learning\nav_yolo_m3fd\data\M3FD_yolo"

os.makedirs(f"{OUT}/images/train", exist_ok=True)
os.makedirs(f"{OUT}/images/val", exist_ok=True)
os.makedirs(f"{OUT}/labels/train", exist_ok=True)
os.makedirs(f"{OUT}/labels/val", exist_ok=True)

# کلاس‌ها
CLASSES = ["People", "Car", "Bus", "Motorcycle", "Lamp", "Truck"]
class_to_id = {c: i for i, c in enumerate(CLASSES)}

def convert_bbox(size, box):
    w, h = size
    xmin, ymin, xmax, ymax = box

    x_center = (xmin + xmax) / 2.0 / w
    y_center = (ymin + ymax) / 2.0 / h
    bw = (xmax - xmin) / w
    bh = (ymax - ymin) / h

    return x_center, y_center, bw, bh

def process_xml(xml_path, out_label_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()

    size = root.find("size")
    w = int(size.find("width").text)
    h = int(size.find("height").text)

    lines = []

    for obj in root.findall("object"):
        cls = obj.find("name").text
        if cls not in class_to_id:
            continue

        cls_id = class_to_id[cls]

        bbox = obj.find("bndbox")
        xmin = int(bbox.find("xmin").text)
        ymin = int(bbox.find("ymin").text)
        xmax = int(bbox.find("xmax").text)
        ymax = int(bbox.find("ymax").text)

        x, y, bw, bh = convert_bbox((w, h), (xmin, ymin, xmax, ymax))
        lines.append(f"{cls_id} {x} {y} {bw} {bh}")

    with open(out_label_path, "w") as f:
        f.write("\n".join(lines))

def walk_dataset():
    for file in os.listdir(ANNOT):
        if file.endswith(".xml"):
            xml_path = os.path.join(ANNOT, file)

            base = file.replace(".xml", "")

            # پشتیبانی از PNG , JPG
            img_png = os.path.join(VIS, base + ".png")
            img_jpg = os.path.join(VIS, base + ".jpg")

            if os.path.exists(img_png):
                img_path = img_png
                img_name = base + ".png"
            elif os.path.exists(img_jpg):
                img_path = img_jpg
                img_name = base + ".jpg"
            else:
                print("Image not found for:", base)
                continue

            # 80% train - 20% val
            is_train = random.random() < 0.8

            if is_train:
                out_img = f"{OUT}/images/train/{img_name}"
                out_lbl = f"{OUT}/labels/train/{base}.txt"
            else:
                out_img = f"{OUT}/images/val/{img_name}"
                out_lbl = f"{OUT}/labels/val/{base}.txt"

            shutil.copy(img_path, out_img)
            process_xml(xml_path, out_lbl)

walk_dataset()
print("DONE: YOLO dataset created successfully!")
