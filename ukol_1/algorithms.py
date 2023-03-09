from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from math import *

class Algorithms:

    def __int__(self):
        pass

    def getPositionAndAngle(self, q, i0, i1):
        eps = 1**(-19)
        # Vectors
        x_qi = i0.x() - q.x()  # i-tý bod
        y_qi = i0.y() - q.y()
        x_qi1 = i1.x() - q.x()  # dělíme to n protože cyklus je bezpečný pouze pro kladný index a my bychom přerostli pole; po posledním vrcholu následuje zase první vrchol, proto toto
        y_qi1 = i1.y() - q.y()  # i+1-tý bod

        # Determinant
        det = x_qi*y_qi1 - x_qi1*y_qi

        # Position (right half-plane, left half-plane, colinear point)
        if det > eps:
            pos = 1
        elif det < -eps:
            pos = 0
        else:
            pos = -1

        # Numerator
        nu = x_qi*x_qi1 + y_qi*y_qi1

        # Denominator
        nrm_qi = (x_qi**2 + y_qi**2)**0.5
        nrm_qi1 =(x_qi1**2 + y_qi1**2)**0.5
        nrms = nrm_qi*nrm_qi1

        # Angle
        if nrms == 0:
            cos_a = 0
        else:
            cos_a = nu/nrms
            if cos_a > 1:
                cos_a = 1
            elif cos_a < -1:
                cos_a = -1
        omega = abs(acos(cos_a))

        # Position and angle
        return pos, omega

    def getWindingNumber (self, q, pol):
        eps = 1**(-19)
        n = len(pol)
        omega_sum = 0

        # Proces all vertices
        for i in range(n-1):

            pos, omega = self.getPositionAndAngle(q, pol[i], pol[(i + 1) % n])

            if pos == 1:
                omega_sum += omega
            elif pos == 0:
                omega_sum -= omega
            else:
                q_x = q.x()
                q_y = q.y()
                i_x = pol[i].x()
                i_y = pol[i].y()
                i1_x = pol[(i + 1) % n].x()
                i1_y = pol[(i + 1) % n].y()
                if (i_x <= q_x <= i1_x) and (i_y <= q_y <= i1_y):
                    return 1

        if abs(abs(omega_sum)-2*pi) < eps:
            return 1

        return 0



    def getPointPolygonPositionR(self, q, pol): #vstup bod a polygon
        kr = 0 #proměnná počtu průsečíků
        kl = 0
        n = len(pol) #délka polygonu

        # proces all vertices
        for i in range(n): #Zpracujeme všechny vrcholy polygonu

            #reduce coordinate - přesuneme počátek souřadnic do bodu q
            xi = pol[i].x() - q.x()    #i-tý bod
            yi = pol[i].y() - q.y()
            xi1 = pol[(i + 1) % n].x() - q.x()       #dělíme to n protože cyklus je bezpečný pouze pro kladný index a my bychom přerostli pole; po posledním vrcholu následuje zase první vrchol, proto toto
            yi1 = pol[(i + 1) % n].y() - q.y()     #i+1-tý bod

            # State where point is vertex
            if xi == 0 and yi == 0:
                return 1

            # Compute intersection - počítáme prusečík obou přímek q a ii-1
            if (yi1 - yi) == 0:
                continue
            else:
                xm = (xi1 * yi - xi * yi1) / (yi1 - yi)

            #Hledáme segment protnutý paprskem (no prostě ty průsečíky) MOŽNÁ??
            #Suitable segment
            if (yi1 > 0) and (yi <= 0) or (yi >0) and (yi1 <= 0): #prvek nad nebo prvek pod, je to redukce na tu jednu polorovinu, str 16 přednáška 3
                # increment amount of intersections budeme zvětšovat počet průsečíků - pakliže leží ve zvolené polorovině
                if xm > 0:
                    kr+=1

            #Left half-plane
            elif (yi1 < 0) and (yi >= 0) or (yi < 0) and (yi1 >= 0):
                if xm < 0:
                    kl+=1
        # State where point is on polygon boundary
        if (kr % 2) != (kl % 2):
            return 1

        # State where point is inside polygon
        if (kr % 2) == 1:
            return 1

        return 0    #když se nesplnila podmínka ležení v polygonu, vrátíme automaticky 0.

    def getRayCrossing(self, q, pol):
        kr = 0  # proměnná počtu průsečíků
        kl = 0
        n = len(pol)  # délka polygonu

        # proces all vertices
        for i in range(n):  # Zpracujeme všechny vrcholy polygonu

            # reduce coordinate - přesuneme počátek souřadnic do bodu q
            xi = pol[i].x() - q.x()  # i-tý bod
            yi = pol[i].y() - q.y()
            xi1 = pol[(i + 1) % n].x() - q.x()  # dělíme to n protože cyklus je bezpečný pouze pro kladný index a my bychom přerostli pole; po posledním vrcholu následuje zase první vrchol, proto toto
            yi1 = pol[(i + 1) % n].y() - q.y()  # i+1-tý bod

            # State where point is vertex
            if xi == 0 and yi == 0:
                return 1

            # Compute intersection - počítáme prusečík obou přímek q a ii-1
            if (yi1 - yi) == 0:
                continue
            else:
                xm = (xi1 * yi - xi * yi1) / (yi1 - yi)

            # Hledáme segment protnutý paprskem (no prostě ty průsečíky) MOŽNÁ??
            # Suitable segment
            if ((yi1 > 0) and (yi <= 0)) or ((yi > 0) and (yi1 <= 0)):  # prvek nad nebo prvek pod, je to redukce na tu jednu polorovinu, str 16 přednáška 3
                # increment amount of intersections budeme zvětšovat počet průsečíků - pakliže leží ve zvolené polorovině
                if xm > 0:
                    kr += 1

            # Left half-plane
            elif ((yi1 < 0) and (yi >= 0)) or ((yi < 0) and (yi1 >= 0)):
                if xm < 0:
                    kl += 1
        # State where point is on polygon boundary
        if (kr % 2) != (kl % 2):
            return 1

        # State where point is inside polygon
        if (kr % 2) == 1:
            return 1

        return 0  # když se nesplnila podmínka ležení v polygonu, vrátíme automaticky 0.

