from RSAtools import factorN #factordb & yafu
from RSAtools import publickey
from RSAtools import pubenc_m
from RSAtools import pqeflagenc_m

from RSAtools import ned_pq
from RSAtools import nc12e12_m
from RSAtools import endpc_m
from RSAtools import lowenc_m
from RSAtools import epq_d
from RSAtools import epqc_m
from RSAtools import en_d
from RSAtools import enc_m
from RSAtools import ne_d_wiener
from RSAtools import nec_m_wiener
from RSAtools import pqdpdq_d
from RSAtools import pqdpdqc_m
from RSAtools import ndpdq_d
from RSAtools import ndpdqc_m
from RSAtools import npnq
from pathlib import Path

def fun_call():
    # factorN.printf(RSAdata['n'])
    # publickey.printf()
    # pqeflagenc_m.printf(RSAdata['p'],RSAdata['q'],RSAdata['e'])
    # pubenc_m.printf()

    # ned_pq.printf(RSAdata['n'],RSAdata['e'],RSAdata['d']) 
    # nc12e12_m.printf(RSAdata['n'],RSAdata['c1'],RSAdata['c2'],RSAdata['e1'],RSAdata['e2'])
    # endpc_m.printf(RSAdata['e'],RSAdata['n'],RSAdata['dp'],RSAdata['c'])
    # lowenc_m.printf(RSAdata['e'],RSAdata['n'],RSAdata['c'])

    # epq_d.printf(RSAdata['e'],RSAdata['p'],RSAdata['q'])
    # epqc_m.printf(RSAdata['e'],RSAdata['p'],RSAdata['q'],RSAdata['c'])
    # en_d.printf(RSAdata['e'],RSAdata['n'])
    # enc_m.printf(RSAdata['e'],RSAdata['n'],RSAdata['c'])
    # ne_d_wiener.printf(RSAdata['n'],RSAdata['e'])
    # nec_m_wiener.printf(RSAdata['n'],RSAdata['e'],RSAdata['c'])
    # pqdpdq_d.printf(RSAdata['p'],RSAdata['q'],RSAdata['dp'],RSAdata['dq'])
    # pqdpdqc_m.printf(RSAdata['p'],RSAdata['q'],RSAdata['dp'],RSAdata['dq'],RSAdata['c'])
    # ndpdq_d.printf(RSAdata['n'],RSAdata['dp'],RSAdata['dq'])
    # ndpdqc_m.printf(RSAdata['n'],RSAdata['dp'],RSAdata['dq'],RSAdata['c'])
    pass

