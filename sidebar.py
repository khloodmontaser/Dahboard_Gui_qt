from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QTableWidgetItem, QPushButton, QWidget, QHBoxLayout, QHeaderView
from PySide6.QtWebEngineWidgets import QWebEngineView
from ui_sidebar import Ui_MainWindow
from PySide6.QtGui import QIcon, QFont
from PySide6.QtCore import QSize
import requests
from geopy.geocoders import Nominatim
import base64

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
        
        try:
            response = requests.get('https://gpsuni.azurewebsites.net/Data/GetCarGps')
            response.raise_for_status()
            car_gps_data = response.json()
            latitude1, longitude1 = car_gps_data['vlocation']
            geolocator = Nominatim(user_agent="my_geocoder")
            location1 = geolocator.reverse((latitude1, longitude1))
            location_name1 = location1.address if location1 else "Unknown location"

            # Call the new incident data API
            incident_response = requests.get('https://gpsuni.azurewebsites.net/data/GetIncidentData')
            incident_response.raise_for_status()
            incidents = incident_response.json()

            car_icon_base64 = self.image_to_base64('car.png')
            accident_icon_base64 = self.image_to_base64('accident.png')
            congestion_icon_base64 = self.image_to_base64('congestion.png')
            roadclosure_icon_base64 = self.image_to_base64('roadclosure.png')

            self.map_view = QWebEngineView()
            self.map_view.setHtml(f'''
                <html>
                    <head>
                        <link rel="stylesheet" href="https://unpkg.com/leaflet@1.7.1/dist/leaflet.css" />
                        <script src="https://unpkg.com/leaflet@1.7.1/dist/leaflet.js"></script>
                    </head>
                    <body>
                        <h1>Car GPS Locations</h1>
                        <div id="map" style="width: 100%; height: 100%;"></div>
                        <script>
                            var map = L.map('map').setView([{latitude1}, {longitude1}], 13);
                            
                            L.tileLayer('https://{{s}}.tile.openstreetmap.org/{{z}}/{{x}}/{{y}}.png', {{
                                maxZoom: 19
                            }}).addTo(map);

                            // Define custom icon
                            var carIcon = L.icon({{
                                iconUrl: 'data:image/png;base64,{car_icon_base64}',
                                iconSize: [50, 50], // Adjust the size to your preference
                                iconAnchor: [19, 38], // Adjust the anchor point
                                popupAnchor: [0, -38], // Adjust the popup anchor point
                            }});

                            var accidentIcon = L.icon({{
                            iconUrl: 'data:image/png;base64,{accident_icon_base64}',
                            iconSize: [50, 50],
                            iconAnchor: [19, 38],
                            popupAnchor: [0, -38],
                            }});

                            var congestionIcon = L.icon({{
                            iconUrl: 'data:image/png;base64,{congestion_icon_base64}',
                            iconSize: [50, 50],
                            iconAnchor: [19, 38],
                            popupAnchor: [0, -38],
                        }});
                        
                        var roadClosureIcon = L.icon({{
                            iconUrl: 'data:image/png;base64,{roadclosure_icon_base64}',
                            iconSize: [50, 50],
                            iconAnchor: [19, 38],
                            popupAnchor: [0, -38],
                        }});

                            
                            var marker1 = L.marker([{latitude1}, {longitude1}], {{icon: carIcon}}).addTo(map)
                                .bindPopup('<b>Location 1:</b> {location_name1}')
                                .openPopup();
                            
                            // Add incident markers
                            var incidents = {incidents};
                            incidents.forEach(function(incident) {{
                            var location = incident.location;
                            var type = incident.type;
                            var icon;
                            var popupText = '<b>Incident Type:</b> ' + type;

                            if (type !== 'unknown') {{
                                    if (type === 'accident') {{
                                        icon = accidentIcon;
                                    }} else if (type === 'congestionrate') {{
                                        icon = congestionIcon;
                                    }} else if (type === 'roadclosure') {{
                                        icon = roadClosureIcon;
                                    }}

                                    L.marker([location[0], location[1]], {{icon: icon}}).addTo(map)
                                        .bindPopup(popupText);
                                }}
                        }});
                        </script>
                    </body>
                </html>
            ''')
            self.Dashboard_page_layout.addWidget(self.map_view)
        except requests.RequestException as e:
            print(f"Failed to fetch car GPS data: {e}")


    
    
    def switch_reportsPage(self):
        self.stackedWidget.setCurrentIndex(2)

        try:
            # Fetch data from the API
            response = requests.get("https://gpsuni.azurewebsites.net/Data/GetIncidentData")
            response.raise_for_status()  # Raise an error for bad status codes
            data = response.json()

            # Clear existing table content
            self.tableWidget.setRowCount(0)
            geolocator = Nominatim(user_agent="my_geocoder")
            for row, item in enumerate(data):
                # Extract relevant information from the data dictionary
                key = item.get('key', '')
                location = item.get('location', [])
                incident_type = item.get('type', '')
                status_code = item.get('status')  # Assuming status is provided as 0, 1, or None
                status = "Pending" if status_code is None else ("Active" if status_code == 1 else "Rejected")

                # Deserialize RSUData object
                lat, lang = location

                location_name = ""
                try:
                    location_info = geolocator.reverse((lat, lang))
                    if location_info:
                        location_name = location_info.address
                except Exception as e:
                    print("Error getting location name:", e)

                # Formulate location name
                location_name = f"{incident_type.capitalize()} at {location_name}"

                # Add data to the table
                self.tableWidget.insertRow(row)
                self.tableWidget.setItem(row, 0, QTableWidgetItem(location_name))
                self.tableWidget.setItem(row, 1, QTableWidgetItem(status))

                button_container = QWidget()
                layout = QHBoxLayout(button_container)
                layout.setContentsMargins(0, 0, 0, 0)
                layout.setSpacing(0)

                # Create accept button
                accept_button = QPushButton()
                accept_button.setIcon(QIcon("tick-mark.png"))
                accept_button.setIconSize(QSize(32, 32))
                accept_button.clicked.connect(lambda checked, row=row, key=key: self.accept(row, key))
                layout.addWidget(accept_button)

                # Create reject button
                reject_button = QPushButton()
                reject_button.setIcon(QIcon("tack.png"))
                reject_button.setIconSize(QSize(32, 32))
                reject_button.clicked.connect(lambda checked, row=row, key=key: self.reject(row, key))
                layout.addWidget(reject_button)

                # Set button container as cell widget
                self.tableWidget.setCellWidget(row, 2, button_container)

            # Set table column widths
            self.tableWidget.setColumnWidth(0, 263)
            self.tableWidget.setColumnWidth(1, 260)
            self.tableWidget.setColumnWidth(2, 260)
            self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)

            self.tableWidget.verticalHeader().setDefaultSectionSize(40)

        except requests.RequestException as e:
            print(f"Failed to fetch data from API: {e}")

    def accept(self, row, key):
        url = f"https://gpsuni.azurewebsites.net/Data/accept?key={key}"
        try:
            response = requests.post(url)
            response.raise_for_status()  # Raise an error for bad status codes
            self.tableWidget.item(row, 1).setText("Active")
        except requests.RequestException as e:
            print(f"Failed to accept report: {e}")

    def reject(self, row, key):
        url = f"https://gpsuni.azurewebsites.net/Data/decline?key={key}"
        try:
            response = requests.post(url)
            response.raise_for_status()  # Raise an error for bad status codes
            self.tableWidget.item(row, 1).setText("Rejected")
        except requests.RequestException as e:
            print(f"Failed to reject report: {e}")

    # Function to convert image to base64
    def image_to_base64(self, image_path):
        with open(image_path, 'rb') as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')

 
if __name__ == "__main__":
    app = QApplication([])
    window = MySideBar()
    window.show()
    app.exec()
