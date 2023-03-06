#Import re, pandas
import re, pandas as pd

#Read in a csv as a data frame

df = pd.read_csv('')
df['Notes'].fillna('', inplace = True)

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
ic1_regex = re.compile(r'*|'.join(ic1).replace("| ","|"), re.I)
ic2_regex = re.compile(r'|'.join(ic2).replace("| ","|"), re.I)
ic3_regex = re.compile(r'|'.join(ic3).replace("| ","|"), re.I)
ic4_regex = re.compile(r'|'.join(ic4).replace("| ","|"), re.I)
ic5_regex = re.compile(r'|'.join(ic5).replace("| ","|"), re.I)
ic6_regex = re.compile(r'|'.join(ic6).replace("| ","|"), re.I)

#Create regex for exclusion terms for Criteria 1-3 and 5
ec1_regex = re.compile(r'|'.join(ec1).replace("| ","|"), re.I)
ec2_regex = re.compile(r'|'.join(ec2).replace("| ","|"), re.I)
ec3_regex = re.compile(r'|'.join(ec3).replace("| ","|"), re.I)
ec5_regex = re.compile(r'|'.join(ec5).replace("| ","|"), re.I)

#Create lists to record if criteria are met
cr1_list = []
cr2_list = []
cr3_list = []
cr4_list = []
cr5_list = []
cr6_list = []
for text in df['Notes']:
    print(text)
    #Check if text meets criteria 1
    cr1_list = cr1_list + [bool(ic1_regex.search(text)) == True and bool(ec1_regex.search(text)) == False]
    #Check if text meets criteria 2
    cr2_list = cr2_list + [bool(ic2_regex.search(text)) == True and bool(ec2_regex.search(text)) == False]
    #Check if text meets criteria 3
    cr3_list =cr3_list + [bool(ic3_regex.search(text)) == True and bool(ec3_regex.search(text)) == False]
    #Check if text meets criteria 4
    cr4_list = cr4_list +[bool(ic4_regex.search(text)) == True]
    #Check if text meets criteria 5
    cr5_list = cr5_list +[bool(ic5_regex.search(text)) == True and bool(ec5_regex.search(text)) == False]
    #Check if text meets criteria 6 
    cr6_list = cr6_list +[bool(ic6_regex.search(text)) == True]
    
#Create a dataframe of criteria
criteria_df = pd.DataFrame({'Criteria 1' : cr1_list, 'Criteria 2' : cr2_list, 'Criteria 3' : cr3_list, 'Criteria 4' : cr4_list, 'Criteria 5' : cr5_list, 'Criteria 6' : cr6_list})

#Check if Level 1 is met for any criteria
Level_1 =pd.DataFrame({'Level 1' : criteria_df.any(axis = 1)})

#Concatenate dataframes
total_df = pd.concat([criteria_df, Level_1], axis = 1)

#Write dataframe to csv
total_df.to_csv('Level_1.csv')