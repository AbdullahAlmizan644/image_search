from flask import Flask,redirect,render_template,request,flash,session
from flask_mysqldb import MySQL
import os
from werkzeug.utils import secure_filename
from datetime import datetime
import cv2
import numpy as np
from flask_mail import Mail,Message
from random import randint
from flask_ckeditor import CKEditor


app=Flask(__name__)
ckeditor = CKEditor(app)


db = MySQL(app)
UPLOAD_FOLDER = '/home/zeus/image_recognition/static/image'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','mp3'}
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER
app.config['SECRET_KEY']='image_recognition_project'
app.config['MYSQL_HOST']='127.0.0.1'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='image_recognition'



app.config["MAIL_SERVER"]='smtp.gmail.com' 
app.config["MAIL_PORT"] = 465
app.config['MAIL_USE_TLS'] = False  
app.config['MAIL_USE_SSL'] = True  
app.config["MAIL_USERNAME"] = 'abdullahalmizan644@gmail.com'  
app.config['MAIL_PASSWORD'] = 'mizan52554'  

mail=Mail(app)
otp = randint(000000,999999)


#view
@app.route("/")
def index():
    return render_template("view/index.html")




@app.route("/contact",methods=["GET","POST"])
def contact():
    if "user" in session:
        if request.method=="POST":
            message=request.form.get("message")
            if len(message)<20:
                flash("please write greater than 20 alphabet.",category="error")
                return redirect(request.url)

            cur=db.connection.cursor()
            cur.execute("SELECT * FROM users WHERE name=%s",(session["user"],))
            user=cur.fetchone()

            email=user[2]

            msg = Message(f'message from {user[1]}',sender=email,recipients=['abdullahalmizan644@gmail.com'])  
            msg.body = str(message)  
            mail.send(msg) 
            flash("thanks for your message we will reply soon",category="success")
            return redirect("/")
        return render_template("view/contact.html")
    else:
        return redirect("/login")


@app.route("/person_details")
def person_deatils():
    return render_template("view/person_details.html")



@app.route("/search",methods=["GET","POST"])
def search():
    if "user" in session:
        if request.method=="POST":
            image = request.files['image']

            if image.filename=='':
                flash("No Image Selected",category="error")
                return redirect("/")

            original = cv2.imread(f"/home/zeus/image_recognition/static/image/{image.filename}",0)
            print(original)

            cur=db.connection.cursor()
            cur.execute("select * from person")
            users=cur.fetchall()

            count=0
            for user in users:
                print(user[3])
                a=user[3]
                duplicate = cv2.imread(f"/home/zeus/image_recognition/static/image/{a}",0)# 1) Check if 2 images are equals



                if original.shape == duplicate.shape:
                    print("The images have same size and channels")
                    difference = cv2.subtract(original, duplicate)
                    print(difference)
                    print(count)
                    # b, g, r = cv2.split(difference)

                    if cv2.countNonZero(difference[count]) == 0 and cv2.countNonZero(difference[count+1]) == 0 and cv2.countNonZero(difference[count+2]) == 0:
                        print("The images are completely Equal")
                        cur=db.connection.cursor()
                        cur.execute("select * from person where image=%s",(a,))
                        result=cur.fetchone()
                        print(result)
                        break

                else:
                    print("the images are not equal")
                    result=0
            
                count=count+3
            
            if result==0:
                flash("no person on that image",category="error")
                return redirect("/")
        
            return render_template("view/person_details.html",result=result)
    
    else:
        return redirect("/login")


#auth
@app.route("/login", methods=["GET","POST"])
def login():
    if request.method=="POST":
        username=request.form.get("username")
        password=request.form.get("password")

        cur=db.connection.cursor()
        cur.execute("SELECT * FROM users where name=%s and password=%s",(username,password,))
        user=cur.fetchone()

        if user:
            session["user"]=username
            flash("Logged in successFully!",category="success")
            return redirect("/profile")
        else:
            flash("wrong username or password",category="error")

    return render_template('view/login.html')


@app.route("/user_logout")
def user_logout():
    session.pop("user",None)
    flash("Logout Successfully!",category="error")
    return redirect("/")

