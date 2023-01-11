# -*- coding: utf-8 -*-
"""
Created on April 09 2018

This file is not yet finished.

V3 - complete task 1
also had to update compatability with python 3's true divide outputing floats instead of ints

Forked from O2upshift_OD420only_best_lessruns.py

TODOs
high priority
1. make a way to include 2 simultaneous runs - i.e. change the injection times for the last 48 wells. 
written, not yet tested
loads xml file without error
loads method file without error - 3-4

2. replace cell injection step at time 0 with alpha keto acid injection at some variable time
version 3-5 - add the injection step without an if statement
version 3-5 runs fine
version 3-6 add a conditional statement to the injection
version 3-7 change condition identifier to one from a manual method - doesn't work
version 3-8

low priority
1. include a variable to change the time of each loop
"""
"""
OLD NOTES
This version has less injections so that growth rate can be quantified better 
Also switches shaking mode to fixed time just in case thats the problem (30s)
Kinetic measurement is now for 4 hours

Need to do the following
1. make it so that injection is refill before every injection - Done
2. make it so that OD600 is no longer included - Done
3. make it so that the trigger OD's are more easily editable - Done
4. make it so that injection speed is 200 - Done
5. Make it so that the default casette is the large one - Done


3. import the kinetic loop
4. change injection condition
5. include early OD measurement
6. include early injection
7. change shaking strip

@author: Brian
"""



#function for naming the cycles that the injector should inject on
def cyclefunc(i):
    return str(2*(i%48)+1)

startketotime = '9' #- cycle to start the alphaketoacid injection

import numpy as np

#File to write an xml  file 
target = open('/home/brian/work/grive/Brian/xmlfiles/ketoacidupshift3-9.xml', 'w')


ODstart = [.14,.16,.18,.2] #sets the values to start injection at



print("Truncating the file.  Goodbye!")
target.truncate()

numberofwells = 96
numberofindexes= numberofwells *2 + 7 +2  #extra one added for the alphaketoacid conditional 3-6 and injection 3-8

indexVec =  range(numberofindexes) #start at 0

indexit = iter(indexVec)

noref = 3
numberofSettings = 6
SettingsID = np.array(range(numberofSettings)) + 3
#an extra one is added for the alphaketoacid condition keto3-6
#potential for a bug here because I'm not remembering my logic here. Pretty sure this is ok
ConditionID = np.array(range(numberofwells+1)) + SettingsID[-1] + 1  
InjectionID = np.array(range(numberofwells+1)) + ConditionID[-1] + 1
PartofPlateID = np.array(range(numberofwells)) +InjectionID[-1] + 1

iterSID = iter(SettingsID)
iterCID = iter(ConditionID)
iterIID  = iter(InjectionID )
iterPID  = iter(PartofPlateID)


refIDvec = np.concatenate((InjectionID,ConditionID,SettingsID))



####make the header

target.write("""<?xml version="1.0"?> <MethodStrip xmlns="http://schemas.tecan.com/at/dragonfly/operations/xaml" xmlns:sco="clr-namespace:System.Collections.ObjectModel;assembly=System" xmlns:tadods="clr-namespace:Tecan.At.Dragonfly.Operation.Data.Symbio;assembly=Tecan.At.Dragonfly.Operation.Data" xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml" IsApp="False"><MethodStrip.DataLabels>""")

#for element in refIDvec:
for element in list(set(refIDvec)): #this version orders the refIDs
    target.write('<x:Reference>__ReferenceID'+str(element)+'</x:Reference>')
    
 
