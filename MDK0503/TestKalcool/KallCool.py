from tkinter import *
import webbrowser
import math

MainTXT: Entry
OnswText: Label

# Глобальная память калькулятора
memory = 0.0

def main():
    Wnd = DoTkCool(Tk())
    Wnd.mainloop()

def Credits():
    """Посхалка"""
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

def DoTkCool(Wnd: Tk):
    """Сделать окно C😎😎l"""
    # ВЕРХ
    Wnd.title("C😎😎lкулятор")
    Wnd.geometry("500x500")
    Wnd.resizable(False, False)
    lbl = Label(Wnd, text="C😎😎lкулятор", font=("Comic Sans MS", 14))
    btn = Button(Wnd, text="Автор", font=("Comic Sans MS", 10), command=Credits)
    btn.place(x=450, y=0, height=20)
    lbl.place(x=20, y=0)

    # Поле ввода
    global MainTXT
    MainTXT = Entry(Wnd, width=15, font=("Comic Sans MS", 18))
    MainTXT.bind("<Return>", EkvButCl)
    MainTXT.place(x=10, y=50, height=50)
    EkvBut = Button(Wnd, text="=", font=("Comic Sans MS", 10), command=EkvButCl)
    EkvBut.place(x=250, y=50, height=50)
    global OnswText
    OnswText = Label(Wnd, text="Ответ", font=("Comic Sans MS", 18))
    OnswText.place(x=300, y=50, height=50)

    # Кнопки цифр
    O1But = Button(Wnd, text="1", font=("Comic Sans MS", 14), command=lambda: Addnum(1))
    O1But.place(x=10, y=125, height=25)
    O2But = Button(Wnd, text="2", font=("Comic Sans MS", 14), command=lambda: Addnum(2))
    O2But.place(x=65, y=125, height=25)
    O3But = Button(Wnd, text="3", font=("Comic Sans MS", 14), command=lambda: Addnum(3))
    O3But.place(x=120, y=125, height=25)
    O4But = Button(Wnd, text="4", font=("Comic Sans MS", 14), command=lambda: Addnum(4))
    O4But.place(x=10, y=175, height=25)
    O5But = Button(Wnd, text="5", font=("Comic Sans MS", 14), command=lambda: Addnum(5))
    O5But.place(x=65, y=175, height=25)
    O6But = Button(Wnd, text="6", font=("Comic Sans MS", 14), command=lambda: Addnum(6))
    O6But.place(x=120, y=175, height=25)
    O7But = Button(Wnd, text="7", font=("Comic Sans MS", 14), command=lambda: Addnum(7))
    O7But.place(x=10, y=225, height=25)
    O8But = Button(Wnd, text="8", font=("Comic Sans MS", 14), command=lambda: Addnum(8))
    O8But.place(x=65, y=225, height=25)
    O9But = Button(Wnd, text="9", font=("Comic Sans MS", 14), command=lambda: Addnum(9))
    O9But.place(x=120, y=225, height=25)
    O0But = Button(Wnd, text="0", font=("Comic Sans MS", 14), command=lambda: Addnum(0))
    O0But.place(x=65, y=275, height=25)
    OplBut = Button(Wnd, text="+", font=("Comic Sans MS", 14), command=lambda: Addnum("+"))
    OplBut.place(x=175, y=125, height=25)
    OmsBut = Button(Wnd, text="-", font=("Comic Sans MS", 14), command=lambda: Addnum("-"))
    OmsBut.place(x=175, y=175, height=25)
    OmuBut = Button(Wnd, text="*", font=("Comic Sans MS", 14), command=lambda: Addnum("*"))
    OmuBut.place(x=175, y=225, height=25)
    OdivBut = Button(Wnd, text="/", font=("Comic Sans MS", 14), command=lambda: Addnum("/"))
    OdivBut.place(x=225, y=175, height=25)
    OdivBut = Button(Wnd, text=".", font=("Comic Sans MS", 14), command=lambda: Addnum("."))
    OdivBut.place(x=120, y=275, height=25)

    # Дополнительные кнопки операций
    PowBut = Button(Wnd, text="x^y", font=("Comic Sans MS", 10), command=lambda: Addnum("**"))
    PowBut.place(x=225, y=225, height=25)
    SqrtBut = Button(Wnd, text="√", font=("Comic Sans MS", 10), command=sqrt_button)
    SqrtBut.place(x=275, y=125, height=25)
    FactBut = Button(Wnd, text="x!", font=("Comic Sans MS", 10), command=factorial_button)
    FactBut.place(x=275, y=175, height=25)
    MemAddBut = Button(Wnd, text="M+", font=("Comic Sans MS", 10), command=memory_add_button)
    MemAddBut.place(x=275, y=225, height=25)
    MemReadBut = Button(Wnd, text="MR", font=("Comic Sans MS", 10), command=memory_read_button)
    MemReadBut.place(x=325, y=125, height=25)
    MemClearBut = Button(Wnd, text="MC", font=("Comic Sans MS", 10), command=memory_clear_button)
    MemClearBut.place(x=325, y=175, height=25)
    ClearBut = Button(Wnd, text="C", font=("Comic Sans MS", 10), command=clear_button)
    ClearBut.place(x=325, y=225, height=25)

    return Wnd

