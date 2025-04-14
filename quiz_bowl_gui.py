import tkinter as tk
from tkinter import messagebox, simpledialog, scrolledtext

# Full set of questions for each subject
questions = {
    "Accounting": [
        {"question": "What is the accounting equation?", "options": ["Assets + Liabilities = Owners Equity", "Liabilities + Owners Equity = Assets", "Owners’ Equity – Assets = Liabilities", "Liabilities x Owners Equity + Assets"], "correct_answer": "Assets + Liabilities = Owners Equity"},
        {"question": "Which of the following is an asset?", "options": ["Cash", "Accounts Payable", "Capital Stock", "Revenue"], "correct_answer": "Cash"},
        {"question": "What is the purpose of a balance sheet?", "options": ["To show revenue", "To show financial position at a point in time", "To show cash flow", "To show expenses"], "correct_answer": "To show financial position at a point in time"},
        {"question": "What is depreciation?", "options": ["Increase in asset value", "Decrease in asset value", "Cash inflow", "Cash outflow"], "correct_answer": "Decrease in asset value"},
        {"question": "What is the first step in the accounting cycle?", "options": ["Journalizing", "Posting", "Analyzing transactions", "Preparing financial statements"], "correct_answer": "Analyzing transactions"},
        {"question": "What are liabilities?", "options": ["Assets", "Owners' equity", "Debts owed by a business", "Revenues"], "correct_answer": "Debts owed by a business"},
        {"question": "What is the purpose of a trial balance?", "options": ["To show profitability", "To verify debits equal credits", "To show cash flow", "To show expenses"], "correct_answer": "To verify debits equal credits"},
        {"question": "What is the formula for net income?", "options": ["Revenue - Expenses", "Assets - Liabilities", "Assets + Liabilities", "Revenue + Expenses"], "correct_answer": "Revenue - Expenses"},
        {"question": "What is the cost of goods sold?", "options": ["Revenue", "Expenses", "Cost of inventory sold", "Profit"], "correct_answer": "Cost of inventory sold"},
        {"question": "What is the basic accounting equation expanded?", "options": ["Assets = Liabilities + Owner's Equity + Revenue - Expenses", "Assets = Liabilities + Owner's Equity", "Assets = Liabilities - Owner's Equity", "Assets + Liabilities = Owner's Equity"], "correct_answer": "Assets = Liabilities + Owner's Equity + Revenue - Expenses"}
    ],
    "Business Management & Organizational Behavior": [
        {"question": "What is the primary purpose of organizational behavior studies?", "options": ["To understand the impact of business strategies", "To understand how people interact within organizations", "To develop marketing campaigns", "To improve financial management"], "correct_answer": "To understand how people interact within organizations"},
        {"question": "Which leadership style involves making decisions without consulting team members?", "options": ["Democratic", "Autocratic", "Laissez-faire", "Transformational"], "correct_answer": "Autocratic"},
        {"question": "What does SWOT analysis stand for?", "options": ["Strengths, Weaknesses, Opportunities, Threats", "Sales, Wages, Operations, Technology", "Suppliers, Workers, Outputs, Targets", "Systems, Workflows, Objectives, Time"], "correct_answer": "Strengths, Weaknesses, Opportunities, Threats"},
        {"question": "What is motivation?", "options": ["The process of planning", "The process of leading", "The process of influencing", "The process that initiates, guides, and maintains goal-oriented behaviors"], "correct_answer": "The process that initiates, guides, and maintains goal-oriented behaviors"},
        {"question": "What is the Hawthorne effect?", "options": ["Increased productivity due to improved lighting", "Increased productivity due to observation", "Decreased productivity due to stress", "Decreased productivity due to fatigue"], "correct_answer": "Increased productivity due to observation"},
        {"question": "What is job satisfaction?", "options": ["The salary earned", "The benefits provided", "The extent to which employees like their jobs", "The company's market share"], "correct_answer": "The extent to which employees like their jobs"},
        {"question": "What is conflict management?", "options": ["Avoiding conflicts", "Resolving conflicts effectively", "Ignoring conflicts", "Escalating conflicts"], "correct_answer": "Resolving conflicts effectively"},
        {"question": "What is team cohesion?", "options": ["The size of the team", "The diversity of the team", "The degree to which team members are attracted to each other", "The team's budget"], "correct_answer": "The degree to which team members are attracted to each other"},
        {"question": "What is organizational culture?", "options": ["The company's financial records", "The company's marketing strategy", "The shared values, beliefs, and norms of an organization", "The company's legal structure"], "correct_answer": "The shared values, beliefs, and norms of an organization"},
        {"question": "What is the purpose of performance appraisals?", "options": ["To determine salaries", "To evaluate employee performance", "To hire new employees", "To fire employees"], "correct_answer": "To evaluate employee performance"}
    ],
    "Pre-Calculus Algebra": [
        {"question": "What is the value of x in the equation 2x + 5 = 11?", "options": ["x = 3", "x = 2", "x = 5", "x = 6"], "correct_answer": "x = 3"},
        {"question": "What is the quadratic formula?", "options": ["x = -b ± √(b² - 4ac) / 2a", "x = -b ± √(a² - 4bc) / 2c", "x = b ± √(a² - 4bc) / 2a", "x = b ± √(a² + 4bc) / 2a"], "correct_answer": "x = -b ± √(b² - 4ac) / 2a"},
        {"question": "What is the slope-intercept form of a linear equation?", "options": ["y = mx + b", "ax + by = c", "y - y1 = m(x - x1)", "y = a(x - h)² + k"], "correct_answer": "y = mx + b"},
        {"question": "What is the domain of f(x) = 1/x?", "options": ["All real numbers", "x ≠ 0", "x > 0", "x < 0"], "correct_answer": "x ≠ 0"},
        {"question": "What is the range of f(x) = x²?", "options": ["All real numbers", "y ≥ 0", "y > 0", "y < 0"], "correct_answer": "y ≥ 0"},
        {"question": "What is the value of sin(π/2)?", "options": ["0", "1", "-1", "π/2"], "correct_answer": "1"},
        {"question": "What is the value of cos(π)?", "options": ["0", "1", "-1", "π"], "correct_answer": "-1"},
        {"question": "What is the exponential form of log₂(8) = 3?", "options": ["2³ = 8", "8³ = 2", "3² = 8", "2⁸ = 3"], "correct_answer": "2³ = 8"},
        {"question": "What is the inverse of f(x) = 2x + 1?", "options": ["(x - 1)/2", "2x - 1", "x/2 - 1", "1/2x - 1"], "correct_answer": "(x - 1)/2"},
        {"question": "What is the formula for the sum of an arithmetic series?", "options": ["n(a₁ + aₙ)/2", "n(a₁ + aₙ)", "n(a₁ - aₙ)/2", "n(a₁ - aₙ)"], "correct_answer": "n(a₁ + aₙ)/2"}
    ],
    "Business Database Management": [
        {"question": "Which SQL statement is used to retrieve data from a database?", "options": ["SELECT", "INSERT", "UPDATE", "DELETE"], "correct_answer": "SELECT"},
        {"question": "What does DBMS stand for?", "options": ["Database Management System", "Data Base Model System", "Database Model System", "Data Management System"], "correct_answer": "Database Management System"},
        {"question": "What is a primary key in a database?", "options": ["A foreign key", "A unique identifier", "A data type", "A constraint"], "correct_answer": "A unique identifier"},
        {"question": "What is a foreign key?", "options": ["A primary key", "A key that links tables", "A data type", "A constraint"], "correct_answer": "A key that links tables"},
        {"question": "What is SQL?", "options": ["Structured Query Language", "Structured Question Language", "System Query Language", "System Question Language"], "correct_answer": "Structured Query Language"},
        {"question": "What is normalization in database design?", "options": ["Adding redundant data", "Removing redundant data", "Creating indexes", "Adding constraints"], "correct_answer": "Removing redundant data"},
        {"question": "What is an index in a database?", "options": ["A data type", "A constraint", "A data structure for fast data retrieval", "A primary key"], "correct_answer": "A data structure for fast data retrieval"},
        {"question": "What is a transaction in a database?", "options": ["A query", "A set of SQL statements as a single unit", "A table", "A view"], "correct_answer": "A set of SQL statements as a single unit"},
        {"question": "What is a view in a database?", "options": ["A table", "A query", "A virtual table based on the result-set of an SQL statement", "An index"], "correct_answer": "A virtual table based on the result-set of an SQL statement"},
        {"question": "What is a stored procedure?", "options": ["A query", "A table", "A saved SQL code", "A view"], "correct_answer": "A saved SQL code"}
    ],
    "Business Applications Development": [
        {"question": "Which programming language is commonly used for developing business applications?", "options": ["Java", "Python", "C++", "Ruby"], "correct_answer": "Java"},
        {"question": "What is the purpose of a database in business applications?", "options": ["To store and manage data", "To manage user authentication", "To create graphical user interfaces", "To calculate business metrics"], "correct_answer": "To store and manage data"},
        {"question": "What is an API?", "options": ["Application Programming Interface", "Advanced Program Integration", "Automated Program Interaction", "Application Protocol Interface"], "correct_answer": "Application Programming Interface"},
        {"question": "What is a framework in software development?", "options": ["A programming language", "A set of rules", "A reusable software environment", "A database system"], "correct_answer": "A reusable software environment"},
        {"question": "What is version control?", "options": ["Managing data", "Managing software releases", "Managing code changes", "Managing user interfaces"], "correct_answer": "Managing code changes"},
        {"question": "What is a user interface (UI)?", "options": ["A database", "A programming language", "The point of interaction between users and a computer", "A network protocol"], "correct_answer": "The point of interaction between users and a computer"},
        {"question": "What is a software development life cycle (SDLC)?", "options": ["The process of writing code", "The process of testing software", "The process of planning, creating, testing, and deploying software", "The process of managing databases"], "correct_answer": "The process of planning, creating, testing, and deploying software"},
        {"question": "What is debugging?", "options": ["Writing code", "Testing software", "Finding and fixing errors", "Managing databases"], "correct_answer": "Finding and fixing errors"},
        {"question": "What is object-oriented programming (OOP)?", "options": ["A database model", "A programming paradigm based on objects", "A user interface design", "A network protocol"], "correct_answer": "A programming paradigm based on objects"},
        {"question": "What is a web service?", "options": ["A web browser", "A web page", "A software system supporting machine-to-machine interaction over a network", "A network protocol"], "correct_answer": "A software system supporting machine-to-machine interaction over a network"}
    ],
}

