import sys, os
import pdb
from datetime import datetime
import re

def usage():
    print("python dados.py Arquivo.txt")

#def UniqueHosts(lista):

def TotalErrors404(lista):
    quant = 0
    for linha in lista:
        quant += 1

    print("Total erros 404: %d" % quant)

def UrlsTop5_404(lista):
    url = ""
    _max = 0
    dic = {}
    dic5 = {} 
    count = 0

    for linha in lista:
        url = linha.split(" ")[0]
        if url not in dic:
            dic[url] = 1
        else:
            dic[url] += 1
    
    print("\nAs 5 URLs com mais erros 404:")

    for i in range(5):
        url = ""
        _max = 0
        for k, v in dic.items():
            if v > _max and k not in dic5:
                _max = v
                url = k
        
        dic5[url] = _max
        print("\t%s: %d " % (url, _max))

def QuantError404(lista):
    dias_quant = {}
    dates = re.findall(r'\d{2}/\w{3}/\d{4}', lista)

    #saveTimeStamp = ""
    #for d in lista:
    #    saveTimeStamp = re.findall(r'\d{2}/\w{3}/\d{4}',d)
    #    date = datetime.strptime(saveTimeStamp, '%d/%b/%Y')

    #    if date not in dias_quant:
    #        dias_quant[date] = 1
    #    else:
    #        dias_quant[date] += 1
    
    #print(dias_quant.items())

        #    dateAsString = string.split(" ")[3].split(":")[0].replace("[", "").replace("]", "").replace("/","-")
#    byte = string.split(" ")[-1]


def totalBytes(list_bytes):
    total = 0
    for b in list_bytes:
        try:
            total += int(b)
        except:
            total += 0 

    print("\nTotal de Bytes retornados %d" % total)    

def main(argv):
    linha_404 = []
    list_bytes = []
    try:
        with open(argv[1], "r") as infile:
            lista = infile.readlines()
        
        for linha in lista:
            if " 404 -" in linha:
                linha_404.append(linha)
            else:
                list_bytes.append(linha.split(" ")[-1])
        
        TotalErrors404(linha_404)
        UrlsTop5_404(linha_404)
        totalBytes(list_bytes)
        QuantError404(linha_404)
    except:
        usage()
        return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
