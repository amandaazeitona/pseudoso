import threading

# define os atributos dos recursos (dispositivos de entrada e saída)
class Recursos:

    def __init__(self):
        self.scanner = threading.Lock()
        self.modem = threading.Lock()
        self.impressora = threading.Semaphore(2)
        self.sata = threading.Semaphore(2)
    
    # aloca recurso para ser utilizado por processo
    def aloca_recurso(self, processo):
        for requisicao in enumerate(processo.recursos):
            utilizando = processo.recursos[requisicao]
            if utilizando:
                if requisicao == 'impressora':
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
                elif requisicao == 'sata':
                    print('Processo ' + str(processo.PID) + ' esperando recurso: ' + requisicao)
                    self.sata.acquire()
                    print('Processo ' + str(processo.PID) + ' alocando recurso: ' + requisicao)
                    return()

    # desaloca recurso que estava alocado por processo
    def desaloca_recurso(self, processo):
        for recurso, requisicao in enumerate(processo.recursos):
            utilizando = processo.recursos[requisicao]
            if utilizando:
                if requisicao == 'impressora':
                    print('Processo ' + str(processo.PID) + ' desalocando recurso: ' + requisicao)
                    self.impressora.release()
                elif requisicao == 'scanner':
                    print('Processo ' + str(processo.PID) + ' desalocando recurso: ' + requisicao)
                    self.scanner.release()
                elif requisicao == 'modem':
                    print('Processo ' + str(processo.PID) + ' desalocando recurso: ' + requisicao)
                    self.modem.release()
                elif requisicao == 'sata':
                    print('Processo ' + str(processo.PID) + ' desalocando recurso: ' + requisicao)
                    self.sata.release()
