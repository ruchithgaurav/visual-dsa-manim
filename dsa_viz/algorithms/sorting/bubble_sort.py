def bubble_sort(arr):

    steps = []
    narration = []

    n = len(arr)

    pseudocode = [
        "for i = 0 to n-1",
        "    for j = 0 to n-i-2",
        "        if arr[j] > arr[j+1]",
        "            swap(arr[j], arr[j+1])"
    ]

    # --------------------------------------------------
    # Introduction
    # --------------------------------------------------

    steps.append(("intro",))

    narration.append({
        "step": "intro",
        "text": "Bubble Sort",
        "voice": (
            "Bubble Sort repeatedly compares adjacent elements "
            "and moves the largest element to the end after every pass."
        )
    })

    for i in range(n):

        swapped = False

        # --------------------------------------------------
        # Start Pass
        # --------------------------------------------------

        steps.append(("pass", i))

        narration.append({
            "step": "pass",
            "text": f"Pass {i + 1}",
            "voice": f"Starting pass number {i + 1}."
        })

        for j in range(n - i - 1):

            # Compare (Animation only)

            steps.append(("compare", j, j + 1))

            if arr[j] > arr[j + 1]:

                arr[j], arr[j + 1] = arr[j + 1], arr[j]

                swapped = True

                # Swap (Animation only)

                steps.append(("swap", j, j + 1))

            else:

                # No Swap (Animation only)

                steps.append(("noswap", j, j + 1))

        # --------------------------------------------------
        # End Pass
        # --------------------------------------------------

        steps.append(("sorted", n - i - 1))

        narration.append({
            "step": "sorted",
            "text": f"{arr[n-i-1]} Fixed",
            "voice":
                f"The element {arr[n-i-1]} has reached its correct position."
        })

        if not swapped:

            steps.append(("finished",))

            narration.append({
                "step": "finished",
                "text": "Early Exit",
                "voice":
                    "No swaps occurred in this pass. "
                    "The array is already sorted."
            })

            break

    # --------------------------------------------------
    # Complete
    # --------------------------------------------------

    steps.append(("complete",))

    narration.append({
        "step": "complete",
        "text": "Sorting Complete",
        "voice":
            "Bubble Sort has completed successfully. "
            "The array is now fully sorted."
    })

    return {

        "title": "Bubble Sort",

        "description":
            "Bubble Sort repeatedly compares adjacent elements.",

        "steps": steps,

        "narration": narration,

        "pseudocode": pseudocode,

        "complexity": {
            "time": "Worst : O(n²)\nAverage : O(n²)\nBest : O(n)",
            "space": "O(1)"
        },

        "ui": {
            "default_op": "Comparing"
        }

    }