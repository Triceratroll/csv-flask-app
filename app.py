import os
from flask import Flask, request, render_template, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
from datetime import datetime
from report_1 import generate_order_prices
from report_2 import generate_product_customers
from report_3 import generate_customer_ranking
from utils import clearDirectory


ALLOWED_EXTENSIONS = {'csv'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/upload_report_1', methods=['GET', 'POST'])
    def upload_report_1():
        
        clearDirectory('input')
        clearDirectory('output')
        
        if request.method == 'POST':

            files = request.files.getlist("files")
            for file in files:
                if file and allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    save_location =  os.path.join('input', filename)
                    file.save(save_location)
            
            output_file = generate_order_prices('input', 'output')
            return redirect(url_for('download_file', filename=output_file))  

        return render_template('upload_report_1.html')
    
    
    @app.route('/upload_report_2', methods=['GET', 'POST'])
    def upload_report_2():
        
        clearDirectory('input')
        clearDirectory('output')
        
        if request.method == 'POST':

            files = request.files.getlist("files")
            for file in files:
                if file and allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    save_location =  os.path.join('input', filename)
                    file.save(save_location)
            
            output_file = generate_product_customers('input', 'output')
            return redirect(url_for('download_file', filename=output_file))  

        return render_template('upload_report_2.html')
    

    @app.route('/upload_report_3', methods=['GET', 'POST'])
    def upload_report_3():
        
        clearDirectory('input')
        clearDirectory('output')
        
        if request.method == 'POST':

            files = request.files.getlist("files")
            for file in files:
                if file and allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    save_location =  os.path.join('input', filename)
                    file.save(save_location)
            
            
            output_file = generate_customer_ranking('input', 'output')
            return redirect(url_for('download_file', filename=output_file)) 

        return render_template('upload_report_3.html')
    

    @app.route('/download/<filename>')
    def download_file(filename):
        return send_from_directory('output', filename)  


    return app 