target.write("""</MethodStrip.DataLabels><MethodStrip.Plates><x:Reference>__ReferenceID0</x:Reference></MethodStrip.Plates><InstrumentStrip><PlateStrip DefaultMovementSpeed="NORMAL" HumidityCassetteType="Large" IsReadBarcode="False" LidType="None" Spilling="True" SpillingSwSource="False" SpillingUserValue="True" UseBarcode="False"><PlateStrip.DataLabels><sco:ObservableCollection x:TypeArguments="DataLabel"/></PlateStrip.DataLabels><PlateStrip.Plates><Plate x:Name="__ReferenceID0" Columns="12" PlateNumber="1" Rows="8"><Plate.MicroplateDefinition><MicroplateDefinition DrawingNumber="{x:Null}" ManufacturerRevisionOfTechnicalDrawing="{x:Null}" TecanCatalogNumber="{x:Null}" Version="{x:Null}" Comment="Cat. No.: 655101/655161/655192" CreationDate="2007-09-17T02:45:27.744789-07:00" DisplayName="[GRE96ft] - Greiner 96 Flat Transparent" IsReadOnlyTemplate="True" Manufacturer="Greiner" Material="Polystyrene" Name="GRE96ft" PlateColor="Transparent" PlateType="StandardMTP" RefractiveIndex="1.5"><MicroplateDefinition.MeasurementAreaDefinitions><GridMeasurementPosition CoordinateX="14380" CoordinateY="11240" NumberOfColumns="12" NumberOfRows="8" Well2WellCenterSpacingXAxis="9000" Well2WellCenterSpacingYAxis="9000"/></MicroplateDefinition.MeasurementAreaDefinitions><MicroplateDefinition.PlateFootprintDimension><PlateFootprintDimension OutsideXTolerance="{x:Null}" OutsideYTolerance="{x:Null}" FlangeHeight="2500" Height="14600" HeightTolerance="200" HeightWithCover="17606" OutsideX="127760" OutsideY="85480"/></MicroplateDefinition.PlateFootprintDimension><MicroplateDefinition.WellFootprintDimension><WellFootprintDimension GrowthArea="{x:Null}" BottomColor="None" BottomDimensionX="6390" BottomDimensionY="6390" BottomShape="Flat" BottomThickness="0" Depth="10900" MaximumCapacity="382" TopDimensionX="6960" TopDimensionY="6960" TopShape="Round" WorkingCapacity="200"/></MicroplateDefinition.WellFootprintDimension></MicroplateDefinition></Plate.MicroplateDefinition><Plate.PlateLayout><Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="A1" Column="0" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="0" WellIndex="0"/><Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="A2" Column="1" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="0" WellIndex="1"/><Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="A3" Column="2" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="0" WellIndex="2"/><Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="A4" Column="3" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="0" WellIndex="3"/><Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="A5" Column="4" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="0" WellIndex="4"/><Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="A6" Column="5" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="0" WellIndex="5"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="A7" Column="6" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="0" WellIndex="6"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="A8" Column="7" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="0" WellIndex="7"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="A9" Column="8" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="0" WellIndex="8"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="A10" Column="9" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="0" WellIndex="9"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="A11" Column="10" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="0" WellIndex="10"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="A12" Column="11" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="0" WellIndex="11"/> """)
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="B1" Column="0" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="1" WellIndex="12"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="B2" Column="1" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="1" WellIndex="13"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="B3" Column="2" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="1" WellIndex="14"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="B4" Column="3" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="1" WellIndex="15"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="B5" Column="4" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="1" WellIndex="16"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="B6" Column="5" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="1" WellIndex="17"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="B7" Column="6" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="1" WellIndex="18"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="B8" Column="7" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="1" WellIndex="19"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="B9" Column="8" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="1" WellIndex="20"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="B10" Column="9" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="1" WellIndex="21"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="B11" Column="10" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="1" WellIndex="22"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="B12" Column="11" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="1" WellIndex="23"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="C1" Column="0" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="2" WellIndex="24"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="C2" Column="1" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="2" WellIndex="25"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="C3" Column="2" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="2" WellIndex="26"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="C4" Column="3" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="2" WellIndex="27"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="C5" Column="4" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="2" WellIndex="28"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="C6" Column="5" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="2" WellIndex="29"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="C7" Column="6" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="2" WellIndex="30"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="C8" Column="7" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="2" WellIndex="31"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="C9" Column="8" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="2" WellIndex="32"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="C10" Column="9" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="2" WellIndex="33"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="C11" Column="10" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="2" WellIndex="34"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="C12" Column="11" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="2" WellIndex="35"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="D1" Column="0" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="3" WellIndex="36"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="D2" Column="1" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="3" WellIndex="37"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="D3" Column="2" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="3" WellIndex="38"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="D4" Column="3" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="3" WellIndex="39"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="D5" Column="4" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="3" WellIndex="40"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="D6" Column="5" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="3" WellIndex="41"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="D7" Column="6" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="3" WellIndex="42"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="D8" Column="7" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="3" WellIndex="43"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="D9" Column="8" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="3" WellIndex="44"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="D10" Column="9" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="3" WellIndex="45"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="D11" Column="10" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="3" WellIndex="46"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="D12" Column="11" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="3" WellIndex="47"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="E1" Column="0" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="4" WellIndex="48"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="E2" Column="1" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="4" WellIndex="49"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="E3" Column="2" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="4" WellIndex="50"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="E4" Column="3" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="4" WellIndex="51"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="E5" Column="4" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="4" WellIndex="52"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="E6" Column="5" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="4" WellIndex="53"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="E7" Column="6" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="4" WellIndex="54"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="E8" Column="7" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="4" WellIndex="55"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="E9" Column="8" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="4" WellIndex="56"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="E10" Column="9" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="4" WellIndex="57"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="E11" Column="10" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="4" WellIndex="58"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="E12" Column="11" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="4" WellIndex="59"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="F1" Column="0" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="5" WellIndex="60"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="F2" Column="1" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="5" WellIndex="61"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="F3" Column="2" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="5" WellIndex="62"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="F4" Column="3" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="5" WellIndex="63"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="F5" Column="4" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="5" WellIndex="64"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="F6" Column="5" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="5" WellIndex="65"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="F7" Column="6" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="5" WellIndex="66"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="F8" Column="7" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="5" WellIndex="67"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="F9" Column="8" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="5" WellIndex="68"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="F10" Column="9" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="5" WellIndex="69"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="F11" Column="10" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="5" WellIndex="70"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="F12" Column="11" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="5" WellIndex="71"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="G1" Column="0" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="6" WellIndex="72"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="G2" Column="1" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="6" WellIndex="73"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="G3" Column="2" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="6" WellIndex="74"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="G4" Column="3" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="6" WellIndex="75"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="G5" Column="4" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="6" WellIndex="76"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="G6" Column="5" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="6" WellIndex="77"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="G7" Column="6" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="6" WellIndex="78"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="G8" Column="7" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="6" WellIndex="79"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="G9" Column="8" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="6" WellIndex="80"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="G10" Column="9" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="6" WellIndex="81"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="G11" Column="10" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="6" WellIndex="82"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="G12" Column="11" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="6" WellIndex="83"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="H1" Column="0" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="7" WellIndex="84"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="H2" Column="1" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="7" WellIndex="85"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="H3" Column="2" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="7" WellIndex="86"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="H4" Column="3" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="7" WellIndex="87"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="H5" Column="4" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="7" WellIndex="88"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="H6" Column="5" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="7" WellIndex="89"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="H7" Column="6" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="7" WellIndex="90"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="H8" Column="7" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="7" WellIndex="91"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="H9" Column="8" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="7" WellIndex="92"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="H10" Column="9" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="7" WellIndex="93"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="H11" Column="10" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="7" WellIndex="94"/>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="H12" Column="11" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row="7" WellIndex="95"/>""")
target.write("""</Plate.PlateLayout>""")
target.write("""</Plate></PlateStrip.Plates><GasStrip IsWaitForGas="False" PostMeasurementControlOff="True" PostMeasurementSensorOff="False" SelectedGasConcentrationCO2="10000" SelectedGasConcentrationO2="210000" SelectedGasOption="CO2" SelectedMaximumGasConcentrationCO2="10000" SelectedMaximumGasConcentrationO2="210000" SelectedMinimumGasConcentrationCO2="1000" SelectedMinimumGasConcentrationO2="205000" SelectedOnOffSetting="On"><GasStrip.DataLabels><DataLabel InternalSuffix="{x:Null}" x:Name="__ReferenceID"""+str(next(iterSID))+"""" Index=\""""+str(next(indexit))+"""" MeasureMode="None" OutputName="GasStrip_b0385a06-de22-44fd-a3c4-b8832d07e38e" Type="Undefined" Unit="Unknown"/></GasStrip.DataLabels></GasStrip><TemperatureStrip IsWaitForTemperature="False" PostMeasurementTemperatureOff="False" SelectedMaximumTemperature="37.5" SelectedMinimumTemperature="36.5" SelectedOnOffSetting="On" SelectedTemperature="37" SelectedTemperatureScope="Plate"><TemperatureStrip.DataLabels><DataLabel InternalSuffix="{x:Null}" x:Name="__ReferenceID"""+str(next(iterSID))+"""" Index=\""""+str(next(indexit))+"""" MeasureMode="None" OutputName="TemperatureStrip_480256bf-8c1f-4a51-97bc-6712b8d6ea87" Type="Undefined" Unit="Unknown"/></TemperatureStrip.DataLabels></TemperatureStrip>""")



