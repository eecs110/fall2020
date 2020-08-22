import psonic

MARIO_NOTES = [
    76, 76, 76, 72, 76, 79, 67, 72, 67, 64, 69, 71,
    70, 69, 67, 76, 79, 81, 77, 79, 76, 72, 74, 71
]

# Challenge 1: use a *while* loop to PLAY all of the notes
# in the MARIO_NOTES list.
# Challenge 2: when the song ends, play it again

psonic.use_synth(psonic.PIANO)
psonic.play(MARIO_NOTES[0])
psonic.sleep(0.25)
psonic.play(MARIO_NOTES[1])
psonic.sleep(0.25)
psonic.play(MARIO_NOTES[2])
psonic.sleep(0.25)