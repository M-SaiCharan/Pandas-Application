import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
import seaborn as sns

data_path = r"Iris - all-numbers.csv"
df = pd.read_csv(data_path)

def menu():
    print("\nPandas-Application")
    print("\033[38;5;250m\n\t 1. Math Operations \n\t 2. Graph \n\t 3. print \n\t 4. Exit\n\033[0m")
    choice = input("Enter your choice: ")
    while choice != "4":
        if choice == "1":
            math_operations()
        elif choice == '2':
            graph()
        elif choice == '3':
            printdf()
    print("\nLeaving the Program!\n")
    sys.exit()


def printdf():
    print("\nPrint Options: \n")
    print("\033[38;5;250m\t 1. Entire DataFrame \n\t 2. First 5 rows \n\t 3. Last 5 rows \n\t 4. Shape of the DataFrame \n\t 5. Columns of the DataFrame \n\t 6. Prev Menu\n\033[0m")
    choice = int(input("Enter your choice: "))
    print("\n")
    if choice == 1:
        print(df)
    elif choice == 2:
        print(df.head(5))
    elif choice == 3:
        print(df.tail(5))
    elif choice == 4:
        print(df.shape)
    elif choice == 5:
        print(df.columns)
    elif choice == 6:
        menu()
    else:
        print("Invalid choice\n")
        printdf()

def math_operations():
    print("\nMATH OPERATIONS")
    print('\033[38;5;250m\n\t 1.Mean\n\t 2.Median\n\t 3.Mode \n\t 4.Sum\n\t 5.Prev Menu\033[0m')
    choice = int(input('\nEnter your choice: '))

    if choice == 1:
        opt_col = input(str("Enter the col: "))
        if opt_col in df.columns:
            mean = df[opt_col].mean()
            print(f"\nThe mean of the {opt_col}: \033[32m{mean}\033[0m")
        else:
            print(f"\nThe column {opt_col} does not exist in the dataframe")
        math_operations()
    
    elif choice == 2:
        opt_col = input(str("Enter the col: "))
        if opt_col in df.columns:
            median = df[opt_col].median()
            print(f"\nThe median of the {opt_col}: \033[32m{median}\033[0m")
        else:
            print(f"\nThe column {opt_col} does not exist in the dataframe")
        math_operations()

    elif choice == 3:
        opt_col = input(str("Enter the col: "))
        if opt_col in df.columns:
            mode = df[opt_col].mode()
            print(f"\nThe mode of the {opt_col}: \033[32m{mode}\033[0m")
        else:
            print(f"\nThe column {opt_col} does not exist in the dataframe")
        math_operations()

    elif choice == 4:
        opt_col = input(str("Enter the col: "))
        if opt_col in df.columns:
            col_sum = df[opt_col].sum()
            print(f"\nThe sum of the {opt_col}: \033[32m{col_sum}\033[0m")
        else:
            print(f"\nThe column {opt_col} does not exist in the dataframe")
        math_operations()

    elif choice == 5:
        menu()
    
    else:
        print("Invalid choice")
        math_operations()


def graph():
    print("\nGRAPH OPERATIONS")
    print("\nEnter the graph type:\n")
    print("\033[38;5;250m\t 1. Line Graph \n\t 2. Scatter Plot \n\t 3. Bar Plot \n\t 4. Histogram \n\t 5. Pie Chart \n\t 6. Heat Map \n\t 7. Prev Menu\n\033[0m")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        x_col, y_col = col_selection(1)
        if validate_columns([x_col, y_col]):
            plt.plot(df[x_col], df[y_col])
            plt.xlabel(x_col)
            plt.ylabel(y_col)
            plt.title("Line Graph")
            plt.show()
    
    elif choice == 2:
        x_col, y_col = col_selection(1)
        if validate_columns([x_col, y_col]):
            plt.scatter(df[x_col], df[y_col])
            plt.xlabel(x_col)
            plt.ylabel(y_col)
            plt.title("Scatter Plot")
            plt.show()

    elif choice == 3:
        x_col, y_col = col_selection(1)
        if validate_columns([x_col, y_col]):
            plt.bar(df[x_col], df[y_col])
            plt.xlabel(x_col)
            plt.ylabel(y_col)
            plt.title("Bar Plot")
            plt.show()
    
    elif choice == 4:
        col = col_selection(0)
        if validate_columns([col]):
            plt.hist(df[col], bins=10, color='blue', edgecolor='black')
            plt.xlabel(col)
            plt.ylabel("Frequency")
            plt.title("Histogram")
            plt.show()

    elif choice == 5:
        col = col_selection(0)
        if validate_columns([col]):
            data = df[col].value_counts()
            plt.pie(data, labels=data.index, autopct='%1.1f%%', startangle=140)
            plt.title("Pie Chart")
            plt.show()

    elif choice == 6:
        plt.figure(figsize=(10, 8))
        correlation_matrix = df.corr()  # Calculate the correlation matrix
        sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', square=True, cbar=True)
        plt.title("Heat Map of Correlation Matrix")
        plt.show()

    elif choice == 7:
        menu()

    else:
        print("Invalid choice")
        graph()

def col_selection(n):
    if n == 1:
        x_col = input("Enter the X column: ")
        y_col = input("Enter the Y column: ")
        return x_col, y_col
    elif n == 0:
        col = input("Enter the column: ")
        return col

def validate_columns(columns):
    for col in columns:
        if col not in df.columns:
            print(f"The column '{col}' does not exist in the dataframe.")
            return False
    return True

if __name__ == "__main__":
    menu()
