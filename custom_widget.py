from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QScrollArea, QSlider
from PyQt5.QtCore import Qt

class CustomWidget(QWidget):
    def __init__ (self):
        super().__init__()
        self.parent_HLayout = QHBoxLayout()
        scroll = QScrollArea()
        self.hscrollbar = scroll.horizontalScrollBar()
        #self.hscrollbar.setSingleStep(10)
        self.hscrollbar.setTracking(True)
        self.hscrollbar.valueChanged.connect(self.printer)
        self.address_hlayout = QHBoxLayout()
        scroll.setLayout(self.address_hlayout)
        self.orderNoLabel, self.nameLabel, self.addressLabel, self.contactNoLabel = QLabel(), QLabel(), QLabel(), QLabel()
        self.orderNoLabel.setContentsMargins(4, 3, 2, 3)
        self.nameLabel.setContentsMargins(0, 3, 2, 3)
        self.addressLabel.setContentsMargins(0, 0, 0, 0)
        self.contactNoLabel.setContentsMargins(0, 3, 2, 3)
        self.addressLabel.setFixedHeight(20)
        scroll.setWidget(self.addressLabel)
        scroll.setWidgetResizable(True)
        self.parent_HLayout.addWidget(self.orderNoLabel, 0)
        self.parent_HLayout.addWidget(self.nameLabel, 1)
        self.parent_HLayout.addWidget(scroll, 2)
        self.parent_HLayout.addWidget(self.contactNoLabel, 0)
        self.parent_HLayout.setSpacing(0)
        self.setLayout(self.parent_HLayout)
        # setStyleSheet
        self.orderNoLabel.setStyleSheet('''
            background: #e8e4e1;
            color: #1b1b2f;
            padding-right: 1.5px;
        ''')
        self.nameLabel.setStyleSheet('''QLabel 
           {background: white;
            color: black;}
        ''' '''QLabel:hover { background: blue; color: white; }''')
        self.addressLabel.setStyleSheet('''
            background: white;
            color: black;
        ''')
        self.contactNoLabel.setStyleSheet('''
            background: white;
            color: black;
        ''')
        #self.setStyleSheet("QWidget {background: white; color: black;}" "QWidget.QLabel:hover { background: blue; color: white; }")
        self.parent_HLayout.setContentsMargins(0, 0, 0, 0)

    def setOrderNo(self, number):
        number += 1
        if len(str(number)) > 1:
            self.orderNoLabel.setText(str(number))
        else:
            self.orderNoLabel.setText('0'+str(number))

    def setNameLabel(self, text):
        self.nameLabel.setText(text)

    def setAddressLabel(self, text):
        self.addressLabel.setText(text)

    def setDateLabel(self, text):
        self.contactNoLabel.setText(str(text))

    def printer(self):
        print(self.hscrollbar.value())

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.LeftButton:
            self.hscrollbar.setValue(event.globalPos().x())
            print(self.hscrollbar.value())
            #self.addressLabel.move(event.globalPos().x(), 0)

    #def dropEvent(self, event):
        #pos = self.addressLabel.mapFrom(self, event.pos())
        #print(pos)