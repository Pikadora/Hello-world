import argparse
import subprocess

def off_1():
        command_line =["cat","/tmp/naucore"]
        call = subprocess.Popen(command_line,stdout=subprocess.PIPE)
        filet = call.communicate()
        file_in = filet[0]
        print(file_in)
        lines = file_in.split()
        n = len(lines)
        sl_out = {}
        for i in range(1,n):
                if lines[i] == "offline":
                        sl_out[lines[i-2]] = lines[i]
        if len(sl_out) < 2:
                print('There are no offline services')
        else:
                print ('Attention!!! There is offline services:')
                for ser in sl_out:
                        print ser,':',sl_out[ser]
                        
def off_2():
    with open('/tmp/pika/crit_serv.txt') as life:
        crit_serv = life.read().split()
    command_line =["cat","/tmp/naucore"]
    call = subprocess.Popen(command_line,stdout=subprocess.PIPE)
    filet = call.communicate()
    file_in = filet[0]
    print(file_in)
    lines = file_in.split()
    n = len(lines)
    sl_out = {}
    for i in range(1,n):
        if lines[i] in crit_serv and lines[i + 2] == 'offline':
                sl_out[lines[i]] = lines[i + 2]
    if len(sl_out) < 1:
        print('There are no offline services')
    else:
        print ('Attention!!! There is offline services:')
        for ser in sl_out:
            print ser,':',sl_out[ser]                        
                     
def off_3():
        command_line =["cat","/tmp/naucore"]
        call = subprocess.Popen(command_line,stdout=subprocess.PIPE)
        filet = call.communicate()
        file_in = filet[0]
        print(file_in)
        lines = file_in.split()
        n = len(lines)
        sl_out = {}
        for i in range(1,n):
                if lines[i] == "online":
                        sl_out[lines[i-2]] = lines[i]
        if len(sl_out) < 2:
                print('There are no offline services')
        else:
                print ('Attention!!! There is offline services:')
                for ser in sl_out:
                        print ser,':',sl_out[ser]
#action = 'store_true' означает, что при вводе ключа, выполнять, если ключа нет, то не выполнять
parser = argparse.ArgumentParser(description='Parsing some files.')
parser.add_argument('--one',help = 'offline services',action = 'store_true')
parser.add_argument('--two',help = 'only critical offline services',action = 'store_true')
parser.add_argument('--three',help = 'online services',action = 'store_true')
args = parser.parse_args()


if args.one:
        off_1()
elif args.two:
        off_2()
elif args.three:
        off_3()
else:
        print('Please see the HELP')
