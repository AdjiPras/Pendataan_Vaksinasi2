from flask import Flask, request, jsonify, render_template, json, redirect, redirect, url_for, session, make_response
from flask_mongoengine import MongoEngine #ModuleNotFoundError: No module named 'flask_mongoengine' = (venv) C:\flaskmyproject>pip install flask-mongoengine
from datetime import datetime
from models import MModel
# from selenium.webdriver import Chrome
# from selenium.webdriver.chrome.options import Options
# from selenium.common.exceptions import NoSuchElementException, \
#     TimeoutException, ElementNotInteractableException
from time import sleep
from database import dbBrainly
from pymongo import MongoClient

import pymongo
import datetime
import config2

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["brainlydb"]

application = Flask(__name__)
application.config['SECRET_KEY'] = 'sfh7^erw9*(%sadHGw%R'

# today = datetime.today()
model = MModel()
html_source = ''
 
app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'brainlydb',
    'host': 'localhost',
    'port': 27017
}
db = MongoEngine()
db.init_app(app)

# ============================================================================================================  
# Index
@application.route('/')
def index():
	if 'data_nama' in session:
		# current_time_date = today.strftime("%B %d, %Y")
		data_nama = session['data_nama']
		return render_template('index_vaksin.html', data_nama=data_nama)
	return render_template('form_login.html')

# login	
@application.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		ktp = request.form['ktp']
		nama = request.form['nama']
		if model.authenticate(ktp, nama):
			data_nama = model.getDataForSession(nama)
			session['data_nama'] = data_nama
			return redirect(url_for('index'))
		msg = 'Nama/No. KTP salah.'
		return render_template('form_login.html', msg=msg)
	return render_template('form_login.html')

# Logout	
@application.route('/logout')
def logout():
	session.pop('data_nama', '')
	return redirect(url_for('index'))

# ============================ Data Vaksinasi (Semua) ===================================================
@application.route('/data')
def data():
    if 'data_nama' in session:
        data_nama = session['data_nama']
        nama = data_nama[1]
        container_vaksin = [] 
        container_vaksin = model.selectData()
        return render_template('data.html', container_vaksin=container_vaksin, data_nama=data_nama)
    return render_template('form_login.html')

@application.route('/insert_data', methods=['GET', 'POST'])
def insert_data():
	if 'data_nama' in session:
		if request.method == 'POST':
			ktp = request.form['ktp']
			nama = request.form['nama']
			jenis_kelamin = request.form['jenis_kelamin']
			agama = request.form['agama']
			kota_lahir = request.form['kota_lahir']
			tanggal_lahir = request.form['tanggal_lahir']
			kelurahan = request.form['kelurahan']
			kecamatan = request.form['kecamatan']
			kabupaten_kota = request.form['kabupaten_kota']
			provinsi = request.form['provinsi']
			no_telepon = request.form['no_telepon']
			jenis_vaksin = request.form['jenis_vaksin']
			lokasi_vaksin = request.form['lokasi_vaksin']
			dosis_pertama = request.form['dosis_pertama']
			dosis_kedua = request.form['dosis_kedua']
			tipe_akses = request.form['tipe_akses']
			data_v = (ktp, nama, jenis_kelamin, agama, kota_lahir, tanggal_lahir, kelurahan, kecamatan, kabupaten_kota, provinsi, no_telepon, jenis_vaksin, lokasi_vaksin, dosis_pertama, dosis_kedua, tipe_akses)
			model.insertData(data_v)
			return redirect(url_for('data'))
		else:
			data_nama = session['data_nama']
			return render_template('insert_data.html', data_nama=data_nama)
	return render_template('form_login.html')

@application.route('/update_vk', methods=['GET', 'POST'])
def update_vk():
    if 'data_nama' in session:
        ktp = request.form['ktp']
        nama = request.form['nama']
        jenis_kelamin = request.form['jenis_kelamin']
        agama = request.form['agama']
        kota_lahir = request.form['kota_lahir']
        tanggal_lahir = request.form['tanggal_lahir']
        kelurahan = request.form['kelurahan']
        kecamatan = request.form['kecamatan']
        kabupaten_kota = request.form['kabupaten_kota']
        provinsi = request.form['provinsi']
        no_telepon = request.form['no_telepon']
        jenis_vaksin = request.form['jenis_vaksin']
        lokasi_vaksin = request.form['lokasi_vaksin']
        dosis_pertama = request.form['dosis_pertama']
        dosis_kedua = request.form['dosis_kedua']
        tipe_akses = request.form['tipe_akses']
        data_vk = (nama, jenis_kelamin, agama, kota_lahir, tanggal_lahir, kelurahan, kecamatan, kabupaten_kota, provinsi, no_telepon, jenis_vaksin, lokasi_vaksin, dosis_pertama, dosis_kedua, tipe_akses, ktp)
        model.updateData(data_vk)
        return redirect(url_for('data'))
    return render_template('form_login.html')

@application.route('/update_data/<ktp>')
def update_data(ktp):
	if 'data_nama' in session:
		data_vk = model.getDatabyNo(ktp)
		data_nama = session['data_nama']
		return render_template('edit_data.html', data_vk=data_vk, data_nama=data_nama)
	return redirect(url_for('login')) 

@application.route('/delete_data/<ktp>')
def delete_data(ktp):
    if 'data_nama' in session:
        model.deleteData(ktp)
        return redirect(url_for('data'))
    return render_template('form_login.html')

# ============================ SLEMAN ===================================================

@application.route('/sleman')
def sleman():
    if 'data_nama' in session:
        data_nama = session['data_nama']
        username = data_nama[1]
        container_sleman = [] 
        container_sleman = model.selectSleman()
        return render_template('sleman.html', container_sleman=container_sleman, data_nama=data_nama)
    return render_template('form_login.html')

@application.route('/ambarketawang')
def ambarketawang():
    if 'data_nama' in session:
        data_nama = session['data_nama']
        username = data_nama[1]
        container_ambarketawang = [] 
        container_ambarketawang = model.selectAmbarketawang()
        return render_template('ambarketawang.html', container_ambarketawang=container_ambarketawang, data_nama=data_nama)
    return render_template('form_login.html')

@application.route('/balecatur')
def balecatur():
    if 'data_nama' in session:
        data_nama = session['data_nama']
        username = data_nama[1]
        container_balecatur = [] 
        container_balecatur = model.selectBalecatur()
        return render_template('balecatur.html', container_balecatur=container_balecatur, data_nama=data_nama)
    return render_template('form_login.html')

if __name__ == '__main__':
    application.run(debug=True)