# Import statements necessary
import flask as F
import flask_script as FS

# Set up application
App1 = F.Flask(__name__)

m = FS.Manager(App1)

# Routes
@App1.route('/')
def F1():
    return '<h1>hw!</h1>'

@App1.route('/u/<n>')
def F2(n):
    return '<h1>Hi {}</h1>'.format(n)

@App1.route('/sv/<data>')
def Function3(data):
    dlist = ["h","b","t","m","w","j"]
    if len(data) > 3:
        Data1 = data
        data2 = None
    else:
        Data1 = None
        data2 = data
    return F.render_template('v.html',l=dlist,LN=Data1,SN=data2)

if __name__ == '__main__':
    m.run()
