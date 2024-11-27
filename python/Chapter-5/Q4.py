# What will be the length of following set S:

s = set()
s.add(20)
s.add(20.0)
s.add( '20') # length of s after these perations?

print(len(s)) # output : 2     bcz in python, "20 == 20.0" returns "True"; you can run this "20 == 20.0" in REPL, it will give return "True"
print(s)