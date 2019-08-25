#! -*- coding: UTF-8 -*-

import sys, os
import pdb
import re

log = "relatorio.log"

def usage():
    print("python dados.py arquivo")

#Number of unique hosts
def UniqueHosts(list):
    hostUnique = set()

    for u in list:
        hostUnique.add(u)

    writeLog("Número de hosts únicos: %d" % len(hostUnique))

#5 more URls resulted in 404 errors
def UrlsTop5_404(list):
    url = ""
    _max = 0
    dic = {}
    dic5 = {} 
    count = 0

    for line in list:
        url = line.split(" ")[0]
        if url not in dic:
            dic[url] = 1
        else:
            dic[url] += 1
    
    writeLog("\nAs 5 URLs com mais erros 404:")

    for i in range(5):
        url = ""
        _max = 0
        for k, v in dic.items():
            if v > _max and k not in dic5:
                _max = v
                url = k
        
        dic5[url] = _max
        writeLog("\n\t%s: %d" % (url, _max))

#404 errors per day and total
def QuantError404(list):
    list_data = []
    dateQuant = {}
    date = ""
    saveTimeStamp = ""
    totalErrors = 0

    for d in list:
        date = re.findall(r'\d{2}/\w{3}/\d{4}',d)[0]

        if not saveTimeStamp:
            saveTimeStamp = date

        if date != saveTimeStamp and dateQuant:
            list_data.append(dateQuant.copy())
            del dateQuant[saveTimeStamp]
            saveTimeStamp = date

        if date not in dateQuant:
            dateQuant[date] = 1
        else:
            dateQuant[date] += 1
   
    #ultima data
    list_data.append(dateQuant.copy())

    writeLog("\nErros 404 por dia:")

    for i in list_data:
        for k, v in i.items():
            writeLog("\n\t%s : %s" % (k,v))
            totalErrors += v

    writeLog("\n\nTotal de %d\nAproximadamente %.0f erros por dia" % (totalErrors, totalErrors/float(len(list_data))))

#total Bytes 
def totalBytes(list_bytes):
    total = 0
    for b in list_bytes:
        try:
            total += int(b)
        except:
            total += 0 

    writeLog("\nTotal de Bytes retornados: %d Bytes" % total)    

#LOG
def writeLog(reg):
    with open(log, "a") as infile:
        infile.write(reg)

def main(argv):
    list_404 = []
    list_bytes = []
    list_URLs = []
    
    try:
        #remove log to save next report
        os.remove(log)

        if len(argv) == 2:
            with open(argv[1], "r") as infile:
                list = infile.readlines()

            for line in list:
                list_URLs.append(line.split(" ")[0])
                if " 404 -" in line:
                    list_404.append(line)
                else:
                    list_bytes.append(line.split(" ")[-1])
        
            UniqueHosts(list_URLs)
            writeLog('{:-<45}'.format('\n'))

            QuantError404(list_404)
            writeLog('{:-<45}'.format('\n'))

            UrlsTop5_404(list_404)
            writeLog('{:-<45}'.format('\n'))

            totalBytes(list_bytes)

            print("Processado com sucesso")
            return 0

        else:
            usage()
            return 1

    except ValueError:
        return False 


if __name__ == "__main__":
    sys.exit(main(sys.argv))
