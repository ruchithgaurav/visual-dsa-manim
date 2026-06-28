def binary_search(arr, target):

    steps = []
    narration = []

    pseudocode = [
        "left = 0",
        "right = n - 1",
        "while left <= right",
        "mid = (left + right) // 2",
        "if arr[mid] == target",
        "    return mid",
        "elif arr[mid] < target",
        "    left = mid + 1",
        "else",
        "    right = mid - 1"
    ]

    # -------------------------------------------------
    # INTRODUCTION
    # -------------------------------------------------

    steps.append(("intro",))

    narration.append({
        "step": "intro",
        "text": "Binary Search",
        "voice": (
            "Binary Search works on a sorted array by repeatedly "
            "dividing the search space into two halves."
        )
    })

    left = 0
    right = len(arr) - 1

    while left <= right:

        # ---------------------------------------------
        # SEARCH RANGE (Animation only)
        # ---------------------------------------------

        steps.append(("range", left, right))

        # ---------------------------------------------
        # MID (Animation only)
        # ---------------------------------------------

        mid = (left + right) // 2

        steps.append(("mid", mid))

        # ---------------------------------------------
        # FOUND
        # ---------------------------------------------

        if arr[mid] == target:

            steps.append(("found", mid))

            narration.append({
                "step": "found",
                "text": "Target Found",
                "voice": (
                    f"The target value {target} has been found "
                    f"at index {mid}."
                )
            })

            break

        # ---------------------------------------------
        # MOVE RIGHT
        # ---------------------------------------------

        elif arr[mid] < target:

            steps.append(("move_right", mid))

            narration.append({
                "step": "move_right",
                "text": "Searching Right Half",
                "voice": (
                    f"{arr[mid]} is smaller than {target}. "
                    "The search continues in the right half."
                )
            })

            left = mid + 1

        # ---------------------------------------------
        # MOVE LEFT
        # ---------------------------------------------

        else:

            steps.append(("move_left", mid))

            narration.append({
                "step": "move_left",
                "text": "Searching Left Half",
                "voice": (
                    f"{arr[mid]} is greater than {target}. "
                    "The search continues in the left half."
                )
            })

            right = mid - 1

    else:

        steps.append(("not_found",))

        narration.append({
            "step": "not_found",
            "text": "Target Not Found",
            "voice": (
                f"The target value {target} is not present in the array."
            )
        })

    # -------------------------------------------------
    # COMPLETE
    # -------------------------------------------------

    steps.append(("complete",))

    narration.append({
        "step": "complete",
        "text": "Search Complete",
        "voice": (
            "Binary Search has completed."
        )
    })

    return {

        "title": "Binary Search",

        "description":
            "Binary Search efficiently searches a sorted array by repeatedly halving the search space.",

        "steps": steps,

        "narration": narration,

        "pseudocode": pseudocode,

        "complexity": {
            "time": "Worst : O(log n)\nAverage : O(log n)\nBest : O(1)",
            "space": "O(1)"
        },

        "ui": {
            "default_op": "Searching"
        }

    }