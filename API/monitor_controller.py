import sys
sys.path.insert(0, '../API')
sys.path.insert(0, '../hl7parser')
from hl7parser import patient, measure, channel
from Queue import Queue
from alarm_controller import AlarmController

class MonitorController:
	lbMap = {1:("lbTemperatura","C"), 3:("lbPressao","mmHg"), 4:("lbO2","%"), 5:("lbFC","bpm")}

	def __init__(self, monitGui, ident, alarmForm):
		self.monitGui = monitGui
		self.ident = ident
		self.fila = Queue()
		self.alarms = AlarmController(alarmForm)
		self.alarmresp = None
		self.monitGui.alertTemperatura.show()

	def atualizaGui(self):
		paciente = self.fila.get()
		self.setLabel(self.monitGui.lbPaciente, paciente.name)
		self.setLabel(self.monitGui.lbMonitor, self.ident)
		for m in paciente.measures:
			if m.cod == 6:
				continue
			lb = getattr(self.monitGui,self.lbMap[m.cod][0])
			un = self.lbMap[m.cod][1]
			if m.cod == 3:
				self.setLabel(lb, ("%s/%s" % (m.channels[0].data[0], m.channels[1].data[0])), un)
			else:
				self.setLabel(lb, str(m.channels[0].data[0]), un)
		
		self.alarmresp = self.alarms.check(paciente.measures)
		print self.alarmresp

		'''	
		if self.alarmresp[0] == True:
			self.monitGui.alertPressao.show()
		else:
			self.monitGui.alertPressao.hide()
		
		if self.alarmresp[1] == True:
			self.monitGui.alertO2.show()
		else:
			self.monitGui.alertO2.hide()
		'''
	
		if self.alarmresp[2] == True:
			self.monitGui.alertTemperatura.setText("OK")
		else:
			self.monitGui.alertTemperatura.setText("NOT")
		
		'''
		if self.alarmresp[3] == True:
			self.monitGui.alertFC.show()
		else:
			self.monitGui.alertFC.hide()
		'''
		
	def setLabel(self, label, dado, unidade = ''):
		label.setText("%s %s" % (dado, unidade))

	def addPaciente(self, paciente):
		self.fila.put(paciente)

	def atualizaIndividual(self):
		pass

