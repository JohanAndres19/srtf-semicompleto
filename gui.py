import sys
from PyQt5.QtGui import QTextOption , QImage, QPainter
from  PyQt5.QtWidgets import *
from PyQt5.QtCore import QSize, Qt
from qt_for_python.uic.ventanaP import *
from Logica import *;
import random
import threading
#-------------------------------------
#------------- Interfaz---------------

class Ventana_principal(QMainWindow):
    def __init__(self,modelo):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.modelo=modelo
        self.controlador=Controlador(self)
        self.panel_scroll=QScrollArea(self.ui.frame_3)
        self.panel_scroll.resize(self.ui.frame_3.width(), self.ui.frame_3.height())
        #--------------------------------------------------------
        self.lienzo=Lienzo()
        self.panel_scroll.setStyleSheet("border: 2px solid;\n border-radius:15px;")
        self.panel_scroll.setWidget(self.lienzo)
        self.ui.comboBox.addItems(["  ","Round roy"])
        #--------------------------------------------------------
        header =["Proceso","T. llegada","Rafaga","T. comienzo","T. final","T. retorno","T. espera"]
        self.ui.tableWidget.setColumnCount(7)
        self.ui.tableWidget.verticalHeader().setVisible(False)
        self.ui.tableWidget.setHorizontalHeaderLabels(header)
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

    def Get_Lienzo(self):
        return self.lienzo
    
    def Get_modelo(self):
        return self.modelo

class Lienzo(QFrame):
    
    def __init__(self):
        super().__init__()
        self.resize(1600, 700)
        self.setStyleSheet("background: white;\n border: 2px solid;\n border-radius:15px;\n")
        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(Qt.white)
        self.dibujardiagrama=False
    
    def paintEvent(self,evento):
        painter = QPainter()
        painter.drawImage(self.rect(),self.image, self.image.rect())
        if self.dibujardiagrama:
            imagen=self.image.copy(0,0,self.width(),self.height())
            painter.drawImage(self.rect(),imagen,imagen.rect())

        
#--------------------------------------
#------------controlador---------------

class Controlador():
    def __init__(self,ventana):
        self.ventana =ventana
        self.Eventos()

    def Eventos(self):
        self.ventana.ui.boton_simular.clicked.connect(lambda: self.ventana.Get_modelo().Simular())
        self.ventana.ui.boton_bloquear.clicked.connect(lambda:self.ventana.Get_modelo().Bloquear())
        self.ventana.ui.boton_agregar.clicked.connect(lambda: self.ventana.Get_modelo().Agregar())
