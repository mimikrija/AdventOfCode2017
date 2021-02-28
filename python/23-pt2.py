b, c, d, e, f, g, h = 0, 0, 0, 0, 0, 0, 0

b = 79 * 100 + 100000
c = b + 17000
f = 1
d = 2

# end of the initialization block - we are never sent with jnz to any
# lines above here

e = 2  # 11 (this is just for setting the range of e back to 2 so we can merge lines)
g = d  # 12 (I'll just leave this here because this is another one we jump to)

# lines 12 - 19 mean: is there *any* number 2 <= e <= b, such that
# d * e == b --> b / e == d --> b / d == e
# if any(d * e == b for e in range(2, b+1))
# or shorter: is b divisible by d(2)? if yes, f = 0
# so basically it means set f=0, but since I see in the assembly that d
# might change, I will write it as:
if b % d == 0:  # 11-12
    f = 0       # 20



print(b, c, d, e, f, g, h)
print(f'solution h is {h}')
