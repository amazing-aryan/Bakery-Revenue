class Revenue:

    def __init__(self):
        with open("Input/Basic.txt", 'r') as basic:
            self.basic_list = self.process_file(basic, 2)
            self.basic_list = self.stringToList(self.basic_list)
        with open("Input/Delux.txt", 'r') as delux:
            self.delux_list = self.process_file(delux, 2)
            self.delux_list = self.stringToList(self.delux_list)
        with open("Input/Total.txt", 'r') as total:
            self.total_list = self.process_file(total, 1)
            self.total_list = self.stringToList(self.total_list)

    def stringToList(self, list):
        list1 = []
        for x in list:
            list1.append(int(x))
        return list1

    def process_file(self, file, offset):
        file_list = file.read().split()
        return file_list[offset:]

    def revenueData(self, days):
        revenue = sum(self.total_list[(-1)*days:])
        basicRevenue = sum(self.basic_list[(-1)*days:])*5
        deluxRevenue = sum(self.delux_list[(-1)*days:])*6
        percentBasic = round(basicRevenue/revenue * 100, 2)
        percentDelux = 100-percentBasic
        print(f'---------------------\nRevenue : {revenue}\n---------------------\nRevenue breakdown :\nBasic cupcakes -> {percentBasic}%\nDelux cupcakes -> {percentDelux}%\n---------------------')

obj = Revenue()

if __name__ == '__main__':
    choice = int(
        input('Enter your choice:\n1 for week\n2 for month\n3 for year\n'))
    if(choice == 1):
        obj.revenueData(7)
    elif(choice == 2):
        obj.revenueData(30)
    elif(choice == 3):
        obj.revenueData(365)
    else:
        print("Please enter valid choice")

