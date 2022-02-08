import pymysql
import config2

db = cursor = None

class MModel:
	def __init__ (self, no=None, nama=None, no_telp=None):
		self.no = no
		self.nama = nama
		self.no_telp = no_telp
		
	def openDB(self):
		global db, cursor
		db = pymysql.connect(
			host=config2.DB_HOST,
			user=config2.DB_USER,
			password=config2.DB_PASSWORD,
			database=config2.DB_NAME)
		cursor = db.cursor()

	def closeDB(self):
		global db, cursor
		db.close()

	# validasi login dengan table data_pengguna.
	def authenticate(self, ktp=None, nama=None):
		self.openDB()
		cursor.execute("SELECT COUNT(*) FROM data_vaksinasi WHERE ktp = '%s' AND nama = '%s'" % (ktp, nama))
		count_account = (cursor.fetchone())[0]
		self.closeDB()
		return True if count_account>0 else False

# ========================= Data vaksinasi (Semua) ================================
	def selectData(self):
		self.openDB()
		cursor.execute("SELECT ktp, nama, jenis_kelamin, agama, kota_lahir, tanggal_lahir, kelurahan, kecamatan, kabupaten_kota, provinsi, no_telepon, jenis_vaksin, lokasi_vaksin, dosis_pertama, dosis_kedua, tipe_akses FROM `data_vaksinasi`")
		container_vaksin = []
		for ktp, nama, jenis_kelamin, agama, kota_lahir, tanggal_lahir, kelurahan, kecamatan, kabupaten_kota, provinsi, no_telepon, jenis_vaksin, lokasi_vaksin, dosis_pertama, dosis_kedua, tipe_akses in cursor.fetchall():
			container_vaksin.append((ktp, nama, jenis_kelamin, agama, kota_lahir, tanggal_lahir, kelurahan, kecamatan, kabupaten_kota, provinsi, no_telepon, jenis_vaksin, lokasi_vaksin, dosis_pertama, dosis_kedua, tipe_akses))
		self.closeDB()
		return container_vaksin

	def getDataForSession(self, nama):
		self.openDB()
		cursor.execute("SELECT ktp, nama, jenis_kelamin, agama, kota_lahir, tanggal_lahir, kelurahan, kecamatan, kabupaten_kota, provinsi, no_telepon, jenis_vaksin, lokasi_vaksin, dosis_pertama, dosis_kedua, tipe_akses FROM data_vaksinasi WHERE nama='%s'" % nama)
		data_nama = cursor.fetchone()
		return data_nama

	def insertData(self, data_v):
		self.openDB()
		cursor.execute("INSERT INTO data_vaksinasi (ktp, nama, jenis_kelamin, agama, kota_lahir, tanggal_lahir, kelurahan, kecamatan, kabupaten_kota, provinsi, no_telepon, jenis_vaksin, lokasi_vaksin, dosis_pertama, dosis_kedua, tipe_akses) VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % data_v)
		db.commit()
		self.closeDB()

	def updateData(self, data_vk):
		self.openDB()
		cursor.execute("UPDATE data_vaksinasi SET nama='%s', jenis_kelamin='%s', agama='%s', kota_lahir='%s', tanggal_lahir='%s', kelurahan='%s', kecamatan='%s', kabupaten_kota='%s', provinsi='%s', no_telepon='%s', jenis_vaksin='%s', lokasi_vaksin='%s', dosis_pertama='%s', dosis_kedua='%s', tipe_akses='%s' WHERE ktp='%s'" % data_vk)
		db.commit()
		self.closeDB()

	def getDatabyNo(self, ktp):
		self.openDB()
		cursor.execute("SELECT ktp, nama, jenis_kelamin, agama, kota_lahir, tanggal_lahir, kelurahan, kecamatan, kabupaten_kota, provinsi, no_telepon, jenis_vaksin, lokasi_vaksin, dosis_pertama, dosis_kedua, tipe_akses FROM data_vaksinasi WHERE ktp='%s'" % ktp)
		data_vk = cursor.fetchone()
		return data_vk
	
	def deleteData(self, ktp):
		self.openDB()
		cursor.execute("DELETE FROM data_vaksinasi WHERE ktp='%s'" % ktp)
		db.commit()
		self.closeDB()

# ========================= SLEMAN ================================
	def selectSleman(self):
		self.openDB()
		cursor.execute("SELECT ktp, nama, jenis_kelamin, agama, kota_lahir, tanggal_lahir, kelurahan, kecamatan, kabupaten_kota, provinsi, no_telepon, jenis_vaksin, lokasi_vaksin, dosis_pertama, dosis_kedua, tipe_akses FROM `data_vaksinasi` WHERE kabupaten_kota='sleman'")
		container_sleman = []
		for ktp, nama, jenis_kelamin, agama, kota_lahir, tanggal_lahir, kelurahan, kecamatan, kabupaten_kota, provinsi, no_telepon, jenis_vaksin, lokasi_vaksin, dosis_pertama, dosis_kedua, tipe_akses in cursor.fetchall():
			container_sleman.append((ktp, nama, jenis_kelamin, agama, kota_lahir, tanggal_lahir, kelurahan, kecamatan, kabupaten_kota, provinsi, no_telepon, jenis_vaksin, lokasi_vaksin, dosis_pertama, dosis_kedua, tipe_akses))
		self.closeDB()
		return container_sleman

	def getSlemanForSession(self, nama):
		self.openDB()
		cursor.execute("SELECT ktp, nama, jenis_kelamin, agama, kota_lahir, tanggal_lahir, kelurahan, kecamatan, kabupaten_kota, provinsi, no_telepon, jenis_vaksin, lokasi_vaksin, dosis_pertama, dosis_kedua, tipe_akses FROM data_vaksinasi WHERE nama='%s'" % nama)
		data_nama = cursor.fetchone()
		return data_nama

	# AMBARKETAWANG
	def selectAmbarketawang(self):
		self.openDB()
		cursor.execute("SELECT ktp, nama, jenis_kelamin, agama, kota_lahir, tanggal_lahir, kelurahan, kecamatan, kabupaten_kota, provinsi, no_telepon, jenis_vaksin, lokasi_vaksin, dosis_pertama, dosis_kedua, tipe_akses FROM `data_vaksinasi` WHERE kelurahan='ambarketawang'")
		container_ambarketawang = []
		for ktp, nama, jenis_kelamin, agama, kota_lahir, tanggal_lahir, kelurahan, kecamatan, kabupaten_kota, provinsi, no_telepon, jenis_vaksin, lokasi_vaksin, dosis_pertama, dosis_kedua, tipe_akses in cursor.fetchall():
			container_ambarketawang.append((ktp, nama, jenis_kelamin, agama, kota_lahir, tanggal_lahir, kelurahan, kecamatan, kabupaten_kota, provinsi, no_telepon, jenis_vaksin, lokasi_vaksin, dosis_pertama, dosis_kedua, tipe_akses))
		self.closeDB()
		return container_ambarketawang

	def getAmbarketawangForSession(self, nama):
		self.openDB()
		cursor.execute("SELECT ktp, nama, jenis_kelamin, agama, kota_lahir, tanggal_lahir, kelurahan, kecamatan, kabupaten_kota, provinsi, no_telepon, jenis_vaksin, lokasi_vaksin, dosis_pertama, dosis_kedua, tipe_akses FROM data_vaksinasi WHERE nama='%s'" % nama)
		data_nama = cursor.fetchone()
		return data_nama

	# BALECATUR
	def selectBalecatur(self):
		self.openDB()
		cursor.execute("SELECT ktp, nama, jenis_kelamin, agama, kota_lahir, tanggal_lahir, kelurahan, kecamatan, kabupaten_kota, provinsi, no_telepon, jenis_vaksin, lokasi_vaksin, dosis_pertama, dosis_kedua, tipe_akses FROM `data_vaksinasi` WHERE kelurahan='balecatur'")
		container_balecatur = []
		for ktp, nama, jenis_kelamin, agama, kota_lahir, tanggal_lahir, kelurahan, kecamatan, kabupaten_kota, provinsi, no_telepon, jenis_vaksin, lokasi_vaksin, dosis_pertama, dosis_kedua, tipe_akses in cursor.fetchall():
			container_balecatur.append((ktp, nama, jenis_kelamin, agama, kota_lahir, tanggal_lahir, kelurahan, kecamatan, kabupaten_kota, provinsi, no_telepon, jenis_vaksin, lokasi_vaksin, dosis_pertama, dosis_kedua, tipe_akses))
		self.closeDB()
		return container_balecatur

	def getBalecaturForSession(self, nama):
		self.openDB()
		cursor.execute("SELECT ktp, nama, jenis_kelamin, agama, kota_lahir, tanggal_lahir, kelurahan, kecamatan, kabupaten_kota, provinsi, no_telepon, jenis_vaksin, lokasi_vaksin, dosis_pertama, dosis_kedua, tipe_akses FROM data_vaksinasi WHERE nama='%s'" % nama)
		data_nama = cursor.fetchone()
		return data_nama
