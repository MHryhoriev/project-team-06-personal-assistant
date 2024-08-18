# Contact Manager

## Project Description

A personal assistant for managing a contact book and notes. The application allows users to add, edit, and delete contacts and notes, as well as check upcoming birthdays.

## Commands

### Add New Contact
- **Command**: `add-contact`
- **Description**: Add a new contact to your contact book.

### Add New Note
- **Command**: `add-note`
- **Description**: Create a new note to store important information.

### Add Tag
- **Command**: `add-tag`
- **Description**: Add a tag to an existing note for better organization.

### Edit Contact
- **Command**: `edit-contact`
- **Description**: Modify the details of an existing contact.

### Edit Note
- **Command**: `edit-note`
- **Description**: Update the text or other details of an existing note.

### Search Contact
- **Command**: `search-contact`
- **Description**: Find a contact based on a given criterion.

### Search Note
- **Command**: `search-note`
- **Description**: Find a note based on a given criterion.

### Remove Contact
- **Command**: `remove-contact`
- **Description**: Delete a contact from your contact book.

### Remove Note
- **Command**: `remove-note`
- **Description**: Delete a note from your list.

### Remove Tag
- **Command**: `remove-tag`
- **Description**: Remove a tag from a note.

### Show All Notes
- **Command**: `show-all-notes`
- **Description**: Display a list of all notes.

### Show All Contacts
- **Command**: `show-all-contacts`
- **Description**: Display a list of all contacts.

### Check Upcoming Birthdays
- **Command**: `check-birthdays`
- **Description**: Show birthdays that are approaching.

### Sort Notes
- **Command**: `sort-notes`
- **Description**: Sort notes by tags.

### Exit
- **Command**: `exit`
- **Description**: Close the application.

### Help
- **Command**: `help`
- **Description**: Show available commands and their descriptions.

## Usage

To use any command, simply enter it in the command line interface followed by any required parameters.


## Data Storage System

### Overview

This system provides functionality for managing persistent data storage using JSON files. It includes mechanisms to save and load data, ensuring that information is preserved between application runs.

### Functionality

1. **Data Storage**: 
   - The system saves data to a specified JSON file. This is done through the `Storage` class and its concrete implementations (`NoteStorage` and `ContactStorage`), which handle different types of data.

2. **Data Caching**:
   - To optimize performance, data is cached in memory. When data is loaded from the file, it is stored in a cache to avoid redundant file operations.

3. **Loading Data**:
   - On application startup, the system loads data from the JSON file. If the file does not exist or there are issues with reading the data, an empty list is returned. Data is parsed and validated before being loaded into memory.

4. **Saving Data**:
   - When changes are made to the data, these changes are saved back to the JSON file. The cache is updated to reflect the most recent changes.

### How It Works

- **Initialization**: 
  - When a `Storage` object is initialized, it is provided with the path to the JSON file where data will be stored.

- **Loading Data**: 
  - Data is read from the file and loaded into memory when the `load_data` method is called. The data is cached for future use.

- **Saving Data**: 
  - Changes to the data are written to the JSON file using the `save_data` method. The cache is also updated to ensure it reflects the latest data.

This setup ensures that data is persistently stored and efficiently managed, providing a seamless experience for users and applications.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/MHryhoriev/project-team-06-personal-assistant.git
    cd project-team-06-personal-assistant
    ```

2. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Running the Application (from the virtual environment)

On Windows, run the application with:

```bash
py src/main.py
```

On macOS and Linux, run the application with:

```bash
python src/main.py
```


