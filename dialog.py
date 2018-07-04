from tkinter import *
from tkinter import messagebox as mb
from tkinter import filedialog
from pathlib import Path
import zipfile


root = Tk()



def onOpen1():
    e1.delete(0, END)
    e1.insert(0, filedialog.askopenfilename(filetypes=(("файлы банков", "*.ZIP;*.zip")
                                                             , ("All files", "*.*"))))
def get_userdata_dir():
    homed = str(Path.home()) + '\.converter\setup.ini'
    print(homed)
    if  Path(homed).exists():
        print('Нету файла и директории. ХУЙ')
    #p = Path()
    #p.write_text('Hello world')


def onopendir2():
    e2.delete(0, END)
    e2.insert(0, filedialog.askdirectory(title='Сохранить сконвертированные файлы в..'))

def cutstring(a):
    tmp=a[0:len(a)-2]
    return tmp
def unzip():
   # with open(e2.get()+"/test2.txt", "w+") as myfile:

     zip_ref = zipfile.ZipFile(e1.get(), 'r')
     spisok=zip_ref.namelist()
     print(spisok)
     stroka3=spisok.__getitem__(0)
     contora=e3.get()

     b=open(e2.get() + "/"+stroka3, "w+")
     print(stroka3)

     zip_open=zip_ref.open(spisok.__getitem__(0))

     k=0;data='01012018';kolvo='0';summa='0'
     for line in zip_open.readlines():
      stroka=line.decode('cp866')

      k+=1

      if k<2:t=stroka.split(',');dat=t[2];kolvo=t[3];summa=t[4];stroka='START;'+dat.replace('.', '')+';1;CREDIT;'+contora+'\n';b.write(stroka)

      if k>=2:t=stroka.split(',');print(t[5]+';'+cutstring(t[6])+';'+t[2]+' '+t[3]+' '+t[4]);b.write(t[5]+';'+cutstring(t[6])+';'+t[2]+' '+t[3]+' '+t[4]+'\n')


    # zip_ref.extractall(e2.get())
     zip_ref.close()

     print('END;'+kolvo+';'+summa+';RUR')
     b.write('END;'+kolvo+';'+summa+';RUR'+'\n')
     print('Работа завершена')
     b.close()
     mb.showinfo(message='Конвертация завершена')


l1 = Label(root, text='Название учреждения', justify=RIGHT)
l2 = Label(root, text='Уникальный идентификатор', justify=RIGHT)
l3 = Label(root, text='Путь на файл', justify=RIGHT)
l4 = Label(root, text='Путь на директорию для сохранения', justify=RIGHT)
e1 = Entry(root, width=50)
e2 = Entry(root, width=50)
e3 = Entry(root, width=50)
e4 = Entry(root, width=50)
#e1.insert(END,'путь на файл')

get_userdata_dir()

b1 = Button(root, text="Выбрать файл для конвертации ", command=onOpen1)


b2 = Button(root, text="Выбор директории для сохранения", command=onopendir2)

#e2.insert(END,'путь на директорию для сохранения')
l3.grid(row=0,column=0)
l4.grid(row=1,column=0)
e1.grid(row=0, column=1,  padx=5, pady=5)
e2.grid(row=1, column=1, padx=5, pady=5)




l1.grid(row=2,column=0, padx=5, pady=5)
e3.grid(row=2, column=1, padx=5, pady=5)
l2.grid(row=3,column=0, padx=5, pady=5)
e4.grid(row=3, column=1, padx=5, pady=5)

b1.grid(row=0, column=2, padx=5, pady=5)
b2.grid(row=1, column=2, padx=5, pady=5)
b3 = Button(root, text="Преобразовать", command=unzip)
b3.grid(row=3, column=2, padx=5, pady=5)

root.title("Конвертор реестров в формат банка ВТБ")
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 3
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 3
root.wm_geometry("+%d+%d" % (x, y))


root.mainloop()