#added in 5
target.write("""<AbsorbanceStrip SelectedInputData="{x:Null}" MeasurementsCount="1" MultipleReadsPerWell="False" NumberFlashes="10" NumberOfMRWPoints="0" Reference="False" SelectedBorder="500" SelectedMultipleReadsPerWell="NotDefined" SelectedPattern="Square" SelectedSize="2" SettleTime="50" WavelengthMeasurement="4200" WavelengthReference="6200"><AbsorbanceStrip.DataLabels>""")
ODfirstref = next(iterSID)
target.write("""<DataLabel InternalSuffix="{x:Null}" x:Name="__ReferenceID"""+str(ODfirstref)+"""" Index=\""""+str(next(indexit))+"""\" MeasureMode="SinglePoint" OutputName="ODfirst" Type="Measurement" Unit="OpticalDensity"/></AbsorbanceStrip.DataLabels></AbsorbanceStrip>""")


#added in 6
#target.write("""<InjectorStrip SelectedRefillMode="Standard"><InjectorStrip.DataLabels><DataLabel InternalSuffix="{x:Null}" x:Name="__ReferenceID"""+str(ODfirstref)+"""" Index=\""""+str(next(indexit))+"""\" MeasureMode="None" OutputName="InjectorStrip_2e9078f2-118b-4d0d-b7c4-c74dfda9fd8e" Type="Undefined" Unit="Unknown"/></InjectorStrip.DataLabels><InjectorStrip.Injectors><tadods:InjectorModel InjectorName="A" IsActive="False" Model="Standard" ReadTimeLikeInjectTime="False" RefillEqualsInjectionSpeed="True" SelectedRefillSpeed="200" SelectedRefillVolume="500" SelectedSpeed="200" SelectedVolume="100" SyringeVolume="500"/><tadods:InjectorModel InjectorName="B" IsActive="True" Model="Standard" ReadTimeLikeInjectTime="False" RefillEqualsInjectionSpeed="True" SelectedRefillSpeed="200" SelectedRefillVolume="1000" SelectedSpeed="200" SelectedVolume="20" SyringeVolume="1000"/></InjectorStrip.Injectors></InjectorStrip>""")

