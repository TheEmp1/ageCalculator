'''
Python program to calculate age in year
'''


from datetime import date

from  calendar import monthrange,weekday,day_name




class calculateAge():

    people_list=list(

    )

    @property


    def opr(self) -> int:
        '''
        This function returns today's date
        '''
    

        return date.today().year
    

    def return_name(self,result,Max=True) -> str:

        '''
        This function returns the name
        '''
        if Max:
            return [
                list(t.values())[0] for t in self.people_list if str(max(result)) in t.values()
                ][0]
        else:
            return [
                list(t.values())[0] for t in self.people_list if str(min(result)) in t.values()
                ][0]

    
    def fun(self,value:str,item:str) -> str :
        '''
        This function returns an item
        '''
 
        return ''.join(
            str(t.get(value)) for t in self.people_list  if str(item) in t.values()
            )
        

    def __init__(self,*args):

        self.dates = args


    def __len__(self):

        return len( self.dates )

    def add(self,PersonInfo:dict):
        '''
        This function adds the person to the list
        '''

        self.people_list.append( PersonInfo )

    def isRepeatable(self):
        '''
        This function checks the length of the list if it is equal to one first less than one it returns false 
        if otherwise it is sorting the list
        '''

        if len( self )<2:

            raise Exception("There is no oldest or youngest person.")
        else:

            for people in self.dates:

                items          = people.split(',')

                DateBirth      = items[1].strip()
                
                name           =  items[0] 

                day,month,year = map(int,DateBirth.split('-'))


                DictInfo       = {

                    'name':name,

                       'DateBirth' : str(date(year,month,day))  ,
                         'year'      : year       ,
                         'day'       : day        ,
                         'month'     : month      ,
                         'Weekday'   :day_name[weekday(year,month,day)]     ,
                         'age'       : int(self.opr-year)
                         } if month  in range(1,13) and day  in range(1,(monthrange(year,month))[1]+1)   else  {'name':name}
   

                self.add( DictInfo )


        
    @property
    def getInfo(self):
        '''
        This function returns the names of people with their ages and their sum
        '''

        Dic = self.people_list
        
        result = [

        ]

        for item in Dic:

           if item.get('age'):

             y,m,d= item.get('year'),item.get('month'),item.get('day')

             result.append(date(y,m,d))

        result.sort()

        smallest = self.return_name(
            result,Max=False
            )

        biggest  = self.return_name(result)


        for item in result :

            print(
                f'{self.fun("name",item)} is {self.fun("age",item)} years old and she/he was born on {self.fun("Weekday",item)} '
                )

        print(
            '\n'.join(


            f"{item.get('name') } Invalid date"      for item in Dic if not item.get('age')
            )
            )

        print(
            f'The oldest one is {smallest}'
            )


        print(
            f'The youngest one is {biggest}'
            )

        return f'Total People:  {self.__len__()}'

 
            








e = (
    'khalid, 1-2-2000','rami, 1-3-1989'
)
obj = calculateAge(
    *e
    )

obj.isRepeatable()

print(obj.getInfo)
