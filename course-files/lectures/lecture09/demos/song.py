import psonic

psonic.use_synth(psonic.PIANO)

def high_part_1():
    psonic.play_pattern_timed(74, 0.5)
    psonic.play_pattern_timed([67, 69, 71, 72], 0.25)
    psonic.play_pattern_timed([74, 67, 67], 0.5)
    psonic.play_pattern_timed(76, 0.5)
    psonic.play_pattern_timed([72, 74, 76, 78], 0.25)
    psonic.play_pattern_timed([79, 67, 67], 0.5)
    psonic.play_pattern_timed(72, 0.5)
    psonic.play_pattern_timed([74, 72, 71, 69],0.25)
    psonic.play_pattern_timed(71, 0.5)
    psonic.play_pattern_timed([72, 71, 69, 67], 0.25)
    psonic.play_pattern_timed(66, 0.5)
    psonic.play_pattern_timed([67, 69, 71, 67], 0.25)
    psonic.play_pattern_timed([71, 69], 0.5)
    psonic.sleep(0.5)

def high_part_2():
    psonic.play_pattern_timed(83, 0.5)
    psonic.play_pattern_timed([79,81,83,79], 0.25)
    psonic.play_pattern_timed(81, 0.5)
    psonic.play_pattern_timed([74,76,78,74], 0.25)
    psonic.play_pattern_timed(79, 0.5)
    psonic.play_pattern_timed([76,78,79,74], 0.25)
    psonic.play_pattern_timed(73, 0.5)
    psonic.play_pattern_timed([71, 73], 0.25)
    psonic.play_pattern_timed(69, 0.5) 
    psonic.play_pattern_timed([69,71,73,74,76,78], 0.25)
    psonic.play_pattern_timed([79, 78, 76, 78, 69, 73], 0.5)
    psonic.play_pattern_timed(74, 1.5)



high_part_1()
high_part_1()
high_part_2()
high_part_2()

