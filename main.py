import psycopg2, random, string
from psycopg2 import Error

# try:
connection = psycopg2.connect(user="strukov",
                              # пароль, который указали при установке PostgreSQL
                              password="Aa!135",
                              host="95.31.130.149",
                              port="5432",
                              database="codemania")




cursor = connection.cursor()

# #---------------------------Users-----------------------------------
# val = [
#     # (id, lastname, firstname, patronymic, avatar, email, password, sex, dateBirthDay)
#     'Касперский Евгений Валентинович mentor2.jpg eugenkasper@mail.ru secure123secure 0 1965-10-04'.split(),
#     'Дуров Павел Валерьевич mentor5.jpg durovmilliarder@mail.ru milliarder123milliarder 0 1984-10-10'.split(),
#     'Элбакян Александра Асановна mentor.jpg alexandra@mail.ru sc1-hubt0p 1 1988-11-6'.split(),
#     'Данилов Игорь Анатольевич mentor3.jpg igorweb@mail.ru web123web 0 1964-4-22'.split(),
#     'Скляров Дмитрий Витальевич mentor4.jpg sclarovbaum@mail.ru mg3ubaum 0 1974-12-18'.split(),
#     'Пянтковская Татьяна Алексеевна NULL tat2006@mail.ru gzynrjdcrfz17 1 2006-08-17'.split(),
#     'Кузнецов Илья Евгеньевич NULL ilyanew@mail.ru 2007zxc2406 0 2007-06-24'.split()
#
# ]
# a = '''INSERT INTO users(email, password, firstname, lastname, patronymic, sex, avatar, "dateBirthDay") VALUES '''
# for i in range(5):
#     a += f"('{val[i][4]}', '{val[i][5]}', '{val[i][1]}', '{val[i][0]}', '{val[i][2]}', {val[i][6]}, '{val[i][3]}', '{val[i][7]}'), "
# a = a.rstrip(', ')
# cursor.execute(a)
#
# a = '''INSERT INTO users(email, password, firstname, lastname, patronymic, sex, avatar, "dateBirthDay") VALUES '''
# for i in range(5, 7):
#     a += f"('{val[i][4]}', '{val[i][5]}', '{val[i][0]}', '{val[i][1]}', '{val[i][2]}', {val[i][6]}, NULL, '{val[i][7]}'), "
# a = a.rstrip(', ')
# cursor.execute(a)
#
#
# #--------------------------Courses------------------------------------
#
# val = [
#     # (id, title, descripton, cover, plan, price)
#     (0, 'Python', 'На Python пишут веб-приложения и нейросети, проводят научные вычисления и автоматизируют процессы. Язык просто выучить, даже если вы никогда не программировали.',
#      'Python.jpj', ' ', 5000),
#     (1, 'SQL для анализа данных', 'Курс для тех, кому нужно работать с базами данных. Вы освоите язык запросов SQL — и с его помощью сможете самостоятельно получать нужные данные, сопоставлять и анализировать их.',
#      'SQL.jpg', ' ', 6000),
#     (2, 'Алгоритмы и структуры данных', 'Вы получите фундаментальные знания и научитесь решать реальные задачи с помощью алгоритмов.',
#      'Algoritms.jpg', ' ', 3000),
#     (3, 'Data Scientist', 'Освойте data science с нуля. Вы попробуете силы в аналитике данных, машинном обучении, дата-инженерии и подробно изучите направление, которое нравится вам больше.',
#      'Data.jpg', ' ', 10000),
#     (4, 'Веб-дизайн', 'Научитесь создавать удобные сайты и приложения, работать с анимацией и презентовать проекты клиентам.',
#      'Web-design.jpg', ' ', 2000),
#     (5, 'Android-разработка', 'Вы научитесь программировать на Kotlin, пройдёте основы Android-разработки и сможете создавать мобильные приложения для смартфонов на этой платформе.',
#      'Android.jpg', ' ', 4000),
#     (6, 'PR-менеджер', 'Вы научитесь формировать положительный имидж продукта и выстраивать бренд-коммуникации с помощью блогеров и СМИ.',
#      'PR.jpg', ' ', 7000),
#     (7, 'Веб-вёрстка', 'Верстальщик воплощает в жизнь замысел веб-дизайнера и создаёт рабочие сайты из дизайн-макетов. На курсе вы научитесь верстать одностраничные лендинги, сайты услуг и мероприятий, интернет-магазины.',
#      'Web-layout.jpg', ' ', 2000),
#     (8, 'Введение в программирование', 'Вы узнаете о современных IT-профессиях и актуальных технологиях. Познакомитесь на практике с популярными языками программирования, напишете сайт и небольшие программы.',
#      'Programming.jpg', ' ', 5000),
#     (9, 'iOS-разработка', 'OS-разработчик создаёт приложения для устройств Apple — онлайн-банки, навигаторы, фитнес-трекеры и другие полезные сервисы. Он программирует логику на языке Swift.',
#      'IOS.jpg', ' ', 6000)
#
# ]
# a = 'INSERT INTO courses(title, description, cover, plan, price) VALUES '
# for i in range(len(val)):
#     a += f"('{val[i][1]}', '{val[i][2]}', '{val[i][3]}', '{val[i][4]}', {val[i][5]}), "
# a = a.rstrip(', ')
#
# cursor.execute(a)
#
#
# # --------------------------Lessons------------------------------------
#
# val = [
#     # (id, idCourse, idUser, title, description, datetime, duration, isComplete, file, commentFile)
#     [0] * 10 + [1] * 10 + [2] * 10 + [3] * 10 + [4] * 10 + [5] * 10 + [6] * 10 + [7] * 10 + [8] * 10 + [9] * 10,
#     [6] * 50 + [7] * 50,
#     [f'Урок {n} №{i}.' for n in ['python', 'SQL', 'Алгоритмы и структуры данных',
#                                           'Data Scientist', 'Веб-дизайн', 'Android', 'PR',
#                                           'Веб-вёрстке', 'Введение в программирование', 'iOS'] for i in range(1, 11)],
#     [f'Описание к уроку {n} №{i}.' for n in ['python', 'SQL', 'Алгоритмы и структуры данных',
#                                           'Data Scientist', 'Веб-дизайн', 'Android', 'PR',
#                                           'Веб-вёрстке', 'Введение в программирование', 'iOS'] for i in range(1, 11)],
#     [f"NOW() + interval '{random.randint(2, 120)} day {random.randint(2, 300)} minutes'" for i in range(100)],
#     [random.randint(1, 4) * 60 for i in range(100)],
#     [random.choice(['True', 'False']) for i in range(100)],
#     ['NULL'] * 100,
#     ['NULL'] * 100
# ]
# a = 'INSERT INTO lessons("idCourse", "idUser", title, description, datetime, duration, "isComplete", file, "commentFile") VALUES '
# for i in range(100):
#     a += f"({val[0][i] + 1}, {val[1][i]}, '{val[2][i]}', '{val[3][i]}', {val[4][i]}, {val[5][i]}, {val[6][i]}, {val[7][i]}, {val[8][i]}), "
# a = a.rstrip(', ')
#
# cursor.execute(a)
#
#
# # ---------------------Tokens-----------------------------------------
#
# val = [
#     # (id, token, idUser)
#     [''.join(random.choice(list(string.ascii_lowercase) + list('0123456789')) for i in range(20)) for j in range(7)]
# ]
# a = 'INSERT INTO tokens(token, "idUser") VALUES '
# for i in range(7):
#     a += f"('{val[0][i]}', {i + 1}), "
# a = a.rstrip(', ')
#
# cursor.execute(a)
#
# # ---------------------Tags-----------------------------------------
#
# val = [
#     # (id, name)
#     [0, 'Программирование'],
#     [1, 'Дизайн'],
#     [2, 'Работа с людьми'],
#     [3, 'Базы данных'],
#     [4, 'Мобильная разработка'],
#     [5, 'Легкий'],
#     [6, 'Средний'],
#     [7, 'Сложный'],
#     [8, 'Python'],
#     [9, 'SQL'],
#     [10, 'Kotlin'],
#     [11, 'Swift'],
#     [12, 'HTML'],
#     [13, 'CSS'],
#     [14, 'Для новичков'],
#     [15, 'Java']
# ]
# a = 'INSERT INTO tags(name) VALUES '
# for i in range(16):
#     a += f"('{val[i][1]}'), "
# a = a.rstrip(', ')
#
# cursor.execute(a)
#
#
# # ---------------------CourseMentors-----------------------------------------
#
# val = [
#     # (id, idCourse, idMentor)
#     [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 2, 4, 6, 8],
#     [0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 2, 4, 3, 4, 0]
# ]
# a = 'INSERT INTO courseMentors("idCourse", "idMentor") VALUES '
# for i in range(len(val[0])):
#     a += f"({val[0][i] + 1}, {val[1][i] + 1}), "
# a = a.rstrip(', ')
#
# cursor.execute(a)
#
#
# # ----------------------TagsCourses----------------------------------------
#
# val = [
#     # (id, idTag, idCourse)
#     [0, 8, 5, 14, 9, 5, 3, 0, 7, 3, 6, 2, 1, 12, 13, 5, 6, 10, 15, 2, 7, 12, 13, 5, 0, 5, 14, 11, 6, 0],
#     [0, 0, 0, 0,  1, 1, 1, 2, 2, 3, 3, 4, 4,  4,  4, 4, 5,  5,  5, 6, 6,  7,  7, 7, 8, 8,  8,  9, 9, 9]
# ]
# a = 'INSERT INTO tagsCourses("idTag", "idCourse") VALUES '
# for i in range(len(val[0])):
#     a += f"({val[1][i] + 1}, {val[0][i] + 1}), "
# a = a.rstrip(', ')
#
# cursor.execute(a)
#
#
# # ---------------------Materials-----------------------------------------
#
# val = [
#     # (id, title, cover, url)
#     ['Документация Python', ' ', 'https://www.python.org/doc/'],
#     ['Документация Swift', ' ', 'https://www.swift.org/documentation/'],
#     ['Документация HTML', ' ', 'https://developer.mozilla.org/ru/docs/Web/HTML'],
#     ['Документация CSS', ' ', 'https://developer.mozilla.org/ru/docs/Web/CSS/Reference'],
#     ['Документация SQL', ' ', 'https://dev.mysql.com/doc/']
# ]
# a = 'INSERT INTO materials(title, cover, url) VALUES '
# for i in range(len(val)):
#     a += f"('{val[i][0]}', '{val[i][1]}', '{val[i][2]}'), "
# a = a.rstrip(', ')
#
# cursor.execute(a)
#
#
# # ---------------------SoldCourses-----------------------------------------
#
# val = [
#     # (id, idUser, idCourse, startEducation)
#     ['5', '0', 'DATE(NOW())'],
#     ['5', '1', 'DATE(NOW())'],
#     ['5', '2', 'DATE(NOW())'],
#     ['5', '3', 'DATE(NOW())'],
#     ['5', '4', 'DATE(NOW())'],
#     ['6', '5', 'DATE(NOW())'],
#     ['6', '6', 'DATE(NOW())'],
#     ['6', '7', 'DATE(NOW())'],
#     ['6', '8', 'DATE(NOW())'],
#     ['6', '9', 'DATE(NOW())'],
# ]
# a = 'INSERT INTO soldCourses("idUser", "idCourse", "startEducation") VALUES '
# for i in range(10):
#     a += f"({int(val[i][0]) + 1}, {int(val[i][1]) + 1}, {val[i][2]}), "
# a = a.rstrip(', ')
#
# cursor.execute(a)
#
# # ---------------------Заполнить plan в таблице courses-----------------------------------------
# # Данные берутся из текущих уроков
#
# a = """SELECT * FROM lessons WHERE "idCourse" = 1"""
# cursor.execute(a)
# data = cursor.fetchall()
# ans = []
# for i in range(10):
#     a = f"""SELECT * FROM lessons WHERE "idCourse" = {i + 1}"""
#     cursor.execute(a)
#     data = cursor.fetchall()
#     json = []
#     for j in data:
#         j = {
#             "idCourse": i + 1,
#             "title": j[3],
#             "description": j[4],
#             "duration": j[6],
#             "file": j[8],
#             "commentFile": j[9]
#             }
#         json.append(j)
#     ans.append(json)
# import pprint
# # pprint.pprint(ans)
#
# for i, e in enumerate(ans):
#     a = f"""
#         UPDATE courses
#         SET plan = '{str(e).replace("'", '"')}'
#         WHERE id = {i + 1}
#     """
#     cursor.execute(a)
#
# # --------------------------------------Chats----------------------------------------------------
#
# val = [
#     #(firstIdUser, secondIdCourse)
# ]
# for i in range(1, 6):
#     val.append([i, 6])
# for i in range(1, 6):
#     val.append([i, 7])
#
# a = 'INSERT INTO chats("firstIdUser", "secondIdUser") VALUES '
# for i, j in val:
#     a += f"({i}, {j}), "
# a = a.rstrip(', ')
#
# cursor.execute(a)
#
#
# --------------------------------------Messages---------------------------------------------------------------
ch1 = [
    ['Здравствуйте, вы преподаёте курс Python?', 6],
    ['Да, я.', 1],
    ['Я не могу создать список, поможете?', 6],
    ['Конечно! Что именно у вас не получается?', 1],
    ['', 6],
    ['В этом случае, необходимо добавить отступ слева, список же в цикле!', 1],
    ['Хорошо, теперь поняла, спасибо!', 6],
    ['Удачи!', 1]
]

