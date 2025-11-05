import tkinter as tk
from tkinter import ttk, messagebox

# --- 1. Data Model ---
# Dictionary structure:
# { "Name": [ID, Coursework_Total, Exam_Mark] }
students_data = {
    "Ava Williams": [1001, 45, 70],
    "Liam Thompson": [1002, 39, 60],
    "Sophia Brown": [1003, 54, 80],
    "Noah Wilson": [1004, 33, 50],
    "Mia Garcia": [1005, 39, 65],
    "James Lee": [1006, 48, 75],
    "Isabella Scott": [1007, 42, 68],
    "Mason Harris": [1008, 45, 72],
    "Lily Adams": [1009, 38, 58],
    "Ethan Moore": [1010, 51, 78],
}

# Define the maximum possible scores (used for percentage calculation)
MAX_COURSEWORK = 60
MAX_EXAM = 100
MAX_TOTAL = MAX_COURSEWORK + MAX_EXAM # 160

# --- 2. Helper Functions ---

def calculate_grade(percentage):
    """Calculates a letter grade based on the overall percentage."""
    if percentage >= 70:
        return 'A'
    elif percentage >= 60:
        return 'B'
    elif percentage >= 50:
        return 'C'
    elif percentage >= 40:
        return 'D'
    else:
        return 'F'

def get_full_record(name, data_list):
    """Calculates and returns a formatted string of all student details."""
    student_id, cw_total, exam_mark = data_list
    
    total_score = cw_total + exam_mark
    overall_percentage = (total_score / MAX_TOTAL) * 100
    grade = calculate_grade(overall_percentage)
    
    return (
        f"Name: {name}\n"
        f"Number: {student_id}\n"
        f"Coursework Total: {cw_total}\n"
        f"Exam Mark: {exam_mark}\n"
        f"Overall Percentage: {overall_percentage:.2f}%\n"
        f"Grade: {grade}"
    )

# --- 3. Controller Functions ---

def view_all_records():
    """Displays all student records with full details."""
    text_area.delete("1.0", tk.END)
    text_area.insert(tk.END, "--- All Student Records ---\n\n")
    
    for name, data_list in students_data.items():
        record_string = get_full_record(name, data_list)
        text_area.insert(tk.END, record_string + "\n\n")
        
def find_extreme_score(is_highest=True):
    """Finds and displays either the highest or lowest scoring student."""
    text_area.delete("1.0", tk.END)
    
    # Calculate total scores for comparison
    total_scores = {}
    for name, data_list in students_data.items():
        total_scores[name] = data_list[1] + data_list[2] # CW + Exam
        
    if not total_scores:
        text_area.insert(tk.END, "No student data available.")
        return
        
    # Find the name corresponding to the max/min total score
    if is_highest:
        title = "Highest Score"
        extreme_name = max(total_scores, key=total_scores.get)
    else:
        title = "Lowest Score"
        extreme_name = min(total_scores, key=total_scores.get)

    text_area.insert(tk.END, f"--- {title} ---\n\n")
    record_string = get_full_record(extreme_name, students_data[extreme_name])
    text_area.insert(tk.END, record_string)

def show_highest_score():
    find_extreme_score(is_highest=True)

def show_lowest_score():
    find_extreme_score(is_highest=False)

def view_individual_record():
    """Displays the full record for the selected student."""
    selected_name = student_dropdown.get()
    text_area.delete("1.0", tk.END)
    
    if selected_name in students_data:
        text_area.insert(tk.END, f"--- Individual Record ---\n\n")
        record_string = get_full_record(selected_name, students_data[selected_name])
        text_area.insert(tk.END, record_string)
    else:
        messagebox.showwarning("Not Found", "Please select a valid student.")


# --- 4. GUI Setup (The View) ---

# Main window
root = tk.Tk()
root.title("Student Manager")
root.geometry("600x600")
root.configure(bg="#1c7740")

# --- Title ---
tk.Label(root, text="Student Manager", font=("Arial", 20, "bold"), bg="#ffffff").pack(pady=20)

# --- Top Button Frame (Row 1) ---
button_frame_top = tk.Frame(root, bg="#EFF174")
button_frame_top.pack(pady=10)

tk.Button(button_frame_top, text="View All Student Records", command=view_all_records).pack(side=tk.LEFT, padx=10)
tk.Button(button_frame_top, text="Show Highest Score", command=show_highest_score).pack(side=tk.LEFT, padx=10)
tk.Button(button_frame_top, text="Show Lowest Score", command=show_lowest_score).pack(side=tk.LEFT, padx=10)

# --- Individual View Frame (Row 2) ---
view_frame = tk.Frame(root, bg="#EFF174")
view_frame.pack(pady=15)

tk.Label(view_frame, text="View Individual Student Record:", bg="#EFF174", font=("Arial", 10)).pack(side=tk.LEFT, padx=5)

# Dropdown (Combobox)
student_names = sorted(list(students_data.keys()))
student_var = tk.StringVar() 
student_dropdown = ttk.Combobox(view_frame, textvariable=student_var, values=student_names, state="readonly", width=20)
student_dropdown.pack(side=tk.LEFT, padx=5)

tk.Button(view_frame, text="View Record", command=view_individual_record).pack(side=tk.LEFT, padx=10)

# --- Text Area (Display Box) ---
text_area = tk.Text(root, height=18, width=70, font=("Arial", 11), padx=10, pady=10)
text_area.pack(pady=20, padx=20)

# --- Start the Main Loop ---
root.mainloop()