# Initialize main window
root = tk.Tk()
root.title("Quiz Bowl")

# Global variable to store the current subject selected
current_subject = ""

# Function to show the main quiz window with questions
def show_questions():
    # Create new window for questions
    question_window = tk.Toplevel(root)
    question_window.title(f"{current_subject} Quiz")
    
    # Get the list of questions for the selected subject
    subject_questions = questions.get(current_subject, [])
    question_index = 0
    attempts = 0  # Track the number of attempts for the current question
    score = 0  # Initialize the score

    # Label to display the score
    score_label = tk.Label(question_window, text=f"Score: {score}")
    score_label.grid(row=0, column=1, padx=10, pady=10)

    def display_question():
        nonlocal question_index, attempts, score
        if question_index < len(subject_questions):
            # Clear the previous widgets if any
            for widget in question_window.winfo_children():
                if widget != score_label: # Keep the score label
                    widget.destroy()

            question = subject_questions[question_index]
            tk.Label(question_window, text=question["question"]).grid(row=1, column=0, pady=10)

            # Store the selected answer
            var = tk.StringVar()

            # Create radio buttons for each option
            for i, option in enumerate(question["options"]):
                tk.Radiobutton(question_window, text=option, variable=var, value=option).grid(row=i+2, column=0, padx=10, pady=5)

            # Function to check if the answer is correct
            def check_answer():
                nonlocal attempts, score
                attempts += 1
                if var.get() == question["correct_answer"]:
                    messagebox.showinfo("Correct!", "Your answer is correct!")
                    attempts = 0  # Reset attempts on correct answer
                    score += 10  # Increment score
                    score_label.config(text=f"Score: {score}")  # Update the score label
                    next_button.grid(row=len(question["options"]) + 3, column=0, pady=10)  # Enable the next button
                    submit_button.config(state=tk.DISABLED)  # Disable the submit button after correct answer
                    skip_button.config(state=tk.DISABLED)  # Disable the skip button after correct answer
                elif attempts >= 2:
                    messagebox.showerror("Incorrect", f"The correct answer was: {question['correct_answer']}")
                    attempts = 0  # Reset attempts after 2 tries
                    next_button.grid(row=len(question["options"]) + 3, column=0, pady=10)  # Enable the next button
                    submit_button.config(state=tk.DISABLED)  # Disable the submit button after max attempts
                    skip_button.config(state=tk.DISABLED)  # Disable the skip button after max attempts
                else:
                    messagebox.showwarning("Incorrect", "Please try again!")

            # Button to submit the answer
            submit_button = tk.Button(question_window, text="Submit", command=check_answer)
            submit_button.grid(row=len(question["options"]) + 2, column=0, pady=10)

            # Button to skip the question
            def skip_question():
                nonlocal question_index
                question_index += 1
                next_button.grid(row=len(question["options"]) + 3, column=0, pady=10)  # Enable the next button
                submit_button.config(state=tk.DISABLED)  # Disable the submit button after skipping
                skip_button.config(state=tk.DISABLED)  # Disable the skip button after skipping
                messagebox.showinfo("Skipped", "You skipped the question.")
            
            skip_button = tk.Button(question_window, text="Skip", command=skip_question)
            skip_button.grid(row=len(question["options"]) + 4, column=0, pady=10)

            # Next button to proceed to the next question
            def next_question():
                nonlocal question_index
                question_index += 1
                next_button.grid_forget()  # Hide the "Next" button
                submit_button.config(state=tk.NORMAL)  # Enable the submit button
                skip_button.config(state=tk.NORMAL)  # Enable the skip button
                display_question()  # Display the next question

            next_button = tk.Button(question_window, text="Next", command=next_question)
            next_button.grid_forget()  # Initially hide the "Next" button

        else:
            messagebox.showinfo("Quiz Complete", f"You've completed the quiz!\nYour score is {score} out of {len(subject_questions)*10}")
            question_window.destroy()

    display_question()