@app.route("/signup", methods=["GET","POST"])
def signup():
    if request.method=="POST":
        username=request.form.get("username")
        email=request.form.get("email")
        password1=request.form.get("password1")
        password2=request.form.get("password2")

        cur=db.connection.cursor()
        cur.execute("SELECT * from users where name=%s",(username,))
        data=cur.fetchone()

        if len(username)<5:
            flash("username must be greater than 4 words",category="error")

        elif data:
            flash("username already taken",category="error")

        elif len(email)<5:
            flash("email must be greater than 4 words",category="error")

        elif len(password1)<8:
            flash("password must be greater than 8 digit",category="error")

        elif password1!=password2:
            flash("password doesn't match",category="error")

        else:
            global dict 
            dict={
                "name":username,
                "email":email,
                "password":password1,
            }
            msg = Message('OTP',sender='abdullahalmizan644@gmail.com',recipients=[email])  
            msg.body = str(otp)  
            mail.send(msg)              
            flash("send a otp in your mail.",category="success")
            return redirect("/verify")
    return render_template("view/signup.html")


@app.route("/verify",methods=["GET","POST"])
def verify():
    global dict
    if request.method=="POST":
        user_otp=request.form['otp']
        print(user_otp)

        if int(user_otp)==otp:
            flash("otp match & account created successfully!!",category="success")
            cur=db.connection.cursor()
            cur.execute("INSERT INTO users(name,email,password,date) VALUES(%s,%s,%s,%s)",(dict["name"],dict["email"],dict["password"],datetime.now()))
            db.connection.commit()
            cur.close()
            return redirect("/login")
        
        else:
            flash("Wrong otp",category="error")
            return redirect(request.url)
    return render_template("view/verify.html")



@app.route("/profile",methods=["GET","POST"])
def profile():
    if "user" in session:
        cur=db.connection.cursor() 
        cur.execute("select * from users where name=%s",(session["user"],))
        user=cur.fetchone()
        return render_template("view/profile.html",user=user)

    else:
        return redirect("/login")







#admin
@app.route("/admin_login",methods=["GET","POST"])
def admin_login():
    if request.method=="POST":
        email=request.form.get("email")
        password=request.form.get("password")

        if email=="admin@gmail.com" and password=="12345678":
            session["admin"]=email
            flash("Login Successfully!", category="success")
            return redirect("/dashboard")
        else:
            flash("wrong email or password.", category="error")
    return render_template("admin/login.html")




@app.route("/dashboard")
def dashboard():
    if "admin" in session:
        cur=db.connection.cursor()
        cur.execute("SELECT * FROM users")
        users=cur.fetchall()

        cur=db.connection.cursor()  
        cur.execute("SELECT count(sno) from users ")
        total_users=cur.fetchone()

        cur=db.connection.cursor()  
        cur.execute("SELECT count(sno) from person")
        total_persons=cur.fetchone()

        return render_template("admin/index.html",users=users,total_users=total_users,total_persons=total_persons)
    else:
        return redirect("/admin_login")



@app.route("/users")
def users():
    if "admin" in session:
        cur=db.connection.cursor()
        cur.execute("SELECT * FROM users")
        users=cur.fetchall()

        cur=db.connection.cursor()  
        cur.execute("SELECT count(sno) from users ")
        total_users=cur.fetchone()

        return render_template("admin/user.html",users=users,total_users=total_users)
    
    else:
        return redirect("/admin_login.html")



@app.route("/delete_user/<int:id>")
def delete_user(id):
    if "admin" in session:
        cur=db.connection.cursor()  
        cur.execute("DELETE FROM users WHERE sno=%s",(id,))
        db.connection.commit()
        flash("Block user successfully.",category="error")
        return redirect("/users")

    else:
        return redirect("/admin_login")


@app.route("/person_data")
def person_data():
    if "admin" in session:
        cur=db.connection.cursor()
        cur.execute("SELECT * FROM person")
        persons=cur.fetchall()

        cur=db.connection.cursor()  
        cur.execute("SELECT count(sno) from person ")
        total_persons=cur.fetchone()
        return render_template("admin/person_data.html",persons=persons,total_persons=total_persons)
    
    else:
        return redirect("/admin_login")

