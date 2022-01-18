from tkinter import Tk

from PIL import ImageTk
import tkinter as tk
import interfata

if __name__ == '__main__':

   root=Tk()
   root.iconify()
   root.title('')
   root.geometry('1000x800')

   gui = interfata.interfata(root)
   gui.run_interface()