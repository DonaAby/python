import pyqrcode
from pyqrcode import QRCode
a="donaaby"
url=pyqrcode.create(a)
url.svg("myqr.svg",scale=10)
