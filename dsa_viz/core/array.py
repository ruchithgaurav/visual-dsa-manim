from manim import *
from dsa_viz.core.colors import *


class ArrayCell(VGroup):

    CELL_SIZE = 1.0

    def __init__(self, value):
        super().__init__()

        self.value = value

        # ---------------- Box ----------------
        self.rect = RoundedRectangle(
            width=self.CELL_SIZE,
            height=self.CELL_SIZE,
            corner_radius=0.12,
            fill_color=BOX_COLOR,
            fill_opacity=1,
            stroke_color=WHITE,
            stroke_width=2,
        )

        # ---------------- Value ----------------
        self.text = Text(
            str(value),
            font_size=30,
            color=TEXT,
        )

        self.text.move_to(self.rect.get_center())

        # ---------------- Index Placeholder ----------------
        self.index = Text(
            "",
            font_size=18,
            color=GRAY
        )

        self.index.next_to(self.rect, DOWN, buff=0.12)

        self.add(self.rect, self.text, self.index)

    # --------------------------------------------------

    def set_index(self, idx):
        new_index = Text(
            str(idx),
            font_size=18,
            color=GRAY
        )

        new_index.next_to(self.rect, DOWN, buff=0.12)

        self.index.become(new_index)

    # --------------------------------------------------

    def set_color(self, color):
        return self.rect.animate.set_fill(color)

    def highlight(self):
        return self.set_color(HIGHLIGHT)

    def normal(self):
        return self.set_color(BOX_COLOR)

    def swapping(self):
        return self.set_color(SWAP)

    def sorted(self):
        return self.set_color(SORTED)


# ==========================================================
# ARRAY VISUALIZATION
# ==========================================================

class ArrayViz(VGroup):

    MAX_WIDTH = 10.5

    def __init__(self, values):
        super().__init__()

        self.cells = VGroup()

        for i, value in enumerate(values):
            cell = ArrayCell(value)
            cell.set_index(i)
            self.cells.add(cell)

        self.cells.arrange(
            RIGHT,
            buff=0.18
        )

        # Automatically shrink if array becomes too wide
        if self.cells.width > self.MAX_WIDTH:
            self.cells.scale(self.MAX_WIDTH / self.cells.width)

        self.add(self.cells)

    # --------------------------------------------------

    def swap_visual(self, i, j):
        return Swap(
            self.cells[i],
            self.cells[j],
            run_time=0.5
        )