import pprint
from bs4 import BeautifulSoup as BSoupy
from urllib.request import urlopen
import pdfkit


def convert_to_pdf(all_list,name_file):
    for k,v in zip(all_list,name_file):
        pdfkit.from_url(k,v)


def main():
    with open('Composing Programs.html','r') as f:
        html = f.read()
    soup = BSoupy(html,'html.parser')
    a_list = []
    file_list = []
    for i in soup.find_all('a'):
        a_list.append(str(i.get('href')))
#maybe
    del a_list[0:17]
    del a_list[-3:]
    pprint.pprint(a_list)
    for i in a_list:
        print(str(i))
        namer = input("put .pdf after each name\n")
        namer = namer+".pdf"
        file_list.append(str(namer))
    print(file_list)

    convert_to_pdf(a_list,file_list)


if __name__ == "__main__":
    main()