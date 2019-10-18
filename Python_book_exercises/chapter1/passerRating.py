#program calculates pass rating of a football match

pass_completions = float(input("Enter pass completion: "))
pass_attempts = float(input("Enter pass attemps: "))
total_yard = float(input("Enter total passing yard: "))
interceptions = float(input("Enter interceptions: "))
touchdowns = float(input("Enter touchdowns: "))

C = ((pass_completions / pass_attempts) - .3) / 5

print("completions", C)
Y = ((total_yard / pass_attempts) - 3) / .25

print("yard", Y)
T = ((touchdowns / pass_attempts) * 20)

print("Touchdowns", T)
I = 2.375 - (interceptions / pass_attempts) * 25

print("Intereceptions", I)
pass_rating = ((C + Y +  T + I) / 6) * 100


print("pass rating is: ", pass_rating)
