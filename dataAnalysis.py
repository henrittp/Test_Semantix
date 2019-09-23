#! -*- coding: UTF-8 -*-

import sys, os
import re
from glob import glob

class Action:
    def __init__(self, list, file):
        self.log = "report_%s.log" % file.split("_")[-1]
        self.list = list
        self.list_404 = filter(lambda l: " 404 -" in l, self.list)
        self.list_URLs = map(lambda l: l.split(" ")[0], self.list)
        self.list_bytes = map(lambda l: l.split(" ")[-1], self.list)
    
        self.UniqueHosts()
        self.writeLog('{:-<45}'.format('\n'))

        self.QuantError404()
        self.writeLog('{:-<45}'.format('\n'))

        self.UrlsTop5_404()
        self.writeLog('{:-<45}'.format('\n'))

        self.totalBytes()

    #Number of unique hosts
    def UniqueHosts(self):
        hostUnique = set(self.list_URLs)

        total = sum(1 for hosts in hostUnique)
        self.writeLog("Número de hosts únicos: %d" % total)

    #5 more URls resulted in 404 errors
    def UrlsTop5_404(self):
        url = ""
        _max = 0
        dic = {}
        dic5 = {} 
    
        for line in self.list_404:
            url = line.split(" ")[0]
            if url not in dic:
                dic[url] = 1
            else:
                dic[url] += 1
        
        self.writeLog("\nAs 5 URLs com mais erros 404:")

        for i in range(5):
            url = ""
            _max = 0
            for k, v in dic.items():
                if v > _max and k not in dic5:
                    _max = v
                    url = k
            
            dic5[url] = _max
            self.writeLog("\n\t%s: %d" % (url, _max))

    #404 errors per day and total
    def QuantError404(self):
        list_data = []
        dateQuant = {}
        date = ""
        saveTimeStamp = ""
        totalErrors = 0

        for d in self.list_404:
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
    
        #last date
        list_data.append(dateQuant.copy())

        self.writeLog("\nErros 404 por dia:")

        for i in list_data:
            for k, v in i.items():
                self.writeLog("\n\t%s : %s" % (k,v))
                totalErrors += v

        self.writeLog("\n\nTotal de %d\nAproximadamente %.0f erros por dia" % (totalErrors, totalErrors/float(len(list_data))))

    #total Bytes 
    def totalBytes(self):
        total = 0
        for b in self.list_bytes:
            try:
                total += int(b)
            except:
                total += 0 

        self.writeLog("\nTotal de Bytes retornados: %d Bytes" % total)    

    #LOG
    def writeLog(self, reg):
        with open(self.log, "a") as infile:
            infile.write(reg)

def main():
    try:
        file1 = "NASA_access_log_Aug95"
        file2 = "NASA_access_log_Jul95"

        #remove log to save next report
        map(os.remove, glob("report*"))

        with open(file1, "r") as infile1, open(file2, "r") as infile2:
            one_list = infile1.readlines()
            two_list = infile2.readlines()

        if one_list:
            Action(one_list, file1)
            print("Log de Agosto gerado com sucesso")

        if two_list:
            Action(two_list, file2)
            print("Log de Julho gerado com sucesso")

        return 0

    except:
        print("Failed")

if __name__ == "__main__":
    main()