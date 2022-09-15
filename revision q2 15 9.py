radius = int(input('radius of cylinder: '))
depth = int(input('depth of cylinder: '))

# 2πr(r + h).

area = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679*radius**2
volume = (area*depth)
print ('area =',area)
print('volume =',volume)