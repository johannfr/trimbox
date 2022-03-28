# trimbox

A tool that iterates through a directory, scans for PDFs, scans said PDFs for a `TrimBox`, computes the size in millimeters and appends the `width`x`height`mm to the filename.

## Installation

### For user

To install this only for the particular user logged in:
```bash
pip3 install --user git+https://github.com/johannfr/trimbox
```

### System-wide
If you don't mind a system-wide installation of this application and its dependencies:
```bash
pip3 install git+https://github.com/johannfr/trimbox
```



## Usage

```bash
trimbox <path-to-your-PDF-directory>
```
