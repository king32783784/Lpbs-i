import re

class ResultSorting(object):

    def readfile(self, resultfile):
        fopen = open(resultfile, 'r')
        f = fopen.read().strip()
        return f

    def datasearch(self, searchmode, resultfile, times):
        times=int(times)
        f = self.readfile(resultfile)
        re_list = re.findall(r"%s" % searchmode,f, re.S)
        testarry = []
        for i in re_list:
            testarry.append(float(i))
        j = 0
        averge = []
        for i, data in enumerate(testarry, 1):
            if i % times == 0:
                averge.append((sum(testarry[j:i]) / times))
                j = i
        
        result = []
        for i in averge:
            result.append(float(format(i, '0.2f')))
        return result
 
# useage
#a=ResultSorting()
#sysbench_mem
#count=2097152
#=a.datasearch("Operations performed: %s \((.*?)ops\/sec\)" % count, "resulttmp/performance/Perf_mem/result/result.out", 3)
#c=a.datasearch("8192.00 MB transferred \((.*?)MB\/sec\)", "resulttmp/performance/Perf_mem/result/result.out", 3)
#rint ("isoft | %s | %s" % (b[0], b[1]))
#print ("isoft | %s | %s" % (b[0], b[1]))
# sysbench_cpu

#d = a.datasearch("execution time \(avg\/stddev\):(.*?)\/0.00", "resulttmp/performance/Perf_cpu/result/result.out", 3)
#print (Mk_temp.sysbenchmemops)
#print ("isoft | %s | %s" % (d[0], d[1]))

