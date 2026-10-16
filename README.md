<div align="center">

# ⚡ PYTHON CUSTOM SOCKET WEB SERVER ⚡

<img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=4,11,20&height=120&section=header&text=RAW%20SOCKETS%20&%20HTTP%20SERVER&fontSize=32&fontColor=00ff66&animation=fadeIn" width="100%"/>

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Networking](https://img.shields.io/badge/Architecture-TCP%2FIP%20Sockets-orange.svg?style=for-the-badge)]()
[![Status](https://img.shields.io/badge/Status-Active%20Development-success.svg?style=for-the-badge)]()
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)]()

*A high-performance, lightweight custom HTTP web server and routing engine built entirely from scratch using raw Python sockets.*

</div>

---

## 🚀 About The Project

**Sockets** is a low-level backend engineering project that bypasses heavy web frameworks (like Flask or Django) to implement a custom HTTP server directly on top of Python's raw TCP socket primitives. It parses raw incoming HTTP requests, dispatches routes via a modular controller layer, and serves responsive HTML pages.

---

## 🛠️ Architecture & Project Structure

The project follows a clean, modular separation of network transport, routing logic, and presentation:

```text
Sockets/
├── Server.py     # Core TCP socket listener, connection loop & HTTP request parser
├── views.py      # Endpoint controllers and route response logic
├── index.html    # Home page frontend template
└── blog.html     # Blog page frontend template
