from manim import *

from dsa_viz.core.layout import LayoutManager


class HUD(VGroup):
    """
    Bottom status bar.

    Shows only runtime information.

    Permanent algorithm information like
    Time Complexity and Space Complexity
    belongs in the left info panel.
    """

    def __init__(self):
        super().__init__()

        self.step = 0

        # Layout manager reference
        self.layout = None

        # --------------------------------------------------
        # Background
        # --------------------------------------------------

        self.bg = RoundedRectangle(
            width=8,
            height=0.8,
            corner_radius=0.18,
            fill_color="#1F2937",
            fill_opacity=0.95,
            stroke_color=GRAY,
            stroke_width=1,
        )

        # --------------------------------------------------
        # Labels
        # --------------------------------------------------

        self.step_text = Text(
            "Step: 0",
            font_size=24,
            weight=BOLD
        )

        self.op_text = Text(
            "Operation: -",
            font_size=24,
            color=YELLOW
        )

        self.row = VGroup(
            self.step_text,
            self.op_text
        )

        self.row.arrange(
            RIGHT,
            buff=1.2
        )

        self.row.move_to(self.bg)

        self.add(
            self.bg,
            self.row
        )

    # ======================================================
    # Layout
    # ======================================================

    def attach_layout(self, layout: LayoutManager):

        self.layout = layout

        self.layout.place_hud(self)

    # ======================================================
    # Step
    # ======================================================

    def update_step(self):

        self.step += 1

        new_text = Text(
            f"Step: {self.step}",
            font_size=24,
            weight=BOLD
        )

        new_text.move_to(self.step_text)

        self.step_text.become(new_text)

    # ======================================================
    # Operation
    # ======================================================

    def update_op(self, operation):

        new_text = Text(
            f"Operation: {operation}",
            font_size=24,
            color=YELLOW
        )

        new_text.move_to(self.op_text)

        self.op_text.become(new_text)