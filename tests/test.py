class TestSolution:
    def testfile(self):
        '''Check if the output file generated is same as expected output file'''
        fp = open("input.txt",'r')
        fo = open("output.txt",'w')
        lineNumber = 0
        for line in fp:
          lineNumber += 1
          line = line.rstrip()
          array = line.split(" ")
          if "create_parking_lot" in line:
              length = int(array[-1])
              input_map = self.create(length)
              result = "Created a parking lot with " + str(length) + " slots"
              fo.write(result + "\n")
          elif array[0] == "park":
              status = self.park(input_map,length,array)
              fo.write(status + "\n")
          elif array[0] == "leave":
              index = int(array[1])
              status = self.leave(input_map,index)
              fo.write(status + "\n")
          elif array[0] == "status":
              fo.write("Slot No.  Registration No  Colour" + "\n")
              for i in range(1,length+1):
                 if input_map[i]!="None":
                    answer = input_map[i].split(" ")
                    fo.write(str(i) + "\t" + answer[0] + "\t" + answer[1] + "\n")
          elif array[0] == "registration_numbers_for_cars_with_colour":
              status = self.findregistration(input_map,array[1],length)
              fo.write(status + "\n")
          elif array[0] == "slot_numbers_for_cars_with_colour":
              status = self.findslot(input_map,array[1],length)
              fo.write(status + "\n")
          elif array[0] == "slot_number_for_registration_number":
              status = self.findslotregistration(input_map,array[1],length)
              fo.write(status + "\n")
        fp.close()
        fo.close()
        self.textCompare('expected.txt','output.txt')


    def testcommand(self):
        length = 2
        input_map = self.create(length)
        assert length == len(input_map)
        input_map[0] = "01 white"
        input_map[1] = "02 red"
        status = self.leave(input_map,0)
        assert input_map[0] == "None"
        status = self.findregistration(input_map,"white",2)
        assert status == "Not Found"
        status = self.findslotregistration(input_map,"02",2)
        assert int(status) == 1
        status = self.findslot(input_map,"red",2)
        assert int(status) == 1

    def textCompare(self,fl1,fl2):
        file1 = open(fl1, 'r')
        file2 = open(fl2, 'r')
        lines1=file1.readlines()
        lines2=file2.readlines()
        file1.close()
        file2.close()
        if lines1 == lines2:
          return True
        else:
          return False

    def create(self,length):
        input_map = {}
        for i in range(1,length+1):
           input_map[i]="None"
        return input_map
    def park(self,input_map,length,input_array):
       for i in range(1,length+1):
          status = "Sorry, parking lot is full"
          if input_map[i]=="None":
             input_map[i] = input_array[1]+ " " + input_array[2]
             status = "Allocated slot number: " + str(i)
             break
       return status

    def leave(self,input_map,index):
        input_map[index] = "None"
        result = "Slot number " + str(index) + " is free"
        return result

    def findregistration(self,input_map,color,length):
        l = []
        for i in range(1,length+1):
            if input_map[i]!="None":
              answer = input_map[i].split(" ")
              if answer[1] == color:
                l.append(answer[0])
        if len(l) == 0:
          status = "Not Found"
          return status
        else:
          status = ','.join([str(item) for item in l])
          return status

    def findslot(self,input_map,color,length):
       l = []
       for i in range(1,length+1):
           if input_map[i]!="None":
             answer = input_map[i].split(" ")
             if answer[1] == color:
               l.append(i)
       if len(l) == 0:
          status = "Not Found"
          return status
       else:
          status = ','.join([str(item) for item in l])
          return status

    def findslotregistration(self,input_map,reg_num,length):
       l = []
       for i in range(1,length+1):
           if input_map[i]!="None":
             answer = input_map[i].split(" ")
             if answer[0] == reg_num:
               l.append(i)
       if len(l) == 0:
          status = "Not Found"
          return status
       else:
          status = ','.join([str(item) for item in l])
          return status


test = TestSolution()
test.testfile()
test.testcommand()
                 

