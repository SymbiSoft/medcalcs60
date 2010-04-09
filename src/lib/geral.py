# -*- coding: latin-1 -*-
# ###########################################################
#            Teste Geral                                    #
# ###########################################################
from geralclass import *		
class BMI (MedCalc):
	def __init__ (self):
		self.data = [(u'Peso (kg)','number',0),(u'Altura (cm)','number',0)]
		
	def show (self):
		W = self.getform()[0][2]
		H = self.getform()[1][2]/100.0
		appuifw.note(u"IMC = %f"%(W / H ** 2), "info") 

'''
BSA = (W ** 0.425 x H ** 0.725) x 0.007184
'''		
class BSA (MedCalc):
	def __init__ (self):
		self.data = [(u"Peso (kg)",'number',0),(u"Altura (cm)",'number',0)]

	def show (self):
		W = self.getform()[0][2]
		H = self.getform()[1][2]
		data = (W ** 0.425 * H ** 0.725) * 0.007184
		appuifw.note(u"BSA = %f"%data, "info") 
		

class BEE (MedCalc):
	def __init__ (self):
		act = [u'Repouso',u'Deambulando']
		sexo = [u'homem',u'mulher']
		self.data = [(u'Sexo','combo',(sexo,0)),(u"Peso (kg)",'number',0),(u'Altura (cm)','number',0),(u"Idade",'number',0),(u"Atividade","combo",(act,0))]
		
	def show (self):
		W = self.getform()[1][2]
		H = self.getform()[2][2]
		A = self.getform()[3][2]
		if (self.getform()[0][2][1] == 0):
			bee = 66.5 + (13.75*W) + (5.003*H) - (6.775*A)
		else:
			bee = 655.1 + (9.563*W) + (1.850*H) - (4.676*A)
		appuifw.note(u"Gasto de Energia Basal = %.0f kcal"%bee,"info")
		
class AnestesiaRisk(MedCalcList):
	def __init__ (self):
		self.data = [
		u'Hipertens�o arterial controlada ',
		u'Diabetes controlada',
		u'Doen�a vascular perif�rica controlada',
		u'Doen�a pulm. obstr. cr�nica controlada',
		u'Doen�a Sistemica Controlada',
		u'angina inst. c/ hep EV ou nitrog. ',
		u'bal�o pr�-op. intra-a�rt',
		u'insufici�ncia card�aca c/ edema pulm. ou perif. ',
		u'hipertens�o n�o controlada ',
		u'insufic. renal (creatinina s�rica> 140�mol / L ',
		u'outros debilitante doen�a sist�mica',
		u'Reoperation',
		u'Valvula e cirurg. coronaria',
		u'Multiplas valvulas',
		u'Ventricular aneurisma esq.',
		u'Reparo de defeito septo ventricular ap�s IM',
		u'Bypass de vasos difusos ou calcificados'
		]
		
	def show (self):
		soma = 0
		print self._f