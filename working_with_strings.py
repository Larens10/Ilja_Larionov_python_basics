# ДЗ: Работа со строками

# ДЗ номер 1

name = "Илья"
hobby = 'Тренажёрный зал'
favorite_movie = """    Тренер Картер
Это фильм о баскетбольном тренере, который старается помочь ребятам стать
лучше в жизни"""

print(f'Меня зовут: {name}\nМоё хобби: {hobby}\nМой любимый фильм:{favorite_movie}')

# ДЗ номер 2

subject = "Programming"

print(subject[0])
print(subject[-1])
print(subject[0:5])
print(subject[3:])
# Или все в одном print
print(subject[0],subject[-1],subject[0:5],subject[3:])

# ДЗ номер 3

first_name = "Илья"
last_name = "Ларионов"
simple_line = "Hello!"

print(first_name + " " + last_name)
print(simple_line * 3)

# ДЗ номер 4

first_name = "Илья"
age = 31
city = "Пермь"

print("Меня зовут {}, мой возраст {}, родом из города "
      "{}".format(first_name, age, city))

print(f"Меня зовут {first_name}, мой возраст {age}, родом из города {city}")

# ДЗ номер 5

line_with_spaces = "  Просто строка с пробелами в начале и в конце  "
line_to_split = "Python is great"
letters_of_word = ["П", "и", "т", "о", "Н"]

print(line_with_spaces.strip())
print(line_with_spaces.replace("начале", "середине"))
print(line_to_split.split())
print(" ".join(letters_of_word))