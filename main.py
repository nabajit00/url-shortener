from flask import Flask,request,make_response,abort,render_template,redirect
from dotenv import load_dotenv
from markupsafe import escape
from os import getenv
import validators
import services.url as url_service

load_dotenv()

app = Flask(__name__)

@app.route('/<url_hash>/',methods=['GET'])
def redirect_from_short(url_hash:str):
    url = url_service.get_url(url_hash)
    if url is None:
        abort(404)
    
    return redirect(url_service.get_url(url_hash))
    


@app.route('/',methods=['GET'])
def homepage():
    return render_template('index.html')

@app.route("/create/", methods=['POST'])
def create():
    url = request.form['url']
    if not validators.url(url):
        return render_template('index.html',data={'message':'URL is not valid','status_color':'#FF6868'})
    
    if url_service.url_exists(url):
        return render_template('index.html',data={'message':'Already added','link':url_service.get_short_url(url),'already_present':True})

    return render_template('index.html',data={'message':'Success','link':url_service.add_url(url),'status_color':'#80BCBD'})
    
app.run(debug=(getenv('DEBUG')=='True'))