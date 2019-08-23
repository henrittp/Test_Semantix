import sys, os
import pdb
import datetime

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
    
    #print(sorted(e.items(), key = lambda kv:(kv[1], kv[0]), reverse=True))

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

    #print(dic5)

def QuantError404(lista):
    dias = []
    for linha in lista:
        if " 404 -" in lista:
            dias ="!"            
    return 1
#    dateAsString = string.split(" ")[3].split(":")[0].replace("[", "").replace("]", "").replace("/","-")
#    byte = string.split(" ")[-1]


def totalBytes(list_bytes):
    total = 0
    for b in list_bytes:
        try:
            total += long(b)
        except:
            print("Error")

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
        totalBytes(lista)
    except:
        usage()
        return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
