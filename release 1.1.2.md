# Release 1.1.2
## Changelog
> Release Date: May 18, 2021
- Added Module "File Handling"
- Added command "dirsearch" in module "Directory Handling"
- Changed source code formation
- Updated command "help"
- Replace command "dirmove" to "move"
- Removed entering input value from functions
```
# This is an example
# Before
>zipdir
Directory compress: 
Output filename (Include extension): 
(Zips directory)

# Updated
>zipdir
Usage: zipdir [Compress Directory] [Output Filename]
(Zips directory)
```
- Added Usage to command error.
```
# Example
>zipdir
Usage: zipdir [Compress Directory] [Output Filename]
```
