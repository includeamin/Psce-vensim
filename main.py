import envoltura as env


envoltura_Temp = env.envoltura("SUN1103- fc DI 75.CAB" , "SR4 - Sari.NEW",12 , 360 ,36 , 52
                      , "sugarbeet_calendar.agro")

envoltura_Temp.RunSimular(199)

print(envoltura_Temp.variables)

