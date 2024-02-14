import subprocess
import os
import threading
from tkinter import Tk, Label, Button, Entry, filedialog, StringVar, ttk

class GModServerInstaller:
    def __init__(self, root):
        self.root = root
        root.title("GMod Server Installer")

        style = ttk.Style()
        style.theme_use('clam')

        self.steamcmd_path = StringVar()
        self.gmod_server_dir = StringVar()

        ttk.Label(root, text="SteamCMD Pfad:").pack(pady=5)
        self.steamcmd_path_entry = ttk.Entry(root, textvariable=self.steamcmd_path, width=50)
        self.steamcmd_path_entry.pack(pady=5)
        ttk.Button(root, text="Durchsuchen", command=self.browse_steamcmd_path).pack(pady=5)

        ttk.Label(root, text="GMod Server Pfad:").pack(pady=5)
        self.gmod_server_dir_entry = ttk.Entry(root, textvariable=self.gmod_server_dir, width=50)
        self.gmod_server_dir_entry.pack(pady=5)
        ttk.Button(root, text="Durchsuchen", command=self.browse_gmod_server_dir).pack(pady=5)

        self.install_button = ttk.Button(root, text="Installieren", command=self.start_installation)
        self.install_button.pack(pady=20)

        self.progress = ttk.Progressbar(root, orient="horizontal", length=400, mode="determinate")
        self.progress.pack(pady=10)

    def browse_steamcmd_path(self):
        directory = filedialog.askdirectory()
        self.steamcmd_path.set(directory)

    def browse_gmod_server_dir(self):
        directory = filedialog.askdirectory()
        self.gmod_server_dir.set(directory)

    def update_progress(self, progress):
        self.progress['value'] = progress
        self.root.update_idletasks()

    def simulate_progress(self):
        # Simuliere den Fortschritt
        for _ in range(100):
            self.update_progress(self.progress['value'] + 1)
            time.sleep(0.1)  # Pausiert für 0.1 Sekunden, um den Fortschritt zu simulieren

    def install_gmod_server(self):
        steamcmd_path = self.steamcmd_path.get()
        gmod_server_dir = self.gmod_server_dir.get()
        gmod_appid = "4020"
        login = "anonymous"

        if not os.path.exists(steamcmd_path):
            print("SteamCMD nicht gefunden. Bitte überprüfe den Pfad.")
            return

        install_command = f"\"{steamcmd_path}\\steamcmd.exe\" +login {login} +force_install_dir \"{gmod_server_dir}\" +app_update {gmod_appid} validate +quit"
        try:
            subprocess.run(install_command, shell=True, check=True)
            print("Installation abgeschlossen.")
        except subprocess.CalledProcessError as e:
            print(f"Fehler bei der Installation: {e}")

    def start_installation(self):
        self.progress['value'] = 0
        threading.Thread(target=self.simulate_progress).start()  # Startet die Fortschrittssimulation in einem separaten Thread
        threading.Thread(target=self.install_gmod_server).start()  # Startet die Installation in einem separaten Thread

def main():
    root = Tk()
    app = GModServerInstaller(root)
    root.mainloop()

if __name__ == "__main__":
    main()
