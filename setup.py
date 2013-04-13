# setup.py 
from distutils.core import setup
import py2exe
setup(
    windows = [
    {
        "script": "dxcl.pyw",
        "icon_resources": [(1, "app.ico")]
    }
    ],
)