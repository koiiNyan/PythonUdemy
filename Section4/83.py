# Question: Write a script that detects and prints out your monitor resolution.
#
# Expected output:
#
# Width: 1920,  Height: 1080

from screeninfo import get_monitors
monitors = str(get_monitors())
split_by_plus = monitors.split("+")
split_by_par = (str(split_by_plus[0])).split("(")
split_by_x = split_by_par[1].split("x")
print("Width: {}, Height: {}".format(split_by_x[0], split_by_x[1]))
