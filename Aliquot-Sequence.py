import math

def find_divisors(n):
    divisors = set()
    for i in range(1, math.isqrt(n) + 1):
        if n % i == 0:
            divisors.add(i)
            if n // i != n:
                divisors.add(n // i)
    return sorted(divisors)

def aliquot_sequence(Number):
    sequence = []
    while Number != 1:
        divisors = find_divisors(Number)
        Number = sum(divisors)
        sequence.append(Number)
    return sequence

Number = 100
sequence = aliquot_sequence(Number)
print(f"Aliquot Sequence of {Number} --> {sequence}")
print("Steps:",len(sequence))