import sys, os
import pdb

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
    dic = {}
    count = 0

    for linha in lista:
        count += 1
        if count == 10:
            break
        url = linha.split(" ")[0]
        if url not in dic:
            dic[url] = 1
        else:
            dic[url] += 1
    
    #print(sorted(e.items(), key = lambda kv:(kv[1], kv[0]), reverse=True))
    dic = sorted(dic.items(),reverse=True)
    
    count = 0
    for key in dic:
        count += 1     
        print(key)
        if count == 5:
            break

def QuantError404(lista):
    dias = []
    for linha in lista:
        if " 404 -" in lista:
            dias ="!"            
    return 1

#def totalBytes():

def main(argv):
    linha_404 = []
    try:
        with open(argv[1], "r") as infile:
            lista = infile.readlines()
        
        for linha in lista:
            if " 404 -" in linha:
                linha_404.append(linha)
        
        print("Oi")
        #TotalErrors404(linha_404)
        UrlsTop5_404(linha_404)
    except:
        usage()
        return 1

if __name__ == "__main__":
    sys.exit(main(sys.argv))
