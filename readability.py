from curses.ascii import isalpha

text = input("text: ")
letters = 0
words = 1
sentences = 0


for i in range(len(text)):
    if isalpha(text[i]):
        letters+=1
    elif text[i] == " ":
        words += 1
    elif text[i] == "." or text[i] == "?" or text[i] == "!":
        sentences += 1

l = letters /  words * 100
s =  sentences /  words * 100

index = round(0.0588 * l - 0.296 * s - 15.8)

if index < 1:
    print("Before Grade 1")
elif index > 16:
    print("Grade 16+")

else :
    print(f"Grade {index}")