def give_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'
print('65:', give_grade(65))
print('99:', give_grade(99))
print('84:', give_grade(84))
print('76:', give_grade(76))
print('20:', give_grade(20))
## Visualize this execution (a visual representation): https://goo.gl/RPqCLc
