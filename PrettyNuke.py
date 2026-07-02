# -----------------------------------------------------------------------------------
#  PrettyNuke
#  Version: v01.1
#  Author: Danilo de Lucio
#  Website: www.danilodelucio.com
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
#  [Summary]
#  Theme manager for Nuke.
# -----------------------------------------------------------------------------------


import nuke
import os
import json


PRETTYNUKE_DIR = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/")

THEMES_DIR = os.path.join(PRETTYNUKE_DIR, "themes").replace("\\", "/")
if not os.path.exists(THEMES_DIR):
    os.makedirs(THEMES_DIR)

CONFIG_DIR = os.path.join(PRETTYNUKE_DIR, "config").replace("\\", "/")
if not os.path.exists(CONFIG_DIR):
    os.makedirs(CONFIG_DIR)

CONFIG_FILE = os.path.join(CONFIG_DIR, "config.json")

UI_COLORS = [
    # LOCALIZATION
    ## Progress Bar
    "localizationCompletedColor",
    "localizationProgressColor",
    "localizationOutdatedColor",

    # APPEARANCE
    ## Font
    "UIFont",
    "UIFontSize",

    ## UI Colors
    "UIBackColor",
    "UIBaseColor",
    "UIHighlightColor",
    "UIHighlightedTextColor",
    "UILabelColor",
    "UIButtonColor",
    "UIAnimatedColor",
    "UIKeyframeColor",
    "UIDiskCacheFrameColor",
    "RAMCacheFrameColor",
    "UIFrameSliderHeadColor",
    "UIFrameSliderInOutColor",
    "UIPredictedKeyframeColor",
    "ClipAnnotationMarkerColor",
    "SequenceAnnotationMarkerColor",
    "ShadeDAGNodes", # Nodes shading

    ## Curve Editor / DopeSheet
    "DopeSheetBackground",
    "DopeSheetUnselectedKey",
    "DopeSheetPartSelectedKey",
    "DopeSheetSelectedKey",
    "DopeSheetTimeline",
    "DopeSheetControlText",
    "DopeSheetControlTextShadow",
    "DopeSheetTimeLabel",
    "DopeSheetCurrentFrame",
    "DopeSheetFrameRange",

    # NODE GRAPH
    "DAGBackColor",
    "OverlayColor", # Box selection
    "ArrowColorElbow", # Dots when holding Ctrl

    "NodeColor",
    "LabelColor",
    "SelectedColor",
    "SelectedInputLabelColor",
    "DefaultNodeGLColor",

    ## Bounding Box Warning
    "boundingBoxWarningColor",
    "boundingBoxWarningLineColor",

    ## Arrows
    "ArrowColorLeft",
    "ArrowColorRight",
    "ArrowColorUp",
    "ArrowColorDown",
    "deep_arrow_color",
    "link_knob_arrow_color",
    "clone_arrow_color",
    "expression_arrow_color",
    "link_node_arrow_color",

    # VIEWER HANDLES
    "viewer_bg_color",
    "viewer_fg_color",
    "viewer_bg_color_3D",
    "viewer_fg_color_3D",
    "viewer_sel_color_3D",
    "viewer_min_sel_color_3D",
    "UISplineExpressionColor",
    "UISplineFocusColor",
    "UIRotoPointColor",
    "UIRotoCurveColor",
    "UIRotoTransformJackColor",
    "UIRotoLockedColor",
    "UISplineWarperASourceColor",
    "UISplineWarperBSourceColor",
    "UISplineWarperADestColor",
    "UISplineWarperBDestColor",
    "UISplineWarperCorrespondenceColor",
    "UISplineWarperBoundaryColor",
    "UISplineWarperCutoutColour",
]

NODE_COLORS = [
    # NODE COLORS
    "NodeColourCacheColor",
    "NodeColourDeepColor",
    "NodeColour01Color",
    "NodeColour02Color",
    "NodeColour03Color",
    "NodeColour04Color",
    "NodeColour05Color",
    "NodeColour06Color",
    "NodeColour07Color",
    "NodeColour08Color",
    "NodeColour09Color",
    "NodeColour10Color",
    "NodeColour11Color",
    "NodeColour12Color",
    "NodeColour13Color",

    "NodeColourChoice01",
    "NodeColourChoice02",
    "NodeColourChoice03",
    "NodeColourChoice04",
    "NodeColourChoice05",
    "NodeColourChoice06",
    "NodeColourChoice07",
    "NodeColourChoice08",
    "NodeColourChoice09",
    "NodeColourChoice10",
    "NodeColourChoice11",
    "NodeColourChoice12",
    "NodeColourChoice13",
    "NodeColourChoice14",
    "NodeColourChoice15",
    "NodeColourChoice16",
    "NodeColourChoice17",
    "NodeColourChoice18",
    "NodeColourChoice19",
    "NodeColourChoice20",
]