ch2 = [
    ['Здравствуйте, вы преподаёте курс SQL?', 6],
    ['Да, я.', 2],
    ['Я не могу добавить записи в таблицу, поможете?', 6],
    ['Конечно! Что именно у вас не получается?', 2],
    ['', 6],
    ['В этом случае, необходимо взять название поля в двойные кавычки, потому что в названии есть заглавные буквы!', 1],
    ['Хорошо, теперь работает, спасибо!', 6],
    ['Рад помочь!', 2]
]

ch3 = [
    ['Здравствуйте, вы преподаёте алгоритмы?', 6],
    ['Да, преподаю я.', 3],
    ['У меня не работает бинарный поиск, поможете?', 6],
    ['Конечно! Что именно у вас не получается?', 3],
    ['', 6],
    ['У вас функция возвращает значение, с половинками наоборот, поменяйте знак ">" на "<"!', 3],
    ['Исправила, теперь работает, спасибо!', 6],
    ['Удачи!', 3]
]

ch5 = [
    ['Здравствуйте, вы преподаёте веб-дизайн?', 6],
    ['Да, чем вам помочь?', 5],
    ['У меня не накладывается таблица стилей, поможете?', 6],
    ['Конечно! Расскажите что вы уже сделали!', 5],
    ['', 6],
    ['Банальная ошибка! Добавьте тег со ссылкой на вашу таблицу стилей, как я показывал на уроке.', 5],
    ['Добавила, теперь работает, спасибо!', 6],
    ['Удачи!', 5]
]

