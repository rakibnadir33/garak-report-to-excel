# garak-report-to-excel
Parse Garak LLM vulnerability scanner report files into clean Excel spreadsheets for easier analysis.
# garak-results-parser

A simple utility to parse Garak LLM vulnerability scanner `.jsonl` report files into a clean Excel spreadsheet for easier analysis.

## Requirements

- Python 3.8+
- pandas
- openpyxl

## Install dependencies

pip install -r requirements.txt

## Usage

python garak_results_parser.py

When prompted, paste the full path to your Garak `.jsonl` report file.

## Output

Generates `garak_results.xlsx` in the current directory with three columns:
- probe — the Garak probe name
- prompt — the exact prompt sent to the model
- response — the model's response
- <img width="1569" height="722" alt="image" src="https://github.com/user-attachments/assets/dfe9dade-7e4e-4e5b-a877-8f8bd26c4c1d" />


## Compatible with

Garak v0.14+
