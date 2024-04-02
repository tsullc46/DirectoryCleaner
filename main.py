# Imports necessary modules and functions from other files
import sys
from find_duplicates import find_duplicates
from spinner import Spinner
from file_deletion import confirm_and_delete

# Defines the main function of the script
def main(directory, dry_run=False):
    spinner = Spinner()  # Initializes a Spinner object
    spinner.start()  # Starts the spinner animation

    # Calls the function to find duplicates in the specified directory
    duplicates = find_duplicates(directory)
    
    spinner.stop()  # Stops the spinner animation

    # Calls the function to handle confirmation and deletion of duplicates, if not in dry run mode
    confirm_and_delete(duplicates, dry_run=dry_run)

# The entry point of the Python script, checking for command line arguments
if __name__ == "__main__":
    if len(sys.argv) < 2:
        # Prints usage information if no directory is specified
        print("Usage: python main.py <directory> [--dry-run]")
    else:
        # Extracts the directory path from command line arguments
        directory = sys.argv[1]
        # Checks if the --dry-run option is included in the command line arguments
        dry_run = '--dry-run' in sys.argv
        # Calls the main function with the specified directory and dry run flag
        main(directory, dry_run=dry_run)
