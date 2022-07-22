import interval


def appearance(intervals):
    l = intervals["lesson"]
    p = intervals["pupil"]
    t = intervals["tutor"]
    pupil = [[p[x], p[x+1]] for x in range(0, len(p)-1, 2)]
    tutor = [[t[x], t[x+1]] for x in range(0, len(t)-1, 2)]
    pupil_interval = interval.interval(*pupil)
    tutor_interval = interval.interval(*tutor)
    lesson_interval = interval.interval([*l])
    total = pupil_interval & tutor_interval & lesson_interval
    return int(interval.fpu.up(lambda: sum((c.sup - c.inf for c in total), 0)))


tests = [
    {
        'data': {
            'lesson': [1594663200, 1594666800],
            'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
            'tutor': [1594663290, 1594663430, 1594663443, 1594666473]
        },
        'answer': 3117
    },

    {
        'data': {
            'lesson': [1594702800, 1594706400],
            'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
            'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]
        },
        'answer': 3577
    },

    {
        'data': {
            'lesson': [1594692000, 1594695600],
            'pupil': [1594692033, 1594696347],
            'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
        'answer': 3565
    },
]


if __name__ == '__main__':
   for i, test in enumerate(tests):
       test_answer = appearance(test['data'])
       assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
