def Detection():
    import subprocess

    script_path = "C:\\Users\\user\\PycharmProjects\\TG-food\\test.PS1"  # POWERSHELL SCRIPT PATH
    commandline_options = ["Powershell.exe", '-ExecutionPolicy', 'Unrestricted', script_path]  # INITIALIZING COMMAND

    result = subprocess.run(commandline_options, stdout = subprocess.PIPE, stderr = subprocess.PIPE, universal_newlines = True)  # RUN THE SCRIPT USING SUBPROCESS WITH PARAMS

    print(result.stdout)  # PRINT THE STANDARD OUTPUT FROM POWERSHELL SCRIPT