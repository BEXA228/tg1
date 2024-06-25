mport subprocess

# Команда PowerShell, которую нужно выполнить
command = "conda activate yolo8"

# Запуск команды PowerShell из Python
result = subprocess.run(command, capture_output=True, text=True, shell=True)

# Вывод результата выполнения команды
print(result.stdout)
# conda activate yolo8 && python AI-train-yolo.py