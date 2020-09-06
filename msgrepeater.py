import tkinter
from ipaddress import IPv4Address
from pyairmore.request import AirmoreSession
from pyairmore.services.messaging import MessagingService
from pyairmore.services.device import DeviceService
import time
# The following functions are to format the interface

def configureGrid(numberOfRows, numberOfColumns, minRowHeight = 0, minColWidth = 0):
    '''Similar to
        grid-template-rows: repeat(numberOfRows, minRowHeight);
        grid-template-columns: repeat(numberOfColumns, minColWidth);
    in CSS. Rows and columns are zero-indexed.
    Will expand as elements get bigger, and as window is resized
    Style is applied to the main window
    '''
    
    for row in range(numberOfRows):
        mainWindow.grid_rowconfigure(row, minsize = minRowHeight, weight = 1)
    for column in range(numberOfColumns):
        mainWindow.grid_columnconfigure(column, minsize = minColWidth, weight = 1)

def placeElement(element, beginCoords, endCoords):
    '''beginCoords and endCoords are tuples of the form (row, col)
    To place an element in a single cell, say (2, 3),
    set both beginCoords and endCoords to (2, 3)
    Also possible to span an element across several cells
    '''
    beginRow, beginCol = beginCoords
    endRow, endCol = endCoords
    
    rowSpan = endRow - beginRow + 1
    colSpan = endCol - beginCol + 1
    
    element.grid(
        row = beginRow,
        column = beginCol,
        rowspan = rowSpan,
        columnspan = colSpan
    )

def addPadding(element, innerHorizontal, innerVertical, outerHorizontal, outerVertical):
    '''Add padding around an element ¯\_ツ_/¯
    '''
    element.grid(
        ipadx = innerHorizontal,
        ipady = innerVertical,
        padx = outerHorizontal,
        pady = outerVertical
    )

def stretchToOccupyGridCell(element):
    '''Typically elements would center inside their cells,
    when the window is resized. Use this to make their edges stick to the
    boundaries of the cell
    '''
    element.grid(sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

def testConnection():
    tbox1Value = tbox1.get()
    ip=IPv4Address(tbox1Value)
    session=AirmoreSession(ip)
    was_accepted = session.request_authorization()
    service = DeviceService(session)
    details = service.fetch_device_details()
    phonebrand= str(details.brand+' '+details.device_name)
    if was_accepted:
        label5.configure(text='Connected to '+phonebrand)
    else:
        label5.configure(text='Connected Failed')

# This function will probably be where all your backend stuff happens
def readTextBoxes():
    tbox1Value = tbox1.get()
    tbox2Value = tbox2.get()
    tbox3Value = tbox3.get()
    tbox4Value = tbox4.get()
    ip=IPv4Address(tbox1Value)
    msgsession=AirmoreSession(ip)
    was_accepted = msgsession.request_authorization()
    if was_accepted:
        msgservice=MessagingService(msgsession)
        for i in range(int(tbox4Value)):
            if i<=10:
                 msgservice.send_message(tbox2Value, tbox3Value)
            elif i>10 and i<=30:
                 time.sleep(1)
                 msgservice.send_message(tbox2Value, tbox3Value)
            elif i>30 and i<=40:
                 time.sleep(1.5)
                 msgservice.send_message(tbox2Value, tbox3Value)
            elif i>40:
                 time.sleep(2.5)
                 msgservice.send_message(tbox2Value, tbox3Value)          

    # The variables contain the values in the textboxes
    # Do what you want with their values in this function

def center(win):
    win.update_idletasks()
    width = 500
    height = 280
    x = (win.winfo_screenwidth() // 2) - (width // 2)
    y = (win.winfo_screenheight() // 2) - (height // 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))

# Create the main window
mainWindow = tkinter.Tk()
center(mainWindow)
# Set the text in the title bar
mainWindow.title("Msg Repeater")
# mainWindow.iconbitmap("hasala.ico")
# mainWindow.minsize(500,280)
# Make a grid of 5 rows, and 4 columns, each at least 10 units in length
configureGrid(5, 4, 10, 10)

# Define 4 text labels
label1 = tkinter.Label(text = "IP Address of your Phone")
label2 = tkinter.Label(text = "Recieving Phone Number")
label3 = tkinter.Label(text = "Your Msg")
label4 = tkinter.Label(text = "No of Times")
label5 = tkinter.Label(text = "Not connected to phone")

# Define 4 text boxes
tbox1 = tkinter.Entry()
tbox2 = tkinter.Entry()
tbox3 = tkinter.Entry()
tbox4 = tkinter.Entry()

# Define a button
button = tkinter.Button(text = "Send Message", command = readTextBoxes)
tstbutton =tkinter.Button(text = "Test Connection", command= testConnection)

# Put all elements in the grid
placeElement(label1, (0, 1), (0, 1))
placeElement(tbox1, (0, 2), (0, 2))

placeElement(label2, (1, 1), (1, 1))
placeElement(tbox2, (1, 2), (1, 2))

placeElement(label3, (2, 1), (2, 1))
placeElement(tbox3, (2, 2), (2, 2))

placeElement(label4, (3, 1), (3, 1))
placeElement(tbox4, (3, 2), (3, 2))

placeElement(button, (4, 1), (4, 2))
placeElement(tstbutton, (6, 1), (6, 2))
placeElement(label5,(5,1),(5,2))

# Run
mainWindow.mainloop()