#moved/removed in keto3-5
#target.write("""<InjectorStrip SelectedRefillMode="Standard"><InjectorStrip.DataLabels>""") #"Standard" or "BeforeEveryInjection"
#target.write("""<DataLabel InternalSuffix="{x:Null}" x:Name="__ReferenceID"""+str(next(iterSID))+"""" Index=\""""+str(next(indexit))+"""" MeasureMode="None" OutputName="InjectorStrip_16c42976-8c1c-4672-a5a8-4d3411bdffdf" Type="Undefined" Unit="Unknown"/></InjectorStrip.DataLabels><InjectorStrip.Injectors><tadods:InjectorModel InjectorName="A" IsActive="False" Model="Standard" ReadTimeLikeInjectTime="False" RefillEqualsInjectionSpeed="True" SelectedRefillSpeed="200" SelectedRefillVolume="40" SelectedSpeed="200" SelectedVolume="40" SyringeVolume="500"/><tadods:InjectorModel InjectorName="B" IsActive="True" Model="Standard" ReadTimeLikeInjectTime="False" RefillEqualsInjectionSpeed="True" SelectedRefillSpeed="200" SelectedRefillVolume="1000" SelectedSpeed="200" SelectedVolume="20" SyringeVolume="1000"/>""")
#target.write("""</InjectorStrip.Injectors></InjectorStrip>""")

#target.write("""<KineticLoopStrip Duration="23:59:59" EvaluatedKineticIntervalLabelIndex="0" EvaluatedKineticIntervalLimitType="Cycle" EvaluatedKineticIntervalTimeType="TimeSpan" FixedKineticIntervalMilliseconds="60000" FixedKineticIntervalTimeSpan="00:01:00" FixedKineticIntervalTimeType="TimeSpan" KineticIntervalType="NotDefined" KineticLoopType="Duration" NumberOfCycles="360"><KineticLoopStrip.DataLabels><sco:ObservableCollection x:TypeArguments="DataLabel"/></KineticLoopStrip.DataLabels><KineticLoopStrip.EvaluatedKineticIntervalLimits><EvaluatedKineticIntervalLimit Previous="{x:Null}" x:Name="__ReferenceID1" CycleLimit="1" IntervalMilliseconds="60000" IntervalTimeSpan="00:01:00" ValueLimit="0.1"><EvaluatedKineticIntervalLimit.Next><EvaluatedKineticIntervalLimit Next="{x:Null}" Previous="{x:Reference __ReferenceID1}" x:Name="__ReferenceID2" CycleLimit="1" IntervalMilliseconds="60000" IntervalTimeSpan="00:01:00" ValueLimit="0.1"/></EvaluatedKineticIntervalLimit.Next></EvaluatedKineticIntervalLimit><x:Reference>__ReferenceID2</x:Reference></KineticLoopStrip.EvaluatedKineticIntervalLimits>""")

