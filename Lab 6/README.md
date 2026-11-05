
# Python Lab 06: Dictionary Data Structures and Operations

## Student Details
**Name:** Harshil Soni  
**Roll Number:** IC-2K24-36  
**Course:** Master of Computer Applications (MCA)  
**Subject:** Python Programming Laboratory

## Overview

Lab 06 focuses on mastering Python dictionaries (dict), hash-based key-value lookups, nested data structures, dictionary comprehensions, and data inversion.

The laboratory is divided into three distinct components:

- **Practical Programming Tasks (Q1 - Q5):** Menu-driven console applications demonstrating CRUD operations, data aggregation, validation, filtering, and reporting using dictionary architectures.
- **Section A (Practical Questions):** Programming exercises and their implementations covering dictionary operations and applications.
- **Section B (Code Tracing & Output Analysis):** Tracing edge cases involving dictionary reference assignment, shallow copying, falsy value filtering, hash collisions (1 == 1.0 == True), dictionary mutation during iteration, and dictionary comprehensions.

## File Structure

```text
Lab 6/
│
├── Q1_Student_Database.py
├── Q2_Employee_Database.py
├── Q3_Library_Record_System.py
├── Q4_Word_Frequency_Counter.py
├── Q5_Phone_Directory.py
│
├── SectionA.txt
├── SectionB.txt
└── README.md
```

## Practical Programming Tasks

### 1. Student Record and Grade Management System

**File:** `Q1_Student_Database.py`

**Objective:** Design an interactive, menu-driven student management system using nested dictionaries to track student details and marks across multiple subjects.

**Data Structure:**

```python
records = {
    "roll_no": {
        "name": str,
        "marks": {
            "math": int,
            "phy": int,
            "chem": int
        }
    }
}
```

**Key Functionalities:**

- Add Student: Validates marks between 0 and 100 before creating records; prevents duplicate roll numbers.
- Update Subject Marks: Modifies marks for a specific subject within the nested marks dictionary.
- Delete Student: Safely removes a student record using `.pop()`.
- View Record: Displays details and subject marks for a given roll number.

**Comprehensive Reports:**

- Calculates average marks per student using dictionary comprehensions.
- Identifies the overall topper using `max()` with key extraction.
- Determines the highest scorer in each subject dynamically.
- Filters students scoring below 40 in any subject.
- Groups students into letter grades (A: >=90, B: >=75, C: >=60, D: >=40, F: <40).

### 2. Employee Database and Payroll Analytics

**File:** `Q2_Employee_Database.py`

**Objective:** Implement an employee record system supporting department-level aggregation, payroll calculations, and non-destructive transformations.

**Data Structure:**

```python
employees = {
    "emp_id": {
        "name": str,
        "dept": str,
        "salary": float
    }
}
```

**Key Functionalities:**

- Add Employee: Enforces non-negative salary validation and unique employee IDs.
- Update Salary: Updates compensation with input validation.
- Delete Employee: Removes employee records safely without program termination if ID is absent.
- Search Employee: Retrieves complete details by employee ID.

**Analytical Reports:**

- Computes department-wise total payroll and headcount using `dict.setdefault()`.
- Identifies the highest-paid employee per department.
- Generates a salary-sorted roster in descending order using `sorted()` with a custom lambda key.
- Generates a non-mutating 10% raise simulation for employees earning below 50,000 using dictionary comprehensions.
- Identifies the department with the highest average salary.

### 3. Library Record and Book Lending System

**File:** `Q3_Library_Record_System.py`

**Objective:** Create a multi-copy library catalog tracking book availability, borrowing privileges, and borrower relationships.

**Data Structure:**

```python
books = {
    "isbn": {
        "title": str,
        "author": str,
        "copies": int,
        "issued_to": list,
        "ever_issued": bool
    }
}
```

**Key Functionalities:**

- Add Book / Restock: Adds a new book or increments copy count if the ISBN already exists.
- Issue Book: Checks copy availability, prevents duplicate issuance of the same title to the same member, enforces a maximum borrowing limit of 2 books per member, decrements available copies, and marks `ever_issued` as True.
- Return Book: Restores stock and removes the member ID from the active borrowers list.
- Search: Case-insensitive search by ISBN or partial title.

**Reports:**

