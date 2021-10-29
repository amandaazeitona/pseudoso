import threading

class Recursos:

    def __init__(self):
        self.scanner = threading.Lock()
        self.modem = threading.Lock()
        self.impressora = threading.Semaphore(2)
        self.sata = threading.Semaphore(2)
    
    def aloca_recurso(self, processo):
        for recurso, requisicao in enumerate(processo.recursos):
            utilizando = processo.recursos[requisicao]
            if utilizando:
                if requisicao == 'impressora_codigo':
                    print('Processo ' + str(processo.PID) + ' esperando recurso: ' + requisicao)
                    self.impressora.acquire()
                    print('Processo ' + str(processo.PID) + ' alocando recurso: ' + requisicao)
                    return()
                elif requisicao == 'scanner':
                    print('Processo ' + str(processo.PID) + ' esperando recurso: ' + requisicao)
                    self.scanner.acquire()
                    print('Processo ' + str(processo.PID) + ' alocando recurso: ' + requisicao)
                    return()
                elif requisicao == 'modem':
                    print('Processo ' + str(processo.PID) + ' esperando recurso: ' + requisicao)
                    self.modem.acquire()
                    print('Processo ' + str(processo.PID) + ' alocando recurso: ' + requisicao)
                    return()
                elif requisicao == 'disco_codigo':
                    print('Processo ' + str(processo.PID) + ' esperando recurso: ' + requisicao)
                    self.sata.acquire()
                    print('Processo ' + str(processo.PID) + ' alocando recurso: ' + requisicao)
                    return()

    def desaloca_recurso(self, processo):
        for recurso, requisicao in enumerate(processo.recursos):
            utilizando = processo.recursos[requisicao]
            if utilizando:
                if requisicao == 'impressora_codigo':
                    print('Processo ' + str(processo.PID) + ' desalocando recurso: ' + requisicao)
                    self.impressora.release()
                elif requisicao == 'scanner':
                    print('Processo ' + str(processo.PID) + ' desalocando recurso: ' + requisicao)
                    self.scanner.release()
                elif requisicao == 'modem':
                    print('Processo ' + str(processo.PID) + ' desalocando recurso: ' + requisicao)
                    self.modem.release()
                elif requisicao == 'disco_codigo':
                    print('Processo ' + str(processo.PID) + ' desalocando recurso: ' + requisicao)
                    self.sata.release()
