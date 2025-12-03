########################################################################
## QT GUI BY SPINN TV(YOUTUBE)
########################################################################

########################################################################
## IMPORTS
########################################################################
import os
import sys
########################################################################
# IMPORT GUI FILE
from src.ui_QCustomQMainWindow import *
########################################################################

########################################################################
# IMPORT Custom widgets
from Custom_Widgets import *
from Custom_Widgets.QAppSettings import QAppSettings
########################################################################

from PySide6.QtCore import QTimer
import datetime
########################################################################
## MAIN WINDOW CLASS
########################################################################
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_CustomMainWindow()
        self.ui.setupUi(self)

        ########################################################################
        # APPLY JSON STYLESHEET
        ########################################################################
        # self = QMainWindow class
        # self.ui = Ui_CustomMainWindow / user interface class
        #Use this if you only have one json file named "style.json" inside the root directory, "json" directory or "jsonstyles" folder.
        # loadJsonStyle(self, self.ui) 

        # Use this to specify your json file(s) path/name
        loadJsonStyle(self, self.ui, jsonFiles = {
            "json-styles/style.json"
            }) 

        ########################################################################

        #######################################################################
        # SHOW WINDOW
        #######################################################################
        self.show() 

        ########################################################################
        # UPDATE APP SETTINGS LOADED FROM JSON STYLESHEET 
        # ITS IMPORTANT TO RUN THIS AFTER SHOWING THE WINDOW
        # THIS PROCESS WILL RUN ON A SEPARATE THREAD WHEN GENERATING NEW ICONS
        # TO PREVENT THE WINDOW FROM BEING UNRESPONSIVE
        ########################################################################
        # self = QMainWindow class
        QAppSettings.updateAppSettings(self)

        ########################################################################
        # To apply a new theme from your JSon file
        # Import custom wdgets theme engine
        # from Custom_Widgets.QCustomTheme import QCustomTheme

        # init theme engine
        # self.themeEngine = QCustomTheme()

        # check current theme name
        # print(self.themeEngine.theme)
        
        # set the theme name from json file
        # self.themeEngine.theme = "Default-theme" #or Light, Dark or any custom theme name from the json file
        # self.themeEngine.theme = "Dark" 
        # self.themeEngine.theme = "Light" 
        ########################################################################

        # Get main body component container(component is the loaded external ui file)
        component = self.ui.mainBodyComponentContainer.component
        # if component:
        #     # LEFT
        #     component.leftSideDrawerBtn.clicked.connect(
        #         lambda: print("Left Hamburger button clicked — displaying left panel...")
        #     )

        # create blinking cursor
        self._cursor_visible = True
        self._log_buffer = ""  # store logs separately
        self._cursor_timer = QTimer(self)
        self._cursor_timer.timeout.connect(self._toggle_cursor)
        self._cursor_timer.start(500)

        self.connect_sidebar_buttons()
        self.connect_drawer_buttons()

    def _toggle_cursor(self):
        console = self.ui.mainBodyComponentContainer.component.consoleOutput
        # Just add cursor to the visual content, not buffer
        if self._cursor_visible:
            console.setPlainText(self._log_buffer + "█")
        else:
            console.setPlainText(self._log_buffer + " ")
        self._cursor_visible = not self._cursor_visible
        # scroll to bottom
        console.verticalScrollBar().setValue(console.verticalScrollBar().maximum())

    # append text to console
    def log_to_console(self, message: str):
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        formatted_msg = f"\n{'-'*70}\n[{timestamp}] {message}\n{'-'*70}\n"
        # update buffer
        self._log_buffer += formatted_msg
        # update console immediately (cursor on)
        self.ui.mainBodyComponentContainer.component.consoleOutput.setPlainText(self._log_buffer + "█")
        # scroll
        console = self.ui.mainBodyComponentContainer.component.consoleOutput
        console.verticalScrollBar().setValue(console.verticalScrollBar().maximum())

    def connect_sidebar_buttons(self):
        """Connect all sidebar buttons to log messages"""
        component = self.ui.leftSidebarComponentContainer.component
       
        if component:        
            # Access sidebar buttons directly from the component
            # Menu toggle button
            component.menuBtn.clicked.connect(
                lambda: self.log_to_console("Sidebar: Menu toggle button clicked")
            )
            
            # Main navigation buttons
            component.btnHome.clicked.connect(
                lambda: self.log_to_console("Sidebar: Home button clicked")
            )
            component.btnMessages.clicked.connect(
                lambda: self.log_to_console("Sidebar: Messages button clicked")
            )
            component.btnIntegration.clicked.connect(
                lambda: self.log_to_console("Sidebar: Integration button clicked")
            )
            component.btnFinance.clicked.connect(
                lambda: self.log_to_console("Sidebar: Finance button clicked")
            )
            component.btnThreads.clicked.connect(
                lambda: self.log_to_console("Sidebar: Threads button clicked")
            )
            
            # Bottom section buttons
            component.btnContacts.clicked.connect(
                lambda: self.log_to_console("Sidebar: Contacts button clicked")
            )
            component.btnExplore.clicked.connect(
                lambda: self.log_to_console("Sidebar: Explore button clicked")
            )
            component.btnSettings.clicked.connect(
                lambda: self.log_to_console("Sidebar: Settings button clicked")
            )
            component.btnHelp.clicked.connect(
                lambda: self.log_to_console("Sidebar: Help button clicked")
            )

        # Access right side drawer the same way.............

    def connect_drawer_buttons(self):
        """Connect all drawer buttons to log messages"""        
        # Get hamburger menus
        # Different access from other components
        left_menu = self.getHamburgerMenu("leftHamburgerMenu")
        right_menu = self.getHamburgerMenu("rightHamburgerMenu") 
        top_menu = self.getHamburgerMenu("topHamburgerMenu")
        bottom_menu = self.getHamburgerMenu("bottomHamburgerMenu")
        
        if left_menu:
            # Profile section
            left_menu.getWidget("profileBtn").clicked.connect(
                lambda: self.log_to_console("Left Drawer: Profile button clicked")
            )
            
            # Navigation buttons
            left_menu.getWidget("dashboardBtn").clicked.connect(
                lambda: self.log_to_console("Left Drawer: Dashboard button clicked")
            )
            left_menu.getWidget("messagesBtn").clicked.connect(
                lambda: self.log_to_console("Left Drawer: Messages button clicked")
            )
            left_menu.getWidget("filesBtn").clicked.connect(
                lambda: self.log_to_console("Left Drawer: Files button clicked")
            )
            left_menu.getWidget("calendarBtn").clicked.connect(
                lambda: self.log_to_console("Left Drawer: Calendar button clicked")
            )
            left_menu.getWidget("analyticsBtn").clicked.connect(
                lambda: self.log_to_console("Left Drawer: Analytics button clicked")
            )
            
            # Tools section
            left_menu.getWidget("settingsBtn").clicked.connect(
                lambda: self.log_to_console("Left Drawer: Settings button clicked")
            )
            left_menu.getWidget("notificationsBtn").clicked.connect(
                lambda: self.log_to_console("Left Drawer: Notifications button clicked")
            )
            left_menu.getWidget("helpBtn").clicked.connect(
                lambda: self.log_to_console("Left Drawer: Help & Support button clicked")
            )
            
            # Footer section
            left_menu.getWidget("themeBtn").clicked.connect(
                lambda: self.log_to_console("Left Drawer: Theme button clicked")
            )
            left_menu.getWidget("hideHamburgerBtn").clicked.connect(
                lambda: self.log_to_console("Left Drawer: Close button clicked")
            )
        
        if right_menu:
            # Action buttons
            right_menu.getWidget("shareBtn").clicked.connect(
                lambda: self.log_to_console("Right Drawer: Share button clicked")
            )
            right_menu.getWidget("tagBtn").clicked.connect(
                lambda: self.log_to_console("Right Drawer: Add Tag button clicked")
            )
            right_menu.getWidget("infoBtn").clicked.connect(
                lambda: self.log_to_console("Right Drawer: View Info button clicked")
            )
            right_menu.getWidget("downloadBtn").clicked.connect(
                lambda: self.log_to_console("Right Drawer: Download button clicked")
            )
            right_menu.getWidget("deleteBtn").clicked.connect(
                lambda: self.log_to_console("Right Drawer: Delete button clicked")
            )
        
        if top_menu:
            # Quick action buttons
            top_menu.getWidget("wifiBtn").clicked.connect(
                lambda: self.log_to_console("Top Drawer: WiFi button clicked")
            )
            top_menu.getWidget("bluetoothBtn").clicked.connect(
                lambda: self.log_to_console("Top Drawer: Bluetooth button clicked")
            )
            top_menu.getWidget("flashlightBtn").clicked.connect(
                lambda: self.log_to_console("Top Drawer: Flashlight button clicked")
            )
            top_menu.getWidget("moonBtn").clicked.connect(
                lambda: self.log_to_console("Top Drawer: DND button clicked")
            )
            top_menu.getWidget("brightnessBtn").clicked.connect(
                lambda: self.log_to_console("Top Drawer: Brightness button clicked")
            )
            
            # Clear button
            top_menu.getWidget("clearAllBtn").clicked.connect(
                lambda: self.log_to_console("Top Drawer: Clear All Notifications button clicked")
            )
        
        if bottom_menu:
            # Player control buttons
            bottom_menu.getWidget("shuffleBtn").clicked.connect(
                lambda: self.log_to_console("Bottom Drawer: Shuffle button clicked")
            )
            bottom_menu.getWidget("prevBtn").clicked.connect(
                lambda: self.log_to_console("Bottom Drawer: Previous button clicked")
            )
            bottom_menu.getWidget("playBtn").clicked.connect(
                lambda: self.log_to_console("Bottom Drawer: Play button clicked")
            )
            bottom_menu.getWidget("nextBtn").clicked.connect(
                lambda: self.log_to_console("Bottom Drawer: Next button clicked")
            )
            bottom_menu.getWidget("repeatBtn").clicked.connect(
                lambda: self.log_to_console("Bottom Drawer: Repeat button clicked")
            )
            
            # Expand button
            bottom_menu.getWidget("expandBtn").clicked.connect(
                lambda: self.log_to_console("Bottom Drawer: Expand Player button clicked")
            )

########################################################################
## EXECUTE APP
########################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ########################################################################
    ## 
    ########################################################################
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
########################################################################
## END===>
########################################################################  
