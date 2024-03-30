# Python example script that parses & converts to the markdown style table found in ntdll.md - from the raw ntdll.dll data that is in ntdll.txt! (The ntdll.txt data is from an IDA Freeware export - select all in left functions column, copy, and paste into Notepad) 

def format_to_markdown_table(file_path):
    with open(file_path, 'r') as file:
        # Read the file content
        lines = file.read().strip().split('\n')
    
    # Initialize the markdown table with headers
    headers = ["Function name", "Segment", "Start", "Length", "Locals", "Arguments", "R", "F", "L", "M", "O", "S", "B", "T", "="]
    markdown_table = "| " + " | ".join(headers) + " |" + "\n"
    
    # Add the header separator
    markdown_table += "|" + "|".join(["---"] * len(headers)) + "|" + "\n"
    
    # Format each row of data
    for line in lines[1:]:
        # Replace tabs with proper markdown format and handle missing data with placeholders
        columns = line.split('\t')
        markdown_row = "| " + " | ".join(columns + ["."] * (len(headers) - len(columns))) + " |"
        markdown_table += markdown_row + "\n"
    
    return markdown_table

file_path = 'ntdll.txt'

# Convert to markdown table and print
markdown_table = format_to_markdown_table(file_path)
print(markdown_table)
