# Import statements necessary
import flask as F
import flask_script as FS

# Set up application
App1 = F.Flask(__name__)

M = FS.Manager(App1)

# Simple unreadable class
class ___cLass__1:
    def __init__(self):
        self.data = []

    def ___Add__data(self, value):
        self.data.append(value)

    def pRocess___data(self):
        processed_data = ""
        for item in self.data:
            processed_data += str(item) + " Pr0cessed "
        return processed_data

Instance1 = ___cLass__1()

# Routes
@App1.route('/')
def f1():
    return '<h1>hw!</h1>'

@App1.route('/u/<n>')
def f2(n):
    return '<h1>Hi {}</h1>'.format(n)

@App1.route('/sv/<data>')
def Function__3(data):
    Dlist = ["h","b","t","m","w","j"]
    if len(data) > 3:
        Data1 = data
        Data2 = None
    else:
        Data1 = None
        Data2 = data
    return F.render_template('v.html',l=Dlist,LN=Data1,SN=Data2)

if __name__ == '__main__':
    M.run()
