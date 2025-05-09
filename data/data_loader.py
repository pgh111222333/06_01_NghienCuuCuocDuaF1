import pandas as pd
from tkinter import ttk, messagebox

def load_raw_data():
    try:
        df = pd.read_csv(r'G:\laptrinhpython\TayDuaF1\dataset\f1.csv')
        return df
    except FileNotFoundError:
        print("Error: File 'f1.csv' not found at the specified path.")
    except pd.errors.EmptyDataError:
        print("Error: The file is empty or not in a valid CSV format.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def load_clean_data():
    select_column = ['Driver', 'Constructor', 'Season']
    
    df = load_raw_data()

    return df[select_column].head(1000)

def search_data(data_input):
    select_column = ['Driver', 'Constructor', 'Season']
    
    df = load_raw_data()

    # Lọc dữ liệu theo tên tay đua
    search_term = data_input.lower()
    df_result = df[df['Driver'].str.contains(search_term, case=False, na=False)]

    # Nếu không tìm thấy, chuyển sang tìm theo tên đội đua
    if df_result.empty:
        df_result = df[df['Constructor'].str.contains(search_term, case=False, na=False)]

    # Nếu vẫn không tìm thấy, trả về DataFrame rỗng
    if df_result.empty:
        print(f"Không tìm thấy dữ liệu : {data_input}")
        return pd.DataFrame(columns=select_column)

    # Nhóm dữ liệu và sắp xếp
    group = df_result[['Driver', 'Season', 'Constructor']].drop_duplicates().sort_values(by='Season')

    return group

def add_data(driver, constructor, season):
    df = load_raw_data()  # Tải toàn bộ dữ liệu gốc
    if driver and constructor and season: 
        new_row = pd.DataFrame([{'Driver': driver, 'Constructor': constructor, 'Season': season}])
        df = pd.concat([df, new_row], ignore_index=True)

        try:
            # Lưu lại toàn bộ dữ liệu vào file CSV
            df.to_csv(r'G:\laptrinhpython\TayDuaF1\dataset\f1.csv', index=False)
            print(f"Đã thêm dữ liệu: {new_row}")
        except Exception as e:
            print(f"Gặp lỗi rồi: {e}")
    else:
        print("Vui lòng nhập đầy đủ thông tin!")

def delete_data(driver, constructor, season):
    df = load_raw_data()
    df = df[~((df["Driver"] == driver) & (df["Constructor"] == constructor) & (df["Season"] == int(season)))]

    try:
        df.to_csv(r'G:\laptrinhpython\TayDuaF1\dataset\f1.csv', index=False)
        print(f"Đã thêm dữ liệu: {driver}")
        messagebox.showwarning("Thông báo",f"Bạn đã xóa dữ liệu của {driver} thành công")
    except Exception as e:
        print(f"{e}")

def edit_data(d, c, s, n_d, n_c, n_s):
    df = load_raw_data()

    edit_data = (df["Driver"] == d) & (df["Constructor"] == c) & (df["Season"] == int(s))

    if not edit_data.any():
        messagebox.showwarning("Thông báo","Không thấy dữ liệu để xóa")
        return
    
    df.loc[edit_data, "Driver"] = n_d
    df.loc[edit_data, "Constructor"] = n_c
    df.loc[edit_data, "Season"] = n_s

    try:
        df.to_csv(r'G:\laptrinhpython\TayDuaF1\dataset\f1.csv', index=False)
    except Exception as e:
        messagebox.showerror("Lỗi", f"Lỗi khi ghi file CSV: {e}")
        



# if __name__ == "__main__":
#     data = load_data()
#     if data is not None:
#         print(data.head())