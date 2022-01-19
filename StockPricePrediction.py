from datetime import datetime
from tkinter import *
from tkinter import messagebox
import requests


def getData(from_sym='BTC'):
    url = 'https://min-api.cryptocompare.com/data/price'    
    
    parameters = {'fsym': from_sym,
                  'tsyms': 'USD' }
    

    response = requests.get(url, params=parameters)   
    data = response.json()  
    return data


# ------------------------------------------------------------------------------------------------
def clickConfirm():
    cName = getName.get().strip()
    
    if cName is None or cName == '':
        messagebox.showerror ("Error", "Enter a Cryptocurrency name ")
        return None

    try:
        resultData = getData(cName)

        if len(resultData)==1:
            currentPrice =  resultData['USD']

            now = datetime.now()
            currentTime = now.strftime("%H:%M:%S")

            cName = cName.upper()

            resultLabel.config(text = 'At {} price of {}-USD  is: ${} '.format(currentTime , cName , currentPrice ))

        elif  resultData['Response'] =='Error' :
            mes = resultData['Message']
            messagebox.showerror ("Error", mes)
            return None


    except IOError:
        messagebox.showerror ("Error", "No Internet connection! ")
        return None


# ------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    root = Tk()
    root.title("Stock Price Prediction")
    root.iconbitmap("img0.ico")
    root.geometry("604x684")
    root.configure(bg="#315087")
    root.resizable(False, False)


    img = PhotoImage(file = r"img5.png")
    imageLabel      = Label(root, borderwidth=2, image=img).grid(row=0, column=0)


    nameLabel       = Label(root, text="Enter a Cryptocurrency name to see it's current price: "\
    , bg="#315087"  , fg="#F0F0F0", font=("Monotype Corsiva",19,"bold")).grid(row=1, column=0, pady=[80,15])


    getName         = StringVar()
    border_color    = Frame(root, background="#F0F0F0", bd=2)
    nameEntry       = Entry(border_color, font=("Monotype Corsiva",20,"bold")\
    , textvariable  = getName, width=12, bd=0, relief=SOLID \
    , bg="#315087",   fg="#F0F0F0").grid(row=2,column=0)
    border_color.grid(row=2, column=0, pady=[15,5])


    border_color2   = Frame(root, background="#315087", bd=2)
    confirmButton   = Button(border_color2, text = "Confirm", bg="#F0F0F0", fg="#315087", font=("Monotype Corsiva", 19, "bold")\
    , width=8, relief=SOLID, borderwidth=0, command=clickConfirm).grid(row=3, column=0)
    border_color2.grid(row=3, column=0, pady=[5,20])


    resultLabel     = Label(root)
    resultLabel.grid(row=4, column=0, pady=[20,10])
    resultLabel.config(bg="#315087",    fg = "#FE6B9F" , font=("Monotype Corsiva",20,"bold"))
   
   
    root.mainloop()
