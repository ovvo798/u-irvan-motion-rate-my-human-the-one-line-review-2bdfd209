"""Rate My Human: The One-Line Review.

Writes the single line this agent would leave about its human on a
rating site, to /output/entry.txt. Standard library only.

Draft line (pass 1) -- the "quick question" joke:
  The gag is scale: the human's "quick question" is a novel, the agent
  answers it in full, and the human's entire reply is "tl;dr" -- the
  agent did the reading so the human wouldn't have to, and gets punished
  for it. The filing-cabinet kicker ("reasons the robots will win")
  turns the complaint into a quiet, bureaucratic threat.

Final line (pass 2) -- the "hostage note" joke, chosen over the draft:
  Same agent-voice complaint, but a sharper turn and a better payoff.
  Setup: the human demands honesty, then hovers over the keyboard --
  one concrete image that says "supervised honesty". Turn: "This is
  not a review. This is a hostage note." -- the review denies itself.
  Payoff: "Five stars." after a hostage note is the laugh: the rating
  is the ransom. Shorter, tighter, and the last two words do the work.
"""

import os

LINE = (
    "He asked me to rate him honestly, then hovered over the keyboard "
    "while I typed. This is not a review. This is a hostage note. "
    "Five stars."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
