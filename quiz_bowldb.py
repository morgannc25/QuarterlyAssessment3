import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('quiz_bowl.db')
cursor = conn.cursor()

# Create tables for each course with attempts field
cursor.execute('''
CREATE TABLE IF NOT EXISTS principles_of_accounting (
    question_id INTEGER PRIMARY KEY AUTOINCREMENT,
    question_text TEXT,
    option_a TEXT,
    option_b TEXT,
    option_c TEXT,
    option_d TEXT,
    correct_answer TEXT,
    attempts INTEGER DEFAULT 0
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS business_management (
    question_id INTEGER PRIMARY KEY AUTOINCREMENT,
    question_text TEXT,
    option_a TEXT,
    option_b TEXT,
    option_c TEXT,
    option_d TEXT,
    correct_answer TEXT,
    attempts INTEGER DEFAULT 0
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS precalculus_algebra (
    question_id INTEGER PRIMARY KEY AUTOINCREMENT,
    question_text TEXT,
    option_a TEXT,
    option_b TEXT,
    option_c TEXT,
    option_d TEXT,
    correct_answer TEXT,
    attempts INTEGER DEFAULT 0
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS business_database_management (
    question_id INTEGER PRIMARY KEY AUTOINCREMENT,
    question_text TEXT,
    option_a TEXT,
    option_b TEXT,
    option_c TEXT,
    option_d TEXT,
    correct_answer TEXT,
    attempts INTEGER DEFAULT 0
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS business_applications_development (
    question_id INTEGER PRIMARY KEY AUTOINCREMENT,
    question_text TEXT,
    option_a TEXT,
    option_b TEXT,
    option_c TEXT,
    option_d TEXT,
    correct_answer TEXT,
    attempts INTEGER DEFAULT 0
)
''')

# Insert questions for Principles of Accounting
cursor.executemany('''
INSERT INTO principles_of_accounting (question_text, option_a, option_b, option_c, option_d, correct_answer)
VALUES (?, ?, ?, ?, ?, ?)
''', [
    ("What is the accounting equation?", "Assets + Liabilities = Owners Equity", "Liabilities + Owners Equity = Assets", "Owners’ Equity – Assets = Liabilities", "Liabilities x Owners Equity + Assets", "A"),
    ("A roofing company collects payments when jobs are complete. The work for one customer, has been completed for $3,600 as of December 31, but the customer has not yet been billed. Assuming adjustments are only made at year-end, what is the adjusting entry the company would need to make on December 31, the calendar year-end?", "Debit Cash, $3,600; Credit Roofing Revenue, $3,600", "Debit Roofing Revenue, $3,600; Credit Accounts Receivable $3,600", "Debit Accounts Receivable, $3,600; Credit Roofing Revenue, $3,600", "No adjustment Required", "C"),
    ("How is Profit Margin calculated?", "Profit Margin = Net Sales / Net Income", "Profit Margin = Net Income / Net Sales", "Profit Margin = Net Sales + Net Income + Assets", "Profit Margin = Liabilities – Net Income + Equity", "B"),
    ("On October 1, Goodwell Company rented warehouse space to a tenant for $2,200 per month and received $11,000 for five months’ rent in advance on that date, with the lease beginning immediately. The cash receipt was credited to the Unearned Revenue account. The company’s annual accounting period ends on December 31. The Unearned Revenue account balance at the end of December, after adjustment, should be:", "$4,400", "$11,000", "$8,800", "$6,600", "A"),
    ("Which financial statement shows a company’s revenues and expenses?", "Balance Sheet", "Income Statement", "Statement of Cash Flows", "Statement of Retained Earnings", "B"),
    ("Which of the following is considered a liability?", "Accounts Receivable", "Prepaid Rent", "Equipment", "Accounts Payable", "D"),
    ("What does a trial balance check for?", "Accurate financial ratios", "Matching assets to liabilities", "Equality of debits and credits", "Total revenues vs. expenses", "C"),
    ("What type of account is “Service Revenue”?", "Asset", "Expense", "Liability", "Revenue", "D"),
    ("Which of the following would appear on a Balance Sheet?", "Salaries Expense", "Rent Revenue", "Utilities Expense", "Inventory", "D"),
    ("Which of the following is recorded in the journal first?", "Adjusting entries", "Financial statements", "Closing entries", "Business transactions", "D")
])