# ---------- Операции ----------
def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Деление на ноль")
    return a / b

def power(a, b):
    return a ** b

def sqrt(a):
    if a < 0:
        raise ValueError("Корень из отрицательного числа")
    return math.sqrt(a)

def factorial(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Факториал определён для неотрицательных целых чисел")
    return math.factorial(n)

# ---------- Память ----------
def memory_save(value):
    global memory
    memory = float(value)

def memory_add(value):
    global memory
    memory += float(value)

def memory_read():
    return memory

def memory_clear():
    global memory
    memory = 0.0

# ---------- Обработчики кнопок ----------
def clear_button():
    MainTXT.delete(0, END)

def sqrt_button():
    try:
        val = float(MainTXT.get())
        res = sqrt(val)
        OnswText.config(text=str(res))
    except Exception as e:
        OnswText.config(text=f"Ошибка: {e}")

def factorial_button():
    try:
        val = int(MainTXT.get())
        res = factorial(val)
        OnswText.config(text=str(res))
    except Exception as e:
        OnswText.config(text=f"Ошибка: {e}")

def memory_add_button():
    try:
        val = float(MainTXT.get())
        memory_add(val)
        OnswText.config(text=f"M={memory}")
    except Exception as e:
        OnswText.config(text=f"Ошибка: {e}")

def memory_read_button():
    MainTXT.delete(0, END)
    MainTXT.insert(0, str(memory_read()))

def memory_clear_button():
    memory_clear()
    OnswText.config(text="Память очищена")

# ---------- Вычисление выражения ----------
def EkvButCl(event=None):
    """Нажатие на ="""
    expr = MainTXT.get()
    try:
        # Простой парсер для + - * / ** (без скобок)
        # Заменяем ** на специальный маркер, чтобы не конфликтовать с *
        expr = expr.replace("**", "^")
        # Разбиваем по операторам + и - с учётом унарного минуса
        # Для простоты используем eval с ограничением символов
        allowed = set("0123456789+-*/.^() ")
        if not set(expr) <= allowed:
            raise ValueError("Недопустимые символы в выражении")
        # Заменяем ^ обратно на ** для eval
        expr = expr.replace("^", "**")
        # Ограничиваем встроенные функции
        result = eval(expr, {"__builtins__": None}, {})
        OnswText.config(text=str(result))
    except Exception as e:
        OnswText.config(text=f"Ошибка: {e}")

# ---------- Ввод цифр и операторов ----------
def Addnum(num):
    """Добавляет символ в поле ввода"""
    current = MainTXT.get()
    MainTXT.delete(0, END)
    MainTXT.insert(0, current + str(num))

if __name__ == "__main__":
    main()