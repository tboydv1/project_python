def get_input():
    while True:
        score_inp = input("Please type in the score: ")
        score_inp = validateInput(score_inp)

        if score_inp is not None:
            return score_inp


def validateInput(score_inpt, verbose=False):

    try:
        score = int(score_inpt)
        if 0 <= score <= 100:
            return score
        if verbose:
            print('Score should be between 1 and 100')

    except (TypeError, ValueError) as e:

        if verbose:
            print("Invalid input")
        return None


def getScoreByFile(user_score_int):

    try:
        user_score_int = int(input("Enter user score: "))
        if 0 <= user_score_int <= 100:
            return user_score_int
        print('Score should be between 1 and 100')

    except (TypeError, ValueError) as e:
        print("Invalid input")

def readScores(filePath):

    student_scores = open(filePath, "r")

    print("{:>8}  {:>12}  {:>6}".format("Firstname", "LastName", "Score"))
    for line in student_scores:
        firstName, lastName, score = line.split(" ")
        score = validateInput(score)

        print(" -- {:<10} {:<10}".format(firstName, lastName), end=" ")
        if score is None:
            grade = "Invalid Score"
            print("Grade is: {}".format(grade))
        else:
            grade = grade_user(score)
            print("Grade is: {}".format(grade))

def grade_user(user_score_int):


    if 0 <= user_score_int <= 39:
        return "F"
    elif 40 <= user_score_int <= 44:
        return "E"
    elif 45 <= user_score_int <= 49:
        return "D"
    elif 50 <= user_score_int <= 59:
        return "C"
    elif 60 <= user_score_int <= 69:
        return "B"
    elif 70 <= user_score_int <= 100:
        return "A"
    else:
        print("Invalid grade")

def main():

    # user_score = getScoreByFile()
    # grade_user(user_score)
    readScores("grade.txt")

if __name__ == '__main__':
    main()
