# Euclidean Distance Calculator 🧮

This Python script calculates the **minimum Euclidean distance** between a set of 2D points.

#### Created as second week assignment of Kodluyoruz - IBM Cyberstart

## 📋 Description

The script defines a list of points and computes the Euclidean distance between each unique pair of points. It then finds and prints the **minimum distance** from the calculated distances.

## 🛠️ How It Works

1. **Points Definition:**
   - A list of 2D points is predefined.
2. **Distance Calculation:**

   - For each unique pair of points, the script calculates the **Euclidean distance** using the formula:

   ```scss
   distance = √((x1 - x0)² + (y1 - y0)²)
   ```

3. **Minimum Distance:**
   - The script finds the smallest distance from all the calculated distances and prints it.

## 🚀 How to Run

1. Ensure you have **Python** installed.
2. Copy the script into a `.py` file.
3. Run the script using:
   ```bash
   python script_name.py
   ```

## 🎯 Example Output

```bash
Minimum distance: 1.0
```

## 🔧 Requirements

- **Python 3.x**
- **math** module (comes with Python by default)
