from tinamit.BF import ModeloBF
from variables import *
import numpy as np
import os
import  shutil
import MyPcse as pcs

# https://tinamit.readthedocs.io/es/latest/docu/BF.html#tinamit.BF.ModeloBF
class envoltura(ModeloBF):

    def __init__(self,cropDir,soilDir,wav,co2 ,lat ,long,argoDir):
        self.inputDict = {}
        self.variables ={}
        self.cropDir = cropDir
        self.soilDir = soilDir
        #self.site = (wav,co2)
        self.argoDir = argoDir
        self.lat = lat
        self.long = long
        self.wave = wav
        self.co2=co2
        self.OutPutVars = ["DVS","LAI","RD","SM","TAGP","TRA","TWLV","TWRT","TWSO","TWST","WWLOW","day"]


#https://tinamit.readthedocs.io/es/latest/docu/BF.html#tinamit.BF.ModeloBF.leer_vals
    # This function must change the value of variables in the biophysical model.
    def cambiar_vals_modelo_interno(self, values):

        print("Update output values values")

        for name in values:

            for code in self.variables:
             if code == name:
                 self.variables[code]["val"]=values[name]



    def updateIngrValues(self):
        allinputs ={}
        cropsInputVars =pcs.cropLoader(self.cropDir).items()
        soilVarsInput = pcs.soilLoader(self.soilDir).items()
        for item in cropsInputVars:
            allinputs.update({item[0]:item[1]})
        for item in soilVarsInput:
            allinputs.update({item[0]:item[1]})


        for item in vars_ingreso_PCSE:
            if allinputs.__contains__(item):

               self.variables[item]["val"]= allinputs[item]


    def merge_two_dicts(self,x, y):
        z = x.copy()  # start with x's keys and values
        z.update(y)  # modifies z with y's keys and values & returns None
        return z


    def incrementar(self, paso):
        pass

    def leer_vals(self):
        pass

    def cerrar_modelo(self):
        pass

    def obt_unidad_tiempo(self):
        return 'día'

    # 1
    def inic_vars(self):
        self.variables.clear()


        for number, dic in vars_PCSE.items():



            self.variables[dic["cód"]] = {
                "val": [],
                "unids": dic["unids"],
                "ingr": dic["ingr"],
                "egr": dic["egr"],
            }


    def RunSimular(self,day):
        self.inic_vars()
        model = pcs.modelInit(self.cropDir,self.soilDir,self.wave,self.co2,self.lat,self.long,self.argoDir)
        model.run(day)
        output = model.get_output()

        print(output[day].pop('day'))
        #output[day]["day"] =day
        #print(output[day])
        self.cambiar_vals_modelo_interno(output[day])
        self.updateIngrValues()
        #print(self.variables)
        print("variable dictionary update for " +str(day)+" days")




    def leer_vals_inic(self):
        pass

    def iniciar_modelo(self, tiempo_final, nombre_corrida):
        self.direc_trabajo = os.path.join(self.direc_base, '_temp', nombre_corrida)
        if os.path.isdir(self.direc_trabajo):
            shutil.rmtree(self.direc_trabajo)
        os.makedirs(self.direc_trabajo)

        super().iniciar_modelo(self,tiempo_final,nombre_corrida)


