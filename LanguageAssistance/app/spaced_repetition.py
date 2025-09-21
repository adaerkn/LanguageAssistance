from datetime import date, timedelta


def next_review_sm2(repetitions, interval, easiness, quality):
    if quality < 3:
        repetitions = 0
        interval = 1
        next_date = date.today() + timedelta(days=1)
    else:
        if repetitions == 0:
            interval = 1
        elif repetitions == 1:
            interval = 6
        else:
            interval = round(interval * easiness)

        repetitions += 1
        easiness = easiness + (0.1 - (5 - quality) * (0.08 + (5 - quality) * 0.02))
        if easiness < 1.3:
            easiness = 1.3
        next_date = date.today() + timedelta(days=interval)
    return repetitions, interval, easiness, next_date