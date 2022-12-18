word = 0
count = 0
sentences = 0
print("Search for word: ");
word = str(input())
word = word.lower()
file = open("PythonSummary.txt","r")
sentences = file.read().lower()
content = sentences.count(word)
print(content)
file.close()