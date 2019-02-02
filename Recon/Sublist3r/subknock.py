import argparse
import sublist3r
import os,sys
import subprocess as sp 



ap = argparse.ArgumentParser()

ap.add_argument("-d","--domain",type=str, help="domain to search",required=True)

ap.add_argument("-w","--wordlist",type=str, help="specify path of wordlist")

ap.add_argument("-f","--csvfields",type=str,help="add fields name to the first row of csv output file Eg. -f col1,col2")

ap.add_argument("-j","--json",help="export full report in Json",action='store_true')

ap.add_argument("-b","--bruteforce",action='store_true',help="enable the bruteforce module")

ap.add_argument("-p","--ports",type=str,help="Scan the found subdomains against specific tcp ports")

ap.add_argument("-v","--verbose",action='store_true',help="Enable the verbose mode and display results in realtime")

ap.add_argument("-t","--threads",type=int,help="Number of threads to use for subbrute bruteforce")

ap.add_argument("-e","--engines",type=str,help="Specify a comma-separated list of search engines")

ap.add_argument("-o","--output",action='store_true',help="Save the results to text file")

ap.add_argument("-c","--csv",help="save output in csv file",action='store_true')

ap.add_argument("-s","--savefile",type=str,help="Name of the output file")

ap.add_argument("-S","--silent",action='store_true',help="Silent")

ap.add_argument("-r","--resolve",type=str,help="resolve ip or domain name")

ap.add_argument("-oS","--operatingSystem",type=str,help="operating system you use[mac,linux,windows]")

#ap.add_argument("","",type=,help="")


args = ap.parse_args()



def print_message():
	print("Did you forget something ?")



if args.domain:
	domain = args.domain
else:
	ap.print_help()

if args.operatingSystem:
	os = args.operatingSystem

# def run_p(command):
# 	pid = sp.Popen(args=["open -a Terminal .","--command=%s"%command],shell=True).pid
# 	print("Opening process with pid-",pid)

def run_knock(command):
	os.system(command)


def check_knockpy_req():

	command = "knockpy "
	if args.wordlist:
	    wordlist_path = args.wordlist
	    command = command + "-w " + wordlist_path
	    #print(command) 
	else:
	    #ap.print_help()
	    None
	if args.json:
	    json = True
	    command = command + " -j" 
	else:
	    json = False
	if args.csv:
		csv = True
		command = command + " -c"
	else:
		csv = False
	if args.resolve:
		resolve_ip = args.resolve
		command = command + " -r " + resolve_ip
	#run_knock(command)
	print("starting- " + command)
	run_knock(command)


def check_sub_req():

	if args.bruteforce:
		bruteforce = True
	else:
		bruteforce = False

	if args.verbose:
		verbose = True
	else:
		verbose = False

	if args.threads:
		threads = args.threads
	else:
		print("Number of threads not specified,Setting threads to 2")
		threads = 2

	if args.output:
		output = True
	else:
		output = False

	if args.savefile:
		savefile = args.savefile
	else:
		#ap.print_help()
		None

	if args.silent:
		silent = True
	else:
		silent = False

	if args.ports is None:
		ports = 80
	else:
		ports = args.ports
		print("Using specified ports-%d",ports)

	if args.engines is None:
		engines = None
	elif args.engines is not None:
		engines = args.engines
		print("Using specified engines-%s",engines)
	else:
		None

	if args.csvfields is None:
		csvfields = []
	else:
		csvfields = args.csvfields
		print("Using specified csvfields-%s",csvfields)
	subdomains = sublist3r.main(domain, threads, output, ports, silent, verbose, bruteforce, engines)

check_knockpy_req()

check_sub_req()






