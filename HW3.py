
def open_file():
    file = open("WhatsApp.txt" ,encoding='utf8')
    return file
   
file=open_file()  
def whatApp_file(file):        
    dictionary_id=dict()
    dictionary=dict()
    dictionary_2=dict()
    list1=list()
    num=1
    date=0
    id_num=0
    for line in file:
        line=line.strip()
        if not ':' in line:
            dictionary['datetime']= date
            dictionary['id']=id_num
            dictionary['text'] =line  
            list1.append(dictionary.copy())
            continue
        start=line.find('-')+1
        end=line.find(':',start)        
        if end>0:    
            name=line[start:end]        
            if name not in dictionary_id:
                dictionary_id[name]=num
                num=num+1
                space=line[0:15]
                date1=space.replace(',','')
                dictionary['datetime']= date1
                dictionary['id']=num-1
                text = line.split(':')
                dictionary['text'] = text[2]  
                date=date1
                id_num=num-1
                list1.append(dictionary.copy())


    file_1 = open("WhatsApp.txt" ,encoding='utf8') 
    for line1 in file_1:
        line1=line1.strip()
        if 'נוצרה על ידי' in line1:
            start2=line1.find('"')
            end2=line1.find('"',start2)
            if end2>0:
                nu=line1.split('ידי')
                dictionary_2['creation_date']=line1[0:15]
                c_name=line1.split('"')
                c_name=c_name[1].split('"')
                dictionary_2['chat_name']=c_name[0]
                dictionary_2['creator']=nu[1]
                dictionary_2['num_of_participants']=num-1
            
            chat_name1=c_name[0]
            

    final_dic=dict()
    final_dic['messages']=list1
    final_dic['metadata']=dictionary_2
    import json    
    json_file=chat_name1+".txt"    
    

    with open(json_file, 'w' , encoding='utf8') as json_file:
        json.dump(final_dic,json_file , ensure_ascii=False)
       
     
x=whatApp_file(file)
        
        
        
        
        
    
    
    
    
    
    
    
    
    