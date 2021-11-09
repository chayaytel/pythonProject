# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import datetime
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def ret_first_line():
    with open('C:\\Users\\user\\Searches\\Downloads\\exam.log') as file:
        return file.readline()

def returnCountErrors():
    with open('C:\\Users\\user\\Searches\\Downloads\\exam.log') as file:
        count_errors = 0
        for line in file:
            s = line.split("\t")
            if s[1] == 'ERROR':
                count_errors+=1
        return count_errors

def count_transaction():
    with open('C:\\Users\\user\\Searches\\Downloads\\exam.log') as file:
        counter_transaction = 0
        for line in file:
            list_to_line = line.split("\t")
            list_to_cell = list_to_line[4].split(" ")

            if list_to_cell[0] == 'transaction':
                counter_transaction+=1



        return counter_transaction



def faster_transaction():
    with open('C:\\Users\\user\\Searches\\Downloads\\exam.log') as file:
        start_dic = {}
        end_dic = {}
        for line in file:
            l = line.split("\t")
            i = l[0].split(" ")
            list_to_cell = l[4].split(" ")
            if list_to_cell[0] == 'transaction':
                start_dic[list_to_cell[1]] = i[1]
            elif list_to_cell[0] == 'end':
                end_dic[list_to_cell[2][:5]] = i[1]
        ms = {}
        for x in start_dic:
            e = end_dic[x].split(":")
            s = start_dic[x].split(":")
            e[2] = e[2].split(".")
            s[2] = s[2].split(".")
            plus = 0
            minus = 0
            if int(e[2][1]) > int(s[2][1]):
                plus = int(e[2][1]) - int(s[2][1])
            else:
                minus = int(s[2][1]) - int(e[2][1])
            if int(e[2][0]) > int(s[2][0]):
                plus += 1000*(int(e[2][0]) - int(s[2][0]))
            else:
                minus += 1000*(int(s[2][0]) - int(e[2][0]))
            if int(e[1]) > int(s[1]):
                plus += 60000*(int(e[1]) - int(s[1]))
            else:
                minus += 60000*(int(s[1]) - int(e[1]))
            plus += 1000*(int(e[0]) - int(s[0]))
            ms[x] = plus - minus
        min_ = min(ms.values())
        for k in ms.keys():
            if ms[k] == min_:
                return k


def avg_transaction_in_milliseconds():
    with open('C:\\Users\\user\\Searches\\Downloads\\exam.log') as file:
        start_dic = {}
        end_dic = {}
        for line in file:
            l = line.split("\t")
            i = l[0].split(" ")
            list_to_cell = l[4].split(" ")
            if list_to_cell[0] == 'transaction':
                start_dic[list_to_cell[1]] = i[1]
            elif list_to_cell[0] == 'end':
                end_dic[list_to_cell[2][:5]] = i[1]
        ms = {}
        for x in start_dic:
            e = end_dic[x].split(":")
            s = start_dic[x].split(":")
            e[2] = e[2].split(".")
            s[2] = s[2].split(".")
            plus = 0
            minus = 0
            if int(e[2][1]) > int(s[2][1]):
                plus = int(e[2][1]) - int(s[2][1])
            else:
                minus = int(s[2][1]) - int(e[2][1])
            if int(e[2][0]) > int(s[2][0]):
                plus += 1000*(int(e[2][0]) - int(s[2][0]))
            else:
                minus += 1000*(int(s[2][0]) - int(e[2][0]))
            if int(e[1]) > int(s[1]):
                plus += 60000*(int(e[1]) - int(s[1]))
            else:
                minus += 60000*(int(s[1]) - int(e[1]))
            plus += 1000*(int(e[0]) - int(s[0]))
            ms[x] = plus - minus

        return sum(ms.values())/len(start_dic)













# Press the green button in the gutter to run the script.
if __name__ == '__develeap_test__':
     print_hi('PyCharm')
     print(ret_first_line())
     print(returnCountErrors())
     print(count_transaction())
     print(faster_transaction())
     print(avg_transaction_in_milliseconds())







































   # print(datetime.time(hour=9, minute=56, second=50, microsecond=293).isoformat(timespec='seconds'))

#print(datetime.timedelta(end_dic[list_to_cell[2][:5]], start_dic[list_to_cell[1]]))milliseconds



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
