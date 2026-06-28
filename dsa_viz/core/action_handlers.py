from manim import *

from dsa_viz.core.voice import generate


class ActionHandlers:

    def __init__(self, scene):

        self.scene = scene

        self.result = None
        self.narration = None
        self.index = 0

    # ---------------------------------------------------
    # Initialize
    # ---------------------------------------------------

    def initialize(self, result):

        self.result = result
        self.narration = result["narration"]

    # ---------------------------------------------------
    # Narration
    # ---------------------------------------------------

    def speak(self):

        if self.index >= len(self.narration):
            return

        info = self.narration[self.index]

        audio = generate(
            info["voice"],
            self.result["title"],
            self.index
        )

        self.scene.add_sound(audio)

        self.index += 1

    # ---------------------------------------------------
    # Pointer Movement
    # ---------------------------------------------------

    def compare(self, i, j):

        self.scene.play(

            self.scene.i_pointer.move_to_cell(
                self.scene.array.cells[i]
            ),

            self.scene.j_pointer.move_to_cell(
                self.scene.array.cells[j]
            ),

            run_time=0.3

        )

        self.scene.highlight(i, j)

    # ---------------------------------------------------
    # Swap
    # ---------------------------------------------------

    def swap(self, i, j):

        self.scene.swap(i, j)

    # ---------------------------------------------------
    # Sorted
    # ---------------------------------------------------

    def sorted(self, index):

        self.scene.mark_sorted(index)

    # ---------------------------------------------------
    # Banner
    # ---------------------------------------------------

    def banner(self, text, color=YELLOW):

        banner = Text(
            text,
            font_size=34,
            color=color
        )

        banner.move_to([0, 2.4, 0])

        self.scene.play(FadeIn(banner))
        self.scene.wait(.6)
        self.scene.play(FadeOut(banner))