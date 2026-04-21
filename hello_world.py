import os

def display_message():
    """
    Prints a message to the console to demonstrate version control.
    """
    message = "Git is awesome!"
    print(message)

if __name__ == "__main__":
    # Use os module to ensure consistent path handling
    base_dir = os.path.dirname(os.path.abspath(__file__))
    display_message()