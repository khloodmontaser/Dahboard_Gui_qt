# Emergency Vehicle Dashboard

This application acts as a dashboard for emergency vehicles, displaying real-time data retrieved from Firebase. The front end is developed using Python and PyQt6, while the back end utilizes .NET.

## Key Features

- **Realtime:** Data is synchronized in real-time to every connected client.
- **OFFLINE:** Accessible from client devices even when offline.
- **Scalable:** Scales across multiple databases.

## What is Firebase Database?

The Firebase Realtime Database is a cloud-hosted database where data is stored as JSON and synchronized in real-time to every connected client.

## Used Tools

1. **PYQT6**
2. **PYQT DESIGNER**

## Key Components

- **Interactive Map**
  - ![Interactive Map]([/home/lenovo/Pictures/Screenshots/Screenshot from 2024-06-28 12-32-28.png)](https://github.com/khloodmontaser/Dahboard_Gui_qt/blob/main/Screenshot%20from%202024-06-28%2012-32-28.png))
  
- **Reporting Page**
  - ![Reporting Page](path/to/pic2)

These components are utilized for storing report and car location data.

## Programming Languages

- **.NET**
- **PYTHON**

## Backend Technologies

- **Azure Functions:** Used for hosting backend APIs.
- **AZURE**

## Used Technologies

- **Google Maps Integration:**
  - Provides accurate and continuous location data for emergency vehicles, essential for navigating through congested cityscapes.
  - Visual Representation: Easy to interpret the position and movement of the vehicle.
  - Accessibility: Can be accessed from any device with internet connectivity.

## Incident Types

- ![Incident Type 1](path/to/pic3)
- ![Incident Type 2](path/to/pic4)
- ![Incident Type 3](path/to/pic5)
- ![Incident Type 4](path/to/pic6)

## Implementation of Google Maps GPS Module

- **Ublox NEO-7m GPS Module:** Integrated with the Raspberry Pi. Provides accurate and continuous location data for emergency vehicles, essential for navigating through congested cityscapes.
- **Whole Process of Google Maps Integration:**
  - The frontend periodically fetches GPS data from the Flask API.
  - Updates the Google Maps interface with new coordinates.
  - Real-time location tracking for end-users.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request if you have any ideas for improvements or new features.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
