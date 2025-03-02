# Secure Data Hiding in Image Using Steganography

## Introduction
This project implements **secure data hiding** in images using **Least Significant Bit (LSB) steganography** combined with **AES-based encryption**. It allows users to hide sensitive messages inside images and later extract them securely.

## Features
✅ **LSB Steganography** – Hides data in the least significant bits of image pixels.
✅ **AES-Based Encryption** – Secures messages before embedding.
✅ **End Marker for Extraction** – Prevents data corruption.
✅ **Minimal Image Distortion** – Ensures image quality is preserved.
✅ **CLI-Based Interface** – Simple to use via the command line.
✅ **Cross-Platform** – Works on Windows, Linux, and macOS.

## Technologies Used
- **Programming Language:** Python 🐍
- **Libraries:**
  - `opencv-python` – Image processing
  - `cryptography` – Message encryption (AES-based)
  - `numpy` – Array manipulation
  - `PIL (Pillow)` – Image handling

## Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/steganography-project.git
   cd steganography-project
   ```
2. **Install dependencies**:
   ```bash
   pip install opencv-python cryptography numpy pillow
   ```
3. **Run the script**:
   ```bash
   python steganography.py
   ```

## Usage
### 1️⃣ Hide a Message
- Run the script and select `1` (Hide Data).
- Enter the image path, secret message, and output filename.
- The encrypted message is embedded into the image.

### 2️⃣ Extract a Message
- Run the script and select `2` (Extract Data).
- Enter the encoded image path.
- The message is extracted and decrypted.

## Example Screenshots
📷 **Before & After Image Comparison**
📷 **Extracted Message Output**

## Future Enhancements
- ✅ **GUI Application** for easy use
- ✅ **Support for Video & Audio Steganography**
- ✅ **AI-Powered Steganalysis Resistance**
- ✅ **Cloud & Blockchain Integration**

## Contributors
👤 **Your Name** – Developer

## License
📜 MIT License – Free to modify and distribute.

---
🚀 **Feel free to contribute, enhance, and share your feedback!**

