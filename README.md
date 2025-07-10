# 📊 Graph Assignment

A Python-based number processing project that takes a list of integers and performs **sum**, **multiplication**, **division**, and optional additional steps like **average**, with random number appending based on parity (even/odd). Each operation is modularized into separate files and processed through a pipeline for easy extension.

---

## 📌 Problem Statement

1. **Input**: User enters at least two integers into a list.
2. **Sum Step**:

   * Compute sum of the list.
   * If **even** → proceed to multiplication.
   * If **odd** → append a random number (0–9); repeat up to **3 times** until even.
3. **Product Step**:

   * Compute product of the list.
   * If **even** → proceed to division.
   * If **odd** → append a random number (0–9); repeat up to **3 times** until even.
4. **Division Step**:

   * Perform integer division of the **first element by the last**.
   * If the last number is **0**, raise a `ZeroDivisionError`.
5. **(Optional) Additional Steps**:

   * Any additional step (like average) can easily be added to the pipeline.

---

## 📁 Folder Structure

```
graph_assignment/
├── adder.py         # Handles sum logic and appending if sum is odd
├── multiplier.py    # Handles product logic and appending if product is odd
├── divider.py       # Handles division with zero-check
├── average.py       # Example: Computes average of list (optional step)
├── main.py          # Main script to run the entire process via pipeline
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

* **Windows CMD:**

  ```bash
  venv\Scripts\activate
  ```
* **PowerShell:**

  ```powershell
  .\venv\Scripts\Activate.ps1
  ```
* **macOS/Linux:**

  ```bash
  source venv/bin/activate
  ```

### 4. Run the Program

```bash
python main.py
```

---

## 🔗 Pipeline Feature (How It Works)

The project uses a **pipeline-based design** for easy extensibility:

* Each processing step is a function that takes a list and returns a list.
* You can easily add/remove steps from the pipeline list in `main.py`.

### ➕ How to Add a New Step (Example: Average Calculation)

1. Create a new Python file like `average.py`:

2. Import it in `main.py`:

3. Add it to the pipeline list in `main.py`:

```python
pipeline = [
    ("Sum", process_sum),
    ("Product", process_product),
    ("Division", divide_first_last),
    ("Average", calculate_average),  # New step added here
]
```

That’s it! The new step will automatically run after others in order.

---

* Easy to extend: Simply add a new Python file and plug it into the pipeline.

---
