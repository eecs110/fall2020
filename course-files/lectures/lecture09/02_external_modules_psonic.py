# To get this program to work, you must do three things:
# 1. Install the Python psonic module using PIP:
#    pip3 install python-sonic
# 2. Install the Sonic Pi music program, downloadable at:
#    https://sonic-pi.net/ 
# 3. Make sure that Sonic Pi (the music program) is running

import psonic
# Note: psonic allows us to pass commands into Sonic Pi programmatically


# List of MIDI Notes: https://www.inspiredacoustics.com/en/MIDI_note_numbers_and_center_frequencies
psonic.use_synth(psonic.PIANO)
psonic.play(76)
psonic.sleep(0.25)
psonic.play(76)
psonic.sleep(0.5)
psonic.play(76)
psonic.sleep(0.5)
psonic.play(72)
psonic.sleep(0.25)
psonic.play(76)
psonic.sleep(0.5)
psonic.play(79)
psonic.sleep(1)
psonic.play(67)
psonic.sleep(1)