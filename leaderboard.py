import mysql.connector
import pygame as py



class leaderboard():

    def search(self, name):
        try:
            cnx = mysql.connector.connect(
                host='127.0.0.1',
                database='blockdescenders',
                user='root',
                password='',

            )
        except mysql.connector.Error as err:
            print("Error with connection: {}".format(err))

        else:
            cursor = cnx.cursor()
            query = ("SELECT * FROM leaderboard")
            cursor.execute(query)
            result = cursor.fetchall()
            for i in range(len(result)):
                if result[i][0] == name:
                    return False
                else:
                    return True





    def insert(self, name, level, linescleared, score):
            if self.count() >= 10:
                valid = self.validate(score)
                if valid == False:
                    return
                else:
                    try:
                        cnx = mysql.connector.connect(
                            host='127.0.0.1',
                            database='blockdescenders',
                            user='root',
                            password='',

                        )
                    except mysql.connector.Error as err:
                        print("Error with connection: {}".format(err))

                    else:
                        cursor = cnx.cursor()
                        print("SQL Statement using inputted values")
                        query = "INSERT INTO  leaderboard(name, lvl, linescleared, score) VALUES (%s,%s,%s,%s)"
                        data = (name, level, linescleared, score)
                        print(query)

                        cursor.execute(query, data)
                        cnx.commit()
                        cnx.close()
            else:
                try:
                    cnx = mysql.connector.connect(
                        host='127.0.0.1',
                        database='blockdescenders',
                        user='root',
                        password='',
                    )
                except mysql.connector.Error as err:
                    print("Error with connection: {}".format(err))

                else:
                    cursor = cnx.cursor()
                    print("SQL Statement using inputted values")
                    query = "INSERT INTO  leaderboard(name, lvl, linescleared, score) VALUES (%s,%s,%s,%s)"
                    data = (name, level, linescleared, score)
                    print(query)

                    cursor.execute(query, data)
                    cnx.commit()
                    cnx.close()

    def display(self,screen):
        try:
            cnx = mysql.connector.connect(
                host='127.0.0.1',
                database='blockdescenders',
                user='root',
                password='',

            )
        except mysql.connector.Error as err:
            print("Error with connection: {}".format(err))

        else:
            cursor = cnx.cursor()
            screen.fill((255, 255, 255))
            headfont = py.font.SysFont('', 30)
            head2font = py.font.SysFont('', 30)
            normfont = py.font.SysFont('', 30)
            leaderboard = headfont.render('LEADERBOARD', False, (0, 0, 0))
            rank = head2font.render('RANK', False, (0, 0, 0))
            name = head2font.render('NAME', False, (0, 0, 0))
            level = head2font.render('LEVEL', False, (0, 0, 0))
            linesecleared = head2font.render('LINES', False, (0, 0, 0))
            score = head2font.render('SCORE', False, (0, 0, 0))
            playagain = normfont.render("PRESS SPACE TO PLAY AGAIN", False, (0,0,0))
            query2 = ("SELECT * FROM leaderboard")
            cursor.execute(query2)
            results = cursor.fetchall()

            sortedarray = results
            for i in range(1, len(sortedarray)):
                value = sortedarray[i]
                pos = i
                while pos > 0 and sortedarray[pos - 1][3] < value[3]:
                    sortedarray[pos] = sortedarray[pos - 1]
                    pos -= 1
                sortedarray[pos] = value

            def display(index):
                row1 = (sortedarray[index][0] + "         "
                        + str(sortedarray[index][1]) + "             "
                        + str(sortedarray[index][2]) + "            "
                        + str(sortedarray[index][3]))
                content = normfont.render(row1, False, (0, 0, 0))
                return content

            def render(content, y):
                screen.blit(content, (150, y))

            def rankt(rankt):
                if rankt < 10:
                    rankval = "0" + str(rankt)
                else:
                    rankval = str(rankt)
                ranknum = normfont.render(rankval, False, (0, 0, 0))
                return ranknum

            def renderrank(ranknum, y):
                screen.blit(ranknum, (60, y))

            screen.blit(leaderboard, (225, 10))
            screen.blit(rank, (50, 60))
            screen.blit(name, (150, 60))
            screen.blit(level, (250, 60))
            screen.blit(linesecleared, (350, 60))
            screen.blit(score, (450, 60))
            screen.blit(playagain, (150, 550))
            t = 0
            v = 1
            for q in range(len(sortedarray)):
                content = display(q)
                ranknum = rankt(v)
                render(content, 110 + t)
                renderrank(ranknum, 110 + t)
                t += 40
                v += 1
            cnx.close()

    def validate(self, score):
        try:
            cnx = mysql.connector.connect(
                host='127.0.0.1',
                database='blockdescenders',
                user='root',
                password='',

            )
        except mysql.connector.Error as err:
            print("Error with connection: {}".format(err))

        else:
            cursor = cnx.cursor()
            accepted = True
            query =('SELECT * FROM leaderboard WHERE score = (SELECT MIN(score) FROM leaderboard) LIMIT 1;')
            cursor.execute(query)
            results = cursor.fetchall()
            print(results)
            if score < results[0][3]:
                accepted = False
            else:
                query2 = ("CREATE VIEW q1 AS SELECT name FROM leaderboard WHERE score = (SELECT MIN(score) FROM leaderboard) LIMIT 1;")
                cursor.execute(query2)
                query3 = ("DELETE FROM leaderboard WHERE leaderboard.name = (SELECT * FROM q1)  ")
                cursor.execute(query3)
                query4 = ("DROP VIEW q1;")
                cursor.execute(query4)
                cnx.commit()
                cnx.close()
            return accepted





    def count(self):
        try:
            cnx = mysql.connector.connect(
                host='127.0.0.1',
                database='blockdescenders',
                user='root',
                password='',

            )
        except mysql.connector.Error as err:
            print("Error with connection: {}".format(err))

        else:
            cursor = cnx.cursor()
            query = ("SELECT * FROM leaderboard")
            cursor.execute(query)
            results = cursor.fetchall()
            c = len(results)
            cnx.close()
            return c






