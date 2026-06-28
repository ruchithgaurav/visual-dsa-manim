from manim import *

from dsa_viz.core.base_scene import DSAScene
from dsa_viz.core.runtime import get_runtime_input
from dsa_viz.core.pointer import Pointer
from dsa_viz.core.voice import generate
from dsa_viz.algorithms.sorting.bubble_sort import bubble_sort


class SortingScene(DSAScene):

    def construct(self):

        self.camera.background_color = "#111827"

        # ------------------------------------------------
        # INPUT
        # ------------------------------------------------

        values = get_runtime_input()

        result = bubble_sort(values.copy())

        title = result["title"]
        steps = result["steps"]
        narration = result["narration"]
        pseudocode = result["pseudocode"]
        complexity = result["complexity"]
        ui = result["ui"]

        # ------------------------------------------------
        # TITLE
        # ------------------------------------------------

        self.setup_title(title)

        # ------------------------------------------------
        # ARRAY
        # ------------------------------------------------

        self.setup_array(values.copy())

        # ------------------------------------------------
        # INFO PANEL
        # ------------------------------------------------

        self.setup_info_panel(
            algorithm=title,
            time_complexity=complexity["time"],
            space_complexity=complexity["space"],
        )

        # ------------------------------------------------
        # HUD
        # ------------------------------------------------

        self.setup_hud()

        self.hud.update_op(
            ui.get("default_op", "Running")
        )

        # ------------------------------------------------
        # PSEUDOCODE
        # ------------------------------------------------

        pseudo = VGroup(*[
            Text(
                line,
                font_size=20,
                color=GRAY
            )
            for line in pseudocode
        ])

        pseudo.arrange(
            DOWN,
            aligned_edge=LEFT,
            buff=self.layout.cfg.CODE_LINE_SPACING
        )

        pseudo.scale(
            self.layout.cfg.CODE_SCALE
        )

        self.layout.place_code(pseudo)

        self.add(pseudo)

        # ------------------------------------------------
        # POINTERS
        # ------------------------------------------------

        i_ptr = Pointer("i", color=YELLOW)
        j_ptr = Pointer("j", color=BLUE)

        self.add(i_ptr, j_ptr)

        # ------------------------------------------------
        # NARRATION
        # ------------------------------------------------

        narration_index = 0

        def speak():

            nonlocal narration_index

            if narration_index >= len(narration):
                return

            info = narration[narration_index]

            audio = generate(
                info["voice"],
                title,
                narration_index
            )

            self.add_sound(audio)

            narration_index += 1

        # ------------------------------------------------
        # EXECUTION
        # ------------------------------------------------

        for step in steps:

            op = step[0]

            self.hud.update_step()
            self.hud.update_op(op)

            # --------------------------------------------

            if op == "intro":

                speak()
                self.wait(0.8)

            # --------------------------------------------

            elif op == "pass":

                speak()

                pass_text = Text(
                    f"Pass {step[1] + 1}",
                    color=YELLOW,
                    font_size=34
                )

                self.layout.place_message(pass_text)

                self.play(FadeIn(pass_text))
                self.wait(0.5)
                self.play(FadeOut(pass_text))

            # --------------------------------------------

            elif op == "compare":

                i, j = step[1], step[2]

                self.play(

                    i_ptr.animate.next_to(
                        self.array.cells[i],
                        UP,
                        buff=self.layout.pointer_buffer()
                    ),

                    j_ptr.animate.next_to(
                        self.array.cells[j],
                        UP,
                        buff=self.layout.pointer_buffer()
                    ),

                    run_time=0.3
                )

                self.highlight(i, j)

            # --------------------------------------------

            elif op == "swap":

                self.swap(
                    step[1],
                    step[2]
                )

            # --------------------------------------------

            elif op == "noswap":

                self.wait(0.15)

            # --------------------------------------------

            elif op == "sorted":

                speak()

                self.mark_sorted(
                    step[1]
                )

                self.wait(0.3)

            # --------------------------------------------

            elif op == "finished":

                speak()

                txt = Text(
                    "Early Exit",
                    color=GREEN,
                    font_size=34
                )

                self.layout.place_message(txt)

                self.play(FadeIn(txt))
                self.wait(0.8)
                self.play(FadeOut(txt))

            # --------------------------------------------

            elif op == "complete":

                speak()

                done = Text(
                    "Array Sorted!",
                    color=GREEN,
                    font_size=40
                )

                done.next_to(
                    self.array,
                    DOWN,
                    buff=0.6
                )

                self.play(Write(done))

                self.wait(2)

            self.wait(0.1)