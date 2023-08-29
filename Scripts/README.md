# Description
Sharing my own scripts to perform the same techniques mentioned in the course but using `python` 

## Module #28
- `ProcEnum.py` : Processes Enumeration using Win APIs
   - Win API functions used to perform process enumeration:
      - [`CreateToolhelp32Snapshot`](https://learn.microsoft.com/en-us/windows/win32/api/tlhelp32/nf-tlhelp32-createtoolhelp32snapshot)
      - [`Process32First`](https://learn.microsoft.com/en-us/windows/win32/api/tlhelp32/nf-tlhelp32-process32first)
      - [`Process32Next`](https://learn.microsoft.com/en-us/windows/win32/api/tlhelp32/nf-tlhelp32-process32next)
    - Usage : `python ProcEnum.py <processName>`
    - Example : `python ProcEnum.py notepad.exe`
    - requirments : `ctypes` & `tabulate` libraries need to be installed
    - sample output : 

![Alt text](https://github.com/0xb1tByte/MalDev-Journey/blob/main/Scripts/procEnum_output.png)
