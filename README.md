# Data Analysis using Pandas

This Python script provides an interactive tool for performing basic analytical tasks on the Iris dataset or any other CSV dataset containing numerical values. The tool is built using Python and the Pandas, NumPy, and Matplotlib libraries.

---

## Features

1. **Data Exploration**:
   - View the entire dataset or information about the dataset loaded into the DataFrame.

2. **Mathematical Operations**:
   - Calculate **Mean**, **Median**, **Mode**, and **Sum** for a specified column.

3. **Graphical Visualizations**:
   - Line Graph
   - Scatter Plot
   - Bar Plot
   - Histogram
   - Pie Chart

4. **Interactive Menu**:
   - Navigate between different features with an intuitive menu system.

---

## Prerequisites

### Libraries:
Ensure you have the following Python libraries installed:
- **Pandas**
- **NumPy**
- **Matplotlib**
- **Seaborn**

You can install them using pip:

```bash
pip install -r requirements.txt
```

### Dataset:

- Place the dataset `Iris - all-numbers.csv` in the same directory as the script or update the `data_path` variable with the correct path.

---

## Usage Instructions

1. Clone the repository or download the script.
2. Ensure the dataset `Iris - all-numbers.csv` is in the correct location.
3. Run the script:

   ```bash
   python main.py
   ```
   
5. Follow the interactive menu to perform various operations:
   - **Math Operations**: Enter column names to calculate statistics.
   - **Graphical Visualizations**: Enter X and Y columns to plot graphs.

---

## File Structure

```
project/
├── main.py                  # Main script file
├── Iris - all-numbers.csv   # Dataset file
```

---

## Sample Dataset

The script is designed for numerical datasets like the Iris dataset. Ensure the dataset has meaningful numerical columns to perform calculations and visualizations effectively.

---

## Notes
- Ensure valid column names are provided as inputs to avoid errors.
- Pie charts are based on value counts of a single column.

---


Feel free to contribute and enhance this project!
