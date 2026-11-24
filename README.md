# 🏧 ATM Machine Simulator (Python + Streamlit)

Live_DEMO={live}(https://hr2krmiqqdozypppx4vkwx.streamlit.app/)

A beginner-friendly ATM simulation built with **Python OOP**, available in two versions:

1. **Console version** (Jupyter Notebook / `.ipynb`): uses `input()` and `print()`
2. **Web UI version** (Streamlit / `.py`): the same logic with a simple browser interface

---

## ✨ Features

- 🔐 Create a PIN and set an opening balance
- 🔄 Change PIN (after verifying the old PIN)
- 💰 Check balance (PIN protected)
- 💸 Withdraw money (PIN protected, with insufficient-balance check)
- 🧠 Clean OOP design with a single `ATM` class

---

## 📁 Project Structure

```
├── atm.ipynb              # Console-based ATM (Jupyter / Colab)
├── atm_streamlit_app.py   # Streamlit web UI version
└── README.md
```

---

## 🛠️ Tech Stack

- Python 3
- Streamlit
- Jupyter Notebook (for the console version)

---

## 🚀 How to Run

### 1) Console version (`.ipynb`)

Open `atm.ipynb` in Jupyter Notebook, JupyterLab or Google Colab and run the cells. Follow the on-screen menu:

```
1) Create pin
2) Change pin
3) Check balance
4) Withdrawal
5) Exit
```

### 2) Streamlit version (`.py`)

```bash
# install dependency
pip install streamlit

# run the app
streamlit run atm_streamlit_app.py
```

The app opens in your