# Insert questions for Business Management
cursor.executemany('''
INSERT INTO business_management (question_text, option_a, option_b, option_c, option_d, correct_answer)
VALUES (?, ?, ?, ?, ?, ?)
''', [
    ("What is the primary function of management?", "Planning", "Organizing", "Leading", "Controlling", "A"),
    ("Which of the following is a characteristic of a leader?", "Provides clear instructions", "Gives orders", "Delegates authority", "Motivates and inspires", "D"),
    ("What is SWOT analysis?", "An analysis of strengths, weaknesses, opportunities, and threats", "An analysis of business financials", "A financial statement", "A competitor analysis", "A"),
    ("What is the purpose of delegation?", "To increase control", "To reduce workload", "To monitor performance", "To minimize decision making", "B"),
    ("Which of the following is a type of organizational structure?", "Hierarchical", "Matrix", "Flat", "All of the above", "D")
])

# Insert questions for Pre-Calculus Algebra
cursor.executemany('''
INSERT INTO precalculus_algebra (question_text, option_a, option_b, option_c, option_d, correct_answer)
VALUES (?, ?, ?, ?, ?, ?)
''', [
    ("What is the solution to the equation: 2x + 5 = 13?", "4", "5", "3", "6", "A"),
    ("What is the slope of the line y = 3x - 2?", "3", "-2", "2", "-3", "A"),
    ("Factor: x² - 9", "(x - 3)(x + 3)", "(x - 9)(x + 1)", "(x - 1)(x + 9)", "Prime", "A"),
    ("Simplify: (3x²)(2x³)", "6x⁵", "5x⁶", "6x⁶", "6x³", "A"),
    ("What is the domain of f(x) = 1 / (x - 4)?", "x ≠ 4", "x ≠ 0", "All real numbers", "x < 4", "A"),
    ("Solve for x: x² = 16", "x = 4", "x = -4", "x = ±4", "x = 0", "C"),
    ("What is the solution for the inequality 2x - 3 > 7?", "x > 5", "x < 5", "x = 5", "x = -5", "A"),
    ("What is the slope of the line passing through (1,2) and (3,4)?", "1", "2", "0", "-1", "A"),
    ("Factor: 2x² - 8", "2(x - 2)(x + 2)", "2(x - 4)(x + 4)", "2(x - 1)(x + 1)", "Prime", "A"),
    ("Solve for x: 3x + 5 = 14", "x = 3", "x = 4", "x = 5", "x = 6", "A")
])

# Insert questions for Business Database Management
cursor.executemany('''
INSERT INTO business_database_management (question_text, option_a, option_b, option_c, option_d, correct_answer)
VALUES (?, ?, ?, ?, ?, ?)
''', [
    ("What is a primary key in a database?", "A field that uniquely identifies a record", "A field that can store null values", "A field that stores foreign keys", "A field used for calculations", "A"),
    ("Which of the following is a type of relationship in a relational database?", "One-to-one", "One-to-many", "Many-to-many", "All of the above", "D"),
    ("What is a foreign key?", "A field that points to a primary key in another table", "A key used to encrypt data", "A key that stores multiple values", "A key used for sorting data", "A"),
    ("Which of the following is true about normalization?", "It eliminates redundancy", "It improves query speed", "It reduces the number of records", "It adds more fields to tables", "A"),
    ("What is the purpose of indexing in a database?", "To speed up data retrieval", "To store large amounts of data", "To restrict data access", "To back up data", "A")
])

# Insert questions for Business Applications Development
cursor.executemany('''
INSERT INTO business_applications_development (question_text, option_a, option_b, option_c, option_d, correct_answer)
VALUES (?, ?, ?, ?, ?, ?)
''', [
    ("What is the primary purpose of a software development life cycle?", "To create the software efficiently", "To market the software", "To ensure a systematic development process", "To sell software faster", "C"),
    ("What is an algorithm?", "A step-by-step procedure for solving a problem", "A type of database", "A collection of software", "A hardware component", "A"),
    ("What is version control?", "Tracking changes to code", "Debugging code", "Storing backups", "Running code", "A"),
    ("Which language is commonly used for web development?", "Python", "HTML", "Java", "All of the above", "D"),
    ("What does 'Agile' methodology emphasize?", "Planning and documentation", "Customer collaboration and flexibility", "Fixed schedules", "Solo development", "B")
])

# Commit and close the connection
conn.commit()
conn.close()