def check_themeFiles():
    themes_list = ["<Please select a theme>"]

    for file in os.listdir(THEMES_DIR):
        if "json" in file:
            file_name = file.split(".")[0]
            themes_list.append(file_name)

    themes_list.sort()
    len_themes_list = len(themes_list)

    if len_themes_list > 0:
        return themes_list
    else:
        print("[PrettyNuke Error] - No themes found in themes folder.")
        return False


def get_pref_values():
    prefs = nuke.toNode("preferences")
    node_colors = prefs["pn_export_node_colors"].value()
    prefs_dict = {}

    # Getting all the Preferences knobs
    for knob_name, knob in prefs.knobs().items():
        if hasattr(knob, "value"):
            prefs_dict[knob_name] = knob.value()

    final_dict = {}

    # Comparing with UI_COLORS and NODE_COLORS if enabled
    for knob_name in prefs_dict:
        if knob_name in UI_COLORS:
            final_dict[knob_name] = prefs_dict[knob_name]

        if node_colors: # If Node Colors option is enabled
            if knob_name in NODE_COLORS:
                final_dict[knob_name] = prefs_dict[knob_name]

    final_dict = dict(sorted(final_dict.items()))
    return final_dict


def export_theme_nk_file(prefDict, themeName):
    # Nuke file content (txt)
    lines = []
    lines.append("Preferences {")
    lines.append("    inputs 0")
    lines.append("    name Preferences")

    for knob_name, knob_value in prefDict.items():
        # Checking if string has space (like font "Segoe UI")
        if isinstance(knob_value, str) and " " in knob_value:
            lines.append('    {} "{}"'.format(knob_name, knob_value))
        else:
            lines.append("    {} {}".format(knob_name, knob_value))

    lines.append("}")
    nk_text = "\n".join(lines)

    # Creating Nuke file
    output_path = os.path.join(THEMES_DIR, themeName + ".nk").replace("\\", "/")

    with open(output_path, "w") as f:
        f.write(nk_text)


def export_theme():
    pref_dict = get_pref_values()

    theme_data = {}

    for k, v in pref_dict.items():
        theme_data[k] = v

    # Theme name
    theme_name = nuke.getInput("Theme name:", "")
    if not theme_name:
        print("PrettyNuke - Canceled by the user!")
        return

    # Creating JSON file (theme.json)
    output_path = os.path.join(THEMES_DIR, theme_name + ".json").replace("\\", "/")
    theme_data = dict(sorted(theme_data.items()))

    with open(output_path, "w") as f:
        json.dump(theme_data, f, indent=2)

    # Creating .nk file (if enabled)
    prefs = nuke.toNode("preferences")
    export_nk_file_knob = prefs["pn_export_nk_file"].value()
    if export_nk_file_knob:
        export_theme_nk_file(pref_dict, theme_name)

    nuke.message("Your PrettyNuke Theme has been exported to:\n{}".format(output_path))


def apply_theme():
    prefs = nuke.toNode("preferences")
    selected_theme = prefs["pn_select_theme"].value()

    theme_file = os.path.join(THEMES_DIR, selected_theme + ".json").replace("\\", "/")

    if os.path.exists(theme_file):
        # Opening Theme.json file
        with open(theme_file, "r") as f:
            theme_file_dict = json.load(f)

        for knob_name, knob_value in theme_file_dict.items():
            try:
                prefs[knob_name].setValue(knob_value)

            except:
                print("[PrettyNuke] - '{}' knob not found!".format(knob_name))

            finally:
                pass

        nuke.message("The '{}' theme has been applied!".format(selected_theme))

    else:
        nuke.message("[PrettyNuke Error] - The theme '{}' does not exist!".format(selected_theme))


def load_themes():
    try:
        prefs = nuke.toNode("preferences")
    
    except:
        prefs = nuke.thisNode()
    
    themes_list = check_themeFiles()

    if themes_list:
        selected_theme = themes_list[0]

        prefs["pn_select_theme"].setValues(themes_list)
        prefs["pn_select_theme"].setValue(selected_theme)


def delete_theme():
    prefs = nuke.thisNode()
    selected_theme = prefs["pn_select_theme"].value()

    theme_file = os.path.join(THEMES_DIR, selected_theme + ".json").replace("\\", "/")
    ask_msg = ("Delete theme '{}'? \n\nThis will permanently remove the theme file.\nThis action cannot be undone.").format(selected_theme)
    
    if os.path.exists(theme_file):
        if nuke.ask(ask_msg):
            os.remove(theme_file)
            nuke.message("The '{}' theme has been deleted!".format(selected_theme))
            load_themes()
    else:
        nuke.message("[PrettyNuke Error] - The selected theme does not exist!")


def load_prefsPanel():
    nuke.scriptReadFile(os.path.join(CONFIG_DIR, "pn_pref.nk").replace("\\", "/"))


def open_themes_folder():
    os.startfile(THEMES_DIR)

