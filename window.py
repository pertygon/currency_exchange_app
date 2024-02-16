from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QHBoxLayout,
    QVBoxLayout, QComboBox, QLineEdit, QPushButton,
    QMessageBox
)
import json
import scrap
#Pass values from inputs to function and show exchange rate in label
def show_result():
    pam1 = from_combobox.currentText()
    pam2 = into_combobox.currentText()
    pam3 = amout_input.text()
    try:
        pam3 = int(pam3)
    except:
        wrg_input.exec()
        return 0
    if pam3 == '' or pam3 <= 0:
        wrg_input.exec()
        return 0
    val = scrap.currency(pam1,pam2,str(pam3))
    to_switch.setText(val)
#Load 
f = open('currency-format.json',encoding = 'utf-8',errors = 'ignore')
data = json.load(f)
data = data.keys()
#Create app
app = QApplication([])
window = QWidget()
#Error message
wrg_input = QMessageBox()
wrg_input.setWindowTitle('Wrong input')
wrg_input.setText('Wrong type or value below or equal 0')
#Set widgets
window.setWindowTitle("Currency exchange")
from_label = QLabel('From currency')
from_combobox = QComboBox()
from_combobox.addItems(data)
into_label = QLabel('Into Currency')
into_combobox = QComboBox()
into_combobox.addItems(data)
amout_label = QLabel('Desired Amount')
amout_input = QLineEdit()
submit = QPushButton('Calculate rate')
text_label = QLabel('Calculated convertion:')
to_switch = QLabel()
#Set layouts
main_lay = QVBoxLayout()
row1 = QHBoxLayout()
col1 = QVBoxLayout()
col2 = QVBoxLayout()
col3 = QVBoxLayout()

row2 = QHBoxLayout()
row3 = QHBoxLayout()
col31 = QVBoxLayout()
col32 = QVBoxLayout()
col1.addWidget(from_label)
col1.addWidget(from_combobox)

col2.addWidget(into_label)
col2.addWidget(into_combobox)

col3.addWidget(amout_label)
col3.addWidget(amout_input)
               
row1.addLayout(col1)
row1.addLayout(col2)
row1.addLayout(col3)

row2.addWidget(submit)

col31.addWidget(text_label)
col32.addWidget(to_switch)
row3.addLayout(col31)
row3.addLayout(col32)

main_lay.addLayout(row1)
main_lay.addLayout(row2)
main_lay.addLayout(row3)

window.setLayout(main_lay)

submit.clicked.connect(show_result)

window.show()
app.exec()

