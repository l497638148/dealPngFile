def read_png():
    png_end_marker = b'IEND'
    with open('./parse/out.png', 'rb') as f_png:
        content = f_png.read()

    #  png_end_pos = content.rfind(png_end_marker)
    png_first_pos = content.find(png_end_marker)
    #  print(png_first_pos,png_end_pos)
    zip_data_start = png_first_pos + len(png_end_marker) + 4
    #  zip_data_start = 21322 + len(png_end_marker)
    with open('./parse/file.zip', 'wb') as output_zip:
        output_zip.write(content[zip_data_start:])


