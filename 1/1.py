def function():
    players = [19, 19, 26, 25, 20, 18, 30, 24, 27]
    find_medium_year = 0
    step = 0
    find_old_year = 0

    for el in players:
        find_medium_year += el
        step += 1

    result = find_medium_year / step
    print('Середній вік ', result)

    for elements in players:
        if elements > find_old_year:
            find_old_year = elements

    print('Найстарший вік ', find_old_year)
    print('Сума Наймолодшого і Найстаршого ', find_old_year + result)


print(function())
