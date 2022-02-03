from cube import Cube
c = Cube()
results = [c.roll() for i in range(0, 1000)]
count =[]
for value in range(1, c.sides+1):
    count.append(results.count(value))
print(count)