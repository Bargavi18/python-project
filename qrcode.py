import pyqrcode 
import png 
from pyqrcode import QRCode 


 
s = "Hii, This is Bargavi Kumar. I'm comming from Electronic city Bangalore.I completed college with a CGPA of 8.62 in University College of Engineering Panruti.I completed my schooling at my native which is in Tamilnadu.I scored 94.5% in 10th and 73% in 12th.Currently I'm doing Python Full Stack Course at Besant Technologies Bangalore .My Technical skiulls include HTML, CSS, Javascript, Python and SQL.My strength include Problem solving ability, Time management and Quick learning ability."
url = pyqrcode.create(s) 
url.svg("myqr.svg", scale = 8) 
url.png('myqr.png', scale = 6) 
