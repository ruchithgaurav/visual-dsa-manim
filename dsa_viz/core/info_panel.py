from manim import *

from dsa_viz.core.layout import LayoutManager


class InfoPanel(VGroup):
    """
    Left information panel.

    Displays algorithm metadata:
        • Time Complexity
        • Space Complexity
        • Stable
        • In-place
        • Notes

    Completely independent of the HUD.
    """

    def __init__(self):

        super().__init__()

        self.layout = None

        # ----------------------------------------------------
        # Background
        # ----------------------------------------------------

        self.bg = RoundedRectangle(
            width=3.6,
            height=2.6,
            corner_radius=0.15,
            fill_color="#1F2937",
            fill_opacity=0.95,
            stroke_color=GRAY,
            stroke_width=1
        )

        # ----------------------------------------------------
        # Title
        # ----------------------------------------------------

        self.title = Text(
            "Algorithm",
            font_size=24,
            weight=BOLD
        )

        # ----------------------------------------------------
        # Labels
        # ----------------------------------------------------

        self.time = Text(
            "Time : -",
            font_size=22,
            color=YELLOW
        )

        self.space = Text(
            "Space: -",
            font_size=22,
            color=YELLOW
        )

        self.extra = Text(
            "",
            font_size=20,
            color=GRAY
        )

        self.content = VGroup(
            self.title,
            self.time,
            self.space,
            self.extra
        )

        self.content.arrange(
            DOWN,
            aligned_edge=LEFT,
            buff=0.20
        )

        self.content.move_to(self.bg)

        self.add(
            self.bg,
            self.content
        )

    # =========================================================

    def attach_layout(self, layout: LayoutManager):

        self.layout = layout
        self.layout.place_info(self)

    # =========================================================

    def set_algorithm(self, name):

        self.title.become(

            Text(
                name,
                font_size=24,
                weight=BOLD
            ).move_to(self.title)

        )

    # =========================================================

    def set_complexity(self, time, space):

        self.time.become(

            Text(
                f"Time : {time}",
                font_size=22,
                color=YELLOW
            ).move_to(self.time)

        )

        self.space.become(

            Text(
                f"Space: {space}",
                font_size=22,
                color=YELLOW
            ).move_to(self.space)

        )

    # =========================================================

    def set_extra(self, text):

        self.extra.become(

            Text(
                text,
                font_size=20,
                color=GRAY
            ).move_to(self.extra)

        )