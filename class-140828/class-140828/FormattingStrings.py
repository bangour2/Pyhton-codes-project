__author__ = 'student'

x = 1/7

print(x)

fmtx = "{0:.5f}".format(x) #5 decimal places
print(fmtx)

fmtx = "{0:20.5f}".format(x) #5 decimal places at position x = 20
print(fmtx)

s = "Barb"
fmts = "{:20s}".format(s)
print(fmts)

x = 1
for i in range(0,55):
    x = x + x
fmtx = "{:10d}".format(x)
print(fmtx)

fmtb = "{:10d}  {:10s}".format(x, s)
print(fmtb)

x = 3/8
fmtb = "{:10.5f} {:10s}".format(x, s) #at position 10 from previous
print(fmtb)

print(x,s)
print(str(x)+s)

