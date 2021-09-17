import img2pdf
import ntpath
from tkinter import Tk, filedialog
from PIL import Image
import os
root = Tk()

path = filedialog.askopenfilename(filetypes=[("Image File", '.jpg')], title='select jpg file')
name = ntpath.basename(path)
name = (name.rsplit('.', 1)[0])
print("jpg "+name+" from ----> "+path)
image = Image.open(path)

dirto = os.getcwd()
savedir = filedialog.askdirectory(initialdir=dirto, title='select save location')
pdf_path = savedir+"/"+name+".pdf"
print("save pdf at ----> "+pdf_path)
pdf_bytes = img2pdf.convert(image.filename)
file = open(pdf_path, "wb")
file.write(pdf_bytes)
image.close()
file.close()

# output
print("Successfully create pdf file")
