之文件打开模式:

r : 读取文件，若文件不存在则会报错

w: 写入文件，若文件不存在则会先创建再写入，会覆盖原文件

a : 写入文件，若文件不存在则会先创建再写入，但不会覆盖原文件，而是追加在文件末尾

rb,wb：分别于r,w类似，但是用于读写二进制文件

r+ : 可读、可写，文件不存在也会报错，写操作时会覆盖

w+ : 可读，可写，文件不存在先创建，会覆盖

a+ ：可读、可写，文件不存在先创建，不会覆盖，追加在末尾