ch6 = [
    ['Здравствуйте, вы преподаёте Android?', 7],
    ['Да, чем вам помочь?', 1],
    ['У меня не открывается эмулятор, что делать?', 7],
    ['Это стандартная проблема, у вас не запускается эмулятор, или само приложение не запускается?', 1],
    ['', 7],
    ['Такое частенько случается! Просто переустановите его.', 1],
    ['Спасибо, теперь работает!', 7],
    ['Обращайтесь ещё!', 1]
]

ch9 = [
    ['Здравствуйте, вы вели лекцию "Введение в программирование"?', 7],
    ['Да, я!', 4],
    ['У меня есть вопрос по теме лекции.', 7],
    ['Слушаю!', 4],
    ['', 7],
    ['Android приложения разрабатываются на kotlin, но так же можно использовать C# и python. ', 4],
    ['Спасибо!', 7],
    ['Обращайтесь ещё!', 4]
]



val = [
    #(idChat, text, datetime, idUser, isAudio)
]

for i, e in enumerate(ch1):
    val.append([1, e[0], f"NOW() - interval '5 day 8 hour 12 minute {30 * (len(ch1) - i)} second'", e[1], False])

for i, e in enumerate(ch2):
    val.append([2, e[0], f"NOW() - interval '4 day 3 hour 25 minute {30 * (len(ch1) - i)} second'", e[1], False])

