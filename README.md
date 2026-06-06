# M3FD YOLO Converter

Convert the M3FD Multispectral Dataset (Version 2) into YOLO-compatible format with automatic train/val splitting and clean label generation.

![GitHub](https://img.shields.io/github/license/ArsinShaabani/M3FD-YOLO-Converter)
![GitHub stars](https://img.shields.io/github/stars/ArsinShaabani/M3FD-YOLO-Converter?style=social)
![GitHub forks](https://img.shields.io/github/forks/ArsinShaabani/M3FD-YOLO-Converter?style=social)

## ✨ Features

- **Full M3FD Version 2 Support** - Handles all annotations and modalities
- **Multi-format Input** - Processes both PNG and JPG images seamlessly
- **Automatic Dataset Splitting** - 80/20 train/validation split with reproducible randomization
- **YOLO-Ready Output** - Generates standardized directory structure and label files
- **Zero Configuration** - Minimal setup required, just point to your M3FD root
- **Cross-platform** - Works on Windows, Linux, and macOS

## 📁 Required Dataset Structure

Your M3FD dataset must be organized exactly as follows:

```
M3FD/
├── Annotation/
│   ├── *.xml (Pascal VOC format annotations)
├── Vis/
│   ├── *.png or *.jpg (Visible spectrum images)
└── ir/
    ├── *.png or *.jpg (Infrared spectrum images)
```

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ArsinShaabani/M3FD-YOLO-Converter
   cd M3FD-YOLO-Converter
   ```

3. **Configure dataset path**
   Edit `scripts/xml2yolo_m3fd.py` and set:
   ```python
   ROOT = r"C:\path\to\your\M3FD"  # Update to your M3FD root directory
   ```

## 🔧 Usage

Run the conversion script:
```bash
python scripts/xml2yolo_m3fd.py
```

### Output Structure
The converter creates a `M3FD_yolo` directory with:
```
M3FD_yolo/
├── images/
│   ├── train/   (80% of images)
│   └── val/     (20% of images)
└── labels/
    ├── train/   (YOLO format .txt files)
    └── val/     (YOLO format .txt files)
```

Each label file contains normalized bounding box coordinates in YOLO format:
```
<class_id> <x_center> <y_center> <width> <height>
```
All values are normalized to [0, 1] relative to image dimensions.

## 📊 Dataset Visualization

Explore converted samples with our Jupyter notebook:
```bash
jupyter notebook notebooks/visualize_samples.ipynb
```
The notebook displays:
- Side-by-side VIS/IR image pairs
- Overlaid bounding boxes
- Class distribution statistics
- Sample augmentation examples

## 🏋️‍♂️ YOLOv8 Training

Train your model using the generated configuration:
```bash
yolo train model=yolov8n.pt data=configs/M3FD.yaml epochs=50 imgsz=640
```

The `configs/M3FD.yaml` file is automatically configured to point to your converted dataset.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📧 Contact

Arsin Shaabani - [@ArsinShaabani](https://twitter.com/Arsin_Shaabani)

Project Link: [https://github.com/ArsinShaabani/M3FD-YOLO-Converter](https://github.com/ArsinShaabani/M3FD-YOLO-Converter)

## 🙏 Acknowledgments


- [M3FD Dataset on Kaggle](https://www.kaggle.com/datasets/nus1998/m3fd-dataset) for alternative dataset access
- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics) for the excellent object detection framework