# solves()
def judge(RSAdata):                                              #区分是否有N => 区分是否有p/q => 区分是否有e/d => 区分是否有c
    print("\n")
    print("-----RSAanalyse：-----")

    if "n" in RSAdata.keys():                              
        print("有n存在，可能需要分解n")

        if "p" in RSAdata.keys() and "q" in RSAdata.keys():
            print("有pq存在，无需分解n")

            if "e" in RSAdata.keys() and "d" in RSAdata.keys():
                print("有ed存在，将判断是否存在c")

                if "c" in RSAdata.keys():
                    print("有c存在，npqedc已知,可能求m")    #npqedc
                    epqc_m.printf(RSAdata['e'],RSAdata['p'],RSAdata['q'],RSAdata['c'])

                else:
                    print("无c存在，npqed已知，找不到目标") #npqed
                    epq_d.printf(RSAdata['e'],RSAdata['p'],RSAdata['q'])


            elif "e" in RSAdata.keys() and "d" not in RSAdata.keys():
                print("有e存在，将判断是否存在c")

                if "c" in RSAdata.keys():
                    print("有c存在，npqec已知,可能求m") #npqec
                    epqc_m.printf(RSAdata['e'],RSAdata['p'],RSAdata['q'],RSAdata['c'])

                else:
                    print("无c存在，npqe已知,可能求d")  #npqe
                    epq_d.printf(RSAdata['e'],RSAdata['p'],RSAdata['q'])


            elif "e" not in RSAdata.keys() and "d" in RSAdata.keys():
                print("有d存在，无e，暂无此类解法") #npqdc /npqd


            else:
                print("无ed存在，npq已知，找不到目标") #npqc /npq

        elif "p" in RSAdata.keys() or "q" in RSAdata.keys():
            print("有p或q存在，可直接求得q或p")

            if "e" in RSAdata.keys() and "d" in RSAdata.keys():
                print("有ed存在，将判断是否存在c")

                if "c" in RSAdata.keys():
                    print("有c存在，np/qedc已知,可能求m")    #np/qedc
                    if "p" in RSAdata.keys():
                        RSAdata['q'] = npnq.solves(RSAdata['n'],RSAdata['p'])
                    elif "q" in RSAdata.keys(): 
                        RSAdata['p'] = npnq.solves(RSAdata['n'],RSAdata['q'])
                    epqc_m.printf(RSAdata['e'],RSAdata['p'],RSAdata['q'],RSAdata['c'])
                else:
                    print("无c存在，np/qed已知，可能求q/p") #np/qed
                    if "p" in RSAdata.keys(): 
                        RSAdata['q'] = npnq.solves(RSAdata['n'],RSAdata['p'])
                    elif "q" in RSAdata.keys(): 
                        RSAdata['p'] = npnq.solves(RSAdata['n'],RSAdata['q'])
                    epq_d.printf(RSAdata['e'],RSAdata['p'],RSAdata['q'])

            elif "e" in RSAdata.keys() and "d" not in RSAdata.keys():
                print("有e存在，将判断是否存在c")

                if "c" in RSAdata.keys():
                    print("有c存在，np/qec已知,可能求m") #np/qec
                    if "p" in RSAdata.keys(): 
                        RSAdata['q'] = npnq.solves(RSAdata['n'],RSAdata['p'])
                    elif "q" in RSAdata.keys(): 
                        RSAdata['p'] = npnq.solves(RSAdata['n'],RSAdata['q'])
                    epqc_m.printf(RSAdata['e'],RSAdata['p'],RSAdata['q'],RSAdata['c'])
                else:
                    print("无c存在，np/qe已知,可能求d")  #np/qe
                    if "p" in RSAdata.keys(): 
                        RSAdata['q'] = npnq.solves(RSAdata['n'],RSAdata['p'])
                    elif "q" in RSAdata.keys(): 
                        RSAdata['p'] = npnq.solves(RSAdata['n'],RSAdata['q'])
                    epq_d.printf(RSAdata['e'],RSAdata['p'],RSAdata['q'])

            elif "e" not in RSAdata.keys() and "d" in RSAdata.keys():
                print("有d存在，无e，可能求q/p，暂无其他算法") #np/qdc np/qd
                if "p" in RSAdata.keys(): npnq.printf(RSAdata['n'],RSAdata['p'])
                elif "q" in RSAdata.keys(): npnq.printf(RSAdata['n'],RSAdata['q'])

            else:
                print("无ed存在，np/q已知，可能求q/p")  #np/qc np/q
                if "p" in RSAdata.keys(): npnq.printf(RSAdata['n'],RSAdata['p'])
                elif "q" in RSAdata.keys(): npnq.printf(RSAdata['n'],RSAdata['q'])

        else:
            print("无pq存在，可能需要分解n或不需要用到pq")

            if "e" in RSAdata.keys() and "d" in RSAdata.keys():
                print("有ed存在，将判断是否存在c")

                if "c" in RSAdata.keys():
                    print("有c存在，nedc已知,可能求pq或m")    #nedc
                    if int(RSAdata['e']) < 11:
                        lowenc_m.printf(RSAdata['e'],RSAdata['n'],RSAdata['c'])
                    ned_pq.printf(RSAdata['n'],RSAdata['e'],RSAdata['d'])
                    enc_m.printf(RSAdata['e'],RSAdata['n'],RSAdata['c'])
                    nec_m_wiener.printf(RSAdata['n'],RSAdata['e'],RSAdata['c'])
                    (p,q) = ned_pq.solves(RSAdata['n'],RSAdata['e'],RSAdata['d'])
                    epqc_m.printf(RSAdata['e'],p,q,RSAdata['c'])

                else:
                    print("无c存在，ned已知，可能求pq") #ned
                    factorN.printf(RSAdata['n'])
                    ned_pq.printf(RSAdata['n'],RSAdata['e'],RSAdata['d'])

            elif "e" in RSAdata.keys() and "d" not in RSAdata.keys():
                print("有e存在，将判断是否存在c")

                if "c" in RSAdata.keys():
                    print("有c存在，nec已知,可能求m") #nec

                    if "dp" in RSAdata.keys():
                        endpc_m.printf(RSAdata['e'],RSAdata['n'],RSAdata['dp'],RSAdata['c'])
                    elif "dq" in RSAdata.keys():
                        endpc_m.printf(RSAdata['e'],RSAdata['n'],RSAdata['dq'],RSAdata['c'])
                    else:
                        if int(RSAdata['e']) < 11:
                            lowenc_m.printf(RSAdata['e'],RSAdata['n'],RSAdata['c'])
                        nec_m_wiener.printf(RSAdata['n'],RSAdata['e'],RSAdata['c'])
                        enc_m.printf(RSAdata['e'],RSAdata['n'],RSAdata['c'])
                    
                else:
                    print("无c存在，ne已知,可能求d")  #ne
                    en_d.printf(RSAdata['e'],RSAdata['n'])
                    ne_d_wiener.printf(RSAdata['n'],RSAdata['e'])

            elif "e" not in RSAdata.keys() and "d" in RSAdata.keys():
                print("有d存在，无e，暂无其他算法") #ndc nd

            elif ("e1" in RSAdata.keys() and "e2" in RSAdata.keys()) and ("c1" in RSAdata.keys() and "c2" in RSAdata.keys()):
                print("有ne12c12，共模求m") #nc12e12
                nc12e12_m.printf(RSAdata['n'],RSAdata['c1'],RSAdata['c2'],RSAdata['e1'],RSAdata['e2'])

            elif "dp" in RSAdata.keys() and "dq" in RSAdata.keys():
                print("有dpdq存在，将判断是否存在c")

                if "c" in RSAdata.keys():
                    print("有c存在，ndpdqc已知,可能求m") #ndpdqc
                    ndpdqc_m.printf(RSAdata['n'],RSAdata['dp'],RSAdata['dq'],RSAdata['c'])
                    
                else:
                    print("无c存在，ndpdq已知,可能求d")  #ndpdq
                    ndpdq_d.printf(RSAdata['n'],RSAdata['dp'],RSAdata['dq'])
                    
            else:
                print("无ed存在，n已知，可能求qp")  #n
                factorN.printf(RSAdata['n'])


    else:
        print("无n存在，无需分解n")

        if "p" in RSAdata.keys() and "q" in RSAdata.keys():
            print("有pq存在，可反求n")

            if "e" in RSAdata.keys() and "d" in RSAdata.keys():
                print("有ed存在，将判断是否存在c")

                if "c" in RSAdata.keys():
                    print("有c存在，pqedc已知,可能求m")    #pqedc
                    epqc_m.printf(RSAdata['e'],RSAdata['p'],RSAdata['q'],RSAdata['c'])
                else:
                    print("无c存在，pqed已知，可能求n") #pqed
                    epq_d.printf(RSAdata['e'],RSAdata['p'],RSAdata['q'])

            elif "e" in RSAdata.keys() and "d" not in RSAdata.keys():
                print("有e存在，将判断是否存在c")

                if "c" in RSAdata.keys():
                    print("有c存在，pqec已知,可能求m") #pqec
                    epqc_m.printf(RSAdata['e'],RSAdata['p'],RSAdata['q'],RSAdata['c'])

                elif Path("/flag.enc").is_file():
                    print("flag.enc存在，已知pqe，尝试求m")
                    pqeflagenc_m.printf(RSAdata['p'],RSAdata['q'],RSAdata['e'])

                else:
                    print("无c存在，pqe已知,可能求d")  #pqe
                    epq_d.printf(RSAdata['e'],RSAdata['p'],RSAdata['q'])

            elif "e" not in RSAdata.keys() and "d" in RSAdata.keys():
                print("有d存在，无e，找不到目标") #pqdc / pqd

            elif "dp" in RSAdata.keys() and "dq" in RSAdata.keys():
                print("有dpdq存在，将判断是否存在c")

                if "c" in RSAdata.keys():
                    print("有c存在，pqdpdqc已知,可能求m") #pqdpdqc
                    pqdpdqc_m.printf(RSAdata['p'],RSAdata['q'],RSAdata['dp'],RSAdata['dq'],RSAdata['c'])
                    
                else:
                    print("无c存在，pqdpdq已知,可能求d")  #pqdpdq
                    pqdpdq_d.printf(RSAdata['p'],RSAdata['q'],RSAdata['dp'],RSAdata['dq'])

            else: 
                print("无ed存在，pq已知，找不到目标") #pqc / pq
        
        else:
            print("无pq存在，正在查找目录中pub.key&&flag.enc")
            keypath = Path("pub.key")
            encpath = Path("flag.enc")

            if keypath.is_file():
                print("pub.key存在，将判断flag.enc是否存在")

                if encpath.is_file():
                    print("flag.enc存在，尝试求m")
                    pubenc_m.printf()

                else:
                    print("flag.enc不存在，尝试求ne")
                    publickey.printf()

            else:
                print("pub.key不存在，请仔细检查文件目录和data.txt，若有bug联系作者，然后手撕吧~")

    print("\n")

    