#changed in 3
target.write("""<KineticLoopStrip Duration="04:00:00" EvaluatedKineticIntervalLabelIndex="0" EvaluatedKineticIntervalLimitType="Cycle" EvaluatedKineticIntervalTimeType="TimeSpan" FixedKineticIntervalMilliseconds="60000" FixedKineticIntervalTimeSpan="00:01:00" FixedKineticIntervalTimeType="TimeSpan" KineticIntervalType="NotDefined" KineticLoopType="Duration" NumberOfCycles="230"><KineticLoopStrip.DataLabels><sco:ObservableCollection x:TypeArguments="DataLabel"/></KineticLoopStrip.DataLabels><KineticLoopStrip.EvaluatedKineticIntervalLimits><EvaluatedKineticIntervalLimit Previous="{x:Null}" x:Name="__ReferenceID1" CycleLimit="1" IntervalMilliseconds="60000" IntervalTimeSpan="00:01:00" ValueLimit="0.1"><EvaluatedKineticIntervalLimit.Next><EvaluatedKineticIntervalLimit Next="{x:Null}" Previous="{x:Reference __ReferenceID1}" x:Name="__ReferenceID2" CycleLimit="1" IntervalMilliseconds="60000" IntervalTimeSpan="00:01:00" ValueLimit="0.1"/></EvaluatedKineticIntervalLimit.Next></EvaluatedKineticIntervalLimit><x:Reference>__ReferenceID2</x:Reference></KineticLoopStrip.EvaluatedKineticIntervalLimits>""")

#changed in 7
#target.write("""<ShakingStrip DisplayedAmplitude="2.5" SelectedAmplitude="2500" SelectedDuration="120" SelectedDurationMode="Time" SelectedFrequency="36" SelectedMode="Orbital" SelectedPosition="Incubation" SelectedVentingDuration="10" SelectedVentingInterval="10"><ShakingStrip.DataLabels><DataLabel InternalSuffix="{x:Null}" x:Name="__ReferenceID"""+str(next(iterSID))+"""" Index=\""""+str(next(indexit))+"""" MeasureMode="None" OutputName="ShakingStrip_9782d15a-4b52-4fd9-9ae2-9b83c303414e" Type="Undefined" Unit="Unknown"/></ShakingStrip.DataLabels></ShakingStrip>""")

target.write("""<AbsorbanceStrip SelectedInputData="{x:Null}" MeasurementsCount="1" MultipleReadsPerWell="False" NumberFlashes="10" NumberOfMRWPoints="0" Reference="False" SelectedBorder="500" SelectedMultipleReadsPerWell="NotDefined" SelectedPattern="Square" SelectedSize="2" SettleTime="50" WavelengthMeasurement="4200" WavelengthReference="6200"><AbsorbanceStrip.DataLabels>""")
OD420ref = next(iterSID)
target.write("""<DataLabel InternalSuffix="{x:Null}" x:Name="__ReferenceID"""+str(OD420ref)+"""" Index=\""""+str(next(indexit))+"""\" MeasureMode="SinglePoint" OutputName="OD420" Type="Measurement" Unit="OpticalDensity"/></AbsorbanceStrip.DataLabels></AbsorbanceStrip>""")

#####write the condition to inject alphaketoacids
#version 3-8
##part of plate
#target.write("""<PartOfPlateStrip><PartOfPlateStrip.DataLabels><sco:ObservableCollection x:TypeArguments="DataLabel"/></PartOfPlateStrip.DataLabels>""")
#target.write("""<PartOfPlateStrip.PlateLayout>""")
#for j in range(numberofwells):
#    target.write('<x:Reference>__ReferenceID'+str(PartofPlateID[j])+'</x:Reference>')
#      
#target.write("""</PartOfPlateStrip.PlateLayout>""")

#target.write("""<ConditionStrip EvaluatedLabel="{x:Reference __ReferenceID"""+str(OD420ref)+"""}" ConditionType="AtCycleStart" ConditionValueEvaluationType="GreaterThan" EvaluatedCycle=\""""+startketotime+"""" EvaluatedValue=\"""" + str(round(ODstart[i%len(ODstart)],3)) + """" ExecuteOnce="True"><ConditionStrip.DataLabels><DataLabel InternalSuffix="{x:Null}" x:Name="__ReferenceID"""+str(next(iterCID))+"""" Index=\""""+str(next(indexit))+"""" MeasureMode="None" OutputName="Condition_d08cd3ac-4aaa-4d0a-9c86-d6c55d26f265" Type="Condition" Unit="Unknown"/></ConditionStrip.DataLabels>""")
#target.write("""<ConditionStrip.EvaluatedReferenceWell><Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" x:Name="__ReferenceID""" +str(PartofPlateID[0])+"""" AlphanumericCoordinate=\""""+str(chr(65 + int(i/12) ))+str(i%12+1)+"""" Column=\"""" + str(i%12)+"""" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row=\""""+str(int(i/12))+"""" WellIndex=\""""+str(i)+""""/></ConditionStrip.EvaluatedReferenceWell><InjectorStrip SelectedRefillMode="BeforeEveryInjection"><InjectorStrip.DataLabels>""") #"Standard" or "BeforeEveryInjection"
#target.write("""<DataLabel InternalSuffix="{x:Null}" x:Name="__ReferenceID"""+str(next(iterIID))+"""" Index=\""""+str(next(indexit))+"""" MeasureMode="None" OutputName="InjectorStrip_16c42976-8c1c-4672-a5a8-4d3411bdffdf" Type="Undefined" Unit="Unknown"/></InjectorStrip.DataLabels><InjectorStrip.Injectors><tadods:InjectorModel InjectorName="A" IsActive="True" Model="Standard" ReadTimeLikeInjectTime="False" RefillEqualsInjectionSpeed="True" SelectedRefillSpeed="200" SelectedRefillVolume="40" SelectedSpeed="200" SelectedVolume="40" SyringeVolume="500"/><tadods:InjectorModel InjectorName="B" IsActive="False" Model="Standard" ReadTimeLikeInjectTime="False" RefillEqualsInjectionSpeed="True" SelectedRefillSpeed="200" SelectedRefillVolume="1000" SelectedSpeed="200" SelectedVolume="100" SyringeVolume="1000"/>""")
#target.write("""</InjectorStrip.Injectors></InjectorStrip>""")
#target.write("""</ConditionStrip></PartOfPlateStrip>""")

