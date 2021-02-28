b, c, d, e, f, g, h = 0, 0, 0, 0, 0, 0, 0

b = 79 * 100 + 100000
c = b + 17000
f = 1
d = 2

# end of the initialization block - we are never sent with jnz to any
# lines above here

e = 2  # 11
g = d  # 12 (I'll just leave this here because this is another one we jump to)
while True:
    g = d   # 12
    g *= e
    g -= b
    if g == 0: # if g != 0 goto 17 (if we invert the condition we get this)
        f = 0
    e += 1 # 17
    g = e
    g -= b # 19
    if g == 0: # again, I invert the condition, I think this jnz translates to
        break  # a while loop like this
    # if g != 0 go to 12


print(b, c, d, e, f, g, h)
print(f'solution h is {h}')
