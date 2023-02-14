#Import os and re
import os, re

#Create list of Inclusion terms for Criteria 1
ic1_string = "stimulant, cocaine, cocain, coaine, coke, amphet, cacaine"
ic1 = ic1_string.split(',')

#Create list of exclusion terms for Criteria 1
ec1_string = ("not stimulant, no stimulant, denies stimulant, denied stimulant, denies any stimulant, denied any stimulant,"  
"denies cocaine, denied cocaine, denies any cocaine, denied any cocaine, not cocaine, no cocaine, not coke, no coke, diet coke,"  
"rum and coke, jack and coke, bottle of, can of, glass of, cup of, denies amphet, denied amphet, denies any amphet, denied any " 
"amphet, not amphet, no amphet, coke cola, coke plant, over the counter, over-the-counter, vanilla coke, drink of")
ec1 = ec1_string.split(',')

#Create list of Inclusion terms for Criteria 2
ic2_string = "meth" 
ic2 = ic2_string.split(',')

#Create list of exclusion terms for Criteria 2
ec2_string = ("denies meth, denied meth, denies any meth, denied any meth, meth mile, [oiam]meth, meth[aieou], amethia," 
"methotr, methanol, indometh, betameth, dexameth, methocarb, prometh, not meth, no meth, Dextromethorphan, sulfameth," 
"simethic, methado, methodo, something, samething, Methuen, metheun, method, methyl")
ec2 = ec2_string.split(',')

#Create list of Inclusion terms for Criteria 3
ic3_string = ("Speedball, speed ball, smoked crack, smoke crack, smoking crack, smokes crack, use crack, on crack, used crack," 
"crack pipe, took upper, under the influence of upper") 
ic3 = ic3_string.split(',')

#Create list of exclusion terms for Criteria 3
ec3_string = "crackle"
ec3 = ec3_string.split(',')

#Create list of Inclusion terms for Criteria 4
ic4_string = ("Adderall, addarall, adderol, dextroamph, methylph, Dexedrine, Ritalin, Concerta, Strattera, atomoxetine," 
"Vyvanse, focalin, methylin, procentra, zenzedi, evekeo, metadate, adzenys, aptensio, cotempla, daytrana, dyanavel, mydayis," 
"quillichew, quillivant, lisdex")
ic4 = ic4_string.split(',')

#No exclusion terms for Criteria 4

#Create list of Inclusion terms for Criteria 5
ic5_string = "MDMA, bath salt, Cathinone, ecstasy, ecstacy, molly"
ic5 = ic5_string.split(',')

#Create list of exclusion terms for Criteria 5
ec5_string = "rn molly, molly rn"
ec5 = ec5_string.split(',')

#Create list of Inclusion terms for Criteria 6
ic6_string = "cocaine related, F14.10, F14.11, F14.20, F14.21, F15.10, F15.11, F15.20, F15.21, F16"
ic6 = ic6_string.split(',')

#No exclusion terms for Criteria 6


#Create regex for inclusion terms for Criteria 1-6
ic1_regex = re.compile(r'|'.join(ic1), re.I)
ic2_regex = re.compile(r'|'.join(ic2), re.I)
ic3_regex = re.compile(r'|'.join(ic3), re.I)
ic4_regex = re.compile(r'|'.join(ic4), re.I)
ic5_regex = re.compile(r'|'.join(ic5), re.I)
ic6_regex = re.compile(r'|'.join(ic6), re.I)

#Create regex for exclusion terms for Criteria 1-3 and 5
ec1_regex = re.compile(r'|'.join(ec1), re.I)
ec2_regex = re.compile(r'|'.join(ec2), re.I)
ec3_regex = re.compile(r'|'.join(ec3), re.I)
ec5_regex = re.compile(r'|'.join(ec5), re.I)


#Create dictionary to store values for files
level1 = {}
#Create loop for files in directory
for file in os.listdir(''):
    #Open the file
    with open (os.path.join('', file)) as f:
        read =f.read()
        #Create list to store all met criteria for a file
        cr_list = []
        #Check if file meets criteria 1
        if bool(ic1_regex.search(read)) == True and not bool(ec1_regex.search(read)) == True:
            cr_list = cr_list + ["criteria 1"]
        #Check if file meets criteria 2
        if bool(ic2_regex.search(read)) == True and not bool(ec2_regex.search(read)) == True:
            cr_list = cr_list +["criteria 2"]
        #Check if file meets criteria 3
        if bool(ic3_regex.search(read)) == True and not bool(ec3_regex.search(read)) == True:
            cr_list =cr_list + ["criteria 3"]
        #Check if file meets criteria 4
        if bool(ic4_regex.search(read)) == True:
            cr_list = cr_list +["criteria 4"]
        #Check if file meets criteria 5
        if bool(ic5_regex.search(read)) == True and not bool(ec5_regex.search(read)) == True:
            cr_list = cr_list +["criteria 5"]
        #Check if file meets criteria 6
        if bool(ic6_regex.search(read)) == True: 
            cr_list = cr_list +["criteria 6"]
        #Check if any criteria were met for a given file. If so, add the file to the dictionary
        if len(cr_list) != 0:
            level1[file] = cr_list
print(level1)
        

        