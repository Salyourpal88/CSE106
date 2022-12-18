sentences = [];
s = 0
r = 0
print("Please enter sentence: ");
s = str(input())
print("Insert # of repetitions: ");
r = int(input())
for x in range(r):
    sentences.append(s + "\n")
file = open("CompletedPunishment.txt","w")
file.writelines(sentences)
file.close()