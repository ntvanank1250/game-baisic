def group_by_owners(files):
    dic={}
    value= set(files.values())
    for i in value:
        list=[]
        for y in files.keys():
            if files[y]==i:
                list.append(y)
        dic.update({i:list})
        
    return dic
    

if __name__ == "__main__":    
    files = {
        'Input.txt': 'Randy',
        'Code.py': 'Stan',
        'Output.txt': 'Randy'
    }   
    print(group_by_owners(files))