# Function for admin login (basic check)
def admin_login():
    def verify_password():
        password = entry_password.get()
        if password == "admin123":  # You can replace this with a more secure check
            messagebox.showinfo("Login Successful", "Welcome, Administrator!")
            admin_window.destroy()  # Close the admin login window
            show_admin_panel() # Show admin panel after login
        else:
            messagebox.showerror("Login Failed", "Incorrect password. Try again.")

    admin_window = tk.Toplevel(root)
    admin_window.title("Admin Login")

    tk.Label(admin_window, text="Enter Password:").grid(row=0, column=0, padx=10, pady=10)
    entry_password = tk.Entry(admin_window, show="*")
    entry_password.grid(row=0, column=1, padx=10, pady=10)

    tk.Button(admin_window, text="Login", command=verify_password).grid(row=1, column=0, columnspan=2, pady=10)

# Function for selecting the subject and starting the quiz
def start_quiz():
    global current_subject
    current_subject = "Accounting"  # This will be dynamically set based on user choice
    show_questions()

def select_subject(subject):
    global current_subject
    current_subject = subject
    show_questions()

# Create subject selection screen
def show_subject_selection():
    subject_window = tk.Toplevel(root)
    subject_window.title("Select Subject")

    subjects = ["Accounting", "Business Management & Organizational Behavior", "Pre-Calculus Algebra", "Business Database Management", "Business Applications Development"]
    
    # Create buttons for each subject
    for i, subject in enumerate(subjects):
        tk.Button(subject_window, text=subject, command=lambda s=subject: select_subject(s)).grid(row=i, column=0, padx=10, pady=10)

