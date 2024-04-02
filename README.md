# DirectoryCleaner

DirectoryCleaner is a Python-based tool designed to help you efficiently manage your filesystem by identifying and removing duplicate files. Leveraging advanced hashing algorithms, it ensures accurate detection and safe elimination of duplicates, freeing up valuable disk space and reducing clutter.

## Features

- **Advanced Hashing**: Utilizes SHA-256 hashing for precise duplicate identification.
- **Safety Mechanisms**: Offers previews and backups before deletion to ensure data safety.
- **Customization**: Allows users to customize scanning depth, file size limits, and more.
- **User-Friendly CLI**: Simple and intuitive command-line interface for easy operation.
- **Open-Source**: Encourages community contributions and feedback.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/tsullc46/DirectoryCleaner.git
   ```
2. Navigate to the project directory:
   ```
   cd DirectoryCleaner
   ```
3. Install required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To start cleaning directories, run:

```
python directory_cleaner.py <path_to_directory>
```

Options:
- `-d, --delete`: Automatically delete duplicates after confirmation.
- `-b, --backup`: Create a backup before deleting files.

For detailed help and more options, run:

```
python directory_cleaner.py --help
```

## Contributing

We welcome contributions from the community! If you'd like to contribute, please:
- Fork the repository.
- Create a new branch for your feature or fix.
- Commit your changes.
- Push the branch and open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
