import urllib
def read_text():
    quotes = open(r"D:\workspace_python\message.txt")
    context_of_file = quotes.read()
    print(context_of_file)
    quotes.close();
    profanity_check(context_of_file)

def profanity_check(input_text):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=shot");
    output = connection.read()
    print(output)
    connection.close()

def print_odd_no():
  data = open("input.txt").readlines()

  for n in data: 
    if(n % 2 != 0):
      print(n)
  
##print_odd_no() 

read_text();
    
