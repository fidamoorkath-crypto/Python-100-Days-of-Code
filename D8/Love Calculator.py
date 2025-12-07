def calculate_love_score(name1, name2):
    names = (name1 + name2).lower()
    
    word1 = "true"
    count1 = 0
    
    for letter in names:
        if letter in word1:
            count1 += 1
    
    word2 = "love"
    count2 = 0
    
    for letter in names:
        if letter in word2:
            count2 += 1
    print(f"Your love score is: {count1}{count2}")


calculate_love_score("Angela Yu", "Jack Bauer")
