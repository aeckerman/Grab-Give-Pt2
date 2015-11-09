import urllib

def grab():
	googo = urllib.urlopen('http://google.com/')
	google = googo.read()

	nf = open('.data', 'w')
	nf.write(google)
	nf.close()

if __name__ == '__main__':
	grab()