###make the in between parts
for i in range(numberofwells):
    
    iWellID = str(next(iterPID))
    ##part of plate
    target.write("""<PartOfPlateStrip><PartOfPlateStrip.DataLabels><sco:ObservableCollection x:TypeArguments="DataLabel"/></PartOfPlateStrip.DataLabels>""")
    target.write("""<PartOfPlateStrip.PlateLayout>""")
    for j in range(numberofwells):
        if i == j:
            target.write('<x:Reference>__ReferenceID'+iWellID+'</x:Reference>')
        else:
            target.write('<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" AlphanumericCoordinate="'+str(chr(65 + int(j/12) ))+str(j%12+1)+'" Column="'+str(j%12)+'" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="False" Row="'+str(int(j/12))+'" WellIndex="'+str(j)+'"/>')
          
    target.write("""</PartOfPlateStrip.PlateLayout>""")
    
    #changed in 4
    #changed in keto3 - from str(2*i+1) to cyclefunc
    target.write("""<ConditionStrip EvaluatedLabel="{x:Reference __ReferenceID"""+str(OD420ref)+"""}" ConditionType="AtCycleStart" ConditionValueEvaluationType="GreaterThan" EvaluatedCycle=\""""+cyclefunc(i)+"""" EvaluatedValue=\"""" + str(round(ODstart[i%len(ODstart)],3)) + """" ExecuteOnce="True"><ConditionStrip.DataLabels><DataLabel InternalSuffix="{x:Null}" x:Name="__ReferenceID"""+str(next(iterCID))+"""" Index=\""""+str(next(indexit))+"""" MeasureMode="None" OutputName="Condition_d08cd3ac-4aaa-4d0a-9c86-d6c55d26f265" Type="Condition" Unit="Unknown"/></ConditionStrip.DataLabels>""")
    target.write("""<ConditionStrip.EvaluatedReferenceWell><Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" x:Name="__ReferenceID""" +iWellID+"""" AlphanumericCoordinate=\""""+str(chr(65 + int(i/12) ))+str(i%12+1)+"""" Column=\"""" + str(i%12)+"""" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row=\""""+str(int(i/12))+"""" WellIndex=\""""+str(i)+""""/></ConditionStrip.EvaluatedReferenceWell><InjectorStrip SelectedRefillMode="BeforeEveryInjection"><InjectorStrip.DataLabels>""") #"Standard" or "BeforeEveryInjection"
    target.write("""<DataLabel InternalSuffix="{x:Null}" x:Name="__ReferenceID"""+str(next(iterIID))+"""" Index=\""""+str(next(indexit))+"""" MeasureMode="None" OutputName="InjectorStrip_16c42976-8c1c-4672-a5a8-4d3411bdffdf" Type="Undefined" Unit="Unknown"/></InjectorStrip.DataLabels><InjectorStrip.Injectors><tadods:InjectorModel InjectorName="A" IsActive="True" Model="Standard" ReadTimeLikeInjectTime="False" RefillEqualsInjectionSpeed="True" SelectedRefillSpeed="200" SelectedRefillVolume="40" SelectedSpeed="200" SelectedVolume="40" SyringeVolume="500"/><tadods:InjectorModel InjectorName="B" IsActive="False" Model="Standard" ReadTimeLikeInjectTime="False" RefillEqualsInjectionSpeed="True" SelectedRefillSpeed="200" SelectedRefillVolume="1000" SelectedSpeed="200" SelectedVolume="100" SyringeVolume="1000"/>""")
    target.write("""</InjectorStrip.Injectors></InjectorStrip>""")
    target.write("""</ConditionStrip></PartOfPlateStrip>""")

