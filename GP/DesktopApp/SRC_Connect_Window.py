from PyQt4.QtCore import  *
from PyQt4.QtGui import   *
from SRCC import Ui_Smart_Referee_Card
import socket
import sys

class main (QWidget , Ui_Smart_Referee_Card ) :
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)

        self.IP.setPlaceholderText('Enter Card IP Address')
        self.Port.setPlaceholderText('Enter Card Port Number')
        self.ConnectButton.clicked.connect(self.SocketConnect)

    def SocketConnect(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try :
            s.connect((self.IP.text(), int(self.Port.text())))
            Message = input("Enter your message\n")
            s.sendall(Message.encode('utf-8'))
            data = s.recv(1024)
            print(data.decode('utf-8'))
            s.close()
        except TimeoutError :
            self.ConnectionError.setGeometry(115, 170, 231, 21)
            self.ConnectionError.setText('Connection Failed')
            self.IP.setText('')
            self.Port.setText('')
        except OSError :
            self.ConnectionError.setGeometry(115, 170, 231, 21)
            self.ConnectionError.setText('Connection Failed')
            self.IP.setText('')
            self.Port.setText('')
        except ValueError :
            self.ConnectionError.setGeometry(115, 170 , 231 , 21)
            self.ConnectionError.setText('Enter Correct Info')
            self.IP.setText('')
            self.Port.setText('')



app = QApplication(sys.argv)
window = main()
window.show()
app.exec_()