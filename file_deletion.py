# Import the os module to interact with the operating system, allowing for file deletion.
import os

def confirm_and_delete(duplicates, dry_run=False):
    """
    Prompts the user to select which duplicate files to keep, deleting the rest.
    
    Parameters:
    - duplicates: A list of lists, where each sublist contains the file paths of duplicate files.
    - dry_run (bool): If True, no actual deletion occurs, simulating what would be deleted.
    """
    
    # Check if the duplicates list is empty, indicating no duplicates were found.
    if not duplicates:
        print("No duplicate files found.")
        return  # Exit the function early.

    # Iterate over the list of duplicate file groups.
    for index, files in enumerate(duplicates, start=1):
        print(f"\nDuplicate {index}:")  # Print the group number.
        for i, filepath in enumerate(files):
            print(f"{i+1}: {filepath}")  # Print each file in the group.
        
        # If not in dry run mode, prompt the user for input on which file to keep.
        if not dry_run:
            keep = input("Enter the number of the file you want to keep (or 'all' to keep all): ")
            if keep.isdigit():
                keep = int(keep) - 1  # Convert user input to an index.
                for i, filepath in enumerate(files):
                    if i != keep:
                        print(f"Deleting {filepath}...")  # Notify user of deletion.
                        os.remove(filepath)  # Perform the file deletion.
                        log_deletion(filepath)  # Log the deletion action.
            elif keep.lower() != 'all':
                print("Invalid input. No files were deleted.")  # Handle invalid input.
        else:
            print("Dry run enabled - no files will be deleted.")  # Notify dry run action.

def log_deletion(filepath):
    """
    Logs each deletion to a file for record-keeping.
    
    Parameters:
    - filepath: The path of the file that was deleted.
    """
    with open("deletion_log.txt", "a") as log_file:  # Open the log file in append mode.
        log_file.write(f"Deleted {filepath}\n")  # Write the deletion record.
