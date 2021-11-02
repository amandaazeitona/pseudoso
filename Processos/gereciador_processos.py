import operator
import threading
import time
from despachante import Despachante
from Processos.processo_thread import processo_executa

# inicializa processo
def processos_inicia(processos, fila, memoria):
    processos = sorted(processos, key=operator.attrgetter('tempo_inicializacao'))
    tempo_inicializacao_anterior = 1
    for processo in processos:
        if(processo.tempo_inicializacao > tempo_inicializacao_anterior):
            time.sleep(processo.tempo_inicializacao - tempo_inicializacao_anterior)
            fila.insere_processo(processo, memoria)
            tempo_inicializacao_anterior = processo.tempo_inicializacao
        else:
            fila.insere_processo(processo, memoria)

# gerencia os processos
def processos_gerencia(fila_pronto, processos, recursos, memoria, disco):
    CPU = threading.Lock()
    threads = {}
    despachante = Despachante()
    while(threading.active_count() > 1):
        processo = fila_pronto.remove_processo()
        if processo:
            if processo.prioridade:
                if processo.numero_instrucao == 1:
                    despachante.processo_despacha(processo, CPU)
                    threads['processo.PID'] = threading.Thread(target=processo_executa, args=(processo, recursos, CPU, ))
                    threads['processo.PID'].start()
                elif processo.numero_instrucao == processo.tempo_de_processador:
                    threads['processo.PID'].run()
                    memoria.desaloca_processo_usuario(processo)
                else:
                    threads['processo.PID'].run()
            elif processo.prioridade == 0:
                despachante.processo_despacha(processo, CPU)
                threads['processo.PID'] = threading.Thread(target=processo_executa, args=(processo, recursos, CPU, ))
                threads['processo.PID'].start()
                memoria.desaloca_processo_nucleo(processo)

    despachante.sistema_de_arquivos_executa(disco)
