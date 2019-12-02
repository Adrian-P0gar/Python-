def open_file(file_name):
    list_text = []
    with open(file_name) as f:

        for i in f:
            list_text.append(i.strip().split("\t"))
    return list_text


list_txt = open_file(
    file_name='/home/pogar/Python module/SI 5/Game invetori 1/game_stat.txt')


def count_games(file_name):
    with open(file_name) as file:
        return len(list(file))


def decide(file_name, year):
    row = 0
    while row < len(file_name):
        if int(year) == int(file_name[row][2]):

            return True
        else:
            row += 1
    return False


def get_latest(file_name):
    latest_list = [0]
    latest_title = []
    row = 0
    while row < len(file_name):
        if int(latest_list[-1]) < int(file_name[row][2]):
            latest_list.append(file_name[row][2])
            latest_title.append(file_name[row][0])

            row += 1
        else:
            row += 1
    return latest_title[-1]


def count_by_genre(file_name, genre):
    genre_list = []

    row = 0
    while row < len(file_name):
        if str(file_name[row][3]) == str(genre):
            genre_list.append(1)
        row += 1
    return len(genre_list)


def get_line_number_by_title(file_name, title):
    row = 0
    while row < len(file_name):
        if str(title) == str(file_name[row][0]):

            return row + 1
        else:
            row += 1
    raise ValueError


def print_question():

    print("1. How many games are in the file?")
    print("2. Is there a game from a given year?")
    print("3. Which was the latest game?")
    print('4. How many games do we have by genre?')
    print("5. What is the line number of the given game (by title)?")
    print('6. What is the alphabetical ordered list of the titles?')
    print("7. What are the genres?")
    print('8. hat is the release date of the top sold "First-person shooter" game?')


def sort_abc(file_name):
    list_title = []
    row = 0
    sorted_title = []
    while row < len(file_name):

        list_title.append(file_name[row][0])
        row += 1

    while list_title:
        smallest = min(list_title)
        sorted_title.append(smallest)
        list_title.pop(list_title.index(smallest))

    return sorted_title


def write(word):
    with open('/home/pogar/Python module/SI 5/Game invetori 1/export.py', 'a') as f:
        f.write((str(word) + '\n'))
        f.close()


def get_genres(file_name):
    list_genre = []
    row = 0
    sorted_genre = []
    list_with_single_genre = []
    word_genre = 0
    while row < len(file_name):

        list_genre.append(file_name[row][3])
        row += 1

    set_genre = set(list_genre)

    while word_genre < len(set_genre):
        for i in set_genre:
            list_with_single_genre.append(i)
            word_genre += 1
    while list_with_single_genre:
        smallest = min(list_with_single_genre)
        sorted_genre.append(smallest)
        list_with_single_genre.pop(list_with_single_genre.index(smallest))

    return sorted_genre


def when_was_top_sold_fps(file_name):
    first_person_shooter = []
    d = 0
    while d < len(file_name):
        if file_name[d][3] == 'First-person shooter':
            first_person_shooter.append(file_name[d])
            d += 1
        else:
            d += 1
    sold_number = []
    i = 0
    while i < len(first_person_shooter):
        sold_number.append(first_person_shooter[i][1])
        i += 1
    float_sold_number = []
    for i in sold_number:
        float_sold_number.append(float(i))

    max_float_sold_number = max(float_sold_number)

    n = 0
    while n < len(first_person_shooter):
        if str(max_float_sold_number) == first_person_shooter[n][1]:

            return first_person_shooter[n]
        else:
            n += 1


def main():

    choose = 0
    if choose == 0:
        print_question()
        choose = int(input("What is your question? "))
    if choose == 1:
        print(count_games(
            file_name="/home/pogar/Python module/SI 5/Game invetori 1/game_stat.txt"))
        write(count_games(
            file_name="/home/pogar/Python module/SI 5/Game invetori 1/game_stat.txt"))
    if choose == 2:
        year = input("Give the year: ")
        print(decide(list_txt, year))
        write(decide(list_txt, year))
    if choose == 3:
        print(get_latest(list_txt))
        write(get_latest(list_txt))
    if choose == 4:
        genre = str(input("What is yout genre: "))
        print(count_by_genre(list_txt, genre))
        write(count_by_genre(list_txt, genre))
    if choose == 5:
        title = str(input("Give me the game title: "))
        print(get_line_number_by_title(list_txt, title))
        write(get_line_number_by_title(list_txt, title))
    if choose == 6:
        print(sort_abc(list_txt))
        write(sort_abc(list_txt))
    if choose == 7:
        print(get_genres(list_txt))
        write(get_genres(list_txt))
    if choose == 8:
        print(when_was_top_sold_fps(list_txt))
        write(when_was_top_sold_fps(list_txt))


main()
