![GitHub Downloads (all assets, all releases)](https://img.shields.io/github/downloads/danilodelucio/PrettyNuke/total?style=for-the-badge)

<img width="1920" height="760" alt="PrettyNuke - Cover v2 (Large)" src="https://github.com/user-attachments/assets/1a13c4bf-db92-4845-8687-dbfd8f48fb94" />



# 🧩 Introduction
**PrettyNuke** is a Theme Manager for Nuke that allows users to create and share UI themes across different Nuke versions.

<img width="1108" height="601" alt="PrettyNuke Preferences v1" src="https://github.com/user-attachments/assets/251d1fe5-7b67-4cd2-a094-738fb3ff9ed8" />

<img width="1146" height="480" alt="applying_themes_v1" src="https://github.com/user-attachments/assets/c1cd94ca-a8bb-45b2-98f4-c7a7f39df7b6" />


# 📦 Built-in Themes
**PrettyNuke** comes with 10 ready-to-use themes, all inspired by popular UI themes and carefully set knob by knob. 

## Cyberpunk
<img width="1920" height="760" alt="Cyberpunk v1 (Large)" src="https://github.com/user-attachments/assets/9996096e-af3f-45ce-89b7-1dbe5353f1b8" />

## Diablo
<img width="1920" height="762" alt="Diablo v1 (Large)" src="https://github.com/user-attachments/assets/98f74005-5286-4c34-89ad-9a068cbe81d9" />

## Dracula
<img width="1920" height="761" alt="Dracula v1 (Large)" src="https://github.com/user-attachments/assets/83787b8d-8e61-4c18-8565-557cb45f8399" />

## Forest
<img width="1920" height="760" alt="Forest v1 (Large)" src="https://github.com/user-attachments/assets/4d4c96f1-b285-4d60-bc4a-e5d48d8f9f16" />

## Monokai Machine
<img width="1920" height="762" alt="Monokai Machine v1 (Large)" src="https://github.com/user-attachments/assets/41ca95f6-f732-4c74-bbff-528721e386fd" />

## Nightwish
<img width="1920" height="761" alt="Nightwish v1 (Large)" src="https://github.com/user-attachments/assets/883673a2-13ba-4790-9bc2-d7335386743f" />

## Nord Polar Night
<img width="1920" height="761" alt="Nord Polar Night v1 (Large)" src="https://github.com/user-attachments/assets/2406ab4b-b253-4c20-a326-198b69aa769c" />

## PrettyNuke
<img width="1920" height="760" alt="PrettyNuke v1 (Large)" src="https://github.com/user-attachments/assets/138d216d-6cf1-4220-b8e0-482778eca3a7" />

## Solarized
<img width="1920" height="760" alt="Solarized v1 (Large)" src="https://github.com/user-attachments/assets/927fcd16-e372-4d5a-a444-f611eb3961fd" />

## Starcraft
<img width="1920" height="759" alt="Starcraft v1 (Large)" src="https://github.com/user-attachments/assets/ff4ee112-49d5-4e58-89fd-4ff85c33ce70" />

# 🎨 Custom Themes
You can create custom themes by opening the **Custom Colors** section and changing the color knobs. 

<img width="1146" height="480" alt="custom_colors_v1" src="https://github.com/user-attachments/assets/8dbdaf19-1f30-4a71-b993-3f988019dd56" />

<br> Alternatively, if you want full control over all UI colors, you can update each knob color manually and then export your theme.

- _`Preferences -> Appearance | Node Colors | Node Graph | Viewer Handles`_

<img width="1146" height="480" alt="manually_v1" src="https://github.com/user-attachments/assets/3d9913a4-d281-496f-b490-be531a933ffd" />

# 🪄 Drag-and-Drop

You can drag and drop the `.nk` files into Nuke without needing to install **PrettyNuke**, this will set all color knobs from the selected theme (even for **Nuke Indie**).
> [!NOTE]
> _If you choose this approach, don't forget to open the Preferences panel and hit OK to register the color changes into the preferences file._

<img width="1146" height="480" alt="drag_and_drop_v1" src="https://github.com/user-attachments/assets/8b0e9bbe-0024-4880-b16f-280699d4a2bd" />


# ☢️ Nuke and Python Compatibility
- **PrettyNuke** was developed and tested in **Nuke 12.1v5** and **Nuke 17.0v3** (written in Python 2 and Python 3), but it's designed to work across all Nuke versions.
- It works for commercial and non-commercial versions (except Indie due to the Python limitation).

# 📊 Performance
**PrettyNuke** does not use any kind of callbacks or expressions under the hood. It's designed to be fast and lightweight, without triggering extra code.

# 📥 Download & Install
- Download the latest release of **PrettyNuke**:

👉 [Download PrettyNuke](https://github.com/danilodelucio/PrettyNuke/releases/download/v01.1/PrettyNuke_v01.1.zip)

- Extract the **PrettyNuke** folder and place it inside your `.nuke` directory (usually located at `C:/Users/%USERNAME%/.nuke`).

- Open (or create) the `init.py` file inside `.nuke` and add the following line:

```
nuke.pluginAddPath('./PrettyNuke')
```

- Launch Nuke and go to _Preferences → PrettyNuke_ (or press `Shift` + `S`) to open the Preferences panel.

Enjoy!

# ☕ Support me!

![Supporters Page](https://danilodelucio.com/wp-content/uploads/2025/12/supporter-badges.jpg)

## Enjoying this tool?
Support me with a coffee on my [Supporters](https://www.danilodelucio.com/supporters) page — get a badge and join the wall of supporters! 😎

You can also ⭐ _star this repository_ ⭐ — it helps a lot with visibility and motivates me to keep developing tools for VFX.

Sharing this project or sending me a positive message would help me in the same way.