#---------------------------------------
#---------------Modelo-----------------
class Modelo ():
    
    def __init__(self) :
        self.ventana = Ventana_principal(self)
        self.colaIngresado=[]
        self.colaListo=[]
        self.algoritmo=Algoritmo(self)        
        self.estadoEje=Ejecutado(self.algoritmo)
        self.estadoBloqu=Bloqueado(self.algoritmo)
        self.ProcesoActual=None
        self.ProcesoAnte=None
        self.fila=0
        self.tiempo=0
        self.opcion=0
        

    def RafagaRamdon(self):
        return random.randint(1,14)

    
    def Agregar(self):
        self.opcion=self.ventana.ui.comboBox.currentIndex()
        """
        if self.ventana.ui.tableWidget.rowCount()==0:
            nombre= 'A'+str(self.algoritmo.Get_Fila()+1)
            rafaga= self.RafagaRamdon()
            proceso=Proceso(nombre,self.algoritmo.Tiempocomienzo,rafaga)
        elif '*' not in self.ventana.ui.tableWidget.item(self.ventana.ui.tableWidget.rowCount()-1, 0).text():
            texto=self.ventana.ui.tableWidget.item(self.ventana.ui.tableWidget.rowCount()-1, 0).text()
            aux=''
            for i in texto:
                if i.isnumeric():
                    aux+=i
            aux=int(aux)        
            nombre= 'A'+str(aux+1)
            rafaga= self.RafagaRamdon()
            proceso=Proceso(nombre,self.algoritmo.Tiempocomienzo,rafaga)
        else:
            nombre= 'A'+str(self.ventana.ui.tableWidget.rowCount())
            rafaga= self.RafagaRamdon()
            proceso=Proceso(nombre,self.algoritmo.Tiempocomienzo,rafaga)
        """
        nombre= 'A'+str(self.algoritmo.Get_Fila()+1)
        rafaga= self.RafagaRamdon()
        proceso=Proceso(nombre,self.algoritmo.Tiempocomienzo,rafaga)
        proceso.Set_indice(self.algoritmo.Get_Fila())
        self.algoritmo.Set_Fila(self.algoritmo.Get_Fila()+1)
        self.algoritmo.Get_Colaingresado().append(proceso)
        self.dibujar_tabla2(proceso)
        """
        self.opcion=self.ventana.ui.comboBox.currentIndex()
        nombre='A'+str(self.Get_fila()+1)
        rafaga= self.RafagaRamdon()
        proceso=Proceso(nombre,self.algoritmo.Tiempocomienzo,rafaga)
        proceso.Set_indice(self.fila)
        self.algoritmo.Get_Colaingresado().append(proceso)
        self.colaIngresado.append(proceso)
        self.Set_fila(self.Get_fila()+1)
        self.dibujar_tabla2(proceso)
        """

    def Simular(self):
        self.algoritmo.Set_Estado(self.estadoEje)
        self.algoritmo.Get_Estado().start()
        self.algoritmo.Get_Estado().senal_dibujar.connect(self.dibujar_tabla2)
        self.algoritmo.Get_Estado().senal_actualizar.connect(self.Actualizar_tabla)
        
    def dibujarSemaforo(self,imagen):
        pass
    def  dibujarespera(self):
        pass

    
    def dibujar_tabla2(self,proceso):
        if self.opcion ==1 and self.ProcesoAnte!=proceso:
            self.ProcesoAnte=proceso
            i=proceso.Get_indice()
            print(proceso.Get_nombre(),"indice i cantida de filas tabla",i,self.ventana.ui.tableWidget.rowCount())
            self.ventana.ui.tableWidget.insertRow(i)
            self.ventana.ui.tableWidget.setItem(i, 0, QTableWidgetItem(str(proceso.Get_nombre())))
            self.ventana.ui.tableWidget.setItem(i, 1, QTableWidgetItem(str(proceso.Get_tiempollegada())))
            self.ventana.ui.tableWidget.setItem(i, 2, QTableWidgetItem(str(proceso.Get_rafaga())))
            self.ventana.ui.tableWidget.setItem(i, 3, QTableWidgetItem(str(proceso.Get_tiempocomienzo())))
            self.ventana.ui.tableWidget.setItem(i, 4, QTableWidgetItem(str(proceso.Get_tiempofinal())))
            self.ventana.ui.tableWidget.setItem(i, 5, QTableWidgetItem(str(proceso.Get_tiemporetorno())))
            self.ventana.ui.tableWidget.setItem(i, 6, QTableWidgetItem(str(proceso.Get_tiempoespera())))
            

    def Actualizar_tabla(self,proceso):
        if self.opcion ==1 :
            i=proceso.Get_indice()
            self.ventana.ui.tableWidget.setItem(i, 3, QTableWidgetItem(str(proceso.Get_tiempocomienzo())))
            self.ventana.ui.tableWidget.setItem(i, 4, QTableWidgetItem(str(proceso.Get_tiempofinal())))
            self.ventana.ui.tableWidget.setItem(i, 5, QTableWidgetItem(str(proceso.Get_tiemporetorno())))
            self.ventana.ui.tableWidget.setItem(i, 6, QTableWidgetItem(str(proceso.Get_tiempoespera())))
    
    
    
    def Dibujar_semaro(self):
        pass

    def Bloquear(self):
        self.algoritmo.Set_isbloqueado(True)
        self.algoritmo.Get_Estado().senal_dibujar.connect(self.dibujar_tabla2)
        self.algoritmo.Get_Estado().senal_actualizar.connect(self.Actualizar_tabla)
        

    def Get_fila(self):
        return self.fila

    def Set_fila(self,fila):
        self.fila=fila

    def Get_ventana(self):
        return self.ventana    

#--------------------------------------
#---------------Main------------------- 
if __name__ =="__main__":
    app =QApplication(sys.argv)
    gui = Modelo().Get_ventana()
    gui.show()
    sys.exit(app.exec_())
