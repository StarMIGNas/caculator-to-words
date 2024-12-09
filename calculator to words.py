
from tkinter import *
from tkinter import ttk

def number_to_words_ru():
    try:
        n = int(entry1.get())  # Преобразуем строку в целое число
    except ValueError:
        text1.delete(1.0, END)
        text1.insert(END, "Переобразование работает только для целых чисел")  # Обработка некорректного ввода
        return

    if n == 0:
        entry1.delete(0, END)
        entry1.insert(0, "ноль")
        return

    units = ["", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
    teens = ["десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать",
             "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]
    tens = ["", "десять", "двадцать", "тридцать", "сорок", "пятьдесят",
            "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
    hundreds = ["", "сто", "двести", "триста", "четыреста", "пятьсот",
                "шестьсот", "семьсот", "восемьсот", "девятьсот"]

    # Склонения для тысяч, миллионов и миллиардов
    forms = {
        "тысяча": ["тысяча", "тысячи", "тысяч"],
        "миллион": ["миллион", "миллиона", "миллионов"],
        "миллиард": ["миллиард", "миллиарда", "миллиардов"],
        # добавьте другие формы, если необходимо
    }

    def get_form(value, forms):
        if 10 <= value % 100 <= 20:
            return forms[2]
        elif value % 10 == 1:
            return forms[0]
        elif 2 <= value % 10 <= 4:
            return forms[1]
        else:
            return forms[2]

    def three_digits_to_words(num):
        words = []
        if num >= 100:
            words.append(hundreds[num // 100])
            num %= 100
        if num >= 20:
            words.append(tens[num // 10])
            num %= 10
        if num >= 10:
            words.append(teens[num - 10])
            num = 0
        if num > 0:
            words.append(units[num])
        return words

    parts = []
    groups = [("", 0), ("тысяча", 1), ("миллион", 2), ("миллиард", 3)]
    group_index = 0

    while n > 0:
        current_group = n % 1000
        if current_group > 0:
            words = three_digits_to_words(current_group)
            if groups[group_index][1] == 1:  # Для тысяч меняем 'один' и 'два'
                if len(words) > 0 and words[0] == 'один':
                    words[0] = 'одна'
                elif len(words) > 0 and words[0] == 'два':
                    words[0] = 'две'

            if groups[group_index][0]:
                words.append(get_form(current_group, forms[groups[group_index][0]]))
            parts.append(' '.join(words))
        n //= 1000
        group_index += 1

    result = ' '.join(reversed(parts)).strip()

    # Вставляем результат в поле ввода
    text1.delete(1.0,END)
    text1.insert(END,result.upper())



def delete_entry():
    entry1.delete(0,END)
    text1.delete(1.0,END)
    text1.insert(END, "Вывод сумма не больше 999 милярдов буквами и не меньше 1")


def delete_symbol():
    value=entry1.get()
    entry1.delete(0,END)
    entry1.insert(0,value[0:-1])



def info():
    text1.delete(1.0,END)
    text1.insert(END,"Кнопка Абс переобразует целые числа в текст.")

def add_digit(sym):
    sym = str(sym)
    current_value=entry1.get()
    entry1.delete(0,END)
    entry1.insert(0,current_value+sym)


def calculat():
    value=entry1.get()
    entry1.delete(0,END)
    entry1.insert(0,eval(value))

win = Tk()
win.geometry('400x450')
win.title("Calculator")
win.maxsize(500,500)
entry1=Entry(width=30,bd=5,justify='right',font=('Arial', 18))
entry1.grid(row=0,column=0,columnspan=4)



button1=Button(win,font=('Arial', 18),text='C',width='5',bd=5,command=delete_entry).grid(row=1,column=0,pady=5,padx=5)
button2=Button(win,font=('Arial', 18),text='Del',width='5',bd=5,command=delete_symbol).grid(row=1,column=1,pady=5,padx=5)
button3=Button(win,font=('Arial', 18),text='Абс',width='5',bd=5,command=number_to_words_ru).grid(row=1,column=2,pady=5,padx=5)
button4=Button(win,font=('Arial', 18),text='=',width='5',bd=5,command=calculat).grid(row=5,column=0,pady=5,padx=5)
button5=Button(win,font=('Arial', 18),text='0',width='5',bd=5,command=lambda :add_digit(0)).grid(row=5,column=1,pady=5,padx=5)
button6=Button(win,font=('Arial', 18),text='.',width='5',bd=5,command=lambda :add_digit('.')).grid(row=5,column=2,pady=5,padx=5)
button7=Button(win,font=('Arial', 18),text='?',width='5',bd=5,command=info).grid(row=5,column=3,pady=5,padx=5)

for i in range(3):
    Button(win,font=('Arial', 18),text=i+1,width='5',bd=5,command=lambda x=i + 1: add_digit(x)).grid(row=2,column=i,pady=2,padx=2)

for i in range(3):
    Button(win,font=('Arial', 18),text=i+4,width='5',bd=5,command=lambda x=i + 4: add_digit(x)).grid(row=3,column=i,pady=2,padx=2)

for i in range(3):
    Button(win,font=('Arial', 18),text=i+7,width='5',bd=5,command=lambda x=i + 7: add_digit(x)).grid(row=4,column=i,pady=5,padx=5)

button1=Button(win,font=('Arial', 18),text='*',width='5',bd=5,command=lambda :add_digit('*')).grid(row=1,column=3,pady=5,padx=5)
button1=Button(win,font=('Arial', 18),text='/',width='5',bd=5,command=lambda :add_digit('/')).grid(row=2,column=3,pady=5,padx=5)
button1=Button(win,font=('Arial', 18),text='+',width='5',bd=5,command=lambda :add_digit('+')).grid(row=3,column=3,pady=5,padx=5)
button1=Button(win,font=('Arial', 18),text='-',width='5',bd=5,command=lambda :add_digit('-')).grid(row=4,column=3,pady=5,padx=5)
text1=Text(bd=2,wrap='word',relief="solid",width=35)
text1.grid(row=6,column=0,columnspan=4,sticky='ns')
text1.insert(END,"Вывод сумма не больше 999 милярдов буквами и не меньше 1")
win.mainloop()