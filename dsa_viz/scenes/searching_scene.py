from manim import *

from dsa_viz.core.base_scene import DSAScene
from dsa_viz.core.runtime import get_runtime_input
from dsa_viz.core.pointer import Pointer
from dsa_viz.core.voice import generate
from dsa_viz.algorithms.searching.binary_search import binary_search


class SearchingScene(DSAScene):

    def construct(self):

        self.camera.background_color = "#111827"

        # ------------------------------------------------
        # INPUT
        # ------------------------------------------------

        raw = get_runtime_input()

        if len(raw) > 1:
            target = raw[-1]
            arr = raw[:-1]
        else:
            arr = raw
            target = raw[0]

        result = binary_search(arr.copy(), target)

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

        self.setup_array(arr.copy())

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
            ui.get("default_op", "Searching")
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
        # POINTER
        # ------------------------------------------------

        mid_ptr = Pointer("mid", color=GREEN)

        self.add(mid_ptr)

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
            # INTRO
            # --------------------------------------------

            if op == "intro":

                speak()

                self.wait(0.8)

            # --------------------------------------------
            # SEARCH RANGE
            # --------------------------------------------

            elif op == "range":

                left = step[1]
                right = step[2]

                self.play(

                    *[
                        self.array.cells[i].highlight()
                        for i in range(left, right + 1)
                    ],

                    run_time=0.4

                )

            # --------------------------------------------
            # MID POINTER
            # --------------------------------------------

            elif op == "mid":

                mid = step[1]

                self.play(

                    mid_ptr.animate.next_to(

                        self.array.cells[mid],

                        UP,

                        buff=self.layout.pointer_buffer()

                    ),

                    run_time=0.3

                )

                self.highlight(mid, mid)

            # --------------------------------------------
            # MOVE LEFT
            # --------------------------------------------

            elif op == "move_left":

                speak()

                message = Text(
                    "Searching Left Half",
                    color=BLUE,
                    font_size=30
                )

                self.layout.place_message(message)

                self.play(FadeIn(message))
                self.wait(0.4)
                self.play(FadeOut(message))

            # --------------------------------------------
            # MOVE RIGHT
            # --------------------------------------------

            elif op == "move_right":

                speak()

                message = Text(
                    "Searching Right Half",
                    color=BLUE,
                    font_size=30
                )

                self.layout.place_message(message)

                self.play(FadeIn(message))
                self.wait(0.4)
                self.play(FadeOut(message))

            # --------------------------------------------
            # FOUND
            # --------------------------------------------

            elif op == "found":

                speak()

                mid = step[1]

                self.mark_sorted(mid)

                self.play(

                    Flash(
                        self.array.cells[mid].rect,
                        color=GREEN
                    ),

                    run_time=0.7

                )

                self.hud.update_op("Found")

            # --------------------------------------------
            # NOT FOUND
            # --------------------------------------------

            elif op == "not_found":

                speak()

                message = Text(
                    "Target Not Found",
                    color=RED,
                    font_size=36
                )

                self.layout.place_message(message)

                self.play(Write(message))

                self.wait(1)

            # --------------------------------------------
            # COMPLETE
            # --------------------------------------------

            elif op == "complete":

                speak()

                message = Text(
                    "Binary Search Complete",
                    color=GREEN,
                    font_size=36
                )

                self.layout.place_message(message)

                self.play(Write(message))

                self.wait(2)

            self.wait(0.1)