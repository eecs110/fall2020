import psonic
import random

counter = 0
while counter < 20:
    # plays 20 times:
    psonic.sample(psonic.DRUM_BASS_HARD, rate=random.randrange(1, 5))
    psonic.sample(psonic.DRUM_CYMBAL_CLOSED)
    psonic.sleep(0.125)
    counter += 1