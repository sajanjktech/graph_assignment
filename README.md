# 📊 Graph Assignment

A Python-based number processing project that takes a list of integers and performs **sum**, **multiplication**, and **division**, with random number appending based on parity (even/odd). Each operation is modularized into separate files.

---

## 📌 Problem Statement

1. **Input**: User enters at least two integers into a list.
2. **Sum Step**:
   - Compute sum of the list.
   - If **even** → proceed to multiplication.
   - If **odd** → append a random number (0–9); repeat up to **3 times** until even.
3. **Product Step**:
   - Compute product of the list.
   - If **even** → proceed to division.
   - If **odd** → append a random number (0–9); repeat up to **3 times** until even.
4. **Division Step**:
   - Perform integer division of the **first element by the last**.
   - If the last number is **0**, raise a `ZeroDivisionError`.

---

## 📁 Folder Structure

```
graph_assignment/
├── adder.py         # Handles sum logic and appending if sum is odd
├── multiplier.py    # Handles product logic and appending if product is odd
├── divider.py       # Handles division with zero-check
├── main.py          # Main script to run the entire process
├── .gitignore       # Ignores venv/ and __pycache__/
├── README.md        # This file
└── venv/            # Virtual environment (excluded from Git)
```

---

## 🚀 How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/sajanjktech/graph_assignment.git
cd graph_assignment
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

- **Windows CMD:**
  ```bash
  venv\Scripts\activate
  ```
- **PowerShell:**
  ```powershell
  .\venv\Scripts\Activate.ps1
  ```
- **macOS/Linux:**
  ```bash
  source venv/bin/activate
  ```

### 4. Run the Program

```bash
python main.py
```

---

## 📄 Sample Output

```
Enter at least two integers separated by space: 4 7
Initial list: [4, 7]
Sum of list: 11
Sum is odd. Appending random number: 3
List after appending: [4, 7, 3]
Sum of list: 14
Sum is even. Proceeding to multiplication step.

Final list after sum step: [4, 7, 3]

Product of list: 84
Product is even. Proceeding to division step.

Final list after product step: [4, 7, 3]

List before division: [4, 7, 3]
Final Result (First element / Last element): 1
```

---