#changed in 7
target.write("""<ShakingStrip DisplayedAmplitude="3.5" SelectedAmplitude="3500" SelectedDuration="30" SelectedDurationMode="Time" SelectedFrequency="14" SelectedMode="Double" SelectedPosition="Incubation" SelectedVentingDuration="10" SelectedVentingInterval="10"><ShakingStrip.DataLabels><DataLabel InternalSuffix="{x:Null}" x:Name="__ReferenceID"""+str(next(iterSID))+"""" Index=\""""+str(next(indexit))+"""" MeasureMode="None" OutputName="ShakingStrip_9782d15a-4b52-4fd9-9ae2-9b83c303414e" Type="Undefined" Unit="Unknown"/></ShakingStrip.DataLabels></ShakingStrip>""")

#added in keto3-5 - also need the if statement for version 6
#remove in keto3-6
#target.write("""<InjectorStrip SelectedRefillMode="Standard"><InjectorStrip.DataLabels>""") #"Standard" or "BeforeEveryInjection"
#target.write("""<DataLabel InternalSuffix="{x:Null}" x:Name="__ReferenceID"""+str(next(iterSID))+"""" Index=\""""+str(next(indexit))+"""" MeasureMode="None" OutputName="InjectorStrip_16c42976-8c1c-4672-a5a8-4d3411bdffdf" Type="Undefined" Unit="Unknown"/></InjectorStrip.DataLabels><InjectorStrip.Injectors><tadods:InjectorModel InjectorName="A" IsActive="False" Model="Standard" ReadTimeLikeInjectTime="False" RefillEqualsInjectionSpeed="True" SelectedRefillSpeed="200" SelectedRefillVolume="40" SelectedSpeed="200" SelectedVolume="40" SyringeVolume="500"/><tadods:InjectorModel InjectorName="B" IsActive="True" Model="Standard" ReadTimeLikeInjectTime="False" RefillEqualsInjectionSpeed="True" SelectedRefillSpeed="200" SelectedRefillVolume="1000" SelectedSpeed="200" SelectedVolume="20" SyringeVolume="1000"/>""")
#target.write("""</InjectorStrip.Injectors></InjectorStrip>""")

#add in keto3-6
#taken from the for loop above
#modified condition stripid
#target.write("""<ConditionStrip EvaluatedLabel="{x:Reference __ReferenceID"""+str(OD420ref)+"""}" ConditionType="AtCycleStart" ConditionValueEvaluationType="GreaterThan" EvaluatedCycle=\""""+startketotime+"""" EvaluatedValue=\"""" + str(round(ODstart[i%len(ODstart)],3)) + """" ExecuteOnce="True"><ConditionStrip.DataLabels><DataLabel InternalSuffix="{x:Null}" x:Name="__ReferenceID"""+str(next(iterCID))+"""" Index=\""""+str(next(indexit))+"""" MeasureMode="None" OutputName="Condition_e7bd3e57-c720-49cf-8757-f68100668317" Type="Condition" Unit="Unknown"/></ConditionStrip.DataLabels>""")
#target.write("""<ConditionStrip.EvaluatedReferenceWell><Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" x:Name="__ReferenceID""" +iWellID+"""" AlphanumericCoordinate=\""""+str(chr(65 + int(i/12) ))+str(i%12+1)+"""" Column=\"""" + str(i%12)+"""" Grid="0" IdentifierGroup="None" IsFlagged="False" IsOut="False" IsSelected="True" Row=\""""+str(int(i/12))+"""" WellIndex=\""""+str(i)+""""/></ConditionStrip.EvaluatedReferenceWell>""")
#target.write("""<InjectorStrip SelectedRefillMode="BeforeEveryInjection"><InjectorStrip.DataLabels>""") #"Standard" or "BeforeEveryInjection"
#target.write("""<DataLabel InternalSuffix="{x:Null}" x:Name="__ReferenceID"""+str(next(iterSID))+"""" Index=\""""+str(next(indexit))+"""" MeasureMode="None" OutputName="InjectorStrip_16c42976-8c1c-4672-a5a8-4d3411bdffdf" Type="Undefined" Unit="Unknown"/></InjectorStrip.DataLabels><InjectorStrip.Injectors><tadods:InjectorModel InjectorName="A" IsActive="True" Model="Standard" ReadTimeLikeInjectTime="False" RefillEqualsInjectionSpeed="True" SelectedRefillSpeed="200" SelectedRefillVolume="40" SelectedSpeed="200" SelectedVolume="40" SyringeVolume="500"/><tadods:InjectorModel InjectorName="B" IsActive="False" Model="Standard" ReadTimeLikeInjectTime="False" RefillEqualsInjectionSpeed="True" SelectedRefillSpeed="200" SelectedRefillVolume="1000" SelectedSpeed="200" SelectedVolume="100" SyringeVolume="1000"/>""")
#target.write("""</InjectorStrip.Injectors></InjectorStrip>""")


