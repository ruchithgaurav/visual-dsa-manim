from manim import *

from dsa_viz.core.voice import generate


class AnimationEngine:

    def __init__(self, scene):

        self.scene = scene

        self.result = None
        self.steps = None
        self.narration = None

        self.narration_index = 0

    # -------------------------------------------------
    # ENTRY
    # -------------------------------------------------

    def run(self, result):

        self.result = result

        self.steps = result["steps"]
        self.narration = result["narration"]

        for step in self.steps:

            self.execute(step)

            self.scene.wait(0.1)

    # -------------------------------------------------
    # DISPATCH
    # -------------------------------------------------

    def execute(self, step):

        op = step[0]

        self.scene.hud.update_step()
        self.scene.hud.update_op(op)

        dispatch = {

            "intro": self.intro,

            "pass": self.pass_step,

            "compare": self.compare,

            "swap": self.swap,

            "noswap": self.no_swap,

            "sorted": self.sorted,

            "finished": self.finished,

            "complete": self.complete

        }

        if op in dispatch:

            dispatch[op](step)

    # -------------------------------------------------
    # NARRATION
    # -------------------------------------------------

    def speak(self):

        if self.narration_index >= len(self.narration):
            return

        info = self.narration[self.narration_index]

        audio = generate(
            info["voice"],
            self.result["title"],
            self.narration_index
        )

        self.scene.add_sound(audio)

        self.narration_index += 1

    # -------------------------------------------------
    # ACTIONS
    # -------------------------------------------------

    def intro(self, step):

        self.speak()

        self.scene.wait(.8)

    def pass_step(self, step):

        self.speak()

        banner = Text(
            f"Pass {step[1]+1}",
            font_size=34,
            color=YELLOW
        )

        banner.move_to([0, 2.4, 0])

        self.scene.play(FadeIn(banner))

        self.scene.wait(.5)

        self.scene.play(FadeOut(banner))

    def compare(self, step):

        i = step[1]
        j = step[2]

        self.scene.play(

            self.scene.i_pointer.move_to_cell(
                self.scene.array.cells[i]
            ),

            self.scene.j_pointer.move_to_cell(
                self.scene.array.cells[j]
            ),

            run_time=.3

        )

        self.scene.highlight(i, j)

    def swap(self, step):

        self.scene.swap(
            step[1],
            step[2]
        )

    def no_swap(self, step):

        self.scene.wait(.15)

    def sorted(self, step):

        self.speak()

        self.scene.mark_sorted(step[1])

    def finished(self, step):

        self.speak()

        txt = Text(
            "Early Exit",
            color=GREEN,
            font_size=36
        )

        txt.move_to([0,2.4,0])

        self.scene.play(FadeIn(txt))

        self.scene.wait(.8)

        self.scene.play(FadeOut(txt))

    def complete(self, step):

        self.speak()

        txt = Text(
            "Array Sorted!",
            color=GREEN,
            font_size=42
        )

        txt.next_to(
            self.scene.array,
            DOWN,
            buff=.6
        )

        self.scene.play(Write(txt))

        self.scene.wait(2)