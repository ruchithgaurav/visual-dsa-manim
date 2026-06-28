import os
import sys

algo = sys.argv[1]
values = sys.argv[2:]

values_str = ",".join(values)

scene_map = {
    "bubble": ("dsa_viz/scenes/sorting_scene.py", "SortingScene"),
    "binary": ("dsa_viz/scenes/searching_scene.py", "SearchingScene"),
}

file, scene = scene_map[algo]

# --------------------------------------------------
# PASS DATA TO SCENES
# --------------------------------------------------
os.environ["DSA_INPUT"] = values_str

# --------------------------------------------------
# 2K RENDER CONFIG (IMPORTANT PART)
# --------------------------------------------------
PIXEL_WIDTH = 2560
PIXEL_HEIGHT = 1440
FPS = 60

cmd = (
    f"manim {file} {scene} "
    f"-pqh "
    f"-r {PIXEL_WIDTH},{PIXEL_HEIGHT} "
    f"--fps {FPS}"
)

os.system(cmd)