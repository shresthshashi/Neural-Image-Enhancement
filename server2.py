from flask import Flask, render_template, request
from werkzeug import secure_filename
import os
#import test
import shutil
folder = 'D:/5th sem docs/Minor/srcnn_keras-master/test'
for the_file in os.listdir(folder):
    file_path = os.path.join(folder, the_file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
        #elif os.path.isdir(file_path): shutil.rmtree(file_path)
    except Exception as e:
        print(e)
        
app = Flask(__name__,static_folder='D:/5th sem docs/Minor/srcnn_keras-master/static')

#app.config['UPLOAD_FOLDER'] = os.path.join('static','people_photo')

#PEOPLE_FOLDER = os.path.join('static', 'people_photo')
a='D:'
app.config['UPLOAD_FOLDER'] = os.path.join(a+os.sep,'5th sem docs','Minor','srcnn_keras-master')
@app.route('/')
def upload_f():
   return render_template('index.html')

@app.route('/index')
def index():
   return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contacts')
def contact():
    return render_template('contact.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      print("YESS");
      f = request.files['file']
      k=f
      print(f.filename)
      f.save(os.path.join(app.config['UPLOAD_FOLDER'],'test',secure_filename(f.filename)))
      #k.save(os.path.join(app.config['UPLOAD_FOLDER'],'static',secure_filename(k.filename)))
      #name=os.popen("test.py")
      #name = os.popen("enhance.py --type=photo --model=default %s" %(string)).read()
      #name=os.system("enhance.py --type=photo --model=default %s" %(string))
      os.system("test.py")
      full_filename=os.path.join(app.config['UPLOAD_FOLDER'],"static","image00_answer.bmp")
      #full_path='D:/coding/SE/neural-enhance-master/neural-enhance-master/jim.jpg'
      #print(full_filename)
      print(full_filename)
      #return "saved succesfull"
      return render_template("index2.html",imagename=f.filename)
      

# if __name__ == '__main__':
app.run(debug = False)
