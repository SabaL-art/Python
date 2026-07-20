# Website Change Detector

A terminal-based Website Change Detector built in Python.

Monitor any webpage for changes by periodically checking its content. The program stores a hash of the webpage and notifies you whenever the content changes.

## Features

- Monitor any website using its URL
- Periodic automatic checking
- Detects webpage content changes
- Uses MD5 hashing for efficient comparison
- Saves previous webpage state
- Handles invalid HTTP responses
- Simple terminal interface

## Requirements

- Python 3.10+
- requests

## Installation

Install the required dependency:

```bash
pip install requests
```

## Run

```bash
python3 website_change_detector.py
```

## Usage

1. Enter the website URL.
2. Enter the checking interval (in minutes).
3. The program will continue monitoring until you stop it manually.

Example:

```text
ENTER URL: https://example.com
ENTER TIME INTERVAL FOR PERIODICAL CHECK ( in minutes ): 0.5
```

## Example Output

First run:

```text
FIRST RUN, SAVING THE CONTENT!
```

No changes detected:

```text
NO CHANGE!
```

Website updated:

```text
WEBPAGE CONTENT CHANGED!!
```

HTTP error:

```text
ERROR: HTTP 404
```

## How It Works

1. Downloads the webpage.
2. Converts the page content into an MD5 hash.
3. Compares the new hash with the previously saved hash.
4. If the hashes differ, the webpage has changed.
5. Saves the latest hash for the next comparison.

## Files

```text
website_change_detector.py
old_content.txt    # Stores the MD5 hash of the last checked webpage
```

## Concepts Practiced

- HTTP requests
- Hashing (MD5)
- File handling
- Object-Oriented Programming (OOP)
- Infinite loops
- Time delays
- Classes and methods
- Error handling

## Future Improvements

- Email notifications
- Discord notifications
- Desktop notifications
- Monitor multiple websites
- Detect and highlight what changed
- Custom HTTP headers/User-Agent support
- Logging with timestamps
- Async monitoring for multiple websites

## Author

Sabal