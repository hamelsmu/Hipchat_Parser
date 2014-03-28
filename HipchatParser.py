#Python that parses hit chat

mgc = get_ipython().magic
mgc('cd C:\Users\hhusain\Dropbox (AlixPartners)\Analtyics Materials Learning\Hipchat\hipchat_export\Rooms')

def get_filenames():
    filelist = []
    import os
    for dirpath, dnames, fnames in os.walk("./"):
        for filename in fnames:
            if filename not in ['list.json', 'hipchat_results.txt']:
                filelist.append('\\'.join([dirpath, filename])) 
    
    return filelist

def read_file(filename):
    import json
    fileobj = open(filename, 'rb')
    return json.load(fileobj)
    
def parse_room(filename):
    return filename.split('\\')[0].replace('./', '')

def parse_file(filename):
    chat = read_file(filename)
    parsed_dat = []
    for msg in chat:
        if type(msg) == list:
            continue

        room, date, name, msg_len = parse_room(filename), msg['date'], msg['from']['name'], len(msg['message'])
        parsed_dat.append([filename, str(room), str(date), name, str(msg_len)])
    
    return parsed_dat


def collect_chat_data():
    master_data = []
    filenames = get_filenames()
    for filename in filenames:
        current_data = parse_file(filename)
        
        for msg in current_data:
            master_data.append(msg)
    
    return master_data

def write_out_tofile():
    datlist = collect_chat_data()
    with open('hipchat_results.txt', 'w') as fout:
        #add header
        fout.write('FileName,Room,DateTime,UserName,MsgLength\n')
        for line in datlist:
            data = ','.join(line) + '\n'
            fout.write(data)
            
if __name__ == '__main__':
    write_out_tofile()
    #filelist = get_filenames()
    #test = parse_file('./Customer Segmentation\\2014-03-26.json')
