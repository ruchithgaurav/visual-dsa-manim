from manim import *
from dsa_viz.core.layout import LayoutManager


class PseudoCode(VGroup):

    def __init__(self, lines):
        super().__init__()

        self.layout = None  # injected later
        self.lines = lines

        self.texts = VGroup()

        for line in lines:
            t = Text(line, font_size=24, color=GRAY)
            self.texts.add(t)

        self.texts.arrange(DOWN, aligned_edge=LEFT, buff=0.15)

        # ❌ REMOVE THIS (was causing overlap)
        # self.texts.to_corner(DR)

        self.add(self.texts)

    # =====================================================
    # ATTACH TO GLOBAL LAYOUT
    # =====================================================
    def attach_layout(self, layout: LayoutManager):
        self.layout = layout
        self.layout.place_code(self)

    # =====================================================
    # HIGHLIGHT LOGIC
    # =====================================================
    def highlight_line(self, idx):
        animations = []

        for i, t in enumerate(self.texts):
            color = YELLOW if i == idx else GRAY
            animations.append(t.animate.set_color(color))

        return animations