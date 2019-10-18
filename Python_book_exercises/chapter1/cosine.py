from math import *;
print("Angles of triangle with lengths: 7, 3, 9", end = "\n\n")


##Find angle C when side a = 9, b = 3, c = 7
##formula= c**2 = a**2 + b**2 - 2 * a * b * Cos(c)

side_a, side_b, side_c = 9, 3, 7;

a_b = -(2 * side_a * side_b);

#Square all sides
pow_a = side_a**2
pow_b = side_b**2
pow_c = side_c**2

## add side a and b
sum_ab = pow_a + pow_b


pow_c -= sum_ab


angle_C = acos(pow_c / a_b)

#convert result to degrees


print("Angle C = ", degrees(angle_C))


#Find angle B when side a = 9, b = 3, c = 7

#Square all sides
pow_a = side_a**2
pow_b = side_b**2
pow_c = side_c**2


a_c = -(2 * side_a * side_c);


## add side a and b

sum_ac = pow_a + pow_c


pow_b -= sum_ac

angle_B = acos(pow_b / a_c)

print("Angle B = ", degrees(angle_B))

#Find angle A when side a = 9, b = 3, c = 7

#Square all sides
pow_a = side_a**2
pow_b = side_b**2
pow_c = side_c**2


b_c = -(2 * side_b * side_c);


## add side b and c

sum_bc = pow_b + pow_c


pow_a -= sum_bc

angle_A = acos(pow_a / b_c)

print("Angle B = ", degrees(angle_A))














