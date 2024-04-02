# DirectoryCleaner

DirectoryCleaner is a Python-based utility designed to help users efficiently manage and clean up their directories by finding and removing duplicate files. With an intuitive command-line interface, DirectoryCleaner offers a simple yet powerful solution to declutter your file system and reclaim valuable disk space.

## Features

- **Advanced Hashing**: Utilizes SHA-256 hashing for precise duplicate identification.
- **Safety Mechanisms**: Offers previews and backups before deletion to ensure data safety.
- **Customization**: Allows users to customize scanning depth, file size limits, and more.
- **User-Friendly CLI**: Simple and intuitive command-line interface for easy operation.
- **Open-Source**: Encourages community contributions and feedback.
- **Find Duplicate Files**: Quickly identifies duplicate files in a specified directory and its subdirectories.
- **Dry Run Mode**: Allows users to see which files would be considered duplicates without making any changes.
- **User Confirmation**: Prompts users for confirmation before deleting files, ensuring no accidental data loss.
- **Deletion Logging**: Keeps a record of all deleted files for review.
- **Visual Progress Indicator**: Includes a spinner to indicate that the process is running, enhancing user experience for long-running operations.

## Getting Started

### Prerequisites

- Python 3.6 or newer

### Installation

1. Clone the repository to your local machine:
   ```
   git clone https://github.com/tsullc46/DirectoryCleaner.git
   ```
2. Navigate to the DirectoryCleaner directory:
   ```
   cd DirectoryCleaner
   ```

### Usage

To start using DirectoryCleaner, run the following command in your terminal:

```
python main.py <path-to-directory> [--dry-run]
```

- `<path-to-directory>`: The path to the directory you want to clean up.
- `--dry-run` (optional): Use this option to perform a dry run without deleting any files.

### Example

```
python main.py /path/to/my/directory --dry-run
```

This command will display the duplicate files found in `/path/to/my/directory` without actually deleting them.

## Modules

- `main.py`: The entry point of the application.
- `find_duplicates.py`: Contains logic to find duplicate files.
- `file_hashing.py`: Responsible for generating file hashes.
- `file_deletion.py`: Handles the deletion of files with user confirmation.
- `spinner.py`: Provides a visual indicator for ongoing processes.

## Contributing

Contributions to the DirectoryCleaner project are welcome! Please refer to the CONTRIBUTING.md file for guidelines.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
