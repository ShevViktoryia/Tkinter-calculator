import tkinter

numbers = []

def press_btn(num):
  global numbers
  result_expression = ''

  if num != "/" and num != '+' and num != '*' and num != '-' and num != '-' and num != 'C':
    text_input.insert("end", num)
    numbers.append(num)
  else:
    text_input.delete(1.0, "end")
    numbers.append(num)

  if len(numbers)>=3 and (numbers[-2] == '/' or numbers[-2] == '+' or numbers[-2] == '*' or numbers[-2] == '-'):
    text_input.delete(1.0, "end")
    result_expression = eval(result_expression.join(numbers[0:]))
    text_input.insert(1.0, result_expression)
    numbers = [str(result_expression)]

  if num == "C":
    text_input.delete(1.0, "end")
    numbers = []

  if num == "%":
    cur_num = text_input.get(1.0, "end")
    text_input.delete(1.0, "end")
    if cur_num != '':
      numbers = []
      numbers.append(cur_num[0:-2])
      text_input.insert(1.0, float(numbers[0])/100)


window = tkinter.Tk()

window.title("Calculator")
window.geometry("400x320")

text_input = tkinter.Text(window, width=31, height=1.3, font=("Helvetica", 16))
text_input.grid(columnspan=3, padx=10, pady=10)

button = tkinter.Button(window, text="7", width=10, height=3, bg="lightgrey", command=lambda: press_btn("7"))
button.place(x=10, y=60)

button = tkinter.Button(window, text="8", width=10, height=3, bg="lightgrey", command=lambda: press_btn("8"))
button.place(x=110, y=60)

button = tkinter.Button(window, text="9", width=10, height=3, bg="lightgrey", command=lambda: press_btn("9"))
button.place(x=210, y=60)

button = tkinter.Button(window, text="/", width=9, height=3, bg="lightgrey", command=lambda: press_btn("/"))
button.place(x=310, y=60)

button = tkinter.Button(window, text="4", width=10, height=3, bg="lightgrey", command=lambda: press_btn("4"))
button.place(x=10, y=120)

button = tkinter.Button(window, text="5", width=10, height=3, bg="lightgrey", command=lambda: press_btn("5"))
button.place(x=110, y=120)

button = tkinter.Button(window, text="6", width=10, height=3, bg="lightgrey", command=lambda: press_btn("6"))
button.place(x=210, y=120)

button = tkinter.Button(window, text='*', width=9, height=3, bg="lightgrey", command=lambda: press_btn('*'))
button.place(x=310, y=120)

button = tkinter.Button(window, text="1", width=10, height=3, bg="lightgrey", command=lambda: press_btn("1"))
button.place(x=10, y=180)

button = tkinter.Button(window, text="2", width=10, height=3, bg="lightgrey", command=lambda: press_btn("2"))
button.place(x=110, y=180)

button = tkinter.Button(window, text="3", width=10, height=3, bg="lightgrey", command=lambda: press_btn("3"))
button.place(x=210, y=180)

button = tkinter.Button(window, text="-", width=9, height=3, bg="lightgrey", command=lambda: press_btn("-"))
button.place(x=310, y=180)

button = tkinter.Button(window, text="%", width=10, height=3, bg="lightgrey", command=lambda: press_btn("%"))
button.place(x=10, y=240)

button = tkinter.Button(window, text="0", width=10, height=3, bg="lightgrey", command=lambda: press_btn("0"))
button.place(x=110, y=240)

button = tkinter.Button(window, text="C", width=10, height=3, bg="lightgrey", command=lambda: press_btn("C"))
button.place(x=210, y=240)

button = tkinter.Button(window, text="+", width=9, height=3, bg="lightgrey", command=lambda: press_btn("+"))
button.place(x=310, y=240)

window.mainloop()
