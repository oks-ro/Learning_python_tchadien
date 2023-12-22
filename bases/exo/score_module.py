filename = "scores.txt"

def save_score(user, score):
    with open(filename+".txt", "a") as f:
        f.write(f"{user}:{score}\n")


def show_scores():
    with open(filename+".txt", "r") as f:
        print(f.read())

def show_user_score(user):
    with open(filename+".txt", "r") as f:
        while True:
            score_line_elt = f.readline().split(":")
            if score_line_elt[0] == user:
                print(f"Le score de joueur {user} est: {score_line_elt[1]}")