import tkinter as tk
from tkinter import messagebox
import pandas as pd
from datetime import datetime

# Data storage
data_file = 'attendance_data.csv'

# Function to save the data
def save_data():
    # Get input values
    employee_id = entry_employee_id.get()
    employee_name = entry_employee_name.get()
    work_date = entry_date.get()
    scheduled_hours = float(entry_scheduled_hours.get())
    actual_hours = float(entry_actual_hours.get())
    day_type = combo_day_type.get()

    # Validate the input
    if not employee_id or not employee_name or not work_date or not scheduled_hours or not actual_hours or not day_type:
        messagebox.showerror("Input Error", "Please fill all fields correctly.")
        return

    # Calculate overtime
    overtime_hours = max(0, actual_hours - scheduled_hours)

    if day_type == "Sunday":
        overtime_type = overtime_hours * 2  # Sunday overtime
    else:
        overtime_type = overtime_hours  # Normal overtime

    # Prepare data to save
    data = {
        "Employee ID": [employee_id],
        "Employee Name": [employee_name],
        "Date": [work_date],
        "Scheduled Work Hours": [scheduled_hours],
        "Actual Work Hours": [actual_hours],
        "Overtime Hours": [overtime_hours],
        "Overtime Type": [overtime_type],
        "Sunday Hours": [actual_hours if day_type == "Sunday" else 0],
        "Normal Workday Hours": [actual_hours if day_type != "Sunday" else 0]
    }

    # Create a DataFrame
    df = pd.DataFrame(data)

    # Check if file exists, if not create a new one with headers
    try:
        df_existing = pd.read_csv(data_file)
        df_existing = df_existing.append(df, ignore_index=True)
        df_existing.to_csv(data_file, index=False)
    except FileNotFoundError:
        df.to_csv(data_file, index=False)

    # Clear input fields after saving
    entry_employee_id.delete(0, tk.END)
    entry_employee_name.delete(0, tk.END)
    entry_date.delete(0, tk.END)
    entry_scheduled_hours.delete(0, tk.END)
    entry_actual_hours.delete(0, tk.END)

    # Display success message
    messagebox.showinfo("Success", "Data saved successfully!")

# Create the main window
root = tk.Tk()
root.title("Employee Attendance and Overtime")

# Create labels and entry widgets
label_employee_id = tk.Label(root, text="Employee ID:")
label_employee_id.grid(row=0, column=0, padx=10, pady=5, sticky="e")

entry_employee_id = tk.Entry(root)
entry_employee_id.grid(row=0, column=1, padx=10, pady=5)

label_employee_name = tk.Label(root, text="Employee Name:")
label_employee_name.grid(row=1, column=0, padx=10, pady=5, sticky="e")

entry_employee_name = tk.Entry(root)
entry_employee_name.grid(row=1, column=1, padx=10, pady=5)

label_date = tk.Label(root, text="Date (YYYY-MM-DD):")
label_date.grid(row=2, column=0, padx=10, pady=5, sticky="e")

entry_date = tk.Entry(root)
entry_date.grid(row=2, column=1, padx=10, pady=5)

label_scheduled_hours = tk.Label(root, text="Scheduled Work Hours:")
label_scheduled_hours.grid(row=3, column=0, padx=10, pady=5, sticky="e")

entry_scheduled_hours = tk.Entry(root)
entry_scheduled_hours.grid(row=3, column=1, padx=10, pady=5)

label_actual_hours = tk.Label(root, text="Actual Work Hours:")
label_actual_hours.grid(row=4, column=0, padx=10, pady=5, sticky="e")

entry_actual_hours = tk.Entry(root)
entry_actual_hours.grid(row=4, column=1, padx=10, pady=5)

label_day_type = tk.Label(root, text="Day Type:")
label_day_type.grid(row=5, column=0, padx=10, pady=5, sticky="e")

# Dropdown for day type
day_types = ["Normal", "Sunday"]
combo_day_type = tk.StringVar(root)
combo_day_type.set(day_types[0])  # default to "Normal"
dropdown_day_type = tk.OptionMenu(root, combo_day_type, *day_types)
dropdown_day_type.grid(row=5, column=1, padx=10, pady=5)

# Save button
save_button = tk.Button(root, text="Save", command=save_data)
save_button.grid(row=6, column=0, columnspan=2, pady=20)

# Start the GUI
root.mainloop()
