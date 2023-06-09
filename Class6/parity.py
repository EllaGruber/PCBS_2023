#! /usr/bin/env python
# Time-stamp: <2021-12-01 10:00:13 christophe@pallier.org>
"""This is a simple decision experiment.

At each trial, a number between 0 and 9 is presented at the center of the
screen and the participant must press the key 'f' if the number is even, 'j' if
it is odd.

"""

import random
from expyriment import design, control, stimuli

#TARGETS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
words = ['bonjour', 'chien', 'président']
pseudos = ['lopadol', 'mirance', 'clapour' ]
TARGETS = words + pseudos
N_TRIALS_PER_TARGET = 1
WORD_RESPONSE = 'f'
PEUDOS_RESPONSE = 'j'
MAX_RESPONSE_DELAY = 2000

exp = design.Experiment(name="Parity Decision", text_size=40)
control.initialize(exp)

# prepare the stimuli
trials = [(token, stimuli.TextLine(token)) for token in TARGETS * N_TRIALS_PER_TARGET]
random.shuffle(trials)

cue = stimuli.FixCross(size=(50, 50), line_width=4)
blankscreen = stimuli.BlankScreen()
instructions = stimuli.TextScreen("Instructions",
    f"""When you'll see a number, your task to decide, as q:wuickly as possible, whether it is even or odd.

    if it is even, press '{WORD_RESPONSE}'

    if it is odd, press '{PEUDOS_RESPONSE}'

    There will be {len(trials)} trials in total.

    Press the space bar to start.""")

exp.add_data_variable_names(['token',
                             'word',
                             'respkey',
                             'RT'])

control.start(skip_ready_screen=True)
instructions.present()
exp.keyboard.wait()

for token, stim in trials:
    blankscreen.present()
    exp.clock.wait(1000)
    cue.present()
    exp.clock.wait(500)
    stim.present()
    key, rt = exp.keyboard.wait_char([WORD_RESPONSE, PEUDOS_RESPONSE],
                                     duration=MAX_RESPONSE_DELAY)
    if token in words:
        word_pseudo="word"
    else:
        word_pseudo="pseudo"
    exp.data.add([token, word_pseudo, key, rt])

control.end()