# Create main menu
def main_menu():
    tk.Label(root, text="Welcome to the Quiz Bowl", font=("Arial", 20)).pack(pady=20)

    tk.Button(root, text="Quiz Taker", command=show_subject_selection, width=20, height=2).pack(pady=10)
    tk.Button(root, text="Admin Login", command=admin_login, width=20, height=2).pack(pady=10)

# Admin Panel Functions
def show_admin_panel():
    admin_panel = tk.Toplevel(root)
    admin_panel.title("Admin Panel")

    tk.Button(admin_panel, text="Add Question", command=add_question).grid(row=0, column=0, padx=10, pady=10)
    tk.Button(admin_panel, text="View Questions", command=view_questions).grid(row=1, column=0, padx=10, pady=10)
    tk.Button(admin_panel, text="Modify/Delete Questions", command=modify_delete_questions).grid(row=2, column=0, padx=10, pady=10)

def add_question():
    add_window = tk.Toplevel(root)
    add_window.title("Add Question")

    tk.Label(add_window, text="Subject:").grid(row=0, column=0)
    subject_var = tk.StringVar(add_window)
    subject_var.set("Accounting")  # Default subject
    subject_dropdown = tk.OptionMenu(add_window, subject_var, *questions.keys())
    subject_dropdown.grid(row=0, column=1)

    tk.Label(add_window, text="Question:").grid(row=1, column=0)
    question_entry = tk.Entry(add_window, width=50)
    question_entry.grid(row=1, column=1)

    options_entries = []
    for i in range(4):
        tk.Label(add_window, text=f"Option {i+1}:").grid(row=i+2, column=0)
        entry = tk.Entry(add_window, width=50)
        entry.grid(row=i+2, column=1)
        options_entries.append(entry)

    tk.Label(add_window, text="Correct Answer:").grid(row=6, column=0)
    correct_answer_entry = tk.Entry(add_window, width=50)
    correct_answer_entry.grid(row=6, column=1)

    def save_question():
        subject = subject_var.get()
        question = question_entry.get()
        options = [entry.get() for entry in options_entries]
        correct_answer = correct_answer_entry.get()

        if not all([subject, question, options, correct_answer]):
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        new_question = {"question": question, "options": options, "correct_answer": correct_answer}
        questions[subject].append(new_question)
        messagebox.showinfo("Success", "Question added successfully.")
        add_window.destroy()

    tk.Button(add_window, text="Save", command=save_question).grid(row=7, column=0, columnspan=2, pady=10)

