import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

def save_key(key):
    with open('key.txt', 'w') as f:
        f.write(key)

def encrypt_decrypt(text, key):
    """
    Cifra o descifra el texto utilizando el cifrado César.
    """
    result = ""

    for char in text:
        if char.isalpha():
            # Convertir el carácter a su valor ASCII y sumarle la llave
            char_code = ord(char) + key % 26

            # Si el carácter es mayúscula y se sale del rango ASCII de las mayúsculas, volver a A
            if char.isupper() and char_code > ord('Z'):
                char_code -= 26

            # Si el carácter es minúscula y se sale del rango ASCII de las minúsculas, volver a a
            elif char.islower() and char_code > ord('z'):
                char_code -= 26

            #Si el carácter es mayuscula y se sale del rangode las mayusculas, volver a Z
            elif char.isupper() and char_code < ord('A'):
                char_code += 26
            
            #Si el carácter es minuscula y se sale del rangode las mayusculas, volver a z
            elif char.islower() and char_code < ord('a'):
                char_code += 26

            # Convertir el nuevo valor ASCII a carácter y añadirlo al resultado
            result += chr(char_code)

        else:
            # Si el carácter no es alfabético, añadirlo al resultado sin cifrarlo
            result += char

    return result

def encrypt_file():
    """
    Cifra un archivo de texto seleccionado por el usuario utilizando el cifrado César.
    """
    # Obtener el archivo seleccionado por el usuario
    filepath = filedialog.askopenfilename()

    # Obtener la llave introducida por el usuario
    key = int(key_entry.get())

    # Cifrar el contenido del archivo
    try:
        with open(filepath, 'r') as f:
            plaintext = f.read()
    except FileNotFoundError:
        messagebox.showerror('Error', 'El archivo seleccionado no existe')
        return
    ciphertext = encrypt_decrypt(plaintext, key)

    # Pedirle al usuario que seleccione una ubicación y un nombre para guardar el archivo cifrado
    save_filepath = filedialog.asksaveasfilename(defaultextension='.txt')

    # Guardar el archivo cifrado
    with open(save_filepath, 'w') as f:
        f.write(ciphertext)

    # Guardar la llave en un archivo
    save_key(str(key))

    messagebox.showinfo('YA QUEDOOOOO', 'El archivo se ha cifrado y guardado correctamente.')

def decrypt_file():
    """
    Descifra un archivo de texto cifrado seleccionado por el usuario utilizando el cifrado César.
    """
    # Establecer un valor predeterminado para ciphertext
    ciphertext = ""

    # Obtener el archivo seleccionado por el usuario
    filepath = filedialog.askopenfilename()

    # Obtener la llave introducida por el usuario
    key = int(key_entry.get())

    # Descifrar el contenido del archivo
    try:
        with open(filepath, 'r') as f:
            ciphertext = f.read()
    except FileNotFoundError:
        messagebox.showerror('NO QUEDOOOO', 'El archivo seleccionado no existe')
        return
    decrypted_content = encrypt_decrypt(ciphertext, -key)

    # Pedirle al usuario que seleccione una ubicación y un nombre para guardar el archivo descifrado
    save_filepath = filedialog.asksaveasfilename(defaultextension='.txt')

    # Guardar el archivo descifrado
    with open(save_filepath, 'w') as f:
        f.write(decrypted_content)

    messagebox.showinfo('YA QUEDOOOOOO', 'El archivo se ha descifrado y guardado correctamente.')

def encrypt_image():
    # Abrir la imagen BMP
    filepath = filedialog.askopenfilename(title='Seleccionar archivo BMP', filetypes=[('Imagen BMP', '*.bmp')])
    image = Image.open(filepath)

    # Obtener el desplazamiento de la llave
    shift = int(key_entry.get())

    # Cifrar la imagen
    encrypted_image = image.point(lambda p: (p + shift) % 256)

    # Guardar la imagen cifrada
    save_filepath = filedialog.asksaveasfilename(title='Guardar imagen cifrada', filetypes=[('Imagen BMP', '*.bmp')])
    encrypted_image.save(save_filepath)

    # Guardar la llave en un archivo
    save_key(str(key_entry.get()))

    messagebox.showinfo('YA QUEDOOOOOO', 'La imagen se ha cifrado y guardado correctamente.')

