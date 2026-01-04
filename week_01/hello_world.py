import sys
from datetime import datetime

def get_python_version():
    return sys.version

def get_current_datetime():
    return datetime.now()

def main():
    print("Current Date & Time:", get_current_datetime())
    print("Python Version:", get_python_version())

if __name__ == "__main__":
    main()