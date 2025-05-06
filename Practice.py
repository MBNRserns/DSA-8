u=input("Enter a Sentance  ")

v=["a","e","i","o","u","A","E","I","O","U"]
c=["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z","B","C","D","F","G","H","J","K","L","M","N","P","Q","R","S","T","V","W","X","Y","Z"]

count=0

for i in u:
    if i in c:
        count=count+1

print("The Number of consonants in this Sentance is:  ", count)