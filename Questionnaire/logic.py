import sqlite3
con = sqlite3.connect("../db.sqlite3")
print('database connected')
cur = con.cursor()

# for QN in range(1,11):
#             statement = f"SELECT question{QN} FROM Questionnaire_questionnaire WHERE userid={questions.UserID}"
#             cur.execute(statement)
#             data = cur.fetchall()
#             print(data[0][0])
#         con.close()
class questions:
    UserID = 0
    QN = 1
    QUESTIONS = ["1. I don't feel like doing anything." ,
        '2. I am feeling bored.',
        '3. Nothing seems fun anymore./ I hardly enjoy anything.',
        '4. I find beauty in things around me.',
        '5. I feel loved.',
        "6. I’ve been feeling confident.",
        '7. I feel like my opinion/efforts are not appreciated.',
        "8. I have completed today’s agenda.",
        '9. I get irritated easily.',
        "10. Recently, I have trouble with concentration."]

    OPTIONS = ["Strongly Disagree" ,"Disagree", "Can't Say", "Agree", "Strongly Agree"]
    def __init__(self) -> None:
        pass

    # def show_questions(self,QN):
    #     return questions.QUESTIONS[QN-1]
    
    # def show_options(self):
    #     return questions.OPTIONS
    
    def get_answer(self,QN):
        statement = f"SELECT question{QN} FROM Questionnaire_questionnaire WHERE userid={questions.UserID}"
        cur.execute(statement)
        data = cur.fetchall()
        return data[0][0]

    def xcalculate(self,QN):
        answer = questions.get_answer(QN)
        statement = f"SELECT {answer} FROM Questionnaire_xweightage WHERE QuestionNumber = {QN}"
        cur.execute(statement)
        x = cur.fetchall()
        return x
    
    def ycalculate(self,QN):
        answer = questions.get_answer(QN)
        statement = f"SELECT {answer} FROM Questionnaire_yweightage WHERE QuestionNumber = {QN}"
        cur.execute(statement)
        y = cur.fetchall()
        return y
    
    def get_mood(self):
        pass
