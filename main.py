# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import zipfile
import io
import png
import read
import mix

pic_width = 1000
pic_height = 1000

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def readfile():
    binary_data = io.BytesIO()
    zip = zipfile.ZipFile('./file/test.zip','r')
    for name in zip.namelist():
        file = zip.open(name)
        file_content = file.read()
        zipfile.ZipFile(binary_data, 'a', zipfile.ZIP_DEFLATED).writestr(name, file_content)
    binary_data.seek(0)
    chunk = binary_data.read()
    return chunk

def save_to_local(chunk):
    data = tuple(chunk)
    with open('./file/new.png', 'wb') as f:
        png.Writer(pic_width, pic_height).write(f, data)


def readpng():
    reader = png.Reader('./parse/out.png')
    #  width, height, pixels, metadata = reader.read_flat()
    #  print(metadata)
    chunks = reader.chunks()
    #save_to_local(chunks)
    chunk_lis = list(chunks)
    print(len(chunk_lis))
    #chunk_lis.insert(4, file_chunk)
    print(chunk_lis[4])
    #print(len(chunk_lis[5]))
    #print("chunk number is:", {len(chunk_lis)})
    return chunk_lis


def get_file_chunk():
    file_bytes = readfile()
    print(len(file_bytes))
    z_header = b'zTXt'
    file_chunk = (z_header, file_bytes)
    return file_chunk


def insert_chunk(png_chunk,file_chunk):
    end_index = -1
    for index in range(len(png_chunk)):
        if png_chunk[index][0] == b'IEND':
            end_index = index
            break
    if end_index > 0:
        insert_index = end_index - 1
        png_chunk.insert(insert_index, file_chunk)
    return png_chunk


def exectute():
    png_chunk = readpng()
    file_chunk = get_file_chunk()
    #new_chunk = insert_chunk(png_chunk,file_chunk)
    #save_to_local(png_chunk)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    #  readpng()
    #  readfile()
    #  mix.exec_file()
    read.read_png()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
