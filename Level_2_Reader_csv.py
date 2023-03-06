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
ec2_string = ("meth mile, [oiam]meth, meth[aieou], amethia, methotr, methanol, indometh, betameth, dexameth, methocarb,"
"prometh, not meth, no meth, Dextromethorphan, sulfameth, simethic, methado, methodo, something, samething, Methuen,"
"metheun, method, methyl")
ec2 = ec2_string.split(',')

#Create list of Inclusion terms for Criteria 3
ic3_string = ("Speedball, speed ball, smoked crack, smoke crack, smoking crack, smokes crack, use crack, on crack, used crack,"
"crack pipe, took upper, under the influence of upper") 
ic3 = ic3_string.split(',')

#Create list of exclusion terms for Criteria 3
ec3_string = "crackle"
ec3 = ec3_string.split(',')

#Create list of Inclusion terms for Criteria 4
ic4_string = ("MDMA, bath salt, Cathinone, ecstasy, ecstasy, molly")
ic4 = ic4_string.split(',')

#Create list of exclusion terms for Criteria 4
ec4_string = "rn molly, molly rn"
ec4 = ec4_string.split(',')


#Create list of Inclusion terms for Criteria 5 list a
ic5_string_a = ("Adderall, addarall, adderol, dextroamph, methylph, Dexedrine, Ritalin, Concerta,"
"Strattera, atomoxetine, Vyvanse, focalin, methylin, procentra, zenzedi, evekeo, metadate, adzenys, aptensio, cotempla, daytrana,"
"dyanavel, mydayis, quillichew, quillivant, lisdex")
ic5_a = ic5_string_a.split(',')

#Create list of Inclusion terms for Criteria 5 list b
ic5_string_b = ("Needle, Syringe, shot up, non prescr, non-prescr, not prescr, snort, inject, crush, misuse, recreational")
ic5_b = ic5_string_b.split(',')

#Create list of exclusion terms for Criteria 5 list b word "Needle"
ec5_string_n = ("seizure, g needle, needle decom, defer any needle, fear, needless, pins, kneed, needle exc, afraid, terri, no "
"needle, diabe.*insulin, insulin.*diab")
ec5_n = ec5_string_n.split(',')

#Create list of exclusion terms for Criteria 5 list b word "Syringe"
ec5_string_s = ("seizure, needless, drawn into a syringe, diabe.*insulin, insulin.*diab")
ec5_s = ec5_string_s.split(',')

#Create list of exclusion terms for Criteria 5 list b word "inject"
ec5_string_i = ("seizure, no inject, injection for anaphy, diabe.*insulin, insulin.*diab")
ec5_i = ec5_string_i.split(',')

#Create list of exclusion terms for Criteria 5 list b word "crush"
ec5_string_c = ("crush inj, crush soda")
ec5_c = ec5_string_c.split(',')

#Create list of exclusion terms for Criteria 5 list b word "misuse"
ec5_string_m = ("not misuse, no miuse")
ec5_m = ec5_string_m.split(',')

#Create list of exclusion terms for Criteria 5 list b word "recreational"
ec5_string_r = ("did not endorse any recreat, denies the use of recreat, does not participate in recreat, denies use of "
"recreat, denies using any recreat, no signs of recreate, does not use recreat, not recreat, no recreat, denies any recreat, denie"
"[sd] recreat")
ec5_r = ec5_string_r.split(',')

#Create list of exclusion terms for Criteria 5 list c
ec5_string_lc = ("adhd, as prescri, has a prescri, unrespons, uncons")
ec5_lc = ec5_string_lc.split(',')

#Create list of Inclusion terms for Criteria 6 list a
ic6_string_a = ("Adderall, adderol, dextroamph, methylph, Dexedrine, Ritalin, Concerta, Strattera,"
"atomoxetine, Vyvanse, focalin, methylin, procentra, zenzedi, evekeo, metadate, adzenys, aptensio, cotempla, daytrana,"
"dyanavel, mydayis, quillichew, quillivant, lisdex")
ic6_a = ic6_string_a.split(',')

#Create list of Inclusion terms for Criteria 6 list b
ic6_string_b = "overdose, od, o.d"
ic6_b = ic6_string_b.split(',')

#Create list of exclusion terms for Criteria 6 list c
ec6_string_c = ("unrespons, uncons")
ec6_c = ec6_string_c.split(',')

#Create list of Inclusion terms for Criteria 7
ic7_string = "cocaine related, F14.10, F14.11, F14.20, F14.21, F15.10, F15.11, F15.20, F15.21, F16"
ic7 = ic7_string.split(',')

#No exclusion terms for Criteria 7

#Create regex for inclusion terms for Criteria 1-4
ic1_regex = re.compile(r'*|'.join(ic1).replace("| ","|"), re.I)
ic2_regex = re.compile(r'|'.join(ic2).replace("| ","|"), re.I)
ic3_regex = re.compile(r'|'.join(ic3).replace("| ","|"), re.I)
ic4_regex = re.compile(r'|'.join(ic4).replace("| ","|"), re.I)

#Create regex for inclusion terms for Criteria 5
ic5_a_regex = re.compile(r'|'.join(ic5_a).replace("| ","|"), re.I)
ic5_b_regex = re.compile(r'|'.join(ic5_b).replace("| ","|"), re.I)


#Create regex for inclusion terms for Criteria 6
ic6_a_regex = re.compile(r'|'.join(ic6_a).replace("| ","|"), re.I)
ic6_b_regex = re.compile(r'|'.join(ic6_b).replace("| ","|"), re.I)

