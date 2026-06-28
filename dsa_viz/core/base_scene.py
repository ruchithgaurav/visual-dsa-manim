from manim import *

from dsa_viz.core.layout import LayoutManager, lock_layer


class DSAScene(Scene):

    # ======================================================
    # Scene Setup
    # ======================================================

    def setup(self):
        super().setup()

        self.layout = LayoutManager(self)

    # ======================================================
    # Title
    # ======================================================

    def setup_title(self, text):

        self.title = Text(
            text,
            font_size=48,
            color=WHITE,
            weight=BOLD
        )

        self.layout.place_title(self.title)

        lock_layer(self.title, 20)

        self.play(Write(self.title))

    # ======================================================
    # Array
    # ======================================================

    def setup_array(self, values):

        from dsa_viz.core.array import ArrayViz

        self.values = values

        self.array = ArrayViz(values)

        self.layout.place_array(self.array)

        lock_layer(self.array, 15)

        self.play(FadeIn(self.array))

    # ======================================================
    # HUD
    # ======================================================

    def setup_hud(self):

        from dsa_viz.core.hud import HUD

        self.hud = HUD()

        self.hud.attach_layout(self.layout)

        lock_layer(self.hud, 30)

        self.add(self.hud)

    # ======================================================
    # Info Panel
    # ======================================================

    def setup_info_panel(
        self,
        algorithm,
        time_complexity,
        space_complexity,
        extra=""
    ):

        from dsa_viz.core.info_panel import InfoPanel

        self.info_panel = InfoPanel()

        self.info_panel.attach_layout(self.layout)

        self.info_panel.set_algorithm(algorithm)

        self.info_panel.set_complexity(
            time_complexity,
            space_complexity
        )

        self.info_panel.set_extra(extra)

        lock_layer(self.info_panel, 20)

        self.add(self.info_panel)

    # ======================================================
    # Highlight
    # ======================================================

    def highlight(self, i, j):

        self.play(

            self.array.cells[i].highlight(),

            self.array.cells[j].highlight(),

            run_time=0.25

        )

    # ======================================================
    # Swap
    # ======================================================

    def swap(self, i, j):

        self.play(

            self.array.swap_visual(i, j),

            run_time=0.45

        )

        self.values[i], self.values[j] = (
            self.values[j],
            self.values[i]
        )

        self.array.cells[i], self.array.cells[j] = (
            self.array.cells[j],
            self.array.cells[i]
        )

    # ======================================================
    # Sorted
    # ======================================================

    def mark_sorted(self, index):

        self.play(

            self.array.cells[index].sorted(),

            run_time=0.25

        )