def decrypt_image():
    # Abrir la imagen cifrada
    filepath = filedialog.askopenfilename(title='Seleccionar archivo BMP cifrado', filetypes=[('Imagen BMP cifrada', '*.bmp')])
    image = Image.open(filepath)

    # Obtener el desplazamiento de la llave
    shift = int(key_entry.get())

    # Descifrar la imagen
    decrypted_image = image.point(lambda p: (p - shift) % 256)

    # Guardar la imagen descifrada
    save_filepath = filedialog.asksaveasfilename(title='Guardar imagen descifrada', filetypes=[('Imagen BMP', '*.bmp')])
    decrypted_image.save(save_filepath)

    messagebox.showinfo('YA QUEDOOOOOO :)', 'La imagen se ha descifrado y guardado correctamente.')

# Crear la ventana principal
root = tk.Tk()
root.title('Cifrado de corrimiento')
root.resizable(0,0)
root.iconbitmap("123.ico")
root.geometry("700x700")
root.config(bg="#6E85B2")
root.config(relief="groove")
root.config(bd=0)

# Crear la etiqueta y el cuadro de entrada para la llave
key_label = tk.Label(root, text='Llave:',font=("Arial", 10), bg="#6E85B2", fg="white")
key_label.place(x=10, y=20)
key_entry = tk.Entry(root)
key_entry.place(x=50, y=20, width=200)

# Crear el marco para los botones de archivo
file_frame = tk.Frame(root,bg="#6E85B2", relief="groove", bd=0)
file_frame.place(x=70, y=100, width=600, height=500)

encrypt_name = tk.Label(file_frame, text='CIFRADO DE ARCHIVOS',font=("Arial", 20), bg="#6E85B2", fg="white")
encrypt_name.place(x=150, y=0)
# Crear la etiqueta y el botón para seleccionar el archivo a cifrar
encrypt_label = tk.Label(file_frame, text='Cifrar archivo:',font=("Arial", 10), bg="#6E85B2", fg="white")
encrypt_label.place(x=10, y=100)
encrypt_button = tk.Button(file_frame, text='Seleccionar archivo', command=encrypt_file)
encrypt_button.place(x=200, y=100)
# Crear la etiqueta y el botón para seleccionar el archivo a descifrar
decrypt_label = tk.Label(file_frame, text='Descifrar archivo:',font=("Arial", 10), bg="#6E85B2", fg="white")
decrypt_label.place(x=10, y=150)
decrypt_button = tk.Button(file_frame, text='Seleccionar archivo', command=decrypt_file)
decrypt_button.place(x=200, y=150)


encrypt_name2 = tk.Label(file_frame, text='CIFRADO DE IMAGENES',font=("Arial", 20), bg="#6E85B2", fg="white")
encrypt_name2.place(x=150, y=190)
# Crear la etiqueta y el botón para cifrar imágenes BMP
encrypt_image_label = tk.Label(file_frame, text='Cifrar imagen BMP:',font=("Arial", 10), bg="#6E85B2", fg="white")
encrypt_image_label.place(x=10, y=250)
encrypt_image_button = tk.Button(file_frame, text='Seleccionar archivo', command=encrypt_image)
encrypt_image_button.place(x=200, y=250)

# Crear la etiqueta y el botón para descifrar imágenes BMP
decrypt_image_label = tk.Label(file_frame, text='Descifrar imagen BMP:',font=("Arial", 10), bg="#6E85B2", fg="white")
decrypt_image_label.place(x=10, y=300)
decrypt_image_button = tk.Button(file_frame, text='Seleccionar archivo', command=decrypt_image)
decrypt_image_button.place(x=200, y=300)


# Crear el botón para salir del programa
exit_button = tk.Button(root, text='Salir', command=root.quit)
exit_button.place(x=350, y=650)

root.mainloop()