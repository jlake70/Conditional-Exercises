watchers_age = int(input("Enter users age: "))
movies_rating = input("Enter the movie rating (G,PG,PG-13,R): ")


if movies_rating == "G":
    print("You can watch the movie!")
elif movies_rating == "PG" and watchers_age >=7:
    print("You're old enough for this movie")
elif movies_rating == "PG-13" and watchers_age >=13:
    print("You're old enough for this movie")
elif movies_rating == "R" and watchers_age >=17:
    print("You're old enough for this movie")
else:
    print("You're not allowed to watch this movie!")