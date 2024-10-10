# Password Manager

A simple and user-friendly Password Manager application built with Tkinter. This application allows users to generate strong passwords, save their credentials securely in a JSON file, and retrieve them when needed.

## Features

- **Password Generation**: Generate secure passwords with a combination of letters, numbers, and symbols.
- **Credential Storage**: Save website credentials (website, email, and password) in a JSON file.
- **Retrieve Passwords**: Search for saved passwords by website name.
- **Clipboard Integration**: Automatically copy the generated password to the clipboard for easy access.
- **Environment Variable Support**: Load predefined email addresses from environment variables.

## Setup Instructions

### 1. Clone the Repository

To get started, clone the repository to your local machine:

```bash
git clone https://github.com/Selorme/password_manager.git
```

Navigate into the project directory:

```bash
cd password-manager
```

### 2. Install Dependencies

Make sure you have Python 3.x installed. You can check your version using:

```bash
python --version
```

Install the required libraries:

```bash
pip install pyperclip python-dotenv
```

### 3. Prepare Environment Variables

Create a `.env` file in the root directory of your project and add your email address:

```
MY_EMAIL=your_email@example.com
```

### 4. Prepare Assets

This application requires an image file for the logo:

- `logo.png`: A logo image for the GUI.

Make sure this image is in the same directory as your script.

### 5. Run the Application

Run the application using Python:

```bash
python main.py
```

The Password Manager GUI will open, allowing you to generate passwords, add your credentials, and search for existing passwords.

## Code Explanation

1. **Imports**: The script imports necessary libraries, including `tkinter` for the GUI, `pyperclip` for clipboard functionality, and `json` for data storage.
2. **Password Generation**: The `generate_password()` function creates a random password with letters, numbers, and symbols, and copies it to the clipboard.
3. **Saving Credentials**: The `add_inputs()` function saves the entered website, email, and password to a JSON file, checking for existing entries to avoid duplicates.
4. **Retrieving Credentials**: The `website_exists()` function allows users to search for saved passwords by website name.
5. **UI Setup**: The application creates a Tkinter window with labels, entry fields, and buttons to interact with the password manager.

## License

This project is licensed under the MIT License.
