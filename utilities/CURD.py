import pandas as pd
import tkinter as tk 
from tkinter import ttk
from data.data_loader import add_data
from data.data_loader import edit_data
# from data.data_loader import load_data

def Create_new_data():
    root = tk.Tk()
    root.geometry("700x500")

    input_driver_label = ttk.Label(root, text="Nhập tên tay đua")
    input_driver_label.grid(row=0, column=0, sticky=(tk.S, tk.E),padx=5, pady=10)

    input_driver_entry = ttk.Entry(root, width=20)
    input_driver_entry.grid(row=1,column=0, sticky=(tk.E, tk.S), pady=5, padx=10)

    input_constructor_label = ttk.Label(root, text="Nhập tên đội đua")
    input_constructor_label.grid(row=0, column=2, sticky=(tk.S, tk.E), padx =5, pady=10)

    input_constructor_entry = ttk.Entry(root, width=20)
    input_constructor_entry.grid(row=1,column=2,sticky=(tk.E, tk.S), padx=5, pady=10)

    input_season_label = ttk.Label(root, text="Nhập mùa giải mà tay đua tham gia")
    input_season_label.grid(row=2, column=0, sticky=(tk.E, tk.S), padx=5, pady=10)

    input_season_entry = ttk.Entry(root,width=20)
    input_season_entry.grid(row=3, column=0, sticky=(tk.E, tk.S), padx=5, pady=10)

    search_button = ttk.Button(root, text="Thêm dữ liệu", command=lambda: add_data(input_driver_entry.get(), 
                                                                                                  input_constructor_entry.get(),
                                                                                                  input_season_entry.get()))           

    search_button.grid(row=4,column=0)

    root.mainloop()

def Edit_Data(d, c, s):
    edit_window = tk.Toplevel()
    edit_window.title("Chỉnh sửa dữ liệu")
    edit_window.geometry("700x500")

    # Nhãn và ô nhập liệu cho Driver
    input_driver_label = ttk.Label(edit_window, text="Nhập tên tay đua")
    input_driver_label.grid(row=0, column=0, sticky=(tk.S, tk.E), padx=5, pady=10)

    input_driver_entry = ttk.Entry(edit_window, width=20)
    input_driver_entry.grid(row=1, column=0, sticky=(tk.E, tk.S), pady=5, padx=10)
    input_driver_entry.insert(0, d)  # Đặt giá trị mặc định là `d`

    # Nhãn và ô nhập liệu cho Constructor
    input_constructor_label = ttk.Label(edit_window, text="Nhập tên đội đua")
    input_constructor_label.grid(row=0, column=2, sticky=(tk.S, tk.E), padx=5, pady=10)

    input_constructor_entry = ttk.Entry(edit_window, width=20)
    input_constructor_entry.grid(row=1, column=2, sticky=(tk.E, tk.S), padx=5, pady=10)
    input_constructor_entry.insert(0, c)  # Đặt giá trị mặc định là `c`

    # Nhãn và ô nhập liệu cho Season
    input_season_label = ttk.Label(edit_window, text="Nhập mùa giải mà tay đua tham gia")
    input_season_label.grid(row=2, column=0, sticky=(tk.E, tk.S), padx=5, pady=10)

    input_season_entry = ttk.Entry(edit_window, width=20)
    input_season_entry.grid(row=3, column=0, sticky=(tk.E, tk.S), padx=5, pady=10)
    input_season_entry.insert(0, s)  # Đặt giá trị mặc định là `s`

    # Nút lưu thay đổi
    def save_changes():
        n_d = input_driver_entry.get()
        n_c = input_constructor_entry.get()
        n_s = input_season_entry.get()

        # Gọi hàm edit_data với các giá trị cũ và mới
        edit_data(d, c, s, n_d, n_c, n_s)

        # Đóng cửa sổ chỉnh sửa
        edit_window.destroy()

    save_button = ttk.Button(edit_window, text="Lưu thay đổi", command=save_changes)
    save_button.grid(row=4, column=0, pady=10)

    edit_window.mainloop()