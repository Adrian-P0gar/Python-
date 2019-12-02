def get_most_played(file_name):
    file_txt = []
    with open(file_name) as f:
        for i in f:
            file_txt.append(i.strip().split("\t"))
    sold_number = []
    d = 0
    while d < len(file_txt):

        sold_number.append(file_txt[d][1])
        d += 1
    float_sold_number = []
    for i in sold_number:
        float_sold_number.append(float(i))

    max_sold_number = max(float_sold_number)
    n = 0
    title = ''
    while n < len(file_txt):
        if int(max_sold_number) == int(file_txt[n][1]):
            title += file_txt[n][0]
            return title
        else:
            n += 1


def sum_sold(file_name):
    file_txt = []
    with open(file_name) as f:
        for i in f:
            file_txt.append(i.strip().split("\t"))

    sold_number = []
    d = 0
    while d < len(file_txt):

        sold_number.append(float(file_txt[d][1]))
        d += 1
    sum_sold = [0]
    i = 0
    while i < len(sold_number):
        for n in sold_number:
            sum_sold.append(float(sum_sold[-1]) + float(n))
            i += 1
    total_sum_sold = float(sum_sold[-1])
    return total_sum_sold


def get_selling_avg(file_name):
    sum_sol = sum_sold('game_stat.txt')
    file_txt = []
    with open(file_name) as f:
        for i in f:
            file_txt.append(i.strip().split("\t"))
    count_file_txt = len(file_txt)
    selling_avg = float(float(sum_sol) / float(count_file_txt))
    return selling_avg


def count_longest_title(file_name):
    file_txt = []
    with open(file_name) as f:
        for i in f:
            file_txt.append(i.strip().split("\t"))

    list_longest_title = []
    d = 0
    while d < len(file_txt):
        list_longest_title.append(len(file_txt[d][0]))
        d += 1
    count_longest_title = int(max(list_longest_title))
    return count_longest_title


def get_date_avg(file_name):
    file_txt = []
    with open(file_name) as f:
        for i in f:
            file_txt.append(i.strip().split("\t"))

    sold_number = []
    d = 0
    while d < len(file_txt):

        sold_number.append(int(file_txt[d][2]))
        d += 1
    sum_sold = [0]
    i = 0
    while i < len(sold_number):
        for n in sold_number:
            sum_sold.append(int(sum_sold[-1]) + int(n))
            i += 1
    count_len = len(file_txt)
    sum_ages = int(sum_sold[-1])
    avg_age = sum_ages / int(count_len)
    return(round(avg_age))


def get_game(file_name, title):
    file_txt = []
    with open(file_name) as f:
        for i in f:
            file_txt.append(i.strip().split("\t"))

    game_title = []
    sold = []
    year = []
    genre = []
    publisher = []
    game_detail = []
    d = 0
    while d < len(file_txt):
        if title == file_txt[d][0]:
            while len(game_title) < 1:
                game_title.append(file_txt[d][0])
            while len(sold) < 1:
                sold.append(float(file_txt[d][1]))
            while len(year) < 1:
                year.append(int(file_txt[d][2]))
            while len(genre) < 1:
                genre.append(file_txt[d][3])
            while len(publisher) < 1:
                publisher.append(file_txt[d][4])
            d += 1
        else:
            d += 1
    str_game_title = str(game_title[-1])
    float_sold = float(sold[-1])
    int_year = int(year[-1])
    str_genre = str(genre[-1])
    str_publisher = str(publisher[-1])
    game_detail = [str_game_title, float_sold,
                   int_year, str_genre, str_publisher]
    return game_detail
