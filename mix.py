png_path = './file/test.png'
file_path = './file/test.zip'
out_file_path = './file/new.png'


def exec_file():
    with open(png_path, 'rb') as f_png, open(out_file_path, 'wb') as of_png:
        of_png.write(f_png.read())

    with open(file_path, 'rb') as f_zip, open(out_file_path, 'ab') as of_png:
        of_png.write(f_zip.read())
