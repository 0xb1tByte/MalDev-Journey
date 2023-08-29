# By : Alaa 
# Usage : python ProcEnum.py <processName>
# Example : python ProcEnum.py notepad.exe
import ctypes # to access Win API
import tabulate  # to print the processes table
import sys # to get input from console

# Load the kernel32 library
kernel32 = ctypes.windll.kernel32

# Define the PROCESSENTRY32 structure ( this structure contains process information such as the name of the executable file, the pid ..etc)
class PROCESSENTRY32(ctypes.Structure):
    _fields_ = [
        ("dwSize", ctypes.c_ulong),
        ("cntUsage", ctypes.c_ulong),
        ("th32ProcessID", ctypes.c_ulong),
        ("th32DefaultHeapID", ctypes.c_void_p),
        ("th32ModuleID", ctypes.c_ulong),
        ("cntThreads", ctypes.c_ulong),
        ("th32ParentProcessID", ctypes.c_ulong),
        ("pcPriClassBase", ctypes.c_long),
        ("dwFlags", ctypes.c_ulong),
        ("szExeFile", ctypes.c_char * 260)
    ]

# Initialize the PROCESSENTRY32 structure
pe32 = PROCESSENTRY32() # creates an instance of the PROCESSENTRY32 structure
pe32.dwSize = ctypes.sizeof(PROCESSENTRY32) # sets the dwSize field of the pe32 instance to the size of the PROCESSENTRY32 structure in bytes

# Define CreateToolhelp32Snapshot params
TH32CS_SNAPPROCESS = 0x00000002 # Includes all processes in the system in the snapshot

# Define Constants
INVALID_HANDLE_VALUE = -1
processList = [] # Create an empty list to store the process name and pid


# This function performs process enumeration to determine all the running processes
# 	Win API functions used to perform process enumeration:
#  		- CreateToolhelp32Snapshot: https://learn.microsoft.com/en-us/windows/win32/api/tlhelp32/nf-tlhelp32-createtoolhelp32snapshot
#  		- Process32First: https://learn.microsoft.com/en-us/windows/win32/api/tlhelp32/nf-tlhelp32-process32first
#  		- Process32Next: https://learn.microsoft.com/en-us/windows/win32/api/tlhelp32/nf-tlhelp32-process32next
def ProcEnum (processName):
	# Create a snapshot of all processes
	hProcessSnap = kernel32.CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, None)

	# Check if the handle is valid
	if hProcessSnap == INVALID_HANDLE_VALUE:
	    print("Error: CreateToolhelp32Snapshot failed")
	else:
	    # Get the first process from the snapshot using Process32First
	    success = kernel32.Process32First(hProcessSnap, ctypes.byref(pe32))

	    # Loop through all the processes
	    while success:
	    	# append the process info to the list
	    	processList.append([pe32.szExeFile.decode(), pe32.th32ProcessID])
	    	# Check if the process name is processName
	    	if pe32.szExeFile.decode() == processName:
	            # Print the process ID 
	            print("[+] Found ", processName,"with process ID:", pe32.th32ProcessID, "\n")
	    	# Get the next process from the snapshot using Process32Next
	    	success = kernel32.Process32Next(hProcessSnap, ctypes.byref(pe32))
	    # Format the list into a table using tabulate
	    table = tabulate.tabulate(processList, headers=["Process Name", "PID"], stralign="left")
	    # Print the table
	    print("[+] Processes Enumeration: \n")
	    print(table)
	# Close the handle
	kernel32.CloseHandle(hProcessSnap)


if __name__ == "__main__":
	processName = sys.argv[1]
	ProcEnum (processName)
