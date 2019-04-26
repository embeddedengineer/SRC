from PyQt4.QtCore import  *
from PyQt4.QtGui import   *
from StackedSRCC import Ui_StackedWidget
import mysql.connector
from mysql.connector import Error
import socket
import sys
import threading
import time

class main (QStackedWidget , Ui_StackedWidget ) :

    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.SelectedSquad = []
        self.SubSquad = []
        self.SelectedSquadStr= []
        self.SubSquadStr = []
        self.TeamNames = []
        self.NoOfSubs = [ 3 , 3]
        self.TeamsNumber = 0
        self.setCurrentWidget(self.Main_Page)
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ConnectToDB()
        ReceivingThread = threading.Thread(target=self.ReceiveDataFromCard)
        ReceivingThread.start()

        # Buttons .
        self.AddToDB.clicked.connect(self.InsertSmartCardDataIntoDB)
        self.ConnectButton.clicked.connect(self.SocketConnect)
        self.Back.clicked.connect(self.ConnectMenuFromBack)
        self.TMButton.clicked.connect(self.ConnectMenu)
        self.BTOMM.clicked.connect(self.MainMenu)
        self.VLTButton.clicked.connect(self.ShowLeagueTable)
        self.ANSRCB.clicked.connect(self.MainMenu)
        self.FTIB.clicked.connect(self.MainMenu)
        self.ANTButton.clicked.connect(self.AddNewTeam)
        self.ANCButton.clicked.connect(self.AddNewSmartRefereeCard)
        self.Next.clicked.connect(self.GetAndSendTeamsName)
        self.LeagueBack.clicked.connect(self.MainMenu)
        self.BackToTeamsName.clicked.connect(self.TeamMenu)
        self.SetSquad.clicked.connect(self.GetAndSendTeamsSquad)
        self.SCButton.clicked.connect(self.SelectCard)
        self.BTOSC.clicked.connect(self.SelectCard)
        self.ShowIPPORT.clicked.connect(self.GetIPandPORT)
        self.EditIPPORT.clicked.connect(self.EditEnable)
        self.ApplyEdit.clicked.connect(self.EditIPandPORT)
        self.ConnectToCard.clicked.connect(self.ConnectingToCard)
        self.BTOMMSAC.clicked.connect(self.MainMenu)
        self.AddTeamToDB.clicked.connect(self.AddNewTeamToDB)
        self.SelectTeamButton.clicked.connect(self.GetTeamSquad)
        self.AButton.clicked.connect(self.MoveFromTeamListToMatchList)
        self.RButton.clicked.connect(self.MoveFromMatchListToTeamList)
        self.AddTeamToCardButton.clicked.connect(self.GetSelectedTeamSquad)
        self.ConnectToCardButton.clicked.connect(self.SendOutTeamInfoAndSquadToHW)
        self.MMButton.clicked.connect(self.DisplayMatchMode)
        self.SelectTeamSubButton.clicked.connect(self.DisplaySubInfo)
        self.ApplySubButton.clicked.connect(self.ApplySub)
        self.BackFromMMToMM.clicked.connect(self.MainMenu)

    def SocketConnect(self):
        try :
            self.s.connect((self.IP.text(), int(self.Port.text())))
            self.setCurrentWidget(self.TeamPage)
        except TimeoutError :
            self.ConnectionError.setGeometry(140, 230, 391, 81)
            self.ConnectionError.setStyleSheet('color: red ; font: 28pt "MS Shell Dlg 2";')
            self.ConnectionError.setText('Connection Failed')
            self.IP.setText('')
            self.Port.setText('')
        except OSError :
            self.ConnectionError.setGeometry(140, 230, 391, 81)
            self.ConnectionError.setStyleSheet('color: red ; font: 28pt "MS Shell Dlg 2";')
            self.ConnectionError.setText('Connection Failed')
            self.IP.setText('')
            self.Port.setText('')
        except ValueError :
            self.ConnectionError.setGeometry(140, 230, 391, 81)
            self.ConnectionError.setStyleSheet('color: red ; font: 28pt "MS Shell Dlg 2";')
            self.ConnectionError.setText('Enter Correct Info')
            self.IP.setText('')
            self.Port.setText('')
        except OverflowError :
            self.ConnectionError.setGeometry(140, 230, 391, 81)
            self.ConnectionError.setStyleSheet('color: red ; font: 28pt "MS Shell Dlg 2";')
            self.ConnectionError.setText('Enter Correct Info')
            self.IP.setText('')
            self.Port.setText('')

    def GetAndSendTeamsName(self):
        Message = 'ST,'
        Message = Message + self.FTNL.text() +',' +  self.STNL.text()
        self.s.sendall(Message.encode('utf-8'))
        self.setCurrentWidget(self.Squad_Page)

    def ConnectMenuFromBack(self):
        self.s.close()
        self.setCurrentWidget(self.ConnectPage)
        self.IP.setText('')
        self.Port.setText('')

    def ConnectMenu(self):
        self.setCurrentWidget(self.ConnectPage)
        self.IP.setText('')
        self.Port.setText('')

    def ShowLeagueTable(self):
        self.setCurrentWidget(self.LeagueTablePage)
        # Get Full league data from DB.

    def SelectCard(self):
        self.setCurrentWidget(self.CardSelectPage)
        self.AddCardsNameIntoComboBox()

    def MainMenu(self):
        self.setCurrentWidget(self.Main_Page)

    def GetAndSendTeamsSquad(self):
        Message = 'SS,'
        Message = Message + self.P1T1.text() + ',' + self.P2T1.text() + ',' + self.P3T1.text() + ',' + self.P4T1.text() + ',' + self.P5T1.text() + ',' + self.P6T1.text() + ',' + self.P7T1.text() + ',' + self.P8T1.text() + ',' + self.P9T1.text() + ',' + self.P10T1.text() + ',' + self.P11T1.text()
        Message = Message + ',' + self.P1T2.text() + ',' + self.P2T2.text() + ',' + self.P3T2.text() + ',' + self.P4T2.text() + ',' + self.P5T2.text() + ',' + self.P6T2.text() + ',' + self.P7T2.text() + ',' + self.P8T2.text() + ',' + self.P9T2.text() + ',' + self.P10T2.text() + ',' + self.P11T2.text()
        self.s.sendall(Message.encode('utf-8'))
        self.s.close()
        self.MainMenu()

    def AddNewTeam(self):
        self.setCurrentWidget(self.FTIPage)

    def AddNewSmartRefereeCard(self):
        self.CIP.setText('')
        self.CP.setText('')
        self.RN.setText('')
        self.setCurrentWidget(self.ANSRC)

    def TeamMenu(self):
        self.setCurrentWidget(self.TeamPage)
        self.FTNL.setText('')
        self.STNL.setText('')

    def ConnectToDB(self):
        try:
            self.connection = mysql.connector.connect(host='localhost',
                                                 database='src',
                                                 user='root',
                                                 password='')
        except Error :
            pass

    def InsertSmartCardDataIntoDB(self):
        IP = self.CIP.text()
        PORT = self.CP.text()
        NAME = self.RN.text()
        InsertQuery = """INSERT INTO `smartcard` (`IP`, `PORT`, `NAME`) VALUES (%s,%s,%s);"""
        cursor = self.connection.cursor()
        result = cursor.execute(InsertQuery,(IP,PORT,NAME))
        self.connection.commit()

    def GetCardsNameFromDB(self):
        SplitedNames = []
        cursor = self.connection.cursor()
        cursor.execute("SELECT NAME FROM smartcard")
        Names = cursor.fetchall()
        for Name in Names :
          SplitedNames.append(''.join(Name))
        return SplitedNames

    def AddCardsNameIntoComboBox(self):
        self.NamesComboBox.clear()
        self.NamesComboBox.addItems(self.GetCardsNameFromDB())

    def GetIPandPORT(self):
        self.SelectedCardName = self.NamesComboBox.currentText()
        cursor = self.connection.cursor()
        cursor.execute('SELECT IP , PORT FROM smartcard WHERE NAME = %s',(self.SelectedCardName, ))
        IPandPORT = cursor.fetchall()
        self.IP = IPandPORT[0][0]
        self.PORT = IPandPORT[0][1]
        self.CardIP.setText(self.IP)
        self.CardPort.setText(self.PORT)

    def EditEnable(self):
        self.CardIP.setEnabled(True)
        self.CardPort.setEnabled(True)

    def EditIPandPORT(self):
        NewIP = self.CardIP.text()
        NewPORT = self.CardPort.text()
        cursor = self.connection.cursor()
        if NewIP != self.IP :
            cursor.execute('UPDATE smartcard SET IP = %s WHERE smartcard.NAME = %s', (NewIP,self.SelectedCardName,))
        if NewPORT != self.PORT :
            cursor.execute('UPDATE smartcard SET PORT = %s WHERE smartcard.NAME = %s', (NewPORT, self.SelectedCardName,))
        self.connection.commit()
        self.CardIP.setEnabled(False)
        self.CardPort.setEnabled(False)

    def ConnectingToCard(self):
        cursor = self.connection.cursor()
        cursor.execute('SELECT IP , PORT FROM smartcard WHERE NAME = %s', (self.SelectedCardName,))
        IPandPORT = cursor.fetchall()
        self.ShowTeamsFromDB()
        self.SelectTeamPageClean()
        self.setCurrentWidget(self.SelectTeam)
        self.s.connect((IPandPORT[0][0], int(IPandPORT[0][1])))

    def SelectTeamPageClean(self):
        self.TeamPlayerList.clear()
        self.MatchPlayerList.clear()


    def AddNewTeamToDB(self):
        PlayerNumbers = [self.P1NO , self.P2NO , self.P3NO , self.P4NO , self.P5NO , self.P6NO , self.P7NO , self.P8NO , self.P9NO , self.P10NO , self.P11NO , self.P12NO , self.P13NO , self.P14NO , self.P15NO]
        PlayerNames   = [self.P1NA , self.P2NA , self.P3NA , self.P4NA , self.P5NA , self.P6NA , self.P7NA , self.P8NA ,self.P9NA , self.P10NA , self.P11NA , self.P12NA , self.P13NA , self.P14NA , self.P15NA]
        cursor = self.connection.cursor()
        NewTeamName = self.TeamName.text()
        for i in range(15) :
            cursor.execute('INSERT INTO team ( TeamName , PlayerNum , PlayerName ) VALUES (%s , %s , %s)', (NewTeamName, PlayerNumbers[i].text() , PlayerNames[i].text()  , ))
            self.connection.commit()
        self.MainMenu()

    def ShowTeamsFromDB(self):
        cursor = self.connection.cursor()
        cursor.execute('SELECT DISTINCT TeamName from team')
        AvailableTeams = cursor.fetchall()
        self.TeamNamesCombo.clear()
        for Team in AvailableTeams :
            self.TeamNamesCombo.addItem(Team[0])

    def GetTeamSquad(self):
        self.TeamsNumber += 1
        TeamName = self.TeamNamesCombo.currentText()
        self.TeamNames.append(TeamName)
        cursor = self.connection.cursor()
        cursor.execute('SELECT PlayerName , PlayerNum from team where TeamName like %s' , (TeamName ,))
        Squad = cursor.fetchall()
        self.SelectTeamPageClean()

        for Players in Squad :
            PlayerInfo = str(Players[1]) + " - " + Players[0]
            self.TeamPlayerList.addItem(PlayerInfo)

        if self.TeamsNumber == 2 :
            Message = 'ST'
            for index in self.TeamNames:
                Message = Message + ',' + index
            self.s.sendall(Message.encode('utf-8'))

    def MoveFromTeamListToMatchList(self):
        Player = self.TeamPlayerList.currentItem().text()
        self.MatchPlayerList.addItem(Player)
        self.TeamPlayerList.takeItem(self.TeamPlayerList.currentRow())

    def MoveFromMatchListToTeamList(self):
        Player = self.MatchPlayerList.currentItem().text()
        self.TeamPlayerList.addItem(Player)
        self.MatchPlayerList.takeItem(self.MatchPlayerList.currentRow())

    def GetSelectedTeamSquad(self):
        for index in range(self.MatchPlayerList.count()):
            self.SelectedSquad.append(self.MatchPlayerList.item(index).text())
            self.SelectedSquadStr.append(self.MatchPlayerList.item(index).text()[: self.MatchPlayerList.item(index).text().index(" - ")])
        for index in range(self.TeamPlayerList.count()):
            self.SubSquad.append(self.TeamPlayerList.item(index).text())
            self.SubSquadStr.append(self.TeamPlayerList.item(index).text()[: self.TeamPlayerList.item(index).text().index(" - ")])
        self.SelectTeamLabel.setText("Select Team 2")

    def SendOutTeamInfoAndSquadToHW(self):
        Message = 'SS'
        for index in self.SelectedSquadStr :
            Message = Message +  ',' + index
        self.s.sendall(Message.encode('utf-8'))
        self.MainMenu()

    def DisplayMatchMode(self):
        self.setCurrentWidget(self.MatchMode)
        self.TeamNamesSubCombo.addItems(self.TeamNames)

    def DisplaySubInfo(self):
        self.POutCombo.clear()
        self.PInCombo.clear()
        SelectedTeam = self.TeamNamesSubCombo.currentText()
        if SelectedTeam == self.TeamNames[0] :
            self.SubNum.setText(str(self.NoOfSubs[0]))
            for i in range (0 , int(self.SelectedSquad.__len__() / 2)) :
                self.POutCombo.addItem(self.SelectedSquad[i])
            for j in range (0 , int(self.SubSquad.__len__() / 2)) :
                self.PInCombo.addItem(self.SubSquad[j])

        elif SelectedTeam == self.TeamNames[1]:
            self.SubNum.setText(str(self.NoOfSubs[1]))
            for x in range(int(self.SelectedSquad.__len__() / 2 ), int(self.SelectedSquad.__len__())):
                self.POutCombo.addItem(self.SelectedSquad[x])
            for y in range(int(self.SubSquad.__len__() / 2) , int(self.SubSquad.__len__())):
                self.PInCombo.addItem(self.SubSquad[y])

    def ApplySub(self):
        Pout = self.POutCombo.currentText()
        Pin  = self.PInCombo.currentText()
        SelectedTeam = self.TeamNamesSubCombo.currentText()
        Message = 'CP' + ',' + SelectedTeam + ',' + Pout[:Pout.index(" - ")] + ',' + Pin[:Pin.index(" - ")]
        self.s.sendall(Message.encode('utf-8'))
        self.PInCombo.removeItem(self.PInCombo.findText(Pin))
        if SelectedTeam == self.TeamNames[0]:
            self.NoOfSubs[0] -= 1
            self.SubNum.setText(str(self.NoOfSubs[0]))
            index = self.POutCombo.findText(Pout)
            self.POutCombo.removeItem(index)
            self.POutCombo.insertItem(index , Pin)


        elif SelectedTeam == self.TeamNames[1]:
            self.NoOfSubs[1] -= 1
            self.SubNum.setText(str(self.NoOfSubs[1]))
            index = self.POutCombo.findText(Pout)
            self.POutCombo.removeItem(index)
            self.POutCombo.insertItem(index, Pin)

        self.SelectedSquad[self.SelectedSquad.index(Pout)] = Pin
        self.SubSquad.remove(Pin)

    def ReceiveDataFromCard(self):
        while True:
            try:
                DataFromCard = self.s.recv(1024)
                if DataFromCard :
                    DecodedData = DataFromCard.decode('utf-8')
                    cursor = self.connection.cursor()

                    if DecodedData[:DecodedData.index(',')] == 'SA' :
                        ListedData = DecodedData.split(',')
                        cursor.execute('SELECT PlayerName from team where TeamName like %s and PlayerNum like %s', (ListedData[1],ListedData[2] ,))
                        PlayerName = cursor.fetchall()

                        if ListedData[3] == 'y' :
                            DisplayText = ListedData[1] + " :\n" + "Yellow card to " + PlayerName[0][0]
                            cursor.execute(
                                'INSERT INTO league ( TeamNo1 , TeamNo2 , ScoredTeam ,PlayerNumber , YellowCard ) VALUES (%s , %s , %s , %s , %s)',
                                (self.TeamNames[0], self.TeamNames[1], ListedData[1], ListedData[2], 1,))

                        elif ListedData[3] == 'r' :
                            DisplayText = ListedData[1] + " :\n" + "Red card to " + PlayerName[0][0]
                            cursor.execute(
                                'INSERT INTO league ( TeamNo1 , TeamNo2 , ScoredTeam ,PlayerNumber , RedCard ) VALUES (%s , %s , %s , %s , %s)',
                                (self.TeamNames[0], self.TeamNames[1], ListedData[1], ListedData[2], 1,))


                        elif ListedData[3] == 'g' :
                            DisplayText = ListedData[1] + " :\n" +  PlayerName[0][0]  + " Scored a goal"
                            cursor.execute(
                                'INSERT INTO league ( TeamNo1 , TeamNo2 , ScoredTeam ,PlayerNumber , Goal ) VALUES (%s , %s , %s , %s , %s)',
                                (self.TeamNames[0], self.TeamNames[1], ListedData[1], ListedData[2], 1,))

                        self.MatchNotification.append(DisplayText)
                        self.connection.commit()


            except:
                pass


app = QApplication(sys.argv)
window = main()
window.show()
app.exec_()
