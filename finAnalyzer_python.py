#  expecting hashmap/array as input
import numpy_financial as np

DISCOUNT_RATE = 0.05
print('\n')



General_Data =  {
    
	'id_building' : [1,2,3,4],
	'type_of_building' : ['civil','civil','other','other'],
    'dimension' : [40,55,100,300],
    'floor_number' : [1,1,2,3],
    'year_construction' : [1978,1999,2001,2015],
    'thermal_insulation' : ['good','decent','bad','good']
}	

Energy_Consumption = {
    'id_building' : [1,1],
    'year' : [2023,2023],
    'month' : ['Jan', 'Feb'],
    'type_energy' : ['Electricity', 'Natural Gas'],
    'unit_consumption' : [5000,3000],
    'energetic_cost' : [800,450]
}

Data_Input = {
    'id_building' : [1,1,1],
    'intervention' : ['thermal_cladding','photovoltaic panels','led lightning'],
    'duration' : [10,15,10],
    'expected_savings' : [2000,2500,300],
    'intervention_cost' : [20000,8000,500],
    'unit_price' : [0.5,0.5,0.5],
    'annual_savings' : [1000,1250,150],
    'total_savings' : [10000,18750,1500]
}

def Total_Investment_Cost(Data_Input, id_building):

    search = Data_Input['id_building']
    intervent = Data_Input['intervention_cost']
    building_cost = []

    for index in range(len(search)):
        
        if search[index] == id_building:
        
            building_cost.append(intervent[index])

    return sum(building_cost)

def Total_Annual_Cash_Flow(Data_Input, id_building):

    search = Data_Input['id_building']
    savings = Data_Input['annual_savings']
    building_savings = []

    for index in range(len(search)):

        if search[index] == id_building:
        
            building_savings.append(savings[index])

    return sum(building_savings)
    
def Avrg_Investment_Duration(Data_Input, id_building):

    search = Data_Input['id_building']
    savings = Data_Input['expected_savings']
    duration = Data_Input['duration']

    output = []
    sav_id = []

    for index in range(len(search)):

        if search[index] == id_building:
            
            output.append(savings[index] * duration[index])
            sav_id.append(savings[index])

    sd = sum(sav_id)

    return sum(output)/sd 

def Overall_Roi(Data_Input, id_building):

    search = Data_Input['id_building']
    savings = Data_Input['total_savings']
    cost = Data_Input['intervention_cost']

    cost_id = []
    sav_id = []

    for index in range(len(search)):

        if search[index] == id_building:
        
            cost_id.append(cost[index])
            sav_id.append(savings[index])

    output = (sum(sav_id)-sum(cost_id))/sum(cost_id)

    return print('Overall ROI (%) , Gain obtained from the investment expressed as a percentage' , round(output * 100,3) , '\n')

def Overall_Npv(Data_Input, id_building):

    search = Data_Input['id_building']
    savings = Data_Input['total_savings']
    tot = Total_Investment_Cost(Data_Input, id_building)
    sav = []
    
    for index in range(len(search)):

        if search[index] == id_building:
        
            sav.append(savings[index])

    
    npv = np.npv(DISCOUNT_RATE, [tot, sum(sav)])
    
    return print('Overall NPV , Present value of all future savings generated by the investment, discounted to the present' , round(npv,3) , '\n')

def Overall_IRR(Data_Input, id_building):

    search = Data_Input['id_building']
    savings = Data_Input['total_savings']

    sav = []
    sav.append( - Total_Investment_Cost(Data_Input,id_building))

    for index in range(len(search)):

        if search[index] == id_building:
        
            sav.append(savings[index])

    irr = np.irr(sav)
    
    return print('Overall IRR (%) , the percentage return that the investment is generating' , round(irr, 3) , '\n')

def DebtRatio(Data_Input, id_building):

    output = Total_Annual_Cash_Flow(Data_Input, id_building) / (Total_Investment_Cost(Data_Input,1)/Avrg_Investment_Duration(Data_Input,1))
    
    return print('Debt Service Coverage Ratio' , round(output, 3) , 'The ability to cover the investment with the savings obtained from the investment. DSCR > 1 indicates cash flows are sufficient to cover the debt. DSCR < 1 indicates cash flows are insufficient to cover the deb\n')

            
print('Total cost of all interventions'  ,   Total_Investment_Cost(Data_Input, 1) , '\n')
print('Total Annual Cash Flow, Aggregate annual savings of all interventions' , Total_Annual_Cash_Flow(Data_Input,1), '\n')
print('Average Investment Duration, Cost-Weighted average duration', round(Avrg_Investment_Duration(Data_Input, 1),3) ,'\n')
Overall_Roi(Data_Input, 1)
Overall_Npv(Data_Input, 1)
Overall_IRR(Data_Input, 1)
DebtRatio(Data_Input, 1)