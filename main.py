import pandas as pd
import tkinter as tk
from tkinter import ttk, messagebox
# from data.data_loader import load_clean_data
# from utilities.data_processor import load_less_data
from data.data_loader import load_clean_data
from utilities.CURD import Create_new_data
from data.data_loader import search_data
from data.data_loader import delete_data
from data.data_loader import edit_data
from utilities.CURD import Edit_Data

def delete_confirm(tree):
     confirm = messagebox.askyesno("Xác nhận xóa? ", "Bạn muốn xóa dữ liệu? ")
     d,c,s = select_row(tree)
     if confirm: 
          delete_data(d,c,s)

def edit_confirm(tree):
     confirm = messagebox.askyesno("Thông báo", "Các dữ liệu này sẽ được thay đổi")
     d,c,s = select_row(tree)
     if confirm:
          Edit_Data(d,c,s)

def select_row(tree):
    selected_row = tree.selection()
    if not selected_row:
         messagebox.showwarning("Thông báo","Bạn không chọn gì cả")
         print("Không có hàng nào được chọn")
         return

    values = tree.item(selected_row, "values") 
    driver, constructor, season = values
    return(driver,constructor, season)

def show_data(tree, data):
    for item in tree.get_children():
         tree.delete(item)

    for i in range(len(data)):
         row = data.iloc[i]
         tree.insert("", "end", values=(row["Driver"], row["Constructor"], row["Season"]))

def Create():
    root = tk.Tk()
    root.title("Tay đua F1")
    root.geometry("1000x600")

    columns = ["Driver", "Constructor", "Season"]
    tree = ttk.Treeview(root, columns=columns, show="headings")
    tree.grid(row=1, column=1)

    tree.heading("Driver", text= "Tay đua")
    tree.heading("Constructor", text="Đội đua")
    tree.heading("Season", text="Mùa giải")

    data = load_clean_data()
    if data is None:
            ttk.Label(tree, text="Không thể tải dữ liệu!").grid(row=0, column=0)
            return
    show_data(tree, data)

    # CRUD Button
    open_less_data_button = ttk.Button(root, text="Thêm dữ liệu tay đua", command=Create_new_data)
    open_less_data_button.grid(row=3, column=0, pady=5)

    del_button = ttk.Button(root, text= "Xóa dữ liệu bạn đã chọn", command=lambda: delete_confirm(tree))
    del_button.grid(row=3, column=1, pady=5)

    del_button = ttk.Button(root, text= "Sửa dữ liệu", command=lambda: edit_confirm(tree))
    del_button.grid(row=3, column=2, pady=5)

    # Reload lại dữ liệu
    open_less_data_button = ttk.Button(root, text="Reload lại dữ liệu", command=lambda: show_data(tree, data))
    open_less_data_button.grid(row=0, column=2, pady=5)

    # data_input = search_bar.get()

    # Tìm kiếm
    search_bar = ttk.Entry(root,width=30)
    search_bar.grid(row=0, column=0)

    search_button = ttk.Button(root, text="Tìm kiếm", 
                              command= lambda: show_data(tree, search_data(search_bar.get())))
    search_button.grid(row=0, column=1)
    

    #Filter button
    button_contrusctor_filter_label = ['Red Bull', 'Mercedes', 'Ferrari']

    for idx, constructor in enumerate(button_contrusctor_filter_label):
        filter_button = ttk.Button(root, text=f"{constructor}", command= lambda c=constructor: show_data(tree,search_data(c)))
        filter_button.grid(row=7,column=idx, padx=5, pady=10)
    
    
    # open_raw_data = ttk.Button(root, text="Mở dữ liệu thô", command=load_clean_data)
    # open_raw_data.grid(row=2, column=0)

    root.mainloop()

if __name__ == "__main__":
    Create()