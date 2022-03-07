# Mohamed Yasser Anwar Mahmoud AlKayd
# DNA Cut-Site Program

# - Start of the Program -

sequence = input("Enter DNA sequence: ")
cut_site = input("Enter cut-site sequence: ")
 
if cut_site in sequence:#determine what the cut_site is
    print(sequence.count(cut_site)) #figure out The DNA sequence can be cut at the location that matches
else:#lack of cut_site location means it is equal to 0
    print("0")

# - End of the Program -