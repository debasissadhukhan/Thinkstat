import Survey
table = Survey.Pregnancies()
table.ReadRecords()
print ('Number of pregnancies', len(table.records))
print(table.GetFields())