- Filters titles by a specific author.
- Inverts book-to-member relationships to identify members holding multiple books.
- Lists out-of-stock titles (0 available copies).
- Lists titles that have never been checked out.

### 4. Word Frequency Counter and Text Analyzer

**File:** `Q4_Word_Frequency_Counter.py`

**Objective:** Process raw textual input, clean non-alphanumeric noise, calculate word occurrences, and produce inverted frequency indexes.

**Key Functionalities:**

- Text Normalization: Converts text to lowercase and strips punctuation using character-level checks (`isalnum()`).
- Frequency Mapping: Counts occurrences using `dict.get(word, 0) + 1`.
- Top N Words: Sorts by frequency descending, breaking ties alphabetically.
- Hapax Legomena: Extracts and displays words occurring exactly once.
- Inverted Frequency Dictionary: Groups words by frequency.
- Length-wise Indexing: Groups unique words by their character count.
- Word Search: Instant O(1) frequency lookup for user-queried words.

### 5. Contact Book with Reverse Phone Lookup

**File:** `Q5_Phone_Directory.py`

**Objective:** Build a contact directory supporting multi-number contacts, strict 10-digit validation, global phone uniqueness, and reverse lookup indexing.

**Data Structure:**

```python
directory = {
    "name": {
        "phones": list,
        "email": str,
        "city": str
    }
}
```

**Key Functionalities:**

- Add Contact: Validates phone number length (10 digits, numeric) and ensures global uniqueness.
- Add Secondary Number: Allows multiple distinct contact numbers for an existing person while maintaining global uniqueness.
- Update Details: Allows modifying email or city independently.
- Safe Deletion: Deletes records using `.pop(name, None)` to prevent KeyError exceptions.
- Partial Name Search: Substring search across all contact names.

**Reports and Utilities:**

- Reverse Lookup Dictionary: Dynamically generates `{phone_number: owner_name}` via dictionary comprehension for O(1) phone-to-name resolution.
- City Grouping: Groups contact names by city using `setdefault()`.
- Multi-number Flag: Lists all contacts possessing more than one phone number.
- Sorted Directory: Displays all records in alphabetical order of contact names.

## Section A: Practical Questions

The file `SectionA.txt` contains the practical question-related material for Lab 06, covering Python dictionary concepts and their applications.

## Section B: Code Tracing and Output Analysis

The file `SectionB.txt` documents the step-by-step tracing and expected outputs for eight dictionary code snippets:

1. **Object Reference Assignment:** Demonstrates that `d2 = d` creates a shared reference rather than a copy.
2. **Shallow Copy (`.copy()`):** Shows that top-level dictionaries are separate but nested mutable objects remain shared.
3. **Dictionary Comprehension with Truthiness Filtering:** Traces filtering where falsy values (like 0) are dropped.
4. **`setdefault()` Behavior:** Explains how existing values are preserved and defaults are inserted only for missing keys.
5. **Key Equality and Hash Collisions:** Explains why `{1: "a", 1.0: "b", True: "c"}` has a length of 1.
6. **Dictionary Mutation During Iteration:** Demonstrates why deleting keys while directly iterating over a dictionary causes a `RuntimeError`.
7. **Safe Extraction (`.pop()` and `.popitem()`):** Demonstrates safe retrieval with fallbacks and removal of the most recently inserted item.
8. **Key-Value Inversion Overwrite:** Demonstrates how duplicate values become duplicate keys during inversion, causing earlier entries to be overwritten.

## How to Run the Programs

All programs are written in Python 3 and require no third-party libraries.

Run each program from the terminal:

```bash
# Navigate to the Lab 6 directory
cd "Lab 6"

# Run Question 1: Student Management System
python Q1_Student_Database.py

# Run Question 2: Employee Payroll System
python Q2_Employee_Database.py

# Run Question 3: Library Management System
python Q3_Library_Record_System.py

# Run Question 4: Word Frequency Counter
python Q4_Word_Frequency_Counter.py

# Run Question 5: Contact Book with Reverse Lookup
python Q5_Phone_Directory.py
```

## Conclusion

This laboratory work demonstrates the practical and theoretical application of Python dictionaries. By leveraging average O(1) lookups, nested data structures, dictionary comprehensions, and safe data handling patterns, these implementations provide robust and efficient solutions to common record-keeping and data-processing problems.
