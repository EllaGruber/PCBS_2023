#! /usr/bin/env python
# Time-stamp: <2021-12-01 10:00:13 christophe@pallier.org>
"""This is a simple decision experiment.

At each trial, a number between 0 and 9 is presented at the center of the
screen and the participant must press the key 'f' if the number is even, 'j' if
it is odd.

"""

import random

from expyriment import design, control, stimuli

N_TRIALS = 100
THRESHOLD = 55
SMALLER_RESPONSE = 'f'
LARGER_RESPONSE = 'j'
MAX_RESPONSE_DELAY = 2000
audiotarget= stimuli.Audio("wrong-answer.ogg")
exp = design.Experiment(name="Numerical Distance Effect", text_size=40)
control.initialize(exp)

# prepare the Target list
TARGETS = [random.randint(1,THRESHOLD) for _ in range(N_TRIALS//2)] + [random.randint(THRESHOLD + 1,100) for _ in range(N_TRIALS//2)] #in order to have as much trial below the threshold as above the threshold
# I exlcude also the threshold for not having it in the experiment
# prepare the stimuli
trials = [(number, stimuli.TextLine(str(number))) for number in TARGETS]
random.shuffle(trials)


cue = stimuli.FixCross(size=(50, 50), line_width=4)
blankscreen = stimuli.BlankScreen()
instructions = stimuli.TextScreen("Instructions",
    f"""When you'll see a number, your task to decide, as quickly as possible,
     whether it is smaller or larger than '{THRESHOLD}'.

    if it is smaller, press '{SMALLER_RESPONSE}'

    if it is larger, press '{LARGER_RESPONSE}'.

    Press the space bar to start.""")

exp.add_data_variable_names(['number',
                             'distance',
                             'respkey',
                             'RT'])

control.start(skip_ready_screen=True)
instructions.present()
exp.keyboard.wait()

for number, stim in trials:
    blankscreen.present()
    exp.clock.wait(1000)
    cue.present()
    exp.clock.wait(500)
    stim.present()
    key, rt = exp.keyboard.wait_char([SMALLER_RESPONSE, LARGER_RESPONSE],
                                     duration=MAX_RESPONSE_DELAY)
    exp.data.add([number, number - THRESHOLD , key, rt])

    if (int(number - THRESHOLD > 0) * int(key == SMALLER_RESPONSE) + int(number - THRESHOLD < 0) * int((key == LARGER_RESPONSE))) >= 1:
        audiotarget.present()


control.end()
