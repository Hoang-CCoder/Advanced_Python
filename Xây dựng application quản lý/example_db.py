import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector


class DatabaseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Database App")

        # Database connection fields
        self.db_name = tk.StringVar(value='sinhviendb')
        self.user = tk.StringVar(value='root')
        self.password = tk.StringVar(value='HuyHoang2911@')
        self.host = tk.StringVar(value='127.0.0.1')
        self.port = tk.StringVar(value='3306')
        self.table_name = tk.StringVar(value='sinhvien')

        # Add a title label to show operation status or title
        self.title_label = tk.Label(self.root, text="Welcome to the Database App", font=("Helvetica", 16))
        self.title_label.pack(pady=10)

        # Create the menu bar
        self.create_menu()

        # Create the GUI elements
        self.create_widgets()

    def create_menu(self):
        # Create the main menu
        menu_bar = tk.Menu(self.root)

        # Add File menu
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

        # Add Edit menu
        edit_menu = tk.Menu(menu_bar, tearoff=0)
        edit_menu.add_command(label="Undo", command=self.undo_action)
        edit_menu.add_command(label="Redo", command=self.redo_action)
        menu_bar.add_cascade(label="Edit", menu=edit_menu)

        # Add Help menu
        help_menu = tk.Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about)
        menu_bar.add_cascade(label="Help", menu=help_menu)

        # Configure the menu bar
        self.root.config(menu=menu_bar)

    def new_file(self):
        messagebox.showinfo("New File", "New File Created!")

    def open_file(self):
        messagebox.showinfo("Open File", "File Opened!")

    def undo_action(self):
        messagebox.showinfo("Undo", "Undo action!")

    def redo_action(self):
        messagebox.showinfo("Redo", "Redo action!")

    def show_about(self):
        messagebox.showinfo("About", "This is a Database App created in Python with Tkinter.")

    def create_widgets(self):
        # Connection section
        connection_frame = tk.Frame(self.root)
        connection_frame.pack(pady=10)

        tk.Label(connection_frame, text="Database Name:").grid(row=0, column=0, padx=5, pady=5)
        tk.Entry(connection_frame, textvariable=self.db_name).grid(row=0, column=1, padx=5, pady=5)

        tk.Label(connection_frame, text="User:").grid(row=1, column=0, padx=5, pady=5)
        tk.Entry(connection_frame, textvariable=self.user).grid(row=1, column=1, padx=5, pady=5)

        tk.Label(connection_frame, text="Password:").grid(row=2, column=0, padx=5, pady=5)
        tk.Entry(connection_frame, textvariable=self.password, show="*").grid(row=2, column=1, padx=5, pady=5)

        tk.Label(connection_frame, text="Host:").grid(row=0, column=2, padx=5, pady=5)
        tk.Entry(connection_frame, textvariable=self.host).grid(row=0, column=3, padx=5, pady=5)

        tk.Label(connection_frame, text="Port:").grid(row=1, column=2, padx=5, pady=5)
        tk.Entry(connection_frame, textvariable=self.port).grid(row=1, column=3, padx=5, pady=5)

        tk.Button(connection_frame, text="Create Table", command=self.create_table).grid(row=5, column=1, columnspan=4, pady=10)
        tk.Button(connection_frame, text="Connect", command=self.connect_db).grid(row=5, column=0, columnspan=3, pady=10)

        # Query section
        query_frame = tk.Frame(self.root)
        query_frame.pack(pady=10)

        tk.Label(query_frame, text="Table Name:").grid(row=0, column=0, padx=5, pady=5)
        tk.Entry(query_frame, textvariable=self.table_name).grid(row=0, column=1, padx=5, pady=5)

        tk.Button(query_frame, text="Load Data", command=self.load_data).grid(row=1, columnspan=2, pady=10)

        # Data display section with Treeview
        self.tree_frame = tk.Frame(self.root)
        self.tree_frame.pack(pady=10)

        self.tree = ttk.Treeview(self.tree_frame, columns=("ID", "Ho ten", "MSSV", "Email"), show="headings", height=10)
        self.tree.heading("ID", text="ID")
        self.tree.heading("Ho ten", text="Ho ten")
        self.tree.heading("MSSV", text="MSSV")
        self.tree.heading("Email", text="Email")

        # Cập nhật kích thước cột
        self.tree.column("ID", width=80, anchor="center")  # Độ rộng cột ID
        self.tree.column("Ho ten", width=200, anchor="w")  # Độ rộng cột Ho ten
        self.tree.column("MSSV", width=150, anchor="center")  # Độ rộng cột MSSV
        self.tree.column("Email", width=250, anchor="w")  # Độ rộng cột Email

        self.tree.pack(side="left")

        # Add a scrollbar
        scrollbar = ttk.Scrollbar(self.tree_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")


        # Add "Add Student" functionality
        self.add_student_section()

    def add_student_section(self):
        add_student_frame = tk.Frame(self.root)
        add_student_frame.pack(pady=10)

        self.student_name = tk.StringVar()
        self.student_id = tk.StringVar()
        self.student_email = tk.StringVar()

        tk.Label(add_student_frame, text="Ho Ten:").grid(row=0, column=0, padx=5, pady=5)
        tk.Entry(add_student_frame, textvariable=self.student_name).grid(row=0, column=1, padx=5, pady=5)

        tk.Label(add_student_frame, text="MSSV:").grid(row=1, column=0, padx=5, pady=5)
        tk.Entry(add_student_frame, textvariable=self.student_id).grid(row=1, column=1, padx=5, pady=5)

        tk.Label(add_student_frame, text="Email:").grid(row=2, column=0, padx=5, pady=5)
        tk.Entry(add_student_frame, textvariable=self.student_email).grid(row=2, column=1, padx=5, pady=5)

        tk.Button(add_student_frame, text="Add Student", command=self.add_student).grid(row=3, columnspan=2, pady=10)

    def connect_db(self):
        try:
            self.conn = mysql.connector.connect(
                database=self.db_name.get(),
                user=self.user.get(),
                password=self.password.get(),
                host=self.host.get(),
                port=self.port.get()
            )
            self.cur = self.conn.cursor()
            self.title_label.config(text="Connected to the database successfully!")
            messagebox.showinfo("Success", "Connected to the database successfully!")
        except mysql.connector.Error as e:
            self.title_label.config(text="Error connecting to the database!")
            messagebox.showerror("Error", f"Error connecting to the database: {e}")

    def load_data(self):
        try:
            query = f"SELECT * FROM {self.table_name.get()}"
            self.cur.execute(query)
            rows = self.cur.fetchall()

            # Clear the Treeview
            for item in self.tree.get_children():
                self.tree.delete(item)

            # Insert data into Treeview
            for row in rows:
                self.tree.insert("", "end", values=row)

            self.title_label.config(text="Data loaded successfully!")
        except mysql.connector.Error as e:
            self.title_label.config(text="Error loading data!")
            messagebox.showerror("Error", f"Error loading data: {e}")

    def add_student(self):
        # Get values from the entry fields
        name = self.student_name.get()
        student_id = self.student_id.get()
        email = self.student_email.get()

        if name and student_id and email:
            try:
                insert_query = f"INSERT INTO {self.table_name.get()} (hoten, MSSV, email) VALUES (%s, %s, %s)"
                data_to_insert = (name, student_id, email)
                self.cur.execute(insert_query, data_to_insert)
                self.conn.commit()
                messagebox.showinfo("Success", "Student added successfully!")
                self.clear_entries()
            except mysql.connector.Error as e:
                messagebox.showerror("Error", f"Error adding student: {e}")
        else:
            messagebox.showerror("Input Error", "All fields are required!")

    def clear_entries(self):
        self.student_name.set("")
        self.student_id.set("")
        self.student_email.set("")

    def create_table(self):
        try:
            create_table_query = f"""
                CREATE TABLE IF NOT EXISTS {self.table_name.get()} (
                    sinhvien_ID INT NOT NULL AUTO_INCREMENT,
                    hoten VARCHAR(50) NOT NULL,
                    MSSV VARCHAR(20) NOT NULL,
                    email VARCHAR(100) NOT NULL,
                    PRIMARY KEY (sinhvien_ID)
                ) ENGINE=InnoDB;
            """
            self.cur.execute(create_table_query)
            self.conn.commit()
            self.title_label.config(text=f"Table '{self.table_name.get()}' created successfully!")
            messagebox.showinfo("Success", f"Table '{self.table_name.get()}' created successfully!")
        except mysql.connector.Error as e:
            self.title_label.config(text="Error creating table!")
            messagebox.showerror("Error", f"Error creating table: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = DatabaseApp(root)
    root.mainloop()
