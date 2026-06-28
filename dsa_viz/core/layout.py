from dataclasses import dataclass
import numpy as np
from manim import *


# ==========================================================
# GLOBAL SCREEN LAYOUT
# ==========================================================

@dataclass(frozen=True)
class LayoutConfig:
    """
    Global layout configuration.

    Coordinate system:
        Center = (0, 0)

          TOP
    ------------------------
        Title

    Left      Array      Right
    Info                Code

        Bottom HUD
    ------------------------
    """

    # -----------------------------
    # Screen margins
    # -----------------------------
    TOP_MARGIN = 0.45
    SIDE_MARGIN = 0.60
    BOTTOM_MARGIN = 0.40

    # -----------------------------
    # Main Regions
    # -----------------------------
    TITLE = np.array([0.0, 3.35, 0])

    ARRAY = np.array([0.0, 0.35, 0])

    INFO = np.array([-5.55, 1.60, 0])

    CODE = np.array([5.55, 0.60, 0])

    HUD = np.array([0.0, -3.35, 0])

    # Floating messages
    MESSAGE = np.array([0.0, 2.55, 0])

    # Pointer offset
    POINTER_BUFFER = 0.18

    # Pseudocode
    CODE_SCALE = 0.75
    CODE_LINE_SPACING = 0.15


# ==========================================================
# LAYOUT MANAGER
# ==========================================================

class LayoutManager:

    def __init__(self, scene):
        self.scene = scene
        self.cfg = LayoutConfig()

    # -------------------------------------------------

    def place_title(self, obj):
        obj.move_to(self.cfg.TITLE)
        return obj

    # -------------------------------------------------

    def place_array(self, obj):
        obj.move_to(self.cfg.ARRAY)
        return obj

    # -------------------------------------------------

    def place_info(self, obj):
        obj.move_to(self.cfg.INFO)
        return obj

    # -------------------------------------------------

    def place_code(self, obj):
        obj.move_to(self.cfg.CODE)
        return obj

    # -------------------------------------------------

    def place_hud(self, obj):
        obj.move_to(self.cfg.HUD)
        return obj

    # -------------------------------------------------

    def place_message(self, obj):
        """
        Pass number, Early Exit, etc.
        """
        obj.move_to(self.cfg.MESSAGE)
        return obj

    # -------------------------------------------------

    def pointer_buffer(self):
        return self.cfg.POINTER_BUFFER


# ==========================================================
# DRAW ORDER
# ==========================================================

def lock_layer(obj, z=10):
    obj.set_z_index(z)
    return obj