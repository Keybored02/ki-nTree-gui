# Ki-nTree KiCad Plugin

A KiCad plugin to access the Ki-nTree module directly from the toolbar

---

## Requirements

No dependencies are required. All necessary Python libraries should have come bundled with KiCad.

Ki-nTree has to be installed and configured first. Follow the instruction at [sparkmicro/Ki-nTree](https://github.com/sparkmicro/Ki-nTree). If installing on WIndows, make sure that `kintree` can be called as a command in CLI by adding it to your PATH system variable.

This plugin was tested with KiCad `8.5.0`.

## Usage: KiCad Integration

In KiCad's PCB Editor, navigate to the `Tools` mene and select `Open Plugin directory`

![Image1](/pluign_menu_1.png)

Copy the `Ki-nTree` folder to the plugin directory. Then `Refresh Plugins` in KiCad.

A new icon should appear on the toolbar and in the dropdown menu. 

## Usage: Executable

Alternatively, a `Ki-nTree.exe` file is provided to run the utility directly, withouth a terminal. Basic error logging is provided. 

## Notes

This plugin uses part of the [ActionPlugin Template](https://github.com/adamws/kicad-plugin-template) developed by [adamws](https://github.com/adamws)

The icon used is taken from the Ki-nTree project. For license information refer to their [repo](https://github.com/sparkmicro/Ki-nTree).
