# Exploring ntdll system calls

- These specific codes and ntdll.dll layouts depend on 32 or 64 devices, specific versions, etc. Your ntdll may differ from this example
- This repository is a POC into how you can explore ntdll on your own personal devices, for legal, authorized uses

## Step 1

Requirements:

- IDA Freeware (for the specific format of the scripts in this repository)
- Windows, access to ntdll.dll in user or system paths

Optional / Recommended:

- Python, to process the raw data (from your ntdll.txt file when you export from IDA) if you want to push it to any other format
- Python is used for: raw to markdown, and raw to csv
