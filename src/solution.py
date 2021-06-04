class Solution:

    def read(self):
        command_input = raw_input()
        if "my_program" and ">" in command_input:
           name = command_input.split(" ")
           filename = name[1].split(">")
           fp = open(filename[0],'r')
           fo = open(filename[1],'w')
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
                    print(status)
               elif array[0] == "leave":
                    index = int(array[1])
                    status = self.leave(input_map,index)
                    fo.write(status + "\n")
                    print(status)
               elif array[0] == "status":
                    self.status(input_map,length)
                    fo.write("Slot No.  Registration No  Colour" + "\n")
                    for i in range(1,length+1):
                      if input_map[i]!="None":
                         answer = input_map[i].split(" ")
                         fo.write(str(i) + "\t" + answer[0] + "\t" + answer[1] + "\n")
               elif array[0] == "registration_numbers_for_cars_with_colour":
                    status = self.findregistration(input_map,array[1],length)
                    fo.write(status + "\n")
                    print(status)
               elif array[0] == "slot_numbers_for_cars_with_colour":
                    status = self.findslot(input_map,array[1],length)
                    fo.write(status + "\n")
                    print(status)
               elif array[0] == "slot_number_for_registration_number":
                    status = self.findslotregistration(input_map,array[1],length)
                    fo.write(status + "\n")
                    print(status)

        if command_input == "my_program":
           command = raw_input()
           while command!="exit":
              input_array = command.split(" ")
              if "create_parking_lot" in input_array[0]:
                  length = int(input_array[-1])
                  input_map = self.create(length)
              elif input_array[0] == "park":
                  status = self.park(input_map,length,input_array)
                  print(status)
              elif input_array[0] == "leave":
                  index = int(input_array[1])
                  status = self.leave(input_map,index)
                  print(status)
              elif input_array[0] == "status":
                  self.status(input_map,length)
              elif input_array[0] == "registration_numbers_for_cars_with_colour":
                  status = self.findregistration(input_map,input_array[1],length)
                  print(status)
              elif input_array[0] == "slot_numbers_for_cars_with_colour":
                  status = self.findslot(input_map,input_array[1],length)
                  print(status)
              elif input_array[0] == "slot_number_for_registration_number":
                  status = self.findslotregistration(input_map,input_array[1],length)
                  print(status)
              command = raw_input()

    def create(self,length):
       input_map = {}
       for i in range(1,length+1):
          input_map[i] = "None"
       print("Created a parking lot with " + str(length) + " slots")
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

    def status(self,input_map,length):
        print("Slot No.  Registration No  Colour")
        for i in range(1,length+1):
           if input_map[i]!="None":
              answer = input_map[i].split(" ")
              print(str(i) + "\t" + answer[0] + "\t" + answer[1])

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




ticket = Solution()
ticket.read()


