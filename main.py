import os
import sys
import time
import PyQt5
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from threading import Thread
from PyQt5.QtWidgets import *
from DjikstrasWidget import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.main_ui = Ui_MainWindow()
        self.djikstra = None
        self.main_ui.setupUi(self)
        self.graph = [ [ 1 for i in range(64) ] for j in range(64) ]
        self.objGraph = [[ 0 for i in range(8) ] for j in range(8) ]
        for i in range(64):
            for j in range(64):
                ix = i%8
                iy = i//8
                jx=j%8
                jy=j//8
                if i==j:
                    self.graph[i][j]=0
                elif (ix==jx and (iy==jy-1 or iy==jy+1))or(iy==jy and (ix==jx-1 or ix==jx+1)):
                    self.graph[i][j]=1
                else:
                    self.graph[i][j]=100
        self.modes = ['Erase','Start', 'Obstacles', 'Finish']
        self.modeNum = 1
        self.main_ui.mode.setText(self.modes[self.modeNum%4])
        self.colors = ['light grey','green','orange','red']
        self.color = self.colors[self.modeNum%4]
        self.main_ui.bModeChange.clicked.connect(self.modeChange)
        self.main_ui.bStart.clicked.connect(self.start)
        self.main_ui.b00.clicked.connect(lambda: self.tileClick(self.main_ui.b00, 0))
        self.main_ui.b01.clicked.connect(lambda: self.tileClick(self.main_ui.b01, 1))
        self.main_ui.b02.clicked.connect(lambda: self.tileClick(self.main_ui.b02, 2))
        self.main_ui.b03.clicked.connect(lambda: self.tileClick(self.main_ui.b03, 3))
        self.main_ui.b04.clicked.connect(lambda: self.tileClick(self.main_ui.b04, 4))
        self.main_ui.b05.clicked.connect(lambda: self.tileClick(self.main_ui.b05, 5))
        self.main_ui.b06.clicked.connect(lambda: self.tileClick(self.main_ui.b06, 6))
        self.main_ui.b07.clicked.connect(lambda: self.tileClick(self.main_ui.b07, 7))
        self.main_ui.b10.clicked.connect(lambda: self.tileClick(self.main_ui.b10, 8))
        self.main_ui.b11.clicked.connect(lambda: self.tileClick(self.main_ui.b11, 9))
        self.main_ui.b12.clicked.connect(lambda: self.tileClick(self.main_ui.b12, 10))
        self.main_ui.b13.clicked.connect(lambda: self.tileClick(self.main_ui.b13, 11))
        self.main_ui.b14.clicked.connect(lambda: self.tileClick(self.main_ui.b14, 12))
        self.main_ui.b15.clicked.connect(lambda: self.tileClick(self.main_ui.b15, 13))
        self.main_ui.b16.clicked.connect(lambda: self.tileClick(self.main_ui.b16, 14))
        self.main_ui.b17.clicked.connect(lambda: self.tileClick(self.main_ui.b17, 15))
        self.main_ui.b20.clicked.connect(lambda: self.tileClick(self.main_ui.b20, 16))
        self.main_ui.b21.clicked.connect(lambda: self.tileClick(self.main_ui.b21, 17))
        self.main_ui.b22.clicked.connect(lambda: self.tileClick(self.main_ui.b22, 18))
        self.main_ui.b23.clicked.connect(lambda: self.tileClick(self.main_ui.b23, 19))
        self.main_ui.b24.clicked.connect(lambda: self.tileClick(self.main_ui.b24, 20))
        self.main_ui.b25.clicked.connect(lambda: self.tileClick(self.main_ui.b25, 21))
        self.main_ui.b26.clicked.connect(lambda: self.tileClick(self.main_ui.b26, 22))
        self.main_ui.b27.clicked.connect(lambda: self.tileClick(self.main_ui.b27, 23))
        self.main_ui.b30.clicked.connect(lambda: self.tileClick(self.main_ui.b30, 24))
        self.main_ui.b31.clicked.connect(lambda: self.tileClick(self.main_ui.b31, 25))
        self.main_ui.b32.clicked.connect(lambda: self.tileClick(self.main_ui.b32, 26))
        self.main_ui.b33.clicked.connect(lambda: self.tileClick(self.main_ui.b33, 27))
        self.main_ui.b34.clicked.connect(lambda: self.tileClick(self.main_ui.b34, 28))
        self.main_ui.b35.clicked.connect(lambda: self.tileClick(self.main_ui.b35, 29))
        self.main_ui.b36.clicked.connect(lambda: self.tileClick(self.main_ui.b36, 30))
        self.main_ui.b37.clicked.connect(lambda: self.tileClick(self.main_ui.b37, 31))
        self.main_ui.b40.clicked.connect(lambda: self.tileClick(self.main_ui.b40, 32))
        self.main_ui.b41.clicked.connect(lambda: self.tileClick(self.main_ui.b41, 33))
        self.main_ui.b42.clicked.connect(lambda: self.tileClick(self.main_ui.b42, 34))
        self.main_ui.b43.clicked.connect(lambda: self.tileClick(self.main_ui.b43, 35))
        self.main_ui.b44.clicked.connect(lambda: self.tileClick(self.main_ui.b44, 36))
        self.main_ui.b45.clicked.connect(lambda: self.tileClick(self.main_ui.b45, 37))
        self.main_ui.b46.clicked.connect(lambda: self.tileClick(self.main_ui.b46, 38))
        self.main_ui.b47.clicked.connect(lambda: self.tileClick(self.main_ui.b47, 39))
        self.main_ui.b50.clicked.connect(lambda: self.tileClick(self.main_ui.b50, 40))
        self.main_ui.b51.clicked.connect(lambda: self.tileClick(self.main_ui.b51, 41))
        self.main_ui.b52.clicked.connect(lambda: self.tileClick(self.main_ui.b52, 42))
        self.main_ui.b53.clicked.connect(lambda: self.tileClick(self.main_ui.b53, 43))
        self.main_ui.b54.clicked.connect(lambda: self.tileClick(self.main_ui.b54, 44))
        self.main_ui.b55.clicked.connect(lambda: self.tileClick(self.main_ui.b55, 45))
        self.main_ui.b56.clicked.connect(lambda: self.tileClick(self.main_ui.b56, 46))
        self.main_ui.b57.clicked.connect(lambda: self.tileClick(self.main_ui.b57, 47))
        self.main_ui.b60.clicked.connect(lambda: self.tileClick(self.main_ui.b60, 48))
        self.main_ui.b61.clicked.connect(lambda: self.tileClick(self.main_ui.b61, 49))
        self.main_ui.b62.clicked.connect(lambda: self.tileClick(self.main_ui.b62, 50))
        self.main_ui.b63.clicked.connect(lambda: self.tileClick(self.main_ui.b63, 51))
        self.main_ui.b64.clicked.connect(lambda: self.tileClick(self.main_ui.b64, 52))
        self.main_ui.b65.clicked.connect(lambda: self.tileClick(self.main_ui.b65, 53))
        self.main_ui.b66.clicked.connect(lambda: self.tileClick(self.main_ui.b66, 54))
        self.main_ui.b67.clicked.connect(lambda: self.tileClick(self.main_ui.b67, 55))
        self.main_ui.b70.clicked.connect(lambda: self.tileClick(self.main_ui.b70, 56))
        self.main_ui.b71.clicked.connect(lambda: self.tileClick(self.main_ui.b71, 57))
        self.main_ui.b72.clicked.connect(lambda: self.tileClick(self.main_ui.b72, 58))
        self.main_ui.b73.clicked.connect(lambda: self.tileClick(self.main_ui.b73, 59))
        self.main_ui.b74.clicked.connect(lambda: self.tileClick(self.main_ui.b74, 60))
        self.main_ui.b75.clicked.connect(lambda: self.tileClick(self.main_ui.b75, 61))
        self.main_ui.b76.clicked.connect(lambda: self.tileClick(self.main_ui.b76, 62))
        self.main_ui.b77.clicked.connect(lambda: self.tileClick(self.main_ui.b77, 63))

    def modeChange(self,event):
        self.modeNum+=1
        self.color = self.colors[self.modeNum % 4]
        self.main_ui.mode.setText(self.modes[self.modeNum % 4])

    def tileClick(self,button,graphNum):
        button.setStyleSheet('background-color: '+ self.color)
        self.objGraph[graphNum//8][graphNum%8] = self.modeNum%4

    def start(self):
        startCount = 0
        finishCount = 0
        obstacleList = []
        start = 0
        finish = 0
        for i in range(8):
            for j in range(8):
                if self.objGraph[i][j]==1:
                    startCount+=1
                    start = j+(i*8)
                elif self.objGraph[i][j]==3:
                    finishCount+=1
                    finish = j+(i*8)
                elif self.objGraph[i][j]==2:
                    obstacleList.append(j+(i*8))
        if not(startCount==1) or not(finishCount==1):
            print("Must have exactly 1 start and 1 finish. Please Fix.")
        else:
            print(obstacleList)
            for o in obstacleList:
                for i in range(64):
                    self.graph[o][i]=100
                    self.graph[i][o]=100
            self.djikstra = djikstrasThread(start,finish,self.main_ui,self.graph)


class djikstrasThread(Thread):
    def __init__(self,start,finish,main_ui,graph):
        super().__init__()
        self.graph = graph
        self.start = start
        self.finish = finish
        self.main_ui = main_ui
        self.yellows = []
        self.dist = [[100,str(i)] for i in range(64)] # distance, node
        self.prev = [None for i in range (64)]
        self.dist[start][0]=0 #set start node
        self.dist.sort() # sort queue to prioritize start node
        self.run()

    def run(self):
        print("beginning Djikstra's")
        while(len(self.dist)>0):
            current = self.dist[0]
            i = int(current[1])
            self.dist.remove(current)
            if(current[0] == 100):
                break
            #switch statement to highlight button as yellow
            if(i!=self.start and i != self.finish):
                self.yellows.append(i)
                self.colorTile(i, 'yellow')
            print(self.yellows)
            # end switch
            newDists = self.graph[int(current[1])]
            for j in range(len(newDists)):
                if (j == int(current[1])):
                    continue
                n = None
                for i in range(len(self.dist)):
                    if self.dist[i][1] == str(j): n = i
                if(n==None):
                    continue
                elif(newDists[j]+current[0]<self.dist[n][0]): # can't use the same index since dist keeps getting sorted
                    self.dist[n][0] = newDists[j] + current[0]
                    self.prev[j]= int(current[1])
                j+=1
            self.dist.sort()
            print(self.dist)
        # finishing loop
        if (len(self.dist)>0):
            for i in self.dist:
                if int(i[1]) == self.finish and i[0] ==100:
                    self.main_ui.mode.setText('No Path :(')
                    return
        for i in self.yellows:
            self.colorTile(i,"light grey")
        time.sleep(1)
        newYellows = []
        tmp = self.finish
        while(tmp!= self.start):
            tmp = self.prev[tmp]
            newYellows.append(tmp)
        newYellows.remove(self.start)
        for i in newYellows:
            self.colorTile(i, "yellow")
        self.main_ui.mode.setText("Path Complete")
        return

    def colorTile(self, tile, color):
        if tile ==0:
            self.main_ui.b00.setStyleSheet('background-color: ' + color)
        elif tile == 1:
            self.main_ui.b01.setStyleSheet('background-color: ' + color)
        elif tile == 2:
            self.main_ui.b02.setStyleSheet('background-color: ' + color)
        elif tile == 3:
            self.main_ui.b03.setStyleSheet('background-color: ' + color)
        elif tile == 4:
            self.main_ui.b04.setStyleSheet('background-color: ' + color)
        elif tile == 5:
            self.main_ui.b05.setStyleSheet('background-color: ' + color)
        elif tile == 6:
            self.main_ui.b06.setStyleSheet('background-color: ' + color)
        elif tile == 7:
            self.main_ui.b07.setStyleSheet('background-color: ' + color)
        elif tile == 8:
            self.main_ui.b10.setStyleSheet('background-color: ' + color)
        elif tile == 9:
            self.main_ui.b11.setStyleSheet('background-color: ' + color)
        elif tile == 10:
            self.main_ui.b12.setStyleSheet('background-color: ' + color)
        elif tile == 11:
            self.main_ui.b13.setStyleSheet('background-color: ' + color)
        elif tile == 12:
            self.main_ui.b14.setStyleSheet('background-color: ' + color)
        elif tile == 13:
            self.main_ui.b15.setStyleSheet('background-color: ' + color)
        elif tile == 14:
            self.main_ui.b16.setStyleSheet('background-color: ' + color)
        elif tile == 15:
            self.main_ui.b17.setStyleSheet('background-color: ' + color)
        elif tile == 16:
            self.main_ui.b20.setStyleSheet('background-color: ' + color)
        elif tile == 17:
            self.main_ui.b21.setStyleSheet('background-color: ' + color)
        elif tile == 18:
            self.main_ui.b22.setStyleSheet('background-color: ' + color)
        elif tile == 19:
            self.main_ui.b23.setStyleSheet('background-color: ' + color)
        elif tile == 20:
            self.main_ui.b24.setStyleSheet('background-color: ' + color)
        elif tile == 21:
            self.main_ui.b25.setStyleSheet('background-color: ' + color)
        elif tile == 22:
            self.main_ui.b26.setStyleSheet('background-color: ' + color)
        elif tile == 23:
            self.main_ui.b27.setStyleSheet('background-color: ' + color)
        elif tile == 24:
            self.main_ui.b30.setStyleSheet('background-color: ' + color)
        elif tile == 25:
            self.main_ui.b31.setStyleSheet('background-color: ' + color)
        elif tile == 26:
            self.main_ui.b32.setStyleSheet('background-color: ' + color)
        elif tile == 27:
            self.main_ui.b33.setStyleSheet('background-color: ' + color)
        elif tile == 28:
            self.main_ui.b34.setStyleSheet('background-color: ' + color)
        elif tile == 29:
            self.main_ui.b35.setStyleSheet('background-color: ' + color)
        elif tile == 30:
            self.main_ui.b36.setStyleSheet('background-color: ' + color)
        elif tile == 31:
            self.main_ui.b37.setStyleSheet('background-color: ' + color)
        elif tile == 32:
            self.main_ui.b40.setStyleSheet('background-color: ' + color)
        elif tile == 33:
            self.main_ui.b41.setStyleSheet('background-color: ' + color)
        elif tile == 34:
            self.main_ui.b42.setStyleSheet('background-color: ' + color)
        elif tile == 35:
            self.main_ui.b43.setStyleSheet('background-color: ' + color)
        elif tile == 36:
            self.main_ui.b44.setStyleSheet('background-color: ' + color)
        elif tile == 37:
            self.main_ui.b45.setStyleSheet('background-color: ' + color)
        elif tile == 38:
            self.main_ui.b46.setStyleSheet('background-color: ' + color)
        elif tile == 39:
            self.main_ui.b47.setStyleSheet('background-color: ' + color)
        elif tile == 40:
            self.main_ui.b50.setStyleSheet('background-color: ' + color)
        elif tile == 41:
            self.main_ui.b51.setStyleSheet('background-color: ' + color)
        elif tile == 42:
            self.main_ui.b52.setStyleSheet('background-color: ' + color)
        elif tile == 43:
            self.main_ui.b53.setStyleSheet('background-color: ' + color)
        elif tile == 44:
            self.main_ui.b54.setStyleSheet('background-color: ' + color)
        elif tile == 45:
            self.main_ui.b55.setStyleSheet('background-color: ' + color)
        elif tile == 46:
            self.main_ui.b56.setStyleSheet('background-color: ' + color)
        elif tile == 47:
            self.main_ui.b57.setStyleSheet('background-color: ' + color)
        elif tile == 48:
            self.main_ui.b60.setStyleSheet('background-color: ' + color)
        elif tile == 49:
            self.main_ui.b61.setStyleSheet('background-color: ' + color)
        elif tile == 50:
            self.main_ui.b62.setStyleSheet('background-color: ' + color)
        elif tile == 51:
            self.main_ui.b63.setStyleSheet('background-color: ' + color)
        elif tile == 52:
            self.main_ui.b64.setStyleSheet('background-color: ' + color)
        elif tile == 53:
            self.main_ui.b65.setStyleSheet('background-color: ' + color)
        elif tile == 54:
            self.main_ui.b66.setStyleSheet('background-color: ' + color)
        elif tile == 55:
            self.main_ui.b67.setStyleSheet('background-color: ' + color)
        elif tile == 56:
            self.main_ui.b70.setStyleSheet('background-color: ' + color)
        elif tile == 57:
            self.main_ui.b71.setStyleSheet('background-color: ' + color)
        elif tile == 58:
            self.main_ui.b72.setStyleSheet('background-color: ' + color)
        elif tile == 59:
            self.main_ui.b73.setStyleSheet('background-color: ' + color)
        elif tile == 60:
            self.main_ui.b74.setStyleSheet('background-color: ' + color)
        elif tile == 61:
            self.main_ui.b75.setStyleSheet('background-color: ' + color)
        elif tile == 62:
            self.main_ui.b76.setStyleSheet('background-color: ' + color)
        elif tile == 63:
            self.main_ui.b77.setStyleSheet('background-color: ' + color)



if __name__== '__main__':
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"]='1'
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())