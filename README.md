# Scripts
- `ProcEnum.py` : Processes Enumeration using Win APIs
   - Win API functions used to perform process enumeration:
      - [`CreateToolhelp32Snapshot`](https://learn.microsoft.com/en-us/windows/win32/api/tlhelp32/nf-tlhelp32-createtoolhelp32snapshot)
      - [`Process32First`](https://learn.microsoft.com/en-us/windows/win32/api/tlhelp32/nf-tlhelp32-process32first)
      - [`Process32Next`](https://learn.microsoft.com/en-us/windows/win32/api/tlhelp32/nf-tlhelp32-process32next)
    - Usage : `python ProcEnum.py <processName>`
    - Example : `python ProcEnum.py notepad.exe`
    - requirments : `tabulate` library needs to be installed, you can install it using `pip install tabulate`
    - sample output : 

![Alt text](procEnum_output.PNG)