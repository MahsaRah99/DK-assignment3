#!/usr/bin/python3
#HW3_Q1_python's zen
"""
Reading from and writing in files,
Converting alphabetic numbers to digits
"""

def num2dig(my_file:str, my_file_edited:str):
    """
    gets a file and convert all of its alphabetic
    numbers to digits and writes the context into
    a new file.

    Args:
        my_file (file): input file's name
        my_file_edited (file): output file's name
    """
    
    word_nums = ('one', 'two', 'three', 'four', 'five', 'six',
           'seven', 'eight', 'nine', 'ten', 'eleven',
           'twelve', 'thirteen', 'fourteen', 'fifteen',
           'sixteen', 'seventeen', 'eighteen', 'nineteen',
           'twenty')
    
    dic = dict(map(lambda x: (x[1], x[0]), enumerate(word_nums,1)))
    
    with open(my_file,mode='r', encoding='utf-8') as f\
        ,open(my_file_edited,mode='w+',encoding= 'utf-8') as f2:

        text = f.read()
        for key,val in dic.items():
            if key in text:
                text = text.replace(f"{key} )", str(val)+")")
                text = text.replace(f" {key}"," " + str(val))
                
        f2.write(text)    
        
    
def main():
    num2dig('Zen.txt','Zen_edited.txt') 
 
    
if __name__ == "__main__":
    main()

        

