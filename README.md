# CV Page Merger

This script merges specific pages of a PDF file (your CV) into a single page, adding dynamic links to your GitHub and LinkedIn profiles.

## Description

The `cleandynamic.py` script performs the following tasks:

1. Opens the original PDF file (`input.pdf`).
2. Searches for the positions of the "GitHub" and "LinkedIn" text on the second page.
3. Calculates the dimensions for a new combined page.
4. Merges the first and second pages into a single page, slightly overlapping to avoid lines.
5. Inserts dynamic links to your GitHub and LinkedIn profiles at the specified positions.
6. Saves the combined PDF with a unique filename.

## Installation

To run this script, you need to install the `PyMuPDF` library. For detailed installation instructions, refer to the [PyMuPDF installation documentation](https://pymupdf.readthedocs.io/en/latest/installation.html).


## Usage

Place your original PDF file (named `input.pdf`) in the same directory as the script. Run the script using the following command:
```bash
python3 cleandynamic.py
```

The script will generate a new PDF file with a unique name, combining the specified pages of your CV and including the dynamic links.

## Note

This script is designed for a specific CV format. Feel free to modify it to work with your own PDF files.

## Output

The combined PDF will be saved in the same directory with a unique filename.