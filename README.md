# Aliquot Sequence
An **aliquot sequence** is a sequence of numbers generated from a starting positive integer by repeatedly replacing it with the sum of its proper divisors (divisors excluding the number itself).

## Definition:
1. **Start with a positive integer n**.
2. Calculate the sum of its proper divisors, denoted as \( s(n) \).
3. Replace n with \( s(n) \).
4. Repeat the process indefinitely.

## Example:
- **Starting with 12**:
  - Proper divisors of 12: 1, 2, 3, 4, 6
  - \( s(12) = 1 + 2 + 3 + 4 + 6 = 16 \)
  - Next term: 16
  - Proper divisors of 16: 1, 2, 4, 8
  - \( s(16) = 1 + 2 + 4 + 8 = 15 \)
  - Next term: 15
  - Proper divisors of 15: 1, 3, 5
  - \( s(15) = 1 + 3 + 5 = 9 \)
  - Next term: 9
  - Proper divisors of 9: 1, 3
  - \( s(9) = 1 + 3 = 4 \)
  - Next term: 4
  - Proper divisors of 4: 1, 2
  - \( s(4) = 1 + 2 = 3 \)
  - Next term: 3
  - Proper divisors of 3: 1
  - \( s(3) = 1 \)
  - Next term: 1
  - Proper divisors of 1: none
  - Sequence ends at 1.

## Types of Aliquot Sequences:
- **Terminating**: Sequences that eventually reach 1.
- **Cyclic**: Sequences that enter a loop (e.g., 6 → 6).
- **Diverging**: Sequences that increase indefinitely without settling into a cycle or terminating.

## Summary
Aliquot sequences provide an interesting way to explore the properties of numbers and their divisors, revealing patterns and behaviors in number theory.
