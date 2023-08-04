# imaginary coding interview question from edabit

def interview(time):
    return 'qualified' if sum(time) <= 120 and sum(time[:2]) <= 10 and sum(time[2:4]) <= 20 and sum(time[4:6]) <= 30 and sum(time[6:8]) <= 40 else 'disqualified'

print(interview([5, 5, 10, 10, 25, 15, 20, 20]))
