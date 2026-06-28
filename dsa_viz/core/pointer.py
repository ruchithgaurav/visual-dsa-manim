from manim import *


class Pointer(VGroup):
    """
    Animated pointer used to indicate array indices.
    """

    def __init__(self, label, color=YELLOW):
        super().__init__()

        self.color = color

        # ---------------- Label ----------------
        self.text = Text(
            label,
            font_size=24,
            color=color,
            weight=BOLD,
        )

        # ---------------- Arrow ----------------
        self.arrow = Arrow(
            start=UP * 0.45,
            end=DOWN * 0.05,
            buff=0,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.35,
            color=color,
        )

        self.arrow.next_to(self.text, DOWN, buff=0.05)

        self.add(self.text, self.arrow)

        self.set_z_index(20)

    # --------------------------------------------------
    # Move pointer above a cell
    # --------------------------------------------------

    def move_to_cell(self, cell):
        target = cell.get_top() + UP * 0.45

        return self.animate.move_to(target)

    # --------------------------------------------------
    # Optional emphasis animation
    # --------------------------------------------------

    def pulse(self):
        return Succession(
            self.animate.scale(1.15),
            self.animate.scale(1 / 1.15),
        )