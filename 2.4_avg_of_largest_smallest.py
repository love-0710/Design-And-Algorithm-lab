a=[12,16,82,182,2,280,90,187]
max=a[0]
min=a[0]
for i in a[1:]:
        if i>max:
                max=i
        elif i<min:
                min=i
print((max+min)/2)


