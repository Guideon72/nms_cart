import sys
import ctrl
from PySide6 import QtGui
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QDialog,
    QGroupBox,
    QMainWindow,
    QPushButton,
    QLabel,
    QTabWidget,
    QTableWidget,
    QToolBar,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("NMS Bath Towel")
        self.setGeometry(100, 100, 800, 600)

        # Menu bar creation and configuration
        menu = self.menuBar()

        # File actions menu bar dropdown
        file_menu = menu.addAction("&File")

        # Edit actions menu bar dropdown
        edit_menu = menu.addAction("&Edit")

        # Window actions menu bar dropdown
        window_menu = menu.addMenu("&Window")
        quit_action = window_menu.addAction("Quit Application")
        quit_action.triggered.connect(self.quit)

        # Tool bar creation and configuration
        toolbar = QToolBar("Main window tool bar")
        galaxy_group = GalaxySelection("Choose Galaxy")
        print(galaxy_group.gal_combo.currentText())
        toolbar.addWidget(galaxy_group)
        self.addToolBar(toolbar)

        info_group = TabGroup()

        self.setCentralWidget(info_group)
        self.layout = QVBoxLayout()
        self.layout.addWidget(galaxy_group)

        self.setLayout(self.layout)

    def quit(self):
        print("Exited MainWindow via menu item")
        quit()


class GalaxySelection(QGroupBox):
    def __init__(self, title):
        super().__init__(title)
        self.title = title

        self.gal_combo = QComboBox(self)
        self.gal_combo.addItems(ctrl.get_galaxy_list())

        gs_layout = QVBoxLayout(self)
        gs_layout.addWidget(self.gal_combo)
        self.setLayout(gs_layout)


class TabGroup(QTabWidget):
    def __init__(self):
        super().__init__()
        shape = self.TabShape.Triangular
        self.setTabShape(shape)
        self.addTab(SystemTab(), "Current System")
        self.addTab(PlanetsTab(), "Planets")


class SystemTab(QWidget):
    def __init__(self):
        super().__init__()

        system_label = QLabel(ctrl.get_sys_data())
        system_layout = QVBoxLayout()
        system_layout.addWidget(system_label)
        self.setLayout(system_layout)


class PlanetsTab(QWidget):
    def __init__(self):
        super().__init__()

        planets_label = QLabel(ctrl.get_planet_data())
        planets_layout = QVBoxLayout()
        planets_layout.addWidget(planets_label)
        self.setLayout(planets_layout)


def main():
    nms_app = QApplication(sys.argv)
    mwindow = MainWindow()
    mwindow.show()
    nms_app.exec()


if __name__ == "__main__":
    main()
