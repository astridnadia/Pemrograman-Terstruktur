from datetime import * 
#Function
def diffDate(x):
    today = date.today()
    x = datetime.strptime(x, '%Y-%m-%d').date()
    diff = today - x
    print(abs(diff))
    
diffDate("2021-12-10")
