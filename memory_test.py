from memory import Memory, full_vars

m = Memory()
m.a = 5
b = Memory()
m.b = b
m.b.a = 10

print(full_vars(m))
