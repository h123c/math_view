#encoding:utf-8
import json
import os

#读取数据
path = "/home/hc/Desktop/chenglong/latex_demo/"

img_list = os.listdir(path+"img")
text_list = os.listdir(path+"text")

file_name_list = []  #文件名列表
math_info = {}   #文件名->公式信息
for i in text_list:
    if i[:-4]+".jpg" in img_list:
        file_name_list.append(i[:-4])
    with open(path+"text/"+i,"r") as f:
        info = f.read().split("\t")[1]
    math_info[i[:-4]] = info

#读取html模板
with open("base.html","r") as f:
    base = f.read()

with open("template.html","r") as f:
    template = f.read()

print(len(file_name_list))
show_num = 2 #单页显示数量
total_page = len(file_name_list)//show_num +1 #页数

for i in range(total_page):  #每个html页面
    new_html = base
    if i==0:
        new_html = new_html.replace("pre_url", "0.html")
    else:
        new_html = new_html.replace("pre_url", str(i-1)+".html")
    if i==total_page-1:
        new_html = new_html.replace("next_url", str(i)+".html")
    else:
        new_html = new_html.replace("next_url", str(i+1)+".html")

    new_html = new_html.replace("page_num",str(i))
    new_html = new_html.replace("total_num",str(total_page))

    add_template = ""
    for file in file_name_list[show_num*i:min(len(file_name_list),show_num*(i+1))]:  #每个图像
        print(file)
        new_template = template
        new_template = new_template.replace("img_url",path+"img/"+file+".jpg")
        new_template = new_template.replace("math_char", math_info[file])
        new_template = new_template.replace("file_name", file)
        add_template = add_template + new_template
    new_html = new_html.replace("##base##",add_template)
    with open("./html_file/"+str(i)+".html","w") as f:
        f.write(new_html)
