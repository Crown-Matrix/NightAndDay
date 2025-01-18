# README Guide: Implementing a Scheduled Dark Mode in Python

## **Step 1: Basic Function to Check Dark Mode Status**

### Objective:

Create a function that compares an input time against a predefined schedule and determines if it's within the "dark mode" timeframe.

---

### **Instructions**

1. **Create the Python File**

    - Open your code editor.
    - Create a new Python file named `dark_mode_schedule.py`.

2. **Set Up a Dark Mode Schedule**

    - Define a start time and an end time for dark mode (e.g., 20:00 to 06:00).
    - Use the 24-hour clock format for consistency.

    Example:
    `DARK_MODE_START = "20:00"`
    `DARK_MODE_END = "06:00"`

3. **Define the Function**

    - Create a function called `is_dark_mode(current_time)`.
    - This function will:
        - Accept the current time as a string in the format `HH:MM`.
        - Compare it with the start and end times of dark mode.
        - Return `True` if the current time falls within dark mode hours, otherwise `False`.

4. **Write the Comparison Logic**

    - Convert time strings into comparable integers, e.g., `20:00` → `2000`.
    - Handle the case where the schedule crosses midnight (e.g., 20:00 to 06:00).

5. **Test the Function**
    - Print the result of calling `is_dark_mode()` with different times to verify functionality.

---

### **Code Example**

```python
# Predefined dark mode schedule
DARK_MODE_START = "20:00"  # 8:00 PM
DARK_MODE_END = "06:00"   # 6:00 AM

def is_dark_mode(current_time):
    """
    Determines if the current time falls within dark mode hours.
    :param current_time: str, format HH:MM (24-hour clock)
    :return: bool, True if in dark mode, otherwise False
    """
    # Convert times to integers for comparison
    start = int(DARK_MODE_START.replace(":", ""))
    end = int(DARK_MODE_END.replace(":", ""))
    now = int(current_time.replace(":", ""))

    # Handle schedule crossing midnight
    if start > end:
        return now >= start or now < end
    else:
        return start <= now < end

# Test the function
print(is_dark_mode("21:00"))  # Expected: True (Dark Mode)
print(is_dark_mode("05:30"))  # Expected: True (Dark Mode)
print(is_dark_mode("12:00"))  # Expected: False (Light Mode)

```

### Learning Outcomes

-   Understand how to work with time in Python.
-   Learn basic string manipulation (e.g., `replace()`).
-   Practice conditional statements to handle different scenarios.

---

## **Step 2: Adding User Input**

### Objective:

Expand the program to accept user-defined dark mode start and end times.

---

### **Instructions**

1. **Modify the Script**:

    - Allow the user to input start and end times for dark mode.

2. **Use Input Function**:

    - Use Python’s `input()` function to gather times in `HH:MM` format.

3. **Validate the Input**:
    - Ensure it follows the correct format.

---

### **Code Example**

```python
def get_user_schedule():
    """
    Prompts the user to input dark mode start and end times.
    :return: tuple (start_time, end_time)
    """
    while True:
        try:
            start = input("Enter dark mode start time (HH:MM): ")
            end = input("Enter dark mode end time (HH:MM): ")
            # Validate input format
            if len(start) == 5 and len(end) == 5 and start[2] == ":" and end[2] == ":":
                return start, end
            else:
                raise ValueError
        except ValueError:
            print("Invalid input. Please enter time in HH:MM format.")

# Get user-defined schedule
user_start, user_end = get_user_schedule()
print(f"Dark mode will start at {user_start} and end at {user_end}.")
```

Learning Outcomes

-   Practice using input() for user interaction.
-   Implement error handling with try/except blocks.

# Step 3: Real-Time Timer (Advanced)

In this step, we’ll introduce a loop that checks the current time against the schedule in real-time.
