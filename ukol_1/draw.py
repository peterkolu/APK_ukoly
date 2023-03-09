#knihovyn QtCore , Qt GUi, Qt Widgets
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
import shapefile

class Draw(QTabWidget):

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
       # do této části to je ze cvič 20.2.

        #Query point and polygon
        self.__q = QPointF(0,0)       # jedno podtržíko protected, dvě private
        #self.__pol = []
        self.__pol = QPolygonF()     #funfact:rozdíl mezi Qpoint a QpointF: Qpoint - souřad jen celá čísla, QpointF - souřad i reál čísla
                                    #u polygonu to samý, QPolygon bude z QPoint a QPOlygonF bude z QpointF
        self.__add_vertex = True
        self.__results = []

    #Hugo time
    def setPath(self, width, height):
        # Store the filename data
        filename = QFileDialog.getOpenFileName(None, "Select SHP", "", "SHP files (*.shp)")

        # Return previous polygon if dialog box cancelled
        if bool(filename[0]) == False:
            return self.__pol

        # Store the path
        path = filename[0]

        # Read shapefile from path
        sf = shapefile.Reader(path)
        polygons = sf.shapes()

        # Initialise and extract x,y coordinates from .shp
        x = []
        y = []
        for k in range(len(sf)):
            pol_x = []
            pol_y = []
            for point in polygons[k].points:
                pol_x.append(point[0])
                pol_y.append(point[1])
            x.append(pol_x)
            y.append(pol_y)

        # Rescale loaded shapefile to screen resolution
        # Get minimum for x, y coordinates
        flat_x = []
        flat_x = [item for sublist in x for item in sublist]
        flat_y = []
        flat_y = [item for sublist in y for item in sublist]
        minimum_x = min(flat_x)
        minimum_y = min(flat_y)

        # Shift to the origin
        for i in range(len(x)):
            for j in range(len(x[i])):
                x[i][j] = (x[i][j] - minimum_x)
                y[i][j] = (y[i][j] - minimum_y)

        # Get the interval extent
        flat_xn = []
        flat_xn = [item for sublist in x for item in sublist]
        flat_yn = []
        flat_yn = [item for sublist in y for item in sublist]
        max_xn = max(flat_xn)
        max_yn = max(flat_yn)

        # Initialise the length of pol
        self.__pol = [0] * len(x)

        # Normalise to the interval [0,1]
        for i in range(len(x)):
            self.__pol[i] = QPolygonF()
            for j in range(len(x[i])):
                x[i][j] = int(x[i][j] / max_xn * width)

                # Subtract from Canvas height for axial symmetry
                y[i][j] = int(height - (y[i][j] / max_yn * height))
                p = QPointF(x[i][j], y[i][j])
                self.__pol[i].append(p)

        return self.__pol
        # Hugo konec

    def mousePressEvent(self, e:QMouseEvent):    # event mousePressEvent(e) si pamatuje kam myš klikla (LEVÝM tlačítkem), pravé je "ReleaseEvent"
        #Left mouse button click
        #Co potřebujeme: 1) souřad kurzoru, 2) vytvořit nový Qpoint:p 3) do našeho polygonu přidat bod p 4) chceme překreslit obrazovku "repaint", aby se bod zobrazil
        x = e.position().x()
        y = e.position().y()    #Tak, 1) by byla
        print("Pozice bodu je",x, "a",y)
        #Add point to polygon
        if self.__add_vertex:
            #Create point
            p = QPointF(x,y)
            #Append p to polygone
            self.__pol.append(p)    #Máme 2)
        #Set x,y to point
        else:
            self.__q.setX(x) #319.5
            self.__q.setY(y) #98.5
        #Repaint screen
        self.repaint()          #Pracujeme na 3)

    def paintEvent(self, e:QPaintEvent):

        #Create graphic object
        qp = QPainter(self)

        #Start draw
        qp.begin(self)

        #Hugo time
        # Loop through polygons in polygon list
        for pol in self.__pol:

            # Set color for all polygons
            qp.setPen(Qt.GlobalColor.blue)
            qp.setBrush(Qt.GlobalColor.white)
            qp.drawPolygon(pol)
            # Highlight the polygon containing the point
            # Set a condition
        if len(self.__results) > 0:
            for pol in self.__results:
                qp.setPen(Qt.GlobalColor.darkMagenta)
                qp.setBrush(Qt.GlobalColor.magenta)
                qp.drawPolygon(pol)

        # Set self.__results to [0] to enable new input
        #self.__results = []
        #Hugo konec

        #Set attributes for point
        qp.setPen(Qt.GlobalColor.red)   #barva pera
        qp.setBrush(Qt.GlobalColor.yellow) #barva výplně
        #Draw point
        d = 10  #kresba bodu přes elipsu, viz. sešit
        qp.drawEllipse(int((self.__q.x() - d/2)), int((self.__q.y() - d/2)), d, d)

        #End draw
        qp.end()

    def switchsource(self):     #Metoda, která nastavuje zda přidáváme bod či vrchol
        #Move point or add vertex
        self.__add_vertex = not(self.__add_vertex)

    def getPoint(self):
        #Get point
        return self.__q
    def getPolygon(self):
        #Get polygon
        return self.__pol
    def getResPol(self, pol: QPolygonF):
        #Get result polygon
        self.__results.append(pol)
    def clearResPol(self):
        # remove result polygon
        self.__results = []




