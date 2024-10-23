import os
import subprocess
import pcbnew
import wx

# from .example_dialog import ExampleDialog

class KinTree(pcbnew.ActionPlugin):
    def defaults(self) -> None:
        self.name = "Ki-nTree"
        self.category = "Part import"
        self.description = "Ki-nTree integration in KiCad"
        self.show_toolbar_button = True
        self.icon_file_name = os.path.join(os.path.dirname(__file__), "logo.png")

    def Run(self) -> None:
        # Command to run kintree
        command = ["kintree"]

        try:
            # Run the kintree command without opening a terminal window (background process)
            result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, creationflags=subprocess.CREATE_NO_WINDOW if os.name == 'nt' else 0)

        # Check if kintree ran successfully
        except subprocess.CalledProcessError as e:
            wx.LogError(f"Failed to run kintree: {str(e)}")
        except FileNotFoundError:
            wx.LogError("Kintree not found. Ensure it is installed and in the PATH.")