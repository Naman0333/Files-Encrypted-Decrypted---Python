import tkinter as tk
from tkinter import filedialog, messagebox
import pyAesCrypt

#Buffer size for encryption/decryption
BUFFER_SIZE = 64 * 1024

def password_protect_file():
    # Get the file to protect
    file_path = filedialog.askopenfilename()

    #Get the password from the user
    password = password_entry.get()

    if file_path and password:
        try:
            # Get the output file name
            output_path = filedialog.asksaveasfilename(defaultextension="")

            # Encrypt the file
            pyAesCrypt.encryptFile(file_path,output_path,password,BUFFER_SIZE)
            
            messagebox.showinfo('Success','File password protected!')
        
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    else:
        messagebox.showwarning('Warning','Please select a file.')

def decrpt_file():

    # Get the file to decrypt
    file_path = filedialog.askopenfilename()

    # Get the password from the user
    password = password_entry.get()

    if file_path and password:
        try:
            # Get the output file name 
            output_path =  filedialog.asksaveasfilename(defaultextension="")

            # Decrypt the file
            pyAesCrypt.decryptFile(file_path, output_path, password,BUFFER_SIZE)

            messagebox.showinfo('Success','File decrypted!')
        
        except Exception as e:
            messagebox.showerror('Error',str(e))

    else:
        messagebox.showwarning('Warning','Please select a file.')

# Create the main window    
window = tk.Tk()
window.title('File Password Protecter')
window.geometry('500x250')
window.resizable(False,False)
window.configure(background='light blue')
window.iconbitmap('icon.ico')

# Crate a heading label
heading_label = tk.Label(window, text = "Password Protecter",font=('Arial',20,'bold'),bg='black',fg='white')
heading_label.pack(fill=tk.BOTH)

# Create a main label
main_label = tk.Label(window,text="Enter Password:",font=('Arial',14,'bold'))
main_label.pack(pady=5)

# Create a password entry
password_entry = tk.Entry(window,width=30,show="*")
password_entry.pack(pady=5)

# Create protect and decrypt buttons
protect_button = tk.Button(window,text='Protect File',font=('Arial',8,'bold'),width=15,bg='black',fg='white',command=password_protect_file)
protect_button.pack(pady=5)

decrypt_button = tk.Button(window,text='Decrypt File',font=('Arial',8,'bold'),width=15,bg='black',fg='white',command=decrpt_file)
decrypt_button.pack(pady=5)

# Start the main event loop
window.mainloop()