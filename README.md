# 25 Modern GUI Tutorial

This repository accompanies the **25 Modern GUI Tutorial**, providing a complete project structure for PySide6 / PyQt / Qt-based applications.
It includes custom widgets, automatic UI-to-Python conversion, style management, and a clean, scalable architecture suitable for modern desktop applications.

---

## Project Structure

```
.
├── README.md                # Description of the project
├── requirements.txt         # Python dependencies
├── main.py                  # Entry point of the application
│
├── ui/                      # UI design files
│   ├── main_window.ui       # Main window layout
│   └── ...other UI files
│
├── src/                     # Application source code
│   ├── __init__.py
│   ├── utils.py             # Utility functions
│   ├── helper_functions.py  # Additional helpers
│   ├── ui_main_window.py    # Auto-generated Python from main_window.ui
│   └── ...more modules
│
├── qss/                     # Style sheets and assets
│   ├── scss/                # SCSS source files
│   └── icons/               # Application icons
│
├── logs/
│   └── custom_widgets.log   # Log file
│
├── json_styles/             # JSON style definitions
│   └── style.json
│
└── generated-files/         # Auto-generated output
    ├── Converted UI Python files
    └── Generated JSON configurations
```

---

## Overview

This structure is designed to support modern GUI development by:

* Automatically converting `.ui` files into Python modules
* Keeping UI files, generated files, and source code organized
* Managing styles using SCSS, QSS, and JSON layers
* Providing a clean architecture for large-scale GUI applications

The goal is to simplify GUI development for both beginners and advanced developers, making the tutorial easy to follow and extend.

---

## Support and Full Source Code

Full project source code, extended materials, and additional lessons are available to supporters.

To access the complete source code and support the development of future tutorials:

Patreon:
[https://www.patreon.com/c/spinntv](https://www.patreon.com/c/spinntv)

Your support directly helps maintain and expand this project and future GUI tutorials.

---

## Repository

For updates and the main custom widgets module:

[https://github.com/SpinnCompanyu/QT-PyQt-PySide-Custom-Widgets](https://github.com/SpinnCompanyu/QT-PyQt-PySide-Custom-Widgets)

