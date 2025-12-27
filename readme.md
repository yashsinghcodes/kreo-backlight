# Kreo Swarm Keyboard Backlight Control (macOS / Linux)

This project provides a proof-of-concept implementation for controlling the backlight of the **Kreo Swarm keyboard** on **macOS** and **Linux** by directly communicating with the device over USB HID. The implementation is based on reverse engineering the keyboard’s proprietary lighting protocol, which is normally accessible only through the official Windows software.

At its current stage, the project supports sending a **static lighting configuration** by replaying a captured HID Feature Report.

---

## Project Status

### Current capabilities
- Works on macOS and Linux
- Communicates directly with the keyboard using USB HID Feature Reports
- Controls backlight on the Kreo Swarm keyboard
- Does not require the official Windows software or drivers
- Sends a static, pre-captured lighting payload

### Not yet implemented
- Dynamic color changes
- Brightness control
- Lighting effects (wave, breathing, etc.)
- Per-key or per-zone customization
- Bluetooth mode support (USB only)

---

## Technical Overview

- The Kreo Swarm keyboard exposes a vendor-defined HID interface.
- Backlight configuration is applied using a HID `SET_REPORT` request.
- Feature Report ID: `0x06`
- Payload size: `520` bytes
- The current implementation replays an exact payload captured from the official Windows application.

Because this uses standard HID mechanisms, the same payload format is valid across Windows, macOS, and Linux.

---

## Device Information

- Keyboard model: Kreo Swarm
- Vendor ID (VID): `0x258A`
- Product ID (PID): `0x010C`
- HID usage page: `0xFF00` (vendor-defined)
- HID interface number: `1`

---
