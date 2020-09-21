# put your python code here

l = int(input())
w = int(input())
h = int(input())

sum_of_length_of_all_edges = 4 * (l + w + h)
surface_area = 2 * (l*w + w*h + l*h)
volume = l * w * h

print(sum_of_length_of_all_edges)
print(surface_area)
print(volume)