#target.write("""</ConditionStrip>""")


target.write("""<ConditionStrip EvaluatedLabel="{x:Reference __ReferenceID"""+str(OD420ref)+"""}" ConditionType="AtCycleStart" ConditionValueEvaluationType="GreaterThan" EvaluatedCycle="2" EvaluatedValue="0" ExecuteOnce="True">""")
target.write("""<ConditionStrip.DataLabels>""")
target.write("""<DataLabel InternalSuffix="{x:Null}" x:Name="__ReferenceID"""+str(next(iterCID))+"""" Index=\""""+str(next(indexit))+"""" MeasureMode="None" OutputName="Condition_e7bd3e57-c720-49cf-8757-f68100668317" Type="Condition" Unit="Unknown"/>""")
target.write("""</ConditionStrip.DataLabels>""")
target.write("""<ConditionStrip.EvaluatedReferenceWell>""")
target.write("""<Well CartesianCoordinate="{x:Null}" Color="{x:Null}" ExperimentalGroup="{x:Null}" IdentifierGroupMember="{x:Null}" IdentifierReplicate="{x:Null}" IdentifierReplicates="{x:Null}" x:Name="__ReferenceID""" +str(PartofPlateID[0])+ """" AlphanumericCoordinate="A1" Column="0" Grid="0" Ident$""")
target.write("""</ConditionStrip.EvaluatedReferenceWell>""")
target.write("""<InjectorStrip SelectedRefillMode="Standard">""")
target.write("""<InjectorStrip.DataLabels>""")
target.write("""<DataLabel InternalSuffix="{x:Null}" x:Name="__ReferenceID"""+str(next(iterIID))+"""" Index=\""""+str(next(indexit))+"""" MeasureMode="None" OutputName="InjectorStrip_16c42976-8c1c-4672-a5a8-4d3411bdffdf" Type="Undefined" Unit="Unknown"/>""")
target.write("""</InjectorStrip.DataLabels>""")
target.write("""<InjectorStrip.Injectors>""")
target.write("""<tadods:InjectorModel InjectorName="A" IsActive="False" Model="Standard" ReadTimeLikeInjectTime="False" RefillEqualsInjectionSpeed="True" SelectedRefillSpeed="200" SelectedRefillVolume="40" SelectedSpeed="200" SelectedVolume="40" SyringeVolume="500"/>""")
target.write("""<tadods:InjectorModel InjectorName="B" IsActive="True" Model="Standard" ReadTimeLikeInjectTime="False" RefillEqualsInjectionSpeed="True" SelectedRefillSpeed="200" SelectedRefillVolume="1000" SelectedSpeed="200" SelectedVolume="20" SyringeVolume="1000"/>""")
target.write("""</InjectorStrip.Injectors>""")
target.write("""</InjectorStrip>""")
target.write("""</ConditionStrip>""")



###maker the footer for the kinetic loop



target.write("""</KineticLoopStrip></PlateStrip></InstrumentStrip><DataAnalysisStrip/><ExportStrip><ExcelExportStrip EndTestSettings="{x:Null}" TemplateFilePathname="{x:Null}" TemplateSheetname="{x:Null}"><ExcelExportStrip.DataLabels><sco:ObservableCollection x:TypeArguments="DataLabel"/></ExcelExportStrip.DataLabels></ExcelExportStrip></ExportStrip></MethodStrip>""")



target.close()


#<AbsorbanceStrip SelectedInputData="{x:Null}" MeasurementsCount="1" MultipleReadsPerWell="False" NumberFlashes="10" NumberOfMRWPoints="0" Reference="False" SelectedBorder="500" SelectedMultipleReadsPerWell="NotDefined" SelectedPattern="Square" SelectedSize="2" SettleTime="50" WavelengthMeasurement="4200" WavelengthReference="6200"><AbsorbanceStrip.DataLabels><DataLabel InternalSuffix="{x:Null}" x:Name="__ReferenceID"""+str(next(iterSID))+"""" Index=\""""+str(next(indexit))+"""" MeasureMode="SinglePoint" OutputName="OD420" Type="Measurement" Unit="OpticalDensity"/></AbsorbanceStrip.DataLabels></AbsorbanceStrip>