import bluetooth,os,sys
from xml.etree import ElementTree
from PyOBEX import client,responses
from PyOBEX.client import Client 
if __name__ == "__main__":
	device_addr = sys.argv[1];
	path = sys.argv[2];

	services = bluetooth.find_service(uuid="0000112f", address=device_addr)
	if services:
		port = services[0]["port"]
		names = services[0]["name"]
		
	print("Connecting to port %s with %s"%(port,names))
	c = Client(device_addr,port)
	response = c.connect();


	pieces = path.split("/")
	for piece in pieces:
		print(piece)
		response = c.setpath(piece)
		
	sys.stdout.write("Enteres directory %s \n" % path)
	response = c.listdir();
	if isinstance(responce, responses.FailureResponse):
			sys.stderr.write('Failed to enter directory\n')
			sys.exit(1);
	headers, data = response
	tree = ElementTree.formstring(data)
	for element in tree.findall("file"):
		name = element.attrib["name"]
		if os.path.exists(name):
			sys.stderr.write("File already exist: %s\n" % name)
			continue
		sys.stdout.write("Fetching file: %s\n" % name)
		response = c.get(name)
		if isinstance(responce, responses.FailureResponse):
			sys.stderr.write('Failed to get file:%s\n' % name)
		else:
			sys.stdout.write("Write file: %s\n" % name)
			headers,data = response
			try:
				open(name,"wb").write(data)
			except IOError:
				sys.stderr.write("Failed to write file %s\n" % name)

	c.disconnect()
	sys.exit()






