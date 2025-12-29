# Kreo Swarm RGB Control (HID)

This script directly controls the RGB lighting of the **Kreo Swarm keyboard** by sending **vendor-specific HID feature reports**.
It works by patching the RGB seed inside a known palette payload and then applying a lighting mode payload. Make sure your connected your keyboard via USB.

---

## Requirements

### Hardware
- Kreo Swarm keyboard
- USB HID interface with:
  - VID = 0x258A
  - PID = 0x010C
  - Vendor usage page = 0xFF00
  - Interface number = 1

### Software
- Python 3.8+
- hidapi Python bindings

```bash
pip install hidapi
```

> On Linux, you may need udev rules or root permissions to access HID devices.

---

## Files

- kreo_light.py – Main script to set RGB color and lighting mode
- No external configuration files required

---

## How It Works

1. Opens the vendor HID interface of the keyboard
2. Locates the RGB seed inside a `06 0A` palette feature report
3. Patches the RGB values (R, G, B)
4. Sends the palette payload
5. Sends the mode payload to apply the lighting mode

---

## Usage

```bash
python3 kreo_light.py R G B MODE
```

---

## Arguments

| Argument | Description |
|---------|-------------|
| R | Red value (0–255) |
| G | Green value (0–255) |
| B | Blue value (0–255) |
| MODE | 1-byte hex value controlling lighting mode |

---

## Examples

```bash
python3 kreo_light.py 255 0 0 1
python3 kreo_light.py 0 255 0 1
python3 kreo_light.py 0 0 255 1
python3 kreo_light.py 0 0 0 3
```

---

## MODE Values

MODE is a single hex byte injected directly into the mode feature report.

Common values:
- 01 – Static
- 02 - <TBD>
- 03 - <TBD>
- 04 - <TBD>

Exact behavior depends on keyboard firmware and must be discovered experimentally.

---

## Troubleshooting

### Vendor HID interface not found
- Keyboard not connected
- Incorrect VID or PID
- Insufficient HID permissions
- Try running as root on Linux

### RGB does not change
- Unsupported MODE value
- Different firmware revision
- Try alternative MODE values

---

## Reverse Engineering Notes

- Palette report header: `06 0A 00 00 01 00 00 02`
- RGB seed format: `R G B 00`
- Feature reports are sent using:
```python
h.send_feature_report(...)
```

---

## Disclaimer

This project is for educational and reverse-engineering purposes only.
Not affiliated with Kreo.
Use at your own risk.
