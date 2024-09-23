#Raymond Lin
#Death Row Coders
#SoftDev
#Dictionary and List Review
#2024/9/15
#1 hour
import random
krewes = {
           4: [
               'DUA','TAWAB','EVA','JACK','VICTOR','EVAN','JASON','COLYI','IVAN','TANZEEM',
                'TAHMIM','STANLEY','LEON','NAOMI','NIA','ANASTASIA','JADY','BRIAN','JACOB',
               'ALEX','CHONGTIAN','DANNY','MARCO','ABIDUR','ANKITA','ANDY','ETHAN','AMANDA',
               'AIDAN','LINDA','QIANJUN','JIAYING','KISHI'
               ],
           5: [ 
                'ADITYA','MARGIE','RACHEL','ALEXANDER','ZIYAD','DANNY','ENDRIT','CADEN',
                'VEDANT','SUHANA','KYLE','KEVIN','RAYMOND','CHRISTOPHER','JONATHAN','SASHA',
                'NAFIYU','TIM','WILL','DANIEL','BENJAMIN','CLAIRE','CHLOE','STELLA','TRACY',
                'JESSICA','JACKIE','WEN YUAN','YINWEI','TIFFANY','JAYDEN DANIEL','PRINCEDEN' 
              ]
         }

def randomNum():
    x = random.randint(4,5)
    y = krewes.get(x)
    print(y[random.randint(0,len(y)-1)])
randomNum()