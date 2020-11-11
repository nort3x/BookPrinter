import math
import os


def main(path="", f=1, l=1):
    inp = path
    fac = 1

    first_p = int(f)
    last_page = int(l)

    try:
        os.mkdir("BookOutPut")
    except Exception as e:
        pass
    os.system("cp " + inp + " BookOutPut/")
    os.chdir("BookOutPut")
    os.system("pdfseparate -f " + str(first_p) + " -l " + str(last_page) + " " + inp + " out%d.pdf")

    pages = []
    for i in range(first_p - 1, last_page):
        pages.append("out" + str(i + 1) + ".pdf")

    needed_pages = math.ceil(len(pages) / 4)
    ru = []
    posht = []
    for i in pages[1:len(pages):4]:
        ru.append(i)
        if pages.index(i) + 1 < len(pages):
            ru.append(pages[pages.index(i) + 1])

    for i in pages[0:len(pages):4]:
        posht.append(i)
        if pages.index(i) + 3 < len(pages):
            posht.append(pages[pages.index(i) + 3])
    print(ru)
    print(posht)

    os.system("pdfunite " + " ".join(ru) + " ../top.pdf")
    os.system("pdfunite " + " ".join(posht) + " ../bottom.pdf")
    os.system("rm -r ../BookOutPut/")

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Create a ArcHydro schema')
    parser.add_argument('--input', metavar='path', required=True,
                        help='the path to pdf')
    parser.add_argument('-f', metavar='int', required=True,
                        help='first page')
    parser.add_argument('-l', metavar='int', required=True,
                        help='last page')
    args = parser.parse_args()

    main(path=args.input, f=args.f, l=args.l)

