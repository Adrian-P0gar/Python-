print("What is your new idea: I could make a coffee maker that can also add ice to the coffee.")

while True:
    idea = input("Your ideabank:")
    ideabank = []
    i = 1
    g = i + 1
    ideabank.append(idea)
    with open("filename.txt", "a") as f:

        f.write(idea + "\n")
            
    ideabank = open("filename.txt", "r")
    i = 0
    for idea in ideabank:
        print(str(i+1) +". " +idea)
        i = i+1