#Create regex for inclusion terms for Criteria 7
ic7_regex = re.compile(r'*|'.join(ic7).replace("| ","|"), re.I)


#Create regex for exclusion terms for Criteria 1-4
ec1_regex = re.compile(r'|'.join(ec1).replace("| ","|"), re.I)
ec2_regex = re.compile(r'|'.join(ec2).replace("| ","|"), re.I)
ec3_regex = re.compile(r'|'.join(ec3).replace("| ","|"), re.I)
ec4_regex = re.compile(r'|'.join(ec4).replace("| ","|"), re.I)

#Create regex for exclusion terms for Criteria 5 list b
ec5_n_regex = re.compile(r'|'.join(ec5_n).replace("| ","|"), re.I)
ec5_s_regex = re.compile(r'|'.join(ec5_s).replace("| ","|"), re.I)
ec5_i_regex = re.compile(r'|'.join(ec5_i).replace("| ","|"), re.I)
ec5_c_regex = re.compile(r'|'.join(ec5_c).replace("| ","|"), re.I)
ec5_m_regex = re.compile(r'|'.join(ec5_m).replace("| ","|"), re.I)
ec5_r_regex = re.compile(r'|'.join(ec5_r).replace("| ","|"), re.I)
#Create regex for exclusion terms for Criteria 5 list c
ec5_lc_regex = re.compile(r'|'.join(ec5_lc).replace("| ","|"), re.I)

#Create regex for exclusion terms for Criteria 6
ec6_c_regex = re.compile(r'|'.join(ec6_c).replace("| ","|"), re.I)

#Create lists to record if criteria are met
cr1_list = []
cr2_list = []
cr3_list = []
cr4_list = []
cr5_list = []
cr6_list = []
cr7_list = []
for age, text in zip(df['Age'], df['Notes']):
    #Check if Age is greater than 14
    if age > 14:
        #Check if text meets criteria 1
        cr1_list = cr1_list + [bool(ic1_regex.search(text)) == True and bool(ec1_regex.search(text)) == False]
        #Check if text meets criteria 2
        cr2_list = cr2_list + [bool(ic2_regex.search(text)) == True and bool(ec2_regex.search(text)) == False]
        #Check if text meets criteria 3
        cr3_list =cr3_list + [bool(ic3_regex.search(text)) == True and bool(ec3_regex.search(text)) == False]
        #Check if text meets criteria 4
        cr4_list = cr4_list +[bool(ic4_regex.search(text)) == True]
        #Check if text meets criteria 5
        if bool(ic5_a_regex.search(text)) == True and bool(ic5_b_regex.search(text)) == True:
            #Use loop to check if exclusion criteria for individual words are met
            #Create list to store True/False Values
            tf = []
            for word in ic5_b_regex.findall(text):
                #Change word to all lowercase
                word = str.lower(word)
                #Check for list b words with extra exclusion criteria
                if word == 'needle':
                    tf = tf +[bool(ec5_n_regex.search(text)) == False and bool(ec5_lc_regex.search(text)) == False]
                elif word == 'syringe':
                    tf = tf +[bool(ec5_s_regex.search(text)) == False and bool(ec5_lc_regex.search(text)) == False]
                elif word == 'inject':
                    tf = tf +[bool(ec5_s_regex.search(text)) == False and bool(ec5_lc_regex.search(text)) == False]
                elif word == 'crush':
                    tf = tf +[bool(ec5_c_regex.search(text)) == False and bool(ec5_lc_regex.search(text)) == False]
                elif word == 'misuse':
                    tf = tf +[bool(ec5_c_regex.search(text)) == False and bool(ec5_lc_regex.search(text)) == False]
                elif word == 'recreational':
                    tf = tf +[bool(ec5_r_regex.search(text)) == False and bool(ec5_lc_regex.search(text)) == False]
                #check if list b word is "snort." If so, do not need to check exclusion criteria in list c
                elif word == 'snort':
                    tf = tf + [True]
                #For any other word in list b, determine if list c exclusion criteria are met
                else:
                    tf = tf + [bool(ec5_lc_regex.search(text)) == False]
            if sum(tf) > 0:
                cr5_list = cr5_list + [True]
            else:
                cr5_list = cr5_list + [False]
        else: 
          cr5_list = cr5_list + [False] 
        #Check if text meets criteria 6 
        cr6_list = cr6_list +[bool(ic6_a_regex.search(text)) == True and bool(ic6_b_regex.search(text)) == True and bool(ec6_c_regex.search(text)) == False]
        #Check if text meets criteria 7 
        cr7_list = cr7_list +[bool(ic7_regex.search(text)) == True]
    else:
        #If age is not greater than 14, return all false values
        for i in [cr1_list, cr2_list, cr3_list, cr4_list, cr5_list, cr6_list, cr7_list]:
            i = i.append(False)
#Create a dataframe of criteria
criteria_df = pd.DataFrame({'Criteria 1' : cr1_list, 'Criteria 2' : cr2_list, 'Criteria 3' : cr3_list, 'Criteria 4' : cr4_list, 'Criteria 5' : cr5_list, 'Criteria 6' : cr6_list, 'Criteria 7' : cr7_list})

#Check if Level 2 is met for any criteria
Level_2 =pd.DataFrame({'Level 2' : criteria_df.any(axis = 1)})

#Concatenate dataframes
total_df = pd.concat([criteria_df, Level_2], axis =1 )

#Write dataframe to csv
total_df.to_csv('Level_2.csv')