def view_questions():
    view_window = tk.Toplevel(root)
    view_window.title("View Questions")

    tk.Label(view_window, text="Filter by Subject:").grid(row=0, column=0)
    filter_var = tk.StringVar(view_window)
    filter_var.set("All")  # Default filter
    filter_dropdown = tk.OptionMenu(view_window, filter_var, "All", *questions.keys())
    filter_dropdown.grid(row=0, column=1)

    question_text = scrolledtext.ScrolledText(view_window, width=80, height=20)
    question_text.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
    question_text.config(state=tk.DISABLED)

    def update_view():
        question_text.config(state=tk.NORMAL)
        question_text.delete(1.0, tk.END)
        subject_filter = filter_var.get()
        if subject_filter == "All":
            for subject, question_list in questions.items():
                question_text.insert(tk.END, f"Subject: {subject}\n")
                for q in question_list:
                    question_text.insert(tk.END, f"- {q['question']}\n")
        else:
            for q in questions[subject_filter]:
                question_text.insert(tk.END, f"- {q['question']}\n")
        question_text.config(state=tk.DISABLED)

    filter_var.trace("w", lambda *args: update_view()) #update when filter changes
    update_view()

def modify_delete_questions():
    modify_window = tk.Toplevel(root)
    modify_window.title("Modify/Delete Questions")

    tk.Label(modify_window, text="Subject:").grid(row=0, column=0)
    subject_var = tk.StringVar(modify_window)
    subject_var.set("Accounting")
    subject_dropdown = tk.OptionMenu(modify_window, subject_var, *questions.keys())
    subject_dropdown.grid(row=0, column=1)

    question_listbox = tk.Listbox(modify_window, width=80)
    question_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    def update_listbox():
        question_listbox.delete(0, tk.END)
        for q in questions[subject_var.get()]:
            question_listbox.insert(tk.END, q["question"])

    subject_var.trace("w", lambda *args: update_listbox())
    update_listbox()

    def modify_selected_question():
        selected_index = question_listbox.curselection()
        if not selected_index:
            messagebox.showerror("Error", "Please select a question.")
            return

        selected_index = selected_index[0]
        selected_question = questions[subject_var.get()][selected_index]

        modify_question_window = tk.Toplevel(modify_window)
        modify_question_window.title("Modify Question")

        tk.Label(modify_question_window, text="Question:").grid(row=0, column=0)
        question_entry = tk.Entry(modify_question_window, width=50)
        question_entry.insert(0, selected_question["question"])
        question_entry.grid(row=0, column=1)

        options_entries = []
        for i, option in enumerate(selected_question["options"]):
            tk.Label(modify_question_window, text=f"Option {i+1}:").grid(row=i+1, column=0)
            entry = tk.Entry(modify_question_window, width=50)
            entry.insert(0, option)
            entry.grid(row=i+1, column=1)
            options_entries.append(entry)

        tk.Label(modify_question_window, text="Correct Answer:").grid(row=5, column=0)
        correct_answer_entry = tk.Entry(modify_question_window, width=50)
        correct_answer_entry.insert(0, selected_question["correct_answer"])
        correct_answer_entry.grid(row=5, column=1)

        def save_modified_question():
            modified_question = question_entry.get()
            modified_options = [entry.get() for entry in options_entries]
            modified_correct_answer = correct_answer_entry.get()

            if not all([modified_question, modified_options, modified_correct_answer]):
                messagebox.showerror("Error", "Please fill in all fields.")
                return

            questions[subject_var.get()][selected_index]["question"] = modified_question
            questions[subject_var.get()][selected_index]["options"] = modified_options
            questions[subject_var.get()][selected_index]["correct_answer"] = modified_correct_answer
            messagebox.showinfo("Success", "Question modified successfully.")
            update_listbox()
            modify_question_window.destroy()

        tk.Button(modify_question_window, text="Save", command=save_modified_question).grid(row=6, column=0, columnspan=2, pady=10)

    def delete_selected_question():
        selected_index = question_listbox.curselection()
        if not selected_index:
            messagebox.showerror("Error", "Please select a question.")
            return

        selected_index = selected_index[0]
        if messagebox.askyesno("Confirm", "Are you sure you want to delete this question?"):
            del questions[subject_var.get()][selected_index]
            update_listbox()

    tk.Button(modify_window, text="Modify", command=modify_selected_question).grid(row=2, column=0, padx=10, pady=10)
    tk.Button(modify_window, text="Delete", command=delete_selected_question).grid(row=2, column=1, padx=10, pady=10)

# Start the application
main_menu()
root.mainloop()