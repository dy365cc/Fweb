from flask import Flask,url_for,redirect,request,session
#from flask_bootstrap import Bootstrap
from flask import render_template
import Fform
from mysql import MyDb
import time
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
#Bootstrap(app)

@app.route('/')
def fb_index():
    v_name = ''
    v_pwd = ''
    logform = Fform.loginfor_form()
    if logform.validate_on_submit():
        v_name = logform.name.data
        v_pwd = logform.name.data

        #return redirect(url_for('login_do'))
    return render_template('mypage/index.html')



@app.route('/login_do',methods=['POST'])
def login_do1():
    logform = Fform.loginfor_form()
    p_name = request.form['username']
    p_pwd = request.form['password']
    my_db = MyDb()
    my_data = []
    if p_name != "":
        my_sql = "select * from user where p_name = '"+p_name+"';"
    else:
        my_sql = "select * from user where p_pwd = '"+p_pwd+"';"
    my_db.getdata(my_sql)
    if len(my_db.rst) > 0:
        my_data = my_db.rst
    else:
        return render_template('mypage/index.html', v_info = '用户名密码错误！')
    if my_data[0]["p_pwd"] == p_pwd:
        session['uid'] = my_data[0]['iduser']
        session['uname'] = my_data[0]['p_name']
        session['ulevel'] = my_data[0]['p_level']
        session['utime'] = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
        return render_template('mypage/loginpage.html',l_name = p_name,l_pwd = p_pwd)
    else:
        return render_template('mypage/index.html', v_info = '用户名密码错误！')



if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0',port=8000)