for i, e in enumerate(ch3):
    val.append([3, e[0], f"NOW() - interval '4 day 9 hour 30 minute {30 * (len(ch1) - i)} second'", e[1], False])

for i, e in enumerate(ch5):
    val.append([5, e[0], f"NOW() - interval '3 day 5 hour 46 minute {30 * (len(ch1) - i)} second'", e[1], False])

for i, e in enumerate(ch6):
    val.append([6, e[0], f"NOW() - interval '2 day 10 hour 19 minute {30 * (len(ch1) - i)} second'", e[1], False])

for i, e in enumerate(ch9):
    val.append([9, e[0], f"NOW() - interval '6 day 7 hour 58 minute {30 * (len(ch1) - i)} second'", e[1], False])

for i, e in enumerate(val):
    if e[1] == '':
        val[i][-1] = True

a = 'INSERT INTO messages("idChat", text, datetime, "idUser", "isAudio") VALUES '
for i in val:
    a += f"({i[0]}, '{i[1]}', {i[2]}, {i[3]}, {i[4]}), "
a = a.rstrip(', ')

cursor.execute(a)



connection.commit()

# except (Exception, Error) as error:
#     print("Ошибка при работе с PostgreSQL", error)
#
# finally:
#     if connection:
#         cursor.close()
#         connection.close()
#         print("Соединение с PostgreSQL закрыто")


