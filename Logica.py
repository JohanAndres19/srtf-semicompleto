from PyQt5.QtCore import QThread, pyqtSignal
import time
class Proceso() :
    
    def __init__(self,nombre,tiempollegada,rafaga):
        self.Nombre=nombre
        self.tiempollegada=tiempollegada
        self.rafaga=rafaga
        self.prioridad=0
        self.tiempocomienzo=0
        self.tiempofinal=0
        self.tiemporetorno=0
        self.tiempoespera=0
        self.isbloqueado=False
        self.indice=0
        
    def Set_isbloqueado(self,booleano):
        self.isbloqueado=booleano

    def Get_isbloqueado(self):
        return self.isbloqueado            

    def Get_nombre(self):
        return self.Nombre

    def Get_tiempollegada(self):
        return self.tiempollegada

    def Get_rafaga(self):
        return self.rafaga        

    def Get_tiempocomienzo(self):
        return self.tiempocomienzo

    def Get_tiempofinal(self):
        return self.tiempofinal

    def Get_tiemporetorno(self):
        return self.tiemporetorno       

    def Get_tiempoespera(self):
        return self.tiempoespera

    def Set_rafaga(self,valor):
        self.rafaga=valor

    def Set_Prioridad(self,valor):
        self.prioridad=valor

    def Get_Prioridad(self):
        return self.prioridad

    def Set_tiempocomienzo(self,tiempo):
        self.tiempocomienzo=tiempo

    def Set_tiempofinal(self,tiempo):
        self.tiempofinal=tiempo

    def Set_tiemporetorno(self,tiempo):
        self.tiemporetorno=tiempo

    def Set_tiempoespera(self,tiempo):
        self.tiempoespera=tiempo

    def Get_indice(self):
        return self.indice

    def Set_indice(self,valor):
        self.indice=valor

class Algoritmo:
    
    def __init__(self,modelo) :
        self.estado=None
        self.modelo=modelo
        self.colaingresado=[]
        self.ColaBloqueados=[]
        self.isbloqueado=False
        self.Tiempocomienzo=0;
        self.fila=0

    def ordenar(self):
        if len(self.colaingresado)>0:
            aux=self.colaingresado[0].Get_rafaga()
            pos=-1
            for i in range(1,len(self.colaingresado)):
                if (self.colaingresado[i]).Get_rafaga()<aux:
                    aux=(self.colaingresado[i]).Get_rafaga()
                    pos=i
            if pos!=-1:
                elemento=self.colaingresado.pop(pos)
                self.colaingresado.insert(0,elemento) 

    def Set_Estado(self,estado):
        self.estado=estado

    def Get_Estado(self):
        return self.estado    

    def Get_ColaBloqueados(self):
        return self.ColaBloqueados

    def Set_isbloqueado(self,booleano):
        self.isbloqueado=booleano

    def Get_isbloqueado(self):
        return self.isbloqueado

    def Get_Colaingresado(self):
        return self.colaingresado

    def Get_UltimoElemento(self):
        if len(self.colaingresado)>0:
            return self.colaingresado[-1] 

    def Set_Tiempocomienzo(self,valor):
         self.Tiempocomienzo=valor

    def Get_Tiempocomienzo(self):
        return self.Tiempocomienzo

    def Get_Modelo(self):
        return self.modelo

    def Get_Fila(self):
        return self.fila

    def Set_Fila(self,fila):
        self.fila=fila
            
class Estado_Algoritmo(QThread):
    
    senal_actualizar=pyqtSignal(Proceso)
    senal_dibujar=pyqtSignal(Proceso)

    def __init__(self,algortimo) :
        super().__init__()
        self.algoritmo=algortimo
        

    def Ejecutar(self):
        pass