@app.route("/add_person",methods=["GET","POST"])
def add_person():
    if "admin" in session:
        if request.method=="POST":
            name=request.form.get("name")
            address=request.form.get("ckeditor")
            image = request.files['image']

            if image.filename == '':
                flash('No selected file', category="error")
                return redirect(request.url)
            else:
                image.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(image.filename)))
                cur=db.connection.cursor()
                cur.execute("INSERT INTO person(name,address,image,date,writer) VALUES (%s,%s,%s,%s,%s)",(name,address,image.filename,datetime.now(),"admin",))
                db.connection.commit()
                flash("person  added successfully!",category="success")
                return redirect("/person_data")
    
        return render_template("admin/add_person.html")
    else:
        return redirect("/admin_login")
    

@app.route("/edit_person/<int:id>",methods=["GET","POST"])
def edit_person(id):
    if "admin" in session:
        cur=db.connection.cursor()  
        cur.execute("SELECT * FROM person WHERE sno=%s",(id,))
        post=cur.fetchone()
        if request.method=="POST":
            address=request.form.get("ckeditor")

            cur=db.connection.cursor()
            cur.execute("UPDATE person set address=%s where sno=%s",(address,id,))
            db.connection.commit()
            flash("Edit user post",category="success")
            return redirect("/person_data")
    
        return render_template("admin/edit_person.html",post=post)
    else:
        return redirect("/admin_login")
    


@app.route("/delete_person/<int:id>")
def delete_person(id):
    if "admin" in session:
        cur=db.connection.cursor()  
        cur.execute("DELETE FROM person WHERE sno=%s",(id,))
        db.connection.commit()
        flash("Delete person successfully.",category="error")
        return redirect("/person_data")

    else:
        return redirect("/admin_login")





@app.route("/admin_logout")
def admin_logout():
    session.pop("admin",None)
    flash("Logout Successfully!",category="error")
    return redirect("/admin_login")



@app.route("/write_post",methods=["GET","POST"])
def write_post():
    if "user" in session:
        if request.method=="POST":
            name=request.form.get("name")
            address=request.form.get("ckeditor")
            image = request.files['image']

            if image.filename == '':
                flash('No selected file', category="error")
                return redirect(request.url)
            else:
                image.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(image.filename)))
                cur=db.connection.cursor()
                cur.execute("INSERT INTO person(name,address,image,date,writer) VALUES (%s,%s,%s,%s,%s)",(name,address,image.filename,datetime.now(),session["user"],))
                db.connection.commit()
                flash("post  added successfully!",category="success")
                return redirect("/")
    
        return render_template("user_post/write_post.html")
    else:
        return redirect("/login")



@app.route("/user_post")
def user_post():
    cur=db.connection.cursor()
    cur.execute("SELECT * FROM person")
    posts=cur.fetchall()
    return render_template("user_post/blog.html",posts=posts)





@app.route("/post_details/<int:id>", methods=["GET","POST"])
def post_details(id):
    if "user" in session:
        cur=db.connection.cursor()
        cur.execute("SELECT * FROM person where sno=%s",(id,))
        post=cur.fetchone()

        cur=db.connection.cursor()
        cur.execute("SELECT * FROM users where name=%s",(session["user"],))
        user=cur.fetchone()

        cur=db.connection.cursor()
        cur.execute("SELECT * FROM comment where post_id=%s",(id,))
        comments=cur.fetchall()

        if request.method=="POST":
            comment=request.form.get("comment")

            cur=db.connection.cursor()
            cur.execute("INSERT INTO comment(writer,image,comment,post_id,date) VALUES (%s,%s,%s,%s,%s)",(user[1],user[3],comment,id,datetime.now(),))
            db.connection.commit()
            flash("comment post",category="success")
            return redirect(request.url)

        return render_template("user_post/blog_details.html",post=post,comments=comments)
    
    else:
        return redirect("/login")

    

if __name__=="__main__":
    app.run(debug=True)