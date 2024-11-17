from tkinter import *
firsr_number=second_number=operator=None
def get_digit(digit):
    current = result_lb['text']
    new=current + str(digit)
    result_lb.config(text=new)
def get_operator(op):
    global firsr_number,operator
    firsr_number=int(result_lb['text'])
    operator=op
    result_lb.config(text='')
def clear():
    result_lb.config(text='')
def get_result():
    global firsr_number,second_number,operator
    second_number=int(result_lb['text'])
    if operator=='+':
        result_lb.config(text=str(firsr_number+second_number))
    elif operator=='-':
        result_lb.config(text=str(firsr_number-second_number))
    elif operator=='*':
        result_lb.config(text=str(firsr_number*second_number))
    elif operator=='/':
        result_lb.config(text=str(round(firsr_number/second_number)))
    else:
        if second_number==0:
            result_lb.config(text='Error')
root=Tk()
root.title("Calculator")
root.geometry("340x400")
root.resizable(False,False)
root.configure(bg='pink')
result_lb=Label(root,text='',bg='white',fg='black',width=12)
result_lb.grid(row=0,column=0,sticky='w',columnspan=5,pady=(50,25))
result_lb.config(font=('verdana',30,'bold'))

button7=Button(root,text='7',font=('verdana',16,'bold'),bg='green',fg='white',width=5,height=2,command=lambda:get_digit(7))
button7.grid(row=1,column=0)

button8=Button(root,text='8',font=('verdana',16,'bold'),bg='green',fg='white',width=5,height=2,command=lambda:get_digit(8))
button8.grid(row=1,column=1)

button9=Button(root,text='9',font=('verdana',16,'bold'),bg='green',fg='white',width=5,height=2,command=lambda:get_digit(9))
button9.grid(row=1,column=2)
button_add=Button(root,text='+',font=('verdana',16,'bold'),bg='green',fg='white',width=5,height=2,command=lambda:get_operator('+'))
button_add.grid(row=1,column=3)
button4=Button(root,text='4',font=('verdana',16,'bold'),bg='green',fg='white',width=5,height=2,command=lambda:get_digit(4))
button4.grid(row=2,column=0)
button5=Button(root,text='5',font=('verdana',16,'bold'),bg='green',fg='white',width=5,height=2,command=lambda:get_digit(5))
button5.grid(row=2,column=1)
button6=Button(root,text='6',font=('verdana',16,'bold'),bg='green',fg='white',width=5,height=2,command=lambda:get_digit(6))
button6.grid(row=2,column=2)
button_multp=Button(root,text='*',font=('verdana',16,'bold'),bg='green',fg='white',width=5,height=2,command=lambda:get_operator('*'))
button_multp.grid(row=2,column=3)
button1=Button(root,text='1',font=('verdana',16,'bold'),bg='green',fg='white',width=5,height=2,command=lambda:get_digit(1))
button1.grid(row=3,column=0)
button1=Button(root,text='2',font=('verdana',16,'bold'),bg='green',fg='white',width=5,height=2,command=lambda:get_digit(2))
button1.grid(row=3,column=1)
button1=Button(root,text='3',font=('verdana',16,'bold'),bg='green',fg='white',width=5,height=2,command=lambda:get_digit(3))
button1.grid(row=3,column=2)
button1_subt=Button(root,text='-',font=('verdana',16,'bold'),bg='green',fg='white',width=5,height=2,command=lambda:get_operator('-'))
button1_subt.grid(row=3,column=3)
button_clear=Button(root,text='C',font=('verdana',16,'bold'),bg='dark red',fg='white',width=5,height=2,command=lambda:clear())
button_clear.grid(row=4,column=0)
button0=Button(root,text='0',font=('verdana',16,'bold'),bg='green',fg='white',width=5,height=2,command=lambda:get_digit(0))
button0.grid(row=4,column=1)
button_equ=Button(root,text='=',font=('verdana',16,'bold'),bg='green',fg='white',width=5,height=2,command=get_result)
button_equ.grid(row=4,column=2)
button_div=Button(root,text='/',font=('verdana',16,'bold'),bg='green',fg='white',width=5,height=2,command=lambda:get_operator('/'))
button_div.grid(row=4,column=3)
root.mainloop()