# Morse Code Translator

A simple, interactive Python command-line application that converts text into Morse code using a predefined Morse code dictionary.

## Overview

The Morse Code Translator allows users to enter text and instantly receive its Morse code equivalent. It supports uppercase and lowercase letters, numbers, and several punctuation marks.

The application features a simple terminal interface with ASCII art branding, an option to translate multiple messages in one session, and the ability to clear the terminal screen between translations.

## Features

- **Text-to-Morse Conversion:** Converts supported characters into their corresponding Morse code representations.
- **Character Support:** Supports:
  - Letters (A–Z)
  - Numbers (0–9)
  - Common punctuation marks and special characters.
- **Case Insensitive:** Automatically converts input text to uppercase before translation.
- **Word Separation:** Uses forward slashes (`/`) to distinguish between words in the translated output.
- **Multiple Translations:** Allows users to translate multiple messages without restarting the application.
- **Clear Screen:** Provides an option to clear the terminal screen.
- **Cross-Platform Compatibility:** Supports Windows, macOS, and Linux terminal environments.
- **ASCII Art Interface:** Displays custom ASCII art logos when the application runs.

## Project Structure

```text
morse-code-translator/
│
├── art.py                # ASCII art logos
├── morse_code_dict.py    # Morse code character dictionary
├── script.py             # Main application
├── README.md             # Project documentation
└── .gitignore             # Files and directories ignored by Git
```

## Requirements

- Python 3.x
- No external Python packages required.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/hackerhegod/morse-code-translator.git
   ```

2. Navigate into the project directory:

   ```bash
   cd morse-code-translator
   ```

3. Run the application:

   ```bash
   python script.py
   ```

## Usage

1. Run the application.
2. Enter the text you want to convert when prompted.
3. The application displays the corresponding Morse code.
4. Choose whether to continue translating or exit.
5. If you choose to continue, you can also clear the terminal screen before the next translation.

### Example

**Input:**

```text
HELLO WORLD
```

**Output:**

```text
Text in Morse Code = .... . .-.. .-.. --- / .-- --- .-. .-.. -..
```

### Exiting the Application

When prompted:

```text
Continue? Enter '/end' to exit. Anything else to continue.
```

Enter `/end` to terminate the application.

## How It Works

The application uses a Python dictionary to map individual characters to their corresponding Morse code representations.

The translation process follows these steps:

1. Accepts user input.
2. Converts the input to uppercase.
3. Iterates through each character.
4. Looks up each character in the Morse code dictionary.
5. Appends the corresponding Morse code representation to the output.
6. Uses forward slashes (`/`) to separate words.
7. Skips unsupported characters while maintaining spacing in the output.

## Future Improvements

Potential improvements include:

- [ ] Add Morse code-to-text translation.
- [ ] Implement input validation and clearer handling of unsupported characters.
- [ ] Add audio playback of Morse code using short and long tones.
- [ ] Introduce a graphical user interface (GUI).
- [ ] Allow users to copy translated Morse code directly.

## License

This project is open-source. Feel free to use, modify, and improve it.

---

**Built with Python.**