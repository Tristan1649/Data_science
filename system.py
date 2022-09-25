import datetime
import csv
import matplotlib.pyplot as plt
# в главном меню пользователь выбирает функцию нажимая 1,2 или 3
# для оценки системы было созданы баллы и их сохранения в файл csv.
# пользователь ежедневно в конце дня оценивать работу системы за весь день. результат сохраняется.
# таким образом сохраняя каждый день оценки системы позволяет собрать данные для прогнозирования работы системы на 7 дней и 30 дней вперед.


class Sistem:
    def osenka(self):
        def zapros(self):
            self.now = datetime.datetime.now()
            self.days = datetime.timedelta(days=7)
            self.moth = datetime.timedelta(days=31)
            print('Оцените работу системы за день пл 10 бальной шкале')
            self.a=float(input('универсальность -versatility:'))
            self.b=float(input('надежность-reliability:'))
            self.c=float(input('проверяемость-verifiability:'))
            self.e=float(input('accuracy of the results:'))
            self.f=float(input('security:'))
            self.g=float(input('аппаратная совместимость-hardware compatibility:'))
            self.h=float(input('эффективность-efficiency:'))
            self.i=float(input('адаптируемость-adaptability:'))
            self.j=float(input('повторная входимость-re-entry:'))
            self.k=float(input('реентерабельность-reentrancy:'))

            self.yn = input('Хотите сохранить оценку? \n Введите y/n: ')
            if self.yn == 'y':
                print("Сохранено")
                pass
            else:
                zapros(self)

        zapros(self)
        self.z = self.a + self.b + self.c  + self.e + self.f + self.g + self.h + self.i + self.j + self.k
        self.q = (self.z * 100 / 110)
        now = datetime.date.today()
        day = self.z
        myData = [['Date','Score_system_in_procc','Full_procentage', "Day's_procentage"], 
                [now, day, 110 , day*100//110]]
        myFile = open('csvexample3.csv', 'a+')
        with myFile:
            writer = csv.writer(myFile)
            writer.writerows(myData)
        return f'''
        'результат : {int(self.z)}',
        Процент исправности системы : {int(self.q)}'''

        pass
   
    def prognoz(self):
        with open('csvexample3.csv', newline='') as myFile:
            reader = csv.reader(myFile, delimiter='/', quoting=csv.QUOTE_NONE)
            a = []
            for row in reader:
                try:
                    d = row[0]
                    d = d.split(',')
            
                    o = int(d[3])
                    a.append(o)  
                except:
                    pass
            a.reverse()

            start = input("Хотите осуществить прогноз системы на неделю/месяц? W/M :  ")

            if start.lower() == 'm':
                a = a[:30]
                plt.title("МЕСЯЦ")
                plt.plot(a)
                plt.show()
            elif start.lower() == 'w':
                a = a[:7]
                plt.title("НЕДЕЛЯ")
                plt.plot(a)
                plt.show()

            # можно за 90 дней если есть данные
           
           

s = Sistem()


while True:
    a = int(input(" ГЛАВНОЕ МЕНЮ \n 1)Оценить работу системы \n 2) Осуществить прогноз системы \n 3) Завершить работу \n : "))
    if a == 1:
        s.osenka()
    elif a == 2:
        s.prognoz()
    elif a == 3:
        break
    else:
        print('Выберите один из 3 вариантов')
        
    
