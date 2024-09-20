import random
import tkinter as tk
from tkinter import messagebox


class Quizz:
    def __init__(self, master):

        self.correct_answers = 0
        self.correct_answer = 0
        self.master = master
        self.var = tk.IntVar()
        self.function_queue_t1 = [self.t1_1, self.t1_2, self.t1_3, self.t1_4, self.t1_5]
        random.shuffle(self.function_queue_t1)

        self.function_queue_t2 = [self.t2_1, self.t2_2, self.t2_3, self.t2_4, self.t2_5]
        random.shuffle(self.function_queue_t2)

        self.function_queue_t3 = [self.t3_1, self.t3_2, self.t3_3, self.t3_4, self.t3_5]
        random.shuffle(self.function_queue_t3)

        self.functions_popped = 0

        self.label = tk.Label(master, text="Welcome to quizz buzz", bg='#FFC7EA', font=('Bodoni', 30,"bold"))
        self.label.pack(padx=20, pady=20)
        self.label1 = tk.Label(master, text="Enjoy the Quizz", bg='#FFC7EA', fg='Black', font=('Bodoni', 30,"bold"))

        # --------------------------------------------------------------------------------------------------------------

        # t111 -> t = topic, 1 = 1st topic , 1 = question , 1 = option count

        self.t111 = tk.Radiobutton(master, text=" Thomas Jefferson", activebackground='#FFC7EA', font=('Arial', 18),
                                   bg='#C85C8E', variable=self.var, value=1)
        self.t112 = tk.Radiobutton(master, text="George Washington", activebackground='#FFC7EA', font=('Arial', 18),
                                   bg='#C85C8E', variable=self.var, value=2)
        self.t113 = tk.Radiobutton(master, text="John Adams", activebackground='#FFC7EA', font=('Arial', 18),
                                   bg='#C85C8E', variable=self.var, value=3)
        self.t114 = tk.Radiobutton(master, text="James Madison", activebackground='#FFC7EA', font=('Arial', 18),
                                   bg='#C85C8E', variable=self.var, value=4)
        self.t121 = tk.Radiobutton(master, text=" Artistic", activebackground='#FFC7EA', font=('Arial', 18),
                                   bg='#C85C8E', variable=self.var, value=5)
        self.t122 = tk.Radiobutton(master, text="Economic", activebackground='#FFC7EA', font=('Arial', 18),
                                   bg='#C85C8E', variable=self.var, value=6)
        self.t123 = tk.Radiobutton(master, text="Feudalism", activebackground='#FFC7EA', font=('Arial', 18),
                                   bg='#C85C8E', variable=self.var, value=7)
        self.t124 = tk.Radiobutton(master, text="Plague", activebackground='#FFC7EA', font=('Arial', 18),
                                   bg='#C85C8E', variable=self.var, value=8)
        self.t131 = tk.Radiobutton(master, text="Political", activebackground='#FFC7EA', font=('Arial', 18),
                                   bg='#C85C8E', variable=self.var, value=9)
        self.t132 = tk.Radiobutton(master, text="Cultural", activebackground='#FFC7EA', font=('Arial', 18),
                                   bg='#C85C8E', variable=self.var, value=10)
        self.t133 = tk.Radiobutton(master, text="Feudalism", activebackground='#FFC7EA', font=('Arial', 18),
                                   bg='#C85C8E', variable=self.var, value=11)
        self.t134 = tk.Radiobutton(master, text=" Decline", activebackground='#FFC7EA', font=('Arial', 18),
                                   bg='#C85C8E', variable=self.var, value=12)
        self.t141 = tk.Radiobutton(master, text="Chandragupta", activebackground='#FFC7EA', font=('Arial', 18),
                                   bg='#C85C8E', variable=self.var, value=13)
        self.t142 = tk.Radiobutton(master, text="Ashoka", activebackground='#FFC7EA', font=('Arial', 18),
                                   bg='#C85C8E', variable=self.var, value=14)
        self.t143 = tk.Radiobutton(master, text="Harsha", activebackground='#FFC7EA', font=('Arial', 18),
                                   bg='#C85C8E', variable=self.var, value=15)
        self.t144 = tk.Radiobutton(master, text="Akbar", activebackground='#FFC7EA', font=('Arial', 18),
                                   bg='#C85C8E', variable=self.var, value=16)
        self.t151 = tk.Radiobutton(master, text="1942", activebackground='#FFC7EA', font=('Arial', 18),
                                   bg='#C85C8E', variable=self.var, value=17)
        self.t152 = tk.Radiobutton(master, text="1947", activebackground='#FFC7EA', font=('Arial', 18),
                                   bg='#C85C8E', variable=self.var, value=18)
        self.t153 = tk.Radiobutton(master, text="1950", activebackground='#FFC7EA', font=('Arial', 18),
                                   bg='#C85C8E', variable=self.var, value=19)
        self.t154 = tk.Radiobutton(master, text="1962", activebackground='#FFC7EA', font=('Arial', 18),
                                   bg='#C85C8E', variable=self.var, value=20)
        # -------------------------------------------------------------------------------------------------------------------
        # t211 -> t = topic, 2 = 2st topic , 1 = question , 1 = option count

        self.t211 = tk.Radiobutton(master, text="Australia", activebackground='#FFC7EA', font=('Arial', 18),
                                   bg='#C85C8E', variable=self.var, value=21)
        self.t212 = tk.Radiobutton(master, text="India", activebackground='#FFC7EA', font=('Arial', 18),
                                   bg='#C85C8E', variable=self.var, value=22)
        self.t213 = tk.Radiobutton(master, text="England", activebackground='#FFC7EA', font=('Arial', 18),
                                   bg='#C85C8E', variable=self.var, value=23)
        self.t214 = tk.Radiobutton(master, text="West Indies", activebackground='#FFC7EA', font=('Arial', 18),
                                   bg='#C85C8E', variable=self.var, value=24)
        self.t221 = tk.Radiobutton(master, text=" Lionel Messi", activebackground='#FFC7EA', font=('Arial', 18),
                                   bg='#C85C8E', variable=self.var, value=25)
        self.t222 = tk.Radiobutton(master, text="Cristiano Ronaldo", activebackground='#FFC7EA', font=('Arial', 18),
                                   bg='#C85C8E', variable=self.var, value=26)
        self.t223 = tk.Radiobutton(master, text="Pelé", activebackground='#FFC7EA', font=('Arial', 18),
                                   bg='#C85C8E', variable=self.var, value=27)
        self.t224 = tk.Radiobutton(master, text="Diego Maradona", activebackground='#FFC7EA', font=('Arial', 18),
                                   bg='#C85C8E', variable=self.var, value=28)
        self.t231 = tk.Radiobutton(master, text="Serena", activebackground='#FFC7EA', font=('Arial', 18),
                                   bg='#C85C8E', variable=self.var, value=29)
        self.t232 = tk.Radiobutton(master, text="Sharapova", activebackground='#FFC7EA', font=('Arial', 18),
                                   bg='#C85C8E', variable=self.var, value=30)
        self.t233 = tk.Radiobutton(master, text="Osaka", activebackground='#FFC7EA', font=('Arial', 18),
                                   bg='#C85C8E', variable=self.var, value=31)
        self.t234 = tk.Radiobutton(master, text="Graf", activebackground='#FFC7EA', font=('Arial', 18),
                                   bg='#C85C8E', variable=self.var, value=32)
        self.t241 = tk.Radiobutton(master, text="Strike", activebackground='#FFC7EA', font=('Arial', 18),
                                   bg='#C85C8E', variable=self.var, value=33)
        self.t242 = tk.Radiobutton(master, text="Spare", activebackground='#FFC7EA', font=('Arial', 18),
                                   bg='#C85C8E', variable=self.var, value=34)
        self.t243 = tk.Radiobutton(master, text="Turkey", activebackground='#FFC7EA', font=('Arial', 18),
                                   bg='#C85C8E', variable=self.var, value=35)
        self.t244 = tk.Radiobutton(master, text="Perfect Game", activebackground='#FFC7EA', font=('Arial', 18),
                                   bg='#C85C8E', variable=self.var, value=36)
        self.t251 = tk.Radiobutton(master, text="Badminton", activebackground='#FFC7EA', font=('Arial', 18),
                                   bg='#C85C8E', variable=self.var, value=37)
        self.t252 = tk.Radiobutton(master, text="Volleyball", activebackground='#FFC7EA', font=('Arial', 18),
                                   bg='#C85C8E', variable=self.var, value=38)
        self.t253 = tk.Radiobutton(master, text=" Table Tennis", activebackground='#FFC7EA', font=('Arial', 18),
                                   bg='#C85C8E', variable=self.var, value=39)
        self.t254 = tk.Radiobutton(master, text="Tennis", activebackground='#FFC7EA', font=('Arial', 18),
                                   bg='#C85C8E', variable=self.var, value=40)

        # --------------------------------------------------------------------------------------------------------------

        # t311 -> t = topic, 3 = 3st topic , 1 = question , 1 = option count

        self.t311 = tk.Radiobutton(master, text="China", activebackground='#FFC7EA', font=('Arial', 18),
                                   bg='#C85C8E', variable=self.var, value=41)
        self.t312 = tk.Radiobutton(master, text="Japan", activebackground='#FFC7EA', font=('Arial', 18),
                                   bg='#C85C8E', variable=self.var, value=42)
        self.t313 = tk.Radiobutton(master, text="Thailand", activebackground='#FFC7EA', font=('Arial', 18),
                                   bg='#C85C8E', variable=self.var, value=43)
        self.t314 = tk.Radiobutton(master, text="India", activebackground='#FFC7EA', font=('Arial', 18),
                                   bg='#C85C8E', variable=self.var, value=44)
        self.t321 = tk.Radiobutton(master, text="Eiffel Tower", activebackground='#FFC7EA', font=('Arial', 18),
                                   bg='#C85C8E', variable=self.var, value=45)
        self.t322 = tk.Radiobutton(master, text="Colosseum", activebackground='#FFC7EA', font=('Arial', 18),
                                   bg='#C85C8E', variable=self.var, value=46)
        self.t323 = tk.Radiobutton(master, text="Big Ben", activebackground='#FFC7EA', font=('Arial', 18),
                                   bg='#C85C8E', variable=self.var, value=47)
        self.t324 = tk.Radiobutton(master, text="Statue of Liberty", activebackground='#FFC7EA', font=('Arial', 18),
                                   bg='#C85C8E', variable=self.var, value=48)
        self.t331 = tk.Radiobutton(master, text="Atlantic", activebackground='#FFC7EA', font=('Arial', 18),
                                   bg='#C85C8E', variable=self.var, value=49)
        self.t332 = tk.Radiobutton(master, text="Indian", activebackground='#FFC7EA', font=('Arial', 18),
                                   bg='#C85C8E', variable=self.var, value=50)
        self.t333 = tk.Radiobutton(master, text=" Southern", activebackground='#FFC7EA', font=('Arial', 18),
                                   bg='#C85C8E', variable=self.var, value=51)
        self.t334 = tk.Radiobutton(master, text="Pacific", activebackground='#FFC7EA', font=('Arial', 18),
                                   bg='#C85C8E', variable=self.var, value=52)
        self.t341 = tk.Radiobutton(master, text=" Sahara", activebackground='#FFC7EA', font=('Arial', 18),
                                   bg='#C85C8E', variable=self.var, value=53)
        self.t342 = tk.Radiobutton(master, text="Gobi", activebackground='#FFC7EA', font=('Arial', 18),
                                   bg='#C85C8E', variable=self.var, value=54)
        self.t343 = tk.Radiobutton(master, text="Antarctic", activebackground='#FFC7EA', font=('Arial', 18),
                                   bg='#C85C8E', variable=self.var, value=55)
        self.t344 = tk.Radiobutton(master, text="Atacama", activebackground='#FFC7EA', font=('Arial', 18),
                                   bg='#C85C8E', variable=self.var, value=56)
        self.t351 = tk.Radiobutton(master, text="Suez Canal", activebackground='#FFC7EA', font=('Arial', 18),
                                   bg='#C85C8E', variable=self.var, value=57)
        self.t352 = tk.Radiobutton(master, text="Panama Canal", activebackground='#FFC7EA', font=('Arial', 18),
                                   bg='#C85C8E', variable=self.var, value=58)
        self.t353 = tk.Radiobutton(master, text="Corinth Canal", activebackground='#FFC7EA', font=('Arial', 18),
                                   bg='#C85C8E', variable=self.var, value=59)
        self.t354 = tk.Radiobutton(master, text="Grand Canal", activebackground='#FFC7EA', font=('Arial', 18),
                                   bg='#C85C8E', variable=self.var, value=60)

        # --------------------------------------------------------------------------------------------------------------

        self.btn1 = tk.Button(master, text="Start", font=('Arial', 18), bg='#C85C8E', command=self.topicbtn)
        self.btn1.pack(padx=80, pady=80)

        self.btn2 = tk.Button(self.master, text="HISTORY", font=('Arial', 15), bg='#C85C8E', activebackground="#FFFFFF",
                              command=self.topic1)
        self.btn3 = tk.Button(self.master, text="SPORTS", font=('Arial', 15), activebackground="#FFFFFF", bg='#C85C8E',
                              command=self.topic2)
        self.btn4 = tk.Button(self.master, text="TOURISM", font=('Arial', 15), activebackground="#FFFFFF", bg='#C85C8E',
                              command=self.topic3)

        self.btn5 = tk.Button(self.master, text="LET'S BEGIN ->", font=('Arial', 15), bg='#C85C8E',
                              command=self.t1_ran)
        self.btn6 = tk.Button(self.master, text="LET'S START ->", font=('Arial', 15), bg='#C85C8E',
                              command=self.t2_ran)
        self.btn7 = tk.Button(self.master, text="LET'S PROCEED ->", font=('Arial', 15), bg='#C85C8E',
                              command=self.t3_ran)

        self.end_quiz_button = tk.Button(master, text="End Quiz", font=('Arial', 18), activebackground="#F32424",
                                         bg='#F32424',
                                         command=self.end_quiz)
        self.end_quiz_button.pack(side="bottom", anchor="s", pady=10)
        # --------------------------------------------------------------------------------------------------------------

        self.function_queue_t1 = [self.t1_1, self.t1_2, self.t1_3, self.t1_4, self.t1_5]
        random.shuffle(self.function_queue_t1)  # Shuffle the list of functions
        self.functions_popped = 0

        self.function_queue_t2 = [self.t2_1, self.t2_2, self.t2_3, self.t2_4, self.t2_5]
        random.shuffle(self.function_queue_t2)  # Shuffle the list of functions
        self.functions_popped = 0

        self.function_queue_t3 = [self.t3_1, self.t3_2, self.t3_3, self.t3_4, self.t3_5]
        random.shuffle(self.function_queue_t3)  # Shuffle the list of functions
        self.functions_popped = 0

    def topicbtn(self):
        self.label.config(text="Select QB, But the topics are Random")

        self.btn1.pack_forget()
        self.btn2.pack(padx=20, pady=20)
        self.btn3.pack(padx=20, pady=20)
        self.btn4.pack(padx=20, pady=20)
        self.end_quiz_button.pack(side="bottom", anchor="s", pady=10)

    # ------------------------------------------------------------------------------------------------------------------
    def topic1(self):

        self.btn1.pack_forget()
        self.btn2.pack_forget()
        self.btn3.pack_forget()
        self.btn4.pack_forget()
        self.label.config(text=" ")
        self.label1.pack(padx=20, pady=20)
        self.btn5.pack(padx=20, pady=20)

        self.end_quiz_button.pack(side="bottom", anchor="s", pady=10)

    def t1_1(self):
        self.label.config(text="1. Who was the first president of the United States?", bg='#FFC7EA',font=('Bodoni', 18,"bold"))
        self.btn2.pack_forget()
        self.btn3.pack_forget()
        self.btn4.pack_forget()
        self.t121.pack_forget()
        self.t122.pack_forget()
        self.t123.pack_forget()
        self.t124.pack_forget()

        self.t131.pack_forget()
        self.t132.pack_forget()
        self.t133.pack_forget()
        self.t134.pack_forget()

        self.t141.pack_forget()
        self.t142.pack_forget()
        self.t143.pack_forget()
        self.t144.pack_forget()

        self.t151.pack_forget()
        self.t152.pack_forget()
        self.t153.pack_forget()
        self.t154.pack_forget()

        self.btn5.pack_forget()

        self.label1.pack_forget()
        self.t111.pack(padx=20, pady=20)
        self.t112.pack(padx=20, pady=20)
        self.t113.pack(padx=20, pady=20)
        self.t114.pack(padx=20, pady=20)
        self.btn1.pack_forget()
        self.btn1 = tk.Button(self.master, text="Next", font=('Arial', 18), bg='#0aa851',
                              command=self.evaluate_and_next_t1)
        self.btn1.pack(padx=10, pady=10)
        self.end_quiz_button.pack(side="bottom", anchor="s", pady=10)

        # Set the correct answer for the current question
        self.correct_answer = 2  # Change this to the correct answer index (1 or 2)

    def t1_2(self):
        self.label.config(text="2.What was the Industrial Revolution, and how did it impact society?", bg='#FFC7EA',font=('Bodoni', 18,"bold"))
        self.t111.pack_forget()
        self.t112.pack_forget()
        self.t113.pack_forget()
        self.t114.pack_forget()

        self.t131.pack_forget()
        self.t132.pack_forget()
        self.t133.pack_forget()
        self.t134.pack_forget()

        self.t141.pack_forget()
        self.t142.pack_forget()
        self.t143.pack_forget()
        self.t144.pack_forget()

        self.t151.pack_forget()
        self.t152.pack_forget()
        self.t153.pack_forget()
        self.t154.pack_forget()

        self.btn5.pack_forget()

        self.label1.pack_forget()
        self.var.set(0)  # Reset the IntVar
        self.t121.pack(padx=20, pady=20)
        self.t122.pack(padx=20, pady=20)
        self.t123.pack(padx=20, pady=20)
        self.t124.pack(padx=20, pady=20)
        self.btn2.pack_forget()
        self.btn3.pack_forget()
        self.btn4.pack_forget()
        self.btn1.pack_forget()
        self.btn1 = tk.Button(self.master, text="Next", font=('Arial', 18), bg='#0aa851',
                              command=self.evaluate_and_next_t1)
        self.btn1.pack(padx=10, pady=10)
        self.end_quiz_button.pack(side="bottom", anchor="s", pady=10)

        # Set the correct answer for the current question
        self.correct_answer = 6  # Change this to the correct answer index (1 or 2)

    def t1_3(self):
        self.label.config(text="3.What was the Renaissance, and what impact did it have on European history?",
                          bg='#FFC7EA',font=('Bodoni', 18,"bold"))
        self.t111.pack_forget()
        self.t112.pack_forget()
        self.t113.pack_forget()
        self.t114.pack_forget()

        self.t121.pack_forget()
        self.t122.pack_forget()
        self.t123.pack_forget()
        self.t124.pack_forget()

        self.t141.pack_forget()
        self.t142.pack_forget()
        self.t143.pack_forget()
        self.t144.pack_forget()

        self.t151.pack_forget()
        self.t152.pack_forget()
        self.t153.pack_forget()
        self.t154.pack_forget()

        self.btn5.pack_forget()

        self.label1.pack_forget()
        self.var.set(0)  # Reset the IntVar
        self.t131.pack(padx=20, pady=20)
        self.t132.pack(padx=20, pady=20)
        self.t133.pack(padx=20, pady=20)
        self.t134.pack(padx=20, pady=20)
        self.btn2.pack_forget()
        self.btn3.pack_forget()
        self.btn4.pack_forget()
        self.btn1.pack_forget()
        self.btn1 = tk.Button(self.master, text="Next", font=('Arial', 18), bg='#0aa851',
                              command=self.evaluate_and_next_t1)
        self.btn1.pack(padx=10, pady=10)
        self.end_quiz_button.pack(side="bottom", anchor="s", pady=10)
        # Set the correct answer for the current question
        self.correct_answer = 10  # Change this to the correct answer index (1 or 2)

    def t1_4(self):
        self.label.config(text="4.Who was the first Emperor of the Maurya Dynasty in ancient India?", bg='#FFC7EA',font=('Bodoni', 18,"bold"))
        self.t111.pack_forget()
        self.t112.pack_forget()
        self.t113.pack_forget()
        self.t114.pack_forget()

        self.t121.pack_forget()
        self.t122.pack_forget()
        self.t123.pack_forget()
        self.t124.pack_forget()

        self.t131.pack_forget()
        self.t132.pack_forget()
        self.t133.pack_forget()
        self.t134.pack_forget()

        self.t151.pack_forget()
        self.t152.pack_forget()
        self.t153.pack_forget()
        self.t154.pack_forget()

        self.btn5.pack_forget()
        self.label1.pack_forget()
        self.var.set(0)  # Reset the IntVar
        self.t141.pack(padx=20, pady=20)
        self.t142.pack(padx=20, pady=20)
        self.t143.pack(padx=20, pady=20)
        self.t144.pack(padx=20, pady=20)
        self.btn2.pack_forget()
        self.btn3.pack_forget()
        self.btn4.pack_forget()
        self.btn1.pack_forget()
        self.btn1 = tk.Button(self.master, text="Next", font=('Arial', 18), bg='#0aa851',
                              command=self.evaluate_and_next_t1)
        self.btn1.pack(padx=10, pady=10)
        self.end_quiz_button.pack(side="bottom", anchor="s", pady=10)
        # Set the correct answer for the current question
        self.correct_answer = 13  # Change this to the correct answer index (1 or 2)

    def t1_5(self):
        self.label.config(text="5.In which year did India gain independence from British rule?", bg='#FFC7EA',font=('Bodoni', 18,"bold"))
        self.btn5.pack_forget()

        self.t111.pack_forget()
        self.t112.pack_forget()
        self.t113.pack_forget()
        self.t114.pack_forget()

        self.t121.pack_forget()
        self.t122.pack_forget()
        self.t123.pack_forget()
        self.t124.pack_forget()

        self.t131.pack_forget()
        self.t132.pack_forget()
        self.t133.pack_forget()
        self.t134.pack_forget()

        self.t141.pack_forget()
        self.t142.pack_forget()
        self.t143.pack_forget()
        self.t144.pack_forget()

        self.label1.pack_forget()
        self.var.set(0)  # Reset the IntVar
        self.t151.pack(padx=20, pady=20)
        self.t152.pack(padx=20, pady=20)
        self.t153.pack(padx=20, pady=20)
        self.t154.pack(padx=20, pady=20)
        self.btn2.pack_forget()
        self.btn3.pack_forget()
        self.btn4.pack_forget()
        self.btn1.pack_forget()
        self.btn1 = tk.Button(self.master, text="Next", font=('Arial', 18), bg='#0aa851',
                              command=self.evaluate_and_next_t1)
        self.btn1.pack(padx=10, pady=10)
        self.end_quiz_button.pack(side="bottom", anchor="s", pady=10)
        # Set the correct answer for the current question
        self.correct_answer = 18  # Change this to the correct answer index (1 or 2)

        # --------------------------------------------------------------------------------------------------------------

    def topic2(self):
        self.btn1.pack_forget()
        self.btn2.pack_forget()
        self.btn3.pack_forget()
        self.btn4.pack_forget()
        self.label.config(text=" ")
        self.label1.pack(padx=20, pady=20)
        self.btn6.pack(padx=20, pady=20)

        self.end_quiz_button.pack(side="bottom", anchor="s", pady=10)

    def t2_1(self):
        self.label.config(
            text="1.Which country is known for its dominance in cricket and has won the most Cricket World Cups?",
            bg='#FFC7EA',font=('Bodoni', 18,"bold"))
        self.btn2.pack_forget()
        self.btn3.pack_forget()
        self.btn4.pack_forget()
        self.t221.pack_forget()
        self.t222.pack_forget()
        self.t223.pack_forget()
        self.t224.pack_forget()

        self.t231.pack_forget()
        self.t232.pack_forget()
        self.t233.pack_forget()
        self.t234.pack_forget()

        self.t241.pack_forget()
        self.t242.pack_forget()
        self.t243.pack_forget()
        self.t244.pack_forget()

        self.t251.pack_forget()
        self.t252.pack_forget()
        self.t253.pack_forget()
        self.t254.pack_forget()

        self.btn6.pack_forget()

        self.label1.pack_forget()
        self.t211.pack(padx=20, pady=20)
        self.t212.pack(padx=20, pady=20)
        self.t213.pack(padx=20, pady=20)
        self.t214.pack(padx=20, pady=20)
        self.btn1.pack_forget()
        self.btn1 = tk.Button(self.master, text="Next", font=('Arial', 18), bg='#0aa851',
                              command=self.evaluate_and_next_t2)
        self.btn1.pack(padx=10, pady=10)
        self.end_quiz_button.pack(side="bottom", anchor="s", pady=10)

        # Set the correct answer for the current question
        self.correct_answer = 21  # Change this to the correct answer index (1 or 2)

    def t2_2(self):
        self.label.config(
            text="2.Who is the all-time leading goal scorer in the history of men's international soccer?",
            bg='#FFC7EA',font=('Bodoni', 18,"bold"))
        self.t211.pack_forget()
        self.t212.pack_forget()
        self.t213.pack_forget()
        self.t214.pack_forget()

        self.t231.pack_forget()
        self.t232.pack_forget()
        self.t233.pack_forget()
        self.t234.pack_forget()

        self.t241.pack_forget()
        self.t242.pack_forget()
        self.t243.pack_forget()
        self.t244.pack_forget()

        self.t251.pack_forget()
        self.t252.pack_forget()
        self.t253.pack_forget()
        self.t254.pack_forget()

        self.btn6.pack_forget()

        self.label1.pack_forget()
        self.var.set(0)  # Reset the IntVar
        self.t221.pack(padx=20, pady=20)
        self.t222.pack(padx=20, pady=20)
        self.t223.pack(padx=20, pady=20)
        self.t224.pack(padx=20, pady=20)
        self.btn2.pack_forget()
        self.btn3.pack_forget()
        self.btn4.pack_forget()
        self.btn1.pack_forget()
        self.btn1 = tk.Button(self.master, text="Next", font=('Arial', 18), bg='#0aa851',
                              command=self.evaluate_and_next_t2)
        self.btn1.pack(padx=10, pady=10)
        self.end_quiz_button.pack(side="bottom", anchor="s", pady=10)

        # Set the correct answer for the current question
        self.correct_answer = 26  # Change this to the correct answer index (1 or 2)

    def t2_3(self):
        self.label.config(text="3.Who is known as the GOAT (Greatest of All Time) in women's tennis?", bg='#FFC7EA',font=('Bodoni', 18,"bold"))
        self.t211.pack_forget()
        self.t212.pack_forget()
        self.t213.pack_forget()
        self.t214.pack_forget()

        self.t221.pack_forget()
        self.t222.pack_forget()
        self.t223.pack_forget()
        self.t224.pack_forget()

        self.t241.pack_forget()
        self.t242.pack_forget()
        self.t243.pack_forget()
        self.t244.pack_forget()

        self.t251.pack_forget()
        self.t252.pack_forget()
        self.t253.pack_forget()
        self.t254.pack_forget()

        self.btn6.pack_forget()

        self.label1.pack_forget()
        self.var.set(0)  # Reset the IntVar
        self.t231.pack(padx=20, pady=20)
        self.t232.pack(padx=20, pady=20)
        self.t233.pack(padx=20, pady=20)
        self.t234.pack(padx=20, pady=20)
        self.btn2.pack_forget()
        self.btn3.pack_forget()
        self.btn4.pack_forget()
        self.btn1.pack_forget()
        self.btn1 = tk.Button(self.master, text="Next", font=('Arial', 18), bg='#0aa851',
                              command=self.evaluate_and_next_t2)
        self.btn1.pack(padx=10, pady=10)
        self.end_quiz_button.pack(side="bottom", anchor="s", pady=10)
        # Set the correct answer for the current question
        self.correct_answer = 29  # Change this to the correct answer index (1 or 2)

    def t2_4(self):
        self.label.config(text="4.What is the term for a perfect score of 300 in a game of ten-pin bowling?",
                          bg='#FFC7EA',font=('Bodoni', 18,"bold"))
        self.t211.pack_forget()
        self.t212.pack_forget()
        self.t213.pack_forget()
        self.t214.pack_forget()

        self.t221.pack_forget()
        self.t222.pack_forget()
        self.t223.pack_forget()
        self.t224.pack_forget()

        self.t231.pack_forget()
        self.t232.pack_forget()
        self.t233.pack_forget()
        self.t234.pack_forget()

        self.t251.pack_forget()
        self.t252.pack_forget()
        self.t253.pack_forget()
        self.t254.pack_forget()

        self.btn6.pack_forget()

        self.label1.pack_forget()
        self.var.set(0)  # Reset the IntVar
        self.t241.pack(padx=20, pady=20)
        self.t242.pack(padx=20, pady=20)
        self.t243.pack(padx=20, pady=20)
        self.t244.pack(padx=20, pady=20)
        self.btn2.pack_forget()
        self.btn3.pack_forget()
        self.btn4.pack_forget()
        self.btn1.pack_forget()
        self.btn1 = tk.Button(self.master, text="Next", font=('Arial', 18), bg='#0aa851',
                              command=self.evaluate_and_next_t2)
        self.btn1.pack(padx=10, pady=10)
        self.end_quiz_button.pack(side="bottom", anchor="s", pady=10)
        # Set the correct answer for the current question
        self.correct_answer = 36  # Change this to the correct answer index (1 or 2)

    def t2_5(self):
        self.label.config(text="5.In which sport would you perform a drop shot?", bg='#FFC7EA',font=('Bodoni', 18,"bold"))
        self.btn6.pack_forget()

        self.t211.pack_forget()
        self.t212.pack_forget()
        self.t213.pack_forget()
        self.t214.pack_forget()

        self.t221.pack_forget()
        self.t222.pack_forget()
        self.t223.pack_forget()
        self.t224.pack_forget()

        self.t231.pack_forget()
        self.t232.pack_forget()
        self.t233.pack_forget()
        self.t234.pack_forget()

        self.t241.pack_forget()
        self.t242.pack_forget()
        self.t243.pack_forget()
        self.t244.pack_forget()

        self.label1.pack_forget()
        self.var.set(0)  # Reset the IntVar
        self.t251.pack(padx=20, pady=20)
        self.t252.pack(padx=20, pady=20)
        self.t253.pack(padx=20, pady=20)
        self.t254.pack(padx=20, pady=20)
        self.btn2.pack_forget()
        self.btn3.pack_forget()
        self.btn4.pack_forget()
        self.btn1.pack_forget()
        self.btn1 = tk.Button(self.master, text="Next", font=('Arial', 18), bg='#0aa851',
                              command=self.evaluate_and_next_t2)
        self.btn1.pack(padx=10, pady=10)
        self.end_quiz_button.pack(side="bottom", anchor="s", pady=10)
        # Set the correct answer for the current question
        self.correct_answer = 40  # Change this to the correct answer index (1 or 2)

    # ------------------------------------------------------------------------------------------------------------------
    def topic3(self):
        self.btn1.pack_forget()
        self.btn2.pack_forget()
        self.btn3.pack_forget()
        self.btn4.pack_forget()
        self.label.config(text=" ")
        self.label1.pack(padx=20, pady=20)
        self.btn7.pack(padx=20, pady=20)

        self.end_quiz_button.pack(side="bottom", anchor="s", pady=10)

    def t3_1(self):
        self.label.config(text="1.Which country is known as the Land of the Rising Sun?", bg='#FFC7EA',font=('Bodoni', 18,"bold"))
        self.btn2.pack_forget()
        self.btn3.pack_forget()
        self.btn4.pack_forget()

        self.t321.pack_forget()
        self.t322.pack_forget()
        self.t323.pack_forget()
        self.t324.pack_forget()

        self.t331.pack_forget()
        self.t332.pack_forget()
        self.t333.pack_forget()
        self.t334.pack_forget()

        self.t341.pack_forget()
        self.t342.pack_forget()
        self.t343.pack_forget()
        self.t344.pack_forget()

        self.t351.pack_forget()
        self.t352.pack_forget()
        self.t353.pack_forget()
        self.t354.pack_forget()

        self.btn7.pack_forget()

        self.label1.pack_forget()
        self.t311.pack(padx=20, pady=20)
        self.t312.pack(padx=20, pady=20)
        self.t313.pack(padx=20, pady=20)
        self.t314.pack(padx=20, pady=20)
        self.btn1.pack_forget()
        self.btn1 = tk.Button(self.master, text="Next", font=('Arial', 18), bg='#0aa851',
                              command=self.evaluate_and_next_t3)
        self.btn1.pack(padx=10, pady=10)
        self.end_quiz_button.pack(side="bottom", anchor="s", pady=10)

        # Set the correct answer for the current question
        self.correct_answer = 42  # Change this to the correct answer index (1 or 2)

    def t3_2(self):
        self.label.config(text="2.Which iconic structure is located in the heart of Paris and is a symbol of love?",
                          bg='#FFC7EA',font=('Bodoni', 18,"bold"))
        self.t311.pack_forget()
        self.t312.pack_forget()
        self.t313.pack_forget()
        self.t314.pack_forget()

        self.t331.pack_forget()
        self.t332.pack_forget()
        self.t333.pack_forget()
        self.t334.pack_forget()

        self.t341.pack_forget()
        self.t342.pack_forget()
        self.t343.pack_forget()
        self.t234.pack_forget()

        self.t351.pack_forget()
        self.t352.pack_forget()
        self.t353.pack_forget()
        self.t354.pack_forget()

        self.btn7.pack_forget()

        self.label1.pack_forget()
        self.var.set(0)  # Reset the IntVar
        self.t321.pack(padx=20, pady=20)
        self.t322.pack(padx=20, pady=20)
        self.t323.pack(padx=20, pady=20)
        self.t324.pack(padx=20, pady=20)
        self.btn2.pack_forget()
        self.btn3.pack_forget()
        self.btn4.pack_forget()
        self.btn1.pack_forget()
        self.btn1 = tk.Button(self.master, text="Next", font=('Arial', 18), bg='#0aa851',
                              command=self.evaluate_and_next_t3)
        self.btn1.pack(padx=10, pady=10)
        self.end_quiz_button.pack(side="bottom", anchor="s", pady=10)

        # Set the correct answer for the current question
        self.correct_answer = 45  # Change this to the correct answer index (1 or 2)

    def t3_3(self):
        self.label.config(text="3.Which ocean is the largest on Earth?", bg='#FFC7EA',font=('Bodoni', 18,"bold"))
        self.t311.pack_forget()
        self.t312.pack_forget()
        self.t313.pack_forget()
        self.t314.pack_forget()

        self.t321.pack_forget()
        self.t322.pack_forget()
        self.t323.pack_forget()
        self.t324.pack_forget()

        self.t341.pack_forget()
        self.t342.pack_forget()
        self.t343.pack_forget()
        self.t344.pack_forget()

        self.t351.pack_forget()
        self.t352.pack_forget()
        self.t353.pack_forget()
        self.t354.pack_forget()

        self.btn7.pack_forget()

        self.label1.pack_forget()
        self.var.set(0)  # Reset the IntVar
        self.t331.pack(padx=20, pady=20)
        self.t332.pack(padx=20, pady=20)
        self.t333.pack(padx=20, pady=20)
        self.t334.pack(padx=20, pady=20)
        self.btn2.pack_forget()
        self.btn3.pack_forget()
        self.btn4.pack_forget()
        self.btn1.pack_forget()
        self.btn1 = tk.Button(self.master, text="Next", font=('Arial', 18), bg='#0aa851',
                              command=self.evaluate_and_next_t3)
        self.btn1.pack(padx=10, pady=10)
        self.end_quiz_button.pack(side="bottom", anchor="s", pady=10)
        # Set the correct answer for the current question
        self.correct_answer = 52  # Change this to the correct answer index (1 or 2)

    def t3_4(self):
        self.label.config(text="4.What is the world's largest desert by area?", bg='#FFC7EA',font=('Bodoni', 18,"bold"))
        self.t311.pack_forget()
        self.t312.pack_forget()
        self.t313.pack_forget()
        self.t314.pack_forget()

        self.t321.pack_forget()
        self.t322.pack_forget()
        self.t323.pack_forget()
        self.t324.pack_forget()

        self.t331.pack_forget()
        self.t332.pack_forget()
        self.t333.pack_forget()
        self.t334.pack_forget()

        self.t351.pack_forget()
        self.t352.pack_forget()
        self.t353.pack_forget()
        self.t354.pack_forget()

        self.btn7.pack_forget()
        self.label1.pack_forget()
        self.var.set(0)  # Reset the IntVar
        self.t341.pack(padx=20, pady=20)
        self.t342.pack(padx=20, pady=20)
        self.t343.pack(padx=20, pady=20)
        self.t344.pack(padx=20, pady=20)
        self.btn2.pack_forget()
        self.btn3.pack_forget()
        self.btn4.pack_forget()
        self.btn1.pack_forget()
        self.btn1 = tk.Button(self.master, text="Next", font=('Arial', 18), bg='#0aa851',
                              command=self.evaluate_and_next_t3)
        self.btn1.pack(padx=10, pady=10)
        self.end_quiz_button.pack(side="bottom", anchor="s", pady=10)
        # Set the correct answer for the current question
        self.correct_answer = 55  # Change this to the correct answer index (1 or 2)

    def t3_5(self):
        self.label.config(text="5.Which famous canal connects the Mediterranean Sea to the Red Sea?", bg='#FFC7EA',font=('Bodoni', 18,"bold"))
        self.btn7.pack_forget()

        self.t311.pack_forget()
        self.t312.pack_forget()
        self.t313.pack_forget()
        self.t314.pack_forget()

        self.t321.pack_forget()
        self.t322.pack_forget()
        self.t323.pack_forget()
        self.t324.pack_forget()

        self.t331.pack_forget()
        self.t332.pack_forget()
        self.t333.pack_forget()
        self.t334.pack_forget()

        self.t341.pack_forget()
        self.t342.pack_forget()
        self.t343.pack_forget()
        self.t344.pack_forget()

        self.label1.pack_forget()
        self.var.set(0)  # Reset the IntVar
        self.t351.pack(padx=20, pady=20)
        self.t352.pack(padx=20, pady=20)
        self.t353.pack(padx=20, pady=20)
        self.t354.pack(padx=20, pady=20)
        self.btn2.pack_forget()
        self.btn3.pack_forget()
        self.btn4.pack_forget()
        self.btn1.pack_forget()
        self.btn1 = tk.Button(self.master, text="Next", font=('Arial', 18), bg='#0aa851',
                              command=self.evaluate_and_next_t3)
        self.btn1.pack(padx=10, pady=10)
        self.end_quiz_button.pack(side="bottom", anchor="s", pady=10)
        # Set the correct answer for the current question
        self.correct_answer = 57  # Change this to the correct answer index (1 or 2)

    # ------------------------------------------------------------------------------------------------------------------
    def evaluate_and_next_t1(self):
        # Evaluate the selected answer and update the score
        selected_answer = self.var.get()
        if selected_answer == self.correct_answer:
            self.correct_answers += 1  # Increment correct_answers when the answer is correct

        # Continue to the next random function
        self.t1_ran()

    def evaluate_and_next_t2(self):
        # Evaluate the selected answer and update the score
        selected_answer = self.var.get()
        if selected_answer == self.correct_answer:
            self.correct_answers += 1  # Increment correct_answers when the answer is correct

        # Continue to the next random function
        self.t2_ran()

    def evaluate_and_next_t3(self):
        # Evaluate the selected answer and update the score
        selected_answer = self.var.get()
        if selected_answer == self.correct_answer:
            self.correct_answers += 1  # Increment correct_answers when the answer is correct

        # Continue to the next random function
        self.t3_ran()

    # ------------------------------------------------------------------------------------------------------------------

    def t1_ran(self):
        if self.function_queue_t1:
            selected_function = self.function_queue_t1.pop()  # Corrected line
            self.functions_popped += 1  # Increment functions_popped when a new function is chosen
            selected_function()
        else:
            # All functions have been used, reset the queue and counter
            self.function_queue_t1 = [self.t1_1, self.t1_2, self.t1_3, self.t1_4, self.t1_5]
            random.shuffle(self.function_queue_t1)
            self.functions_popped = 0

            # Display a message thanking the participant
            messagebox.showinfo("Quiz Ended", "Thanks for participating! Come again.")

            # Display a message with the score
            score_message = f"Quiz Ended\n\nScore: {self.correct_answers}/5"
            messagebox.showinfo("Quiz Score", score_message)

            self.master.destroy()

    # ------------------------------------------------------------------------------------------------------------------

    def t2_ran(self):
        if self.function_queue_t2:
            selected_function = self.function_queue_t2.pop()  # Corrected line
            self.functions_popped += 1  # Increment functions_popped when a new function is chosen
            selected_function()
        else:
            # All functions have been used, reset the queue and counter
            self.function_queue_t2 = [self.t2_1, self.t2_2, self.t2_3, self.t2_4, self.t2_5]
            random.shuffle(self.function_queue_t2)
            self.functions_popped = 0

            # Display a message thanking the participant
            messagebox.showinfo("Quiz Ended", "Thanks for participating! Come again.")

            # Display a message with the score
            score_message = f"Quiz Ended\n\nScore: {self.correct_answers}/5"
            messagebox.showinfo("Quiz Score", score_message)

            self.master.destroy()

    # ------------------------------------------------------------------------------------------------------------------

    def t3_ran(self):
        if self.function_queue_t3:
            selected_function = self.function_queue_t3.pop()  # Corrected line
            self.functions_popped += 1  # Increment functions_popped when a new function is chosen
            selected_function()
        else:
            # All functions have been used, reset the queue and counter
            self.function_queue_t3 = [self.t3_1, self.t3_2, self.t3_3, self.t3_4, self.t3_5]
            random.shuffle(self.function_queue_t3)
            self.functions_popped = 0

            # Display a message thanking the participant
            messagebox.showinfo("Quiz Ended", "Thanks for participating! Come again.")

            # Display a message with the score
            score_message = f"Quiz Ended\n\nScore: {self.correct_answers}/5"
            messagebox.showinfo("Quiz Score", score_message)

            self.master.destroy()

    def end_quiz(self):
        result = messagebox.showinfo("Quiz Ended", "Thanks for participating! Come again.")
        if result == "ok":
            self.master.destroy()


root = tk.Tk()
root.geometry('1070x600')
root.configure(bg='#FFC7EA')
root.title("QUIZZ BUZZ")
quizz_instance = Quizz(root)
root.mainloop()
