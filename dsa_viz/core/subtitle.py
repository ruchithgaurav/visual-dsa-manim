from manim import *


class Subtitle(VGroup):

    def __init__(self):
        super().__init__()

        # Background
        self.bg = RoundedRectangle(
            width=12,
            height=1.2,
            corner_radius=0.18,
            fill_color=BLACK,
            fill_opacity=0.85,
            stroke_color=GRAY,
            stroke_width=1,
        )

        # Empty text initially
        self.text = Text(
            "",
            font_size=28,
            color=WHITE,
        )

        self.text.move_to(self.bg)

        self.add(self.bg, self.text)

        # ❌ REMOVED:
        # self.to_edge(DOWN, buff=0.25)

    # NEW: layout-controlled positioning
    def attach_layout(self, layout):
        """
        Let layout manager control subtitle position.
        """
        self.layout = layout
        layout.place_subtitle(self)

    def show(self, message: str):
        """
        Update subtitle with smooth animation.
        """

        new_text = Text(
            message,
            font_size=28,
            color=WHITE,
            line_spacing=0.9,
            should_center=True,
        )

        # Prevent overflow
        if new_text.width > self.bg.width - 0.5:
            new_text.scale((self.bg.width - 0.5) / new_text.width)

        new_text.move_to(self.bg.get_center())

        return Transform(
            self.text,
            new_text,
            replace_mobject_with_target_in_scene=True,
        )

    def clear(self):
        """
        Remove subtitle.
        """
        return self.show("")