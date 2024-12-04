import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

print("Creating a DataFrame\n")
#data_path = input("Enter the address: ")
data_path = r"C:\Users\mulag\Downloads\JupyterLab\Data\Iris - all-numbers.csv"
df = pd.read_csv(data_path)

def menu():
    print("**Pandas**")
    print("\n\t 1. Math Operations \n\t 2. Graph \n\t 3. print \n\t 4. Exit\n")
    choice = input("Enter your choice: ")
    while choice != "4":
        if choice == "1":
            math_operations()
        elif choice == '2':
            graph()
        elif choice == '3':
            printdf()
        #elif choice == '4':
        #   sys.exit(0)
    print("\nLeaving the Program!\n")
    sys.exit()
    

def printdf():
    print(df)

def math_operations():
    print("\n**MATH OPERATIONS**")
    print('\n\t 1.Mean\n\t 2.Median\n\t 3.Mode \n\t 4.Sum\n\t 5.Prev Menu')
    choice = int(input('\nEnter your choice: '))

    if choice == 1:
        opt_col = input(str("Enter the col: "))
        if opt_col in df.columns:
            mean = df[opt_col].mean()
            print(f"The mean of the {opt_col}: {mean}")
        else:
            print(f"The column {opt_col} does not exist in the dataframe")
        math_operations()
    
    elif choice == 2:
        opt_col = input(str("Enter the col: "))
        if opt_col in df.columns:
            median = df[opt_col].median()
            print(f"The median of the {opt_col}: {median}")
        else:
            print(f"The column {opt_col} does not exist in the dataframe")
        math_operations()

    elif choice == 3:
        opt_col = input(str("Enter the col: "))
        if opt_col in df.columns:
            mode = df[opt_col].mode()
            print(f"The mode of the {opt_col}: {mode}")
        else:
            print(f"The column {opt_col} does not exist in the dataframe")
        math_operations()

    elif choice == 4:
        opt_col = input(str("Enter the col: "))
        if opt_col in df.columns:
            sum = df[opt_col].sum()
            print(f"The sum of the {opt_col}: {sum}")
        else:
            print(f"The column {opt_col} does not exist in the dataframe")
        math_operations()

    elif choice == 5:
        menu()
    
    else:
        print("Invalid choice")
        math_operations(df)
        

def graph():
    print("\nEnter the graph type:\n")
    print("\t 1.Line Grpah \n\t 2. Scatter plot \n\t 3. Bar plot \n\t 4. Histogram \n\t 5. Pie Chart \n\t 6. Heat Map \n\t 7. Prev Menu\n")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        x_col, y_col = col_selection(1)
        plt.plot(df[x_col], df[y_col])
        plt.show()
    
    elif choice ==  2:
        x_col, y_col = col_selection(1)
        plt.scatter(df[x_col], df[y_col])
        plt.show()

    elif choice == 3:
        x_col, y_col = col_selection(1)
        plt.bar(df[x_col], df[y_col])
        plt.show()
    
    elif choice == 4:
        plt.hist()

def col_selection(n):
    print("\nSelect the column to perform the operation:\n")
    if n == 1:
        x_col = input("Enter the X column: ")
        y_col = input("Enter the Y column: ")
        return x_col, y_col
    if n == 0:
        col = input("Enter the column")
        return col
    

menu()