import time

# mostra a "vida do processo"
# o processo é iniciado, depois executa as suas instruções, depois é finalizado
# se o processo for do tipo usuário ele pode ser interrompido
def processo_executa(processo, recursos, CPU):
    if processo.prioridade:
        flag_primeira_vez = 1
        for i in range(1, processo.quantidade_instrucoes+1):
            if flag_primeira_vez:
                recursos.aloca_recurso(processo)
            CPU.acquire()
            if flag_primeira_vez:
                print("\nP"+str(processo.PID)+" STARTED")
                flag_primeira_vez = 0
            print("P"+str(processo.PID)+" instruction "+str(processo.numero_instrucao))
            if processo.numero_instrucao == processo.quantidade_instrucoes:
                recursos.desaloca_recurso(processo)
                print("P"+str(processo.PID)+" return SIGINT")
            processo.numero_instrucao += 1
            CPU.release()
            time.sleep(1)
    else:
        CPU.acquire()
        print("\nP"+str(processo.PID)+" STARTED")
        for i in range(1, processo.quantidade_instrucoes+1):
            print("P"+str(processo.PID)+" instruction "+str(processo.numero_instrucao))
            processo.numero_instrucao += 1
            time.sleep(1)
        print("P"+str(processo.PID)+" return SIGINT")
        CPU.release()
