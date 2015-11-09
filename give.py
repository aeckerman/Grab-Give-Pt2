import webbrowser
import os

def give():
	dataO = open('.data', 'r')
	data = dataO.read()
	dataO.close()
	
	outf = open('google.html', 'w')
	outf.write(data)
	outf.close()

	os.system('open google.html')
	
if __name__ == '__main__':
	give()