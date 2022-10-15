text = str(input())
while text == 'q':
    break
w = text.split()
for r in sorted(w):
    print(r)