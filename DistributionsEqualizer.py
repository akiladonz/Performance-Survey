def Modify_Content(Fraction_List,Count_List):
		Zero_count=0
		One_count=0
		Two_count=0
		Three_count=0
		Four_count=0
		Five_count=0
		Six_count=5
		Seven_count=0
		Eight_count=5
		Nine_count=0
		Zero_fractions=[]
		One_fractions=[]
		Two_fractions=[]
		Three_fractions=[]
		Four_fractions=[]
		Five_fractions=[]
		Six_fractions=[]
		Seven_fractions=[]
		Eight_fractions=[]
		Nine_fractions=[]
		Zero_indexes=[]
		One_indexes=[]
		Two_indexes=[]
		Three_indexes=[]
		Four_indexes=[]
		Five_indexes=[]
		Six_indexes=[]
		Seven_indexes=[]
		Eight_indexes=[]
		Nine_indexes=[]
		b=0
		for b in range(0,len(Fraction_List),1):
				if 0.0<Fraction_List[b]<=0.1 and Zero_count<Count_List[0]:
								Zero_fractions.append(Fraction_List[b])
								Zero_indexes.append(b)
								Zero_count=Zero_count+1
				if 0.1 <Fraction_List[b]<=0.2 and One_count<Count_List[1]:
								One_fractions.append(Fraction_List[b])
								One_indexes.append(b)
								One_count=One_count+1
				if 0.2<Fraction_List[b]<=0.3 and Two_count<Count_List[2]:
								Two_fractions.append(Fraction_List[b])
								Two_indexes.append(b)
								Two_count=Two_count+1
				if 0.3<Fraction_List[b]<=0.4 and Three_count<Count_List[3]:
								Three_fractions.append(Fraction_List[b])
								Three_indexes.append(b)
								Three_count=Three_count+1
				if 0.4<Fraction_List[b]<=0.5 and Four_count<Count_List[4]:
								Four_fractions.append(Fraction_List[b])
								Four_indexes.append(b)
								Four_count=Four_count+1
				if 0.5<Fraction_List[b]<=0.6 and Five_count<Count_List[5]:
								Five_fractions.append(Fraction_List[b])
								Five_indexes.append(b)
								Five_count=Five_count+1
				if 0.6<Fraction_List[b]<=0.7 and Six_count<Count_List[6]:
								Six_fractions.append(Fraction_List[b])
								Six_indexes.append(b)
								Six_count=Six_count+1
				if 0.7<Fraction_List[b]<=0.8 and Seven_count<Count_List[7]:
								Seven_fractions.append(Fraction_List[b])
								Seven_indexes.append(b)
								Seven_count=Seven_count+1
				if 0.8<Fraction_List[b]<=0.9 and Eight_count<Count_List[8]:
								Eight_fractions.append(Fraction_List[b])
								Eight_indexes.append(b)
								Eight_count=Eight_count+1
				if 0.9<Fraction_List[b]<=1.0 and Nine_count<Count_List[9]:
								Nine_fractions.append(Fraction_List[b])
								Nine_indexes.append(b)
								Nine_count=Zero_count+1
		Combined_Fractions= Zero_fractions+One_fractions+Two_fractions+Three_fractions+Four_fractions+Five_fractions+Six_fractions+Seven_fractions+Eight_fractions+Nine_fractions 
		Combined_indexes= Zero_indexes+One_indexes+Two_indexes+Three_indexes+Four_indexes+Five_indexes+Six_indexes+Seven_indexes+Eight_indexes+Nine_indexes 
		return Combined_Fractions, Combined_indexes                                                       