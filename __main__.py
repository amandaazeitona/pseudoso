from entrada import files_leitura, processes_leitura
from despachante import Despachante
from Arquivos.classe_disco import Disco
from Recurso.classe_recurso import Recursos
from Filas.fila_modelo import Fila
from Memoria.memoria_modelo import Memoria
from Processos.processo_modelo import Processo
from Processos.gereciador_processos import processos_inicia, processos_gerencia

import threading

print('\nInicializando SO')
print('Lendo processos')
processos = processes_leitura()
print('Lendo arquivos')
arquivos = files_leitura()
print('Alocando memória principal')
memoria = Memoria(1024)
print('Criando disco com arquivos')
disco = Disco(arquivos)
print('Reconhecendo dispositivos')
recursos = Recursos()
print('Criando fila de pronto')
fila_pronto = Fila()
print('Iniciando processos')
inicia_processos = threading.Thread(target=processos_inicia, args=(processos, fila_pronto, memoria, ))
inicia_processos.start()
print('Iniciando gerenciador de processos')
processos_gerencia(fila_pronto, processos, recursos, memoria, disco)
