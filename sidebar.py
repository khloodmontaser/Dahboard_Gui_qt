from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QTableWidgetItem, QPushButton, QWidget, QHBoxLayout, QHeaderView
from PySide6.QtWebEngineWidgets import QWebEngineView
from ui_sidebar import Ui_MainWindow
from PySide6.QtGui import QIcon, QFont
from PySide6.QtCore import QSize

class MySideBar(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("My Menu")

        self.icon_name_widget.setHidden(True)

        self.dashboard_1.clicked.connect(self.switch_to_dashboardPage)
        self.dashboard_2.clicked.connect(self.switch_to_dashboardPage)

        self.reports_1.clicked.connect(self.switch_reportsPage)
        self.reports_2.clicked.connect(self.switch_reportsPage)

        self.map_view = None
        self.Dashboard_page_layout = QVBoxLayout()
        self.Dashboard_page.setLayout(self.Dashboard_page_layout)

        self.switch_to_dashboardPage()

    def switch_to_dashboardPage(self):
        self.stackedWidget.setCurrentIndex(0)

        if self.map_view:
            self.Dashboard_page_layout.removeWidget(self.map_view)
            self.map_view.deleteLater()
        
        self.map_view = QWebEngineView()
        self.map_view.setHtml('<iframe width="100%" height="100%" frameborder="0" style="border:0" src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3473732.303701674!2d29.934953267246824!3d26.756331252976!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x145838b602486847%3A0x6cd6e77be30f8f1!2sEgypt!5e0!3m2!1sen!2sus!4v1620766506254!5m2!1sen!2sus"></iframe>')
        self.Dashboard_page_layout.addWidget(self.map_view)
    
    
    def switch_reportsPage(self):
        self.stackedWidget.setCurrentIndex(2)

        # Dummy data for the table - data
        dummy_data = [
            {"Info": "Accident in makram ebeid", "Status": "Pending", "Action": None},
            {"Info": "Accident in Abas elakad", "Status": "Pending", "Action": None},
            {"Info": "Accident in Ahmed fakhry", "Status": "Pending", "Action": None},
        ]

        # Clear existing table content
        self.tableWidget.setRowCount(0)

        for row, data in enumerate(dummy_data):
            self.tableWidget.insertRow(row)
            for column, (key, value) in enumerate(data.items()):
                if key == "Action" and value is None:

                    button_container = QWidget()
                    layout = QHBoxLayout(button_container)
                    layout.setContentsMargins(0, 0, 0, 0)
                    layout.setSpacing(0)


                    button1 = QPushButton()
                    button1.setIcon(QIcon("/home/lenovo/Desktop/Dashboard/tick-mark.png"))
                    button1.setIconSize(QSize(32, 32))  # Increase icon size
                    button1.clicked.connect(lambda checked, row=row: self.accept_report(row))
                    layout.addWidget(button1)

                    button2 = QPushButton()
                    button2.setIcon(QIcon("/home/lenovo/Desktop/Dashboard/tack.png"))
                    button2.setIconSize(QSize(32, 32)) 
                    button2.clicked.connect(lambda checked, row=row: self.reject_report(row))
                    layout.addWidget(button2)

                    self.tableWidget.setCellWidget(row, column, button_container)
                else:
                    item = QTableWidgetItem(value)
                    item.setFont(QFont("Arial", 12)) 
                    self.tableWidget.setItem(row, column, item)
                    
                    
######################################## table width ################################################################
        self.tableWidget.setColumnWidth(0, 263)
        self.tableWidget.setColumnWidth(1, 260)
        self.tableWidget.setColumnWidth(2, 260)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)

        self.tableWidget.verticalHeader().setDefaultSectionSize(40) 

    def accept_report(self, row):
        item = self.tableWidget.item(row, 1) 
        if item is not None and item.text() == "Pending":
            item.setText("Accepted")


    def reject_report(self, row):
        item = self.tableWidget.item(row, 1) 
        if item is not None and item.text() == "Pending":
            item.setText("Rejected")
 
if __name__ == "__main__":
    app = QApplication([])
    window = MySideBar()
    window.show()
    app.exec()
