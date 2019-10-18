#algorithm to determine basketball team fate

tmp_1 = input("Enter number of points for team_1 one points \n")
tmp_2 = input("Enter number of points for team_2 points \n")

team_1 = int(tmp_1)
team_2 = int(tmp_2)

points_diff = abs(team_1 - team_2)
points_diff -=3

if team_1 > team_2:
    team = 1
else:
    team = 2

temp = input("Which team has the ball? Enter 1 for team_1 and 2 for team_2 ")

team_ahead = int(temp)

if temp == team:
    points_diff += (1/2)
else:
    points_diff -= (1/2)

points_diff = pow(points_diff, 2)

tmp_time = input("Enter number of seconds left in the game ")
time_left = int(tmp_time)

if(points_diff > time_left):
    print("lead is safe for team ",team)
else:
    print("lead is not safe for team ",team)
