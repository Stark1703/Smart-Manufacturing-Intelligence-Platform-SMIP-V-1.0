# 🚀 Installation Guide

## Prerequisites

Install the following software before using the project:

- Python 3.13+
- Git
- Visual Studio Code (recommended)

Verify Python:

```bash
python --version
```

---

# Clone Repository

```bash
git clone https://github.com/<your-username>/Smart-Manufacturing-Intelligence-Platform-SMIP.git

cd Smart-Manufacturing-Intelligence-Platform-SMIP
```

---

# Create Virtual Environment

Windows

```bash
python -m venv .venv
```

Activate

PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

Command Prompt

```cmd
.venv\Scripts\activate.bat
```

Linux / macOS

```bash
source .venv/bin/activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Verify Installation

```bash
python -m generator.master_data.generate_machine_layout
```

Expected output:

```text
INFO     Starting Machine Layout Generation...
INFO     Machine Layout Generation Completed.
```

---

# Python Packages

Current dependencies include:

- pandas
- numpy
- python-dateutil

Additional packages may be added as the project evolves.