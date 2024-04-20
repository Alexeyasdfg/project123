#подключение библиотек
from PyQt5 import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from random import shuffle, randint
#класс Questoin
class Question():
    def __init__(self,question,right_answer, answer1, answer2, answer3):
        self.question = question
        self.right_answer = right_answer
        self.answer1 = answer1
        self.answer2 = answer2
        self.answer3 = answer3
#лист с вопросами
question_list = []
q1 = Question('Какой национальности не существует?', 'Энцы', 'Чулымцы','Смурфы','Алеуты')
question_list.append(q1)
q2 = Question('Кто сильнее: кит или слон?', 'Незнаю', 'Слон','Кит','Медведь')
question_list.append(q2)
q3 = Question('У какой страны больше население?','Бангладеш', 'Швейцария','Эфиопия','Беларусь')
question_list.append(q3)
q4 = Question('Какой язык в Австрии?','Немецкий' , 'Австралийский','Австрийский','Английский')
question_list.append(q4)


app = QApplication([])
main_wind = QWidget()
main_wind.setWindowTitle('Memory card')
main_wind.resize(500, 300)
RadioGroupBox = QGroupBox('Варианты ответов')
Box = QGroupBox('Результаты теста')
button1 = QRadioButton('Энцы')
button2 = QRadioButton('Чулымцы')
button3 = QRadioButton('Смурфы')
button4 = QRadioButton('Алеуты')
answer_button = QPushButton('Ответить')
text = QLabel('Какой национальности не существует?')
text1 = QLabel('Самый сложный вопрос в мире!')
text_box = QLabel('Правильно/Неправильно')
text_box_good = QLabel('Правильный ответ')

radio_buttons = QButtonGroup()
radio_buttons.addButton(button1)
radio_buttons.addButton(button2)
radio_buttons.addButton(button3)
radio_buttons.addButton(button4)
buttons = [button1,button2, button3, button4]
#расположение виджетов по лэйаутам
line1_1 = QVBoxLayout()
line1_1.addWidget(text_box)
line1_1.addWidget(text_box_good, alignment= Qt.AlignCenter)
Box.setLayout(line1_1)
line1 = QHBoxLayout()
line2 = QVBoxLayout()
line3 = QVBoxLayout()
line4 = QHBoxLayout()
line5 = QHBoxLayout()
line_main = QVBoxLayout()

cur_question = randint(0, len(question_list)-1)

def show_result():
    answer_button.setText('Следующий вопрос')
    RadioGroupBox.hide()
    Box.show()

def show_question():
    answer_button.setText('Ответить')
    Box.hide()
    radio_buttons.setExclusive(False)
    button1.setChecked(False)
    button2.setChecked(False)
    button3.setChecked(False)
    button4.setChecked(False)
    radio_buttons.setExclusive(True)
    RadioGroupBox.show()

def start_test():
    if answer_button.text() == 'Следующий вопрос':
        show_question()
    elif answer_button.text() == 'Ответить':
        show_result()
    
def ask(q: Question):      
    shuffle(buttons)
    text.setText(q.question)
    buttons[0].setText(q.right_answer)
    buttons[1].setText(q.answer1)
    buttons[2].setText(q.answer2)
    buttons[3].setText(q.answer3)   

def show_correct(text_in1):
    text_box.setText(text_in1)
    text_box_good.setText(buttons[0].text())


def check_answer():
    main_wind.score +=1
    if buttons[0].isChecked():
        text_in1 = 'Правильно!'
        main_wind.right +=1
    else:
        text_in1 = 'Неправильно!'
    show_correct(text_in1)
    print('Статистика')
    print('-Всего вопросов:',main_wind.score)
    print('-Правильных ответов:',main_wind.right)
    print('Рейтинг:',main_wind.right/main_wind.score*100,'%')
    
    

def next_question():
   
    cur_question = randint(0, len(question_list)-1)
    ask(question_list[cur_question])  
    print('Статистика')
    print('-Всего вопросов:',main_wind.score)
    print('-Правильных ответов:',main_wind.right)



def click_ok():
    if answer_button.text() == 'Ответить':
        check_answer()
    else:
        next_question()


    


line4.addWidget(text)


line2.addStretch(1)
line2.addWidget(button1,stretch=2)
line2.addStretch(1)
line2.addWidget(button2,stretch=2)
line2.addStretch(1)

line3.addWidget(button3)
line3.addWidget(button4)
line5.addStretch(1)
line5.addWidget(answer_button, stretch=3)
line5.addStretch(1)
line1.addLayout(line2)
line1.addLayout(line3)

RadioGroupBox.setLayout(line1)
line_main.addLayout(line4)
hline = QHBoxLayout()

Box.hide()
hline.addStretch(1)
hline.addWidget(RadioGroupBox,stretch=5)
hline.addWidget(Box,stretch=5)
hline.addStretch(1)
line_main.addLayout(hline)
line_main.addLayout(line5)



main_wind.score = 0
main_wind.right = 0
cur_question = randint(0, len(question_list)-1)
next_question()

answer_button.clicked.connect(click_ok)
main_wind.setLayout(line_main)

answer_button.clicked.connect(start_test)
main_wind.show()
app.exec_()