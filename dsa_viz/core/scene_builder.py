from manim import *

from dsa_viz.core.pointer import Pointer


class SceneBuilder:
    """
    Responsible only for building the visual layout.

    It creates:
        • Title
        • Array
        • HUD
        • Pseudocode
        • Pointers

    No animations.
    No algorithm logic.
    """

    def __init__(self, scene):
        self.scene = scene

    # ----------------------------------------------------
    # PUBLIC
    # ----------------------------------------------------

    def build(self, result, values):

        self.build_title(result["title"])

        self.build_array(values)

        self.build_hud(
            result["complexity"],
            result["ui"]
        )

        self.build_pseudocode(
            result["pseudocode"]
        )

        self.build_pointers()

    # ----------------------------------------------------
    # TITLE
    # ----------------------------------------------------

    def build_title(self, title):

        self.scene.setup_title(title)

    # ----------------------------------------------------
    # ARRAY
    # ----------------------------------------------------

    def build_array(self, values):

        self.scene.setup_array(values)

    # ----------------------------------------------------
    # HUD
    # ----------------------------------------------------

    def build_hud(self, complexity, ui):

        self.scene.setup_hud()

        self.scene.hud.set_complexity(
            f"Time: {complexity['time']}    "
            f"Space: {complexity['space']}"
        )

        self.scene.hud.update_op(
            ui.get("default_op", "-")
        )

    # ----------------------------------------------------
    # PSEUDOCODE
    # ----------------------------------------------------

    def build_pseudocode(self, lines):

        pseudo = VGroup()

        for line in lines:

            pseudo.add(

                Text(
                    line,
                    font_size=20,
                    color=GRAY
                )

            )

        pseudo.arrange(
            DOWN,
            aligned_edge=LEFT,
            buff=0.15
        )

        pseudo.scale(0.75)

        self.scene.layout.place_code(pseudo)

        self.scene.add(pseudo)

        # Save reference for later highlighting
        self.scene.pseudocode = pseudo

    # ----------------------------------------------------
    # POINTERS
    # ----------------------------------------------------

    def build_pointers(self):

        self.scene.i_pointer = Pointer(
            "i",
            color=YELLOW
        )

        self.scene.j_pointer = Pointer(
            "j",
            color=BLUE
        )

        self.scene.add(
            self.scene.i_pointer,
            self.scene.j_pointer
        )