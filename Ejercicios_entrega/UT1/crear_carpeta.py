import os

desktop = os.path.join(os.path.expanduser("~"), "Desktop")
folder_name = "MiarchivoPython"

folder_path = os.path.join(desktop, folder_name)
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
    print(f"Carpeta creada en: {folder_path}")
else:
    print("La carpeta ya existe.")
