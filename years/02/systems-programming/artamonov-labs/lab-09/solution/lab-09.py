import platform
import subprocess

def get_kernel_modules():
    current_platform = platform.system()
    
    if 'windows' in current_platform.lower():
        try:
            output = subprocess.check_output(args = ['driverquery'],
                                             universal_newlines = True)
        except UnicodeDecodeError:
            print('OS returned invalid Unicode string.')
            output = None
            
    elif 'darwin' in current_platform.lower():
        output = subprocess.check_output(args = ['kextstat'],
                                         universal_newlines = True)
                                         
    elif 'linux' in current_platform.lower():
        output = subprocess.check_output(args = ['lsmod'],
                                         universal_newlines = True)
                                         
    else:
        output = None
        
    return output

def main():
    kernel_modules = get_kernel_modules()
    print(kernel_modules)
    if kernel_modules is not None:
        print(kernel_modules)
    else:
        print('Unsupported platform')
        
main()
