def cycle_phases():
    yield "follicular"
    yield "ovulation"
    yield "luteal"

phases=cycle_phases()
'''print(next(phases))
print(next(phases))
print(next(phases))'''

for phase in cycle_phases():
    print(phase)