class Ejecutado(Estado_Algoritmo):
    def __init__(self,algoritmo):
        super().__init__(algoritmo)

    def Ejecutar(self):
        while len(self.algoritmo.Get_Colaingresado())>0:
            self.algoritmo.ordenar()
            proceso=self.algoritmo.Get_Colaingresado().pop(0)
            proceso.Set_tiempocomienzo(self.algoritmo.Get_Tiempocomienzo())
            print(proceso.Get_nombre())
            while  proceso.Get_rafaga()>0  and not self.algoritmo.Get_isbloqueado():
                if len(self.algoritmo.Get_Colaingresado())>0 and self.algoritmo.Get_UltimoElemento().Get_rafaga()<proceso.Get_rafaga():
                    new_proceso=Proceso(str(proceso.Get_nombre()+'*'),self.algoritmo.Get_Tiempocomienzo(),proceso.Get_rafaga())
                    new_proceso.Set_indice(self.algoritmo.Get_Fila())
                    self.algoritmo.Get_Colaingresado().append(new_proceso)
                    self.senal_dibujar.emit(new_proceso)
                    self.algoritmo.Set_Fila(self.algoritmo.Get_Fila()+1)
                    break
                proceso.Set_rafaga(proceso.Get_rafaga()-1)
                self.algoritmo.Set_Tiempocomienzo(self.algoritmo.Get_Tiempocomienzo()+1)
                print(proceso.Get_rafaga())
                time.sleep(1.5)                
            if self.algoritmo.Get_isbloqueado():
                new_proceso=Proceso(str(proceso.Get_nombre()+'~'),self.algoritmo.Get_Tiempocomienzo(),proceso.Get_rafaga())
                print("$$$",self.algoritmo.Get_Fila())
                new_proceso.Set_indice(self.algoritmo.Get_Fila())   
                self.algoritmo.Get_ColaBloqueados().append(new_proceso)
                self.algoritmo.Set_Estado(self.algoritmo.Get_Modelo().estadoBloqu)
                self.algoritmo.Get_Estado().start()
                self.senal_dibujar.emit(new_proceso)
                self.algoritmo.Get_Estado().senal_dibujar.connect(self.algoritmo.Get_Modelo().dibujar_tabla2)
                self.algoritmo.Get_Estado().senal_actualizar.connect(self.algoritmo.Get_Modelo().Actualizar_tabla)
                self.algoritmo.Set_isbloqueado(False)
                self.algoritmo.Set_Fila(self.algoritmo.Get_Fila()+1)
            proceso.Set_tiempofinal(self.algoritmo.Get_Tiempocomienzo())
            proceso.Set_tiemporetorno(proceso.Get_tiempofinal()-proceso.Get_tiempollegada())
            aux=proceso.Get_tiempoespera()
            proceso.Set_tiempoespera(proceso.Get_tiempocomienzo()-proceso.Get_tiempollegada()+aux)
            self.senal_actualizar.emit(proceso)
            time.sleep(1)

        
        
    def run(self):
        self.Ejecutar()

class Bloqueado(Estado_Algoritmo):
    def __init__(self,algoritmo):
        super().__init__(algoritmo)

    def Ejecutar(self):
        print("esta haciendo la lista de bloque a dos ")
        while len(self.algoritmo.Get_ColaBloqueados())>0:
            proceso=self.algoritmo.Get_ColaBloqueados().pop(0)
            time.sleep(1.2)
            proceso.Set_tiempocomienzo(proceso.Get_tiempollegada()+2)
            self.algoritmo.Get_Colaingresado().append(proceso)
        
            


    def run(self):
        self.Ejecutar()

def Simular(algoritmo,colaIngresado):
        nombres =['A','B','C','D','E','F','G','H','I','J','K']
        for i in nombres:
            valor=random.randint(11,60)
            aux=Proceso(i,nombres.index(i),valor)
            colaIngresado.append(Proceso)        
        algoritmo.Set_Estado(Ejecutado(algoritmo))
        for i in colaIngresado:
            valor=random.randint(1,60)
            if valor>=1 and valor<=10:
                algoritmo.Set_isbloqueado(True)
            algoritmo.Get_Estado().Ejecutar(i)
        for i in algoritmo.Get_ColaBloqueados():
            print(i.Get_isbloqueado())


if __name__ =="__main__" :
    cola=[]
    Simular(Algoritmo(),cola)




