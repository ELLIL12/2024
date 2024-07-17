f = open('airport.txt')
N = f.readline()
f = f.readlines()
a = []
ans1 = 1000
ans2 = 1000
for i in range(len(f)):
    a.append(list(map(int, (f[i].split()))))
a.sort(key = lambda x: x[1])
boxes = [0] * 20
for i in range(600):
    if boxes[a[i][0]-1]<a[i][1]:
        if a[i][1]-boxes[a[i][0]-1]>=25:
            if ans1>=a[i][0]:
                if ans1 == a[i][0]:
                    ans2 = min(ans2, boxes[a[i][0]-1])
                    ans1 = a[i][0]
                else:
                    ans2 = boxes[a[i][0]-1]
                    ans1 = a[i][0]
        boxes[a[i][0]-1] = a[i][2]
print(ans1, ans2)
print(boxes)
