# Release 1.0.4.2
## Changelog
> Release Date: Pending
- Bug fixes related to commands that takes multiple input values
> This bug fixes applies to the following commands:
> "move", "dircopy", "zipdir"
- Changed version definition "Commit version" to "Code version"
- Added command "changelog" in module "JaylyTerminal Support"
- Changed program welcome message (same with version **1.0.2.4** and **1.0.3.2**)
- When using command "dirsize", it will print directory size every second instead of every tick
> Before
```
>C:\>dirsize /loop
Directory size: [size] ([size in bytes])
[It loops every single tick]
```
> Now
```
>C:\>dirsize /loop
Directory size: [size] ([size in bytes]) | 00:00:01
Directory size: [size] ([size in bytes]) | 00:00:02
Directory size: [size] ([size in bytes]) | 00:00:03
Directory size: [size] ([size in bytes]) | 00:00:04
```
- Command "dirsize" now accept one more input extension "time"
> "time" allows program to print directory size for certain amount of **seconds**
```
C:\>dirsize /loop /time 5
Directory size: [Size] ([Size in bytes]) | [Time]
Directory size: [Size] ([Size in bytes]) | [Time]
Directory size: [Size] ([Size in bytes]) | [Time]
Directory size: [Size] ([Size in bytes]) | [Time]
Directory size: [Size] ([Size in bytes]) | [Time]
C:\>
```
> "/time 5" means loop for 5 seconds in this example.
- Fixed command "exit
> The command "exit" will now close python console.