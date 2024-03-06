import subprocess
import os
from colorama import Fore, Style

current_cmd="null"
current_directory = os.path.dirname(os.path.abspath(__file__))
powershell_directory = os.path.join(current_directory, "PowerShell")


print("===========================")
print("Willkommen im mini Shell!")
print("===========================")
print()
print("Gebe 'help' ein um hilfe zu bekommen.")
print()

def start_powershell_script(script_path):
    try:
        subprocess.run(["powershell", "-File", script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Fehler beim Ausführen des Powershell-Skripts: {e}")

def main_menu():
    current_cmd = input("Tool $ ")

    if current_cmd == "test":
        print("Es wurde getestet :D")
        main_menu()
    
    elif current_cmd == "help":
        print()
        print(Fore.CYAN + "test  " + Style.RESET_ALL + "- Befehl um das Programm zu testen")
        print(Fore.CYAN + "help " + Style.RESET_ALL + "- Hilfe zum Programm" )
        print(Fore.CYAN + "exit " + Style.RESET_ALL + "- Das Programm beenden")
        print(Fore.CYAN + "scoop-initial-setup " + Style.RESET_ALL + "- Installiere Scoop")
        print(Fore.CYAN + "uninstall-scoop " + Style.RESET_ALL + "- Deinstalliere Scoop")        
        print()
        main_menu()
    
    elif current_cmd == "scoop-initial-setup":
        print("Das Installationsprogramm für weitere Programme wird installiert. Bitte warten...")
        start_powershell_script(os.path.join(powershell_directory, "install_scoop.ps1"))
        main_menu()
    
    elif current_cmd == "uninstall-scoop":
        print("Scoop wird deinstalliert. Bitte warten...")
        start_powershell_script(os.path.join(powershell_directory, "uninstall_scoop.ps1"))
        print(Fore.GREEN + "Scoop wurde Erfolgreich installiert" + Style.RESET_ALL)

        main_menu()

    elif current_cmd == "exit":
        print("Auf Wiedersehen :)")

    else:
        print(Fore.RED + "Dieser Befehl ist nicht vorhanden. Überprüfe ggf. die Schreibweise." + Style.RESET_ALL)
        main_menu()


if __name__ == "__main__":
    main_menu()