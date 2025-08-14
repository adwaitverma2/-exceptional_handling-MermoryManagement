import logging

# Create the file before attempting to read it
with open("nonexistent.txt", "w") as f:
    f.write("This is a test file.\n")

# Setup logging
logging.basicConfig(filename="file_errors.log", level=logging.ERROR,
                    format="%(asctime)s - %(levelname)s - %(message)s")

file_path = "nonexistent.txt"

try:
    with open(file_path, "r") as f:
        content = f.read()
        print("File content:", content)
except FileNotFoundError as e:
    logging.error(f"Error opening file: {e}")
    print("An error occurred. Check 'file_errors.log' for details.")
