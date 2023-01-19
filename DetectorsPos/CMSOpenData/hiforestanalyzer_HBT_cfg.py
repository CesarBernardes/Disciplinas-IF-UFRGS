#Loading necessary libraries
import FWCore.ParameterSet.Config as cms
from RecoMuon.TrackingTools.MuonServiceProxy_cff import *
import PhysicsTools.PythonAnalysis.LumiList as LumiList
import FWCore.ParameterSet.Types as CfgTypes
process = cms.Process('HiForestHBT')
process.options = cms.untracked.PSet(SkipEvent = cms.untracked.vstring('ProductNotFound'))

#Number of events: put '-1' unless testing
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

#HiForest script init
process.load("HiForest_cff")
process.HiForest.inputLines = cms.vstring("HiForest V3",)
version = 'no git info'
process.HiForest.HiForestVersion = cms.string(version)

goodJSON = 'Cert_150436-152957_HI7TeV_StreamExpress_Collisions10_JSON_MuonPhys_v2.txt'
myLumis = LumiList.LumiList(filename = goodJSON).getCMSSWString().split(',')
import FWCore.Utilities.FileUtils as FileUtils
##files2010data = FileUtils.loadListFromFile ('CMS_HIRun2010_HIAllPhysics_ZS-v2_RECO_file_index.txt')
##process.source = cms.Source("PoolSource",
##    fileNames = cms.untracked.vstring(*files2010data    
##    )
##)

##mylist = FileUtils.loadListFromFile('CMS_HIRun2010_HIAllPhysics_ZS-v2_RECO_file_index.txt')
##readFiles = cms.untracked.vstring(*mylist)
##process.source = cms.Source("PoolSource",
##        fileNames = cms.untracked.vstring(*mylist),
##)

process.source = cms.Source("PoolSource",
  fileNames = cms.untracked.vstring(
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/001DA267-7243-E011-B38F-001617C3B6CE.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/0066DFBA-8F42-E011-A129-003048F1CA08.root', 
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/0074BED0-4642-E011-B7D1-0030487BF6DC.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/00896E66-7243-E011-88E9-003048CF99BE.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/00942EEB-1843-E011-BFC6-0025901D5D78.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/00C14524-A241-E011-8681-001D09F2AF96.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/00CFD683-BF43-E011-9AE8-003048F1C592.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/00EE9498-1443-E011-857F-003048CF65B4.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/02046476-1843-E011-8A5F-003048F1BFB0.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/020AA340-B541-E011-A913-003048F01118.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/026B1178-0D42-E011-A691-001D09F34488.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/0276E2D1-8F43-E011-9CA3-0030487CD812.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/027AD9DC-8F42-E011-B93A-0030487CD846.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/029034A4-FA44-E011-B0BE-0030489454C0.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/029F2DD0-E543-E011-B89A-003048D2BE06.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/02AF478F-0D42-E011-AACF-0019B9F4A1D7.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/02C1911F-3443-E011-8893-001D09F24FEC.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/02C81180-EE41-E011-9A7A-003048F17C2E.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/02CE606C-BA43-E011-9D4D-001D09F25456.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/0419D93F-2D42-E011-941D-003048F174A0.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/041C207D-D341-E011-A718-0025901D5C62.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/045A69BA-9A42-E011-A797-0025901AF65A.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/04E6F08D-2841-E011-822F-003048F16B8C.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/060D607D-6C43-E011-9C1A-003048F1DBB0.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/06575280-DC43-E011-9334-001D09F290CE.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/066F9E0D-1F42-E011-8704-003048F117B4.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/0686C22B-8E42-E011-B964-0030487CD712.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/069F3A4C-6041-E011-A95B-001D09F23A20.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/06B4358D-5E42-E011-AF39-001D09F26C5C.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/06B58577-E142-E011-9A0E-0030486780EC.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/06DD5270-EE42-E011-88B4-003048F0117E.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/080D2E34-6041-E011-AEAF-00304879FC6C.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/082B6866-7641-E011-801F-001D09F29524.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/0843F574-0D42-E011-AD3C-001D09F29619.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/086484B7-4841-E011-90E5-001617E30D12.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/086DC6AA-D142-E011-A79A-003048CFAD12.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/087647CB-7841-E011-9E27-003048F11822.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/0876B473-2741-E011-BB1A-0025901D61DC.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/08962FFB-9942-E011-BFEF-003048CEA258.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/08F3A509-9042-E011-A903-00304879F96C.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/08FD4EFB-4B41-E011-8224-001D09F2305C.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/0A008840-AA41-E011-8519-001D09F2525D.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/0A1317D1-3D44-E011-AF13-001D09F251FE.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/0A3AF889-D743-E011-B247-0030487CD7EE.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/0A4A6F22-9043-E011-AACC-001617C3B6C6.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/0A716793-9242-E011-8FA9-003048F02D34.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/0A72E45A-3843-E011-8049-003048F1BFAC.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/0A826D78-7243-E011-91D6-003048F1C9A2.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/0A82BB5C-A641-E011-9770-003048D374F2.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/0AD2AAC6-B542-E011-8162-003048F23D78.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/0ADC537E-CD42-E011-8A45-001617DBD316.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/0AF56AE4-4142-E011-BD2A-0025901D4306.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/0C0AE44E-BE43-E011-8EBC-003048F1BF76.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/0C3643DC-E841-E011-B43B-003048FEB8CE.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/0C73254E-7641-E011-A385-003048F17C14.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/0C830CB2-0B42-E011-8B82-003048F1183E.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/0C9EE814-2042-E011-8DF0-003048F1BFAC.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/0CA7B776-2841-E011-9961-0030489454C0.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/0CCDA06D-2741-E011-BFAA-00304896B902.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/0CD4DC32-2E41-E011-B0C5-003048F11822.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/0CDC4605-2A42-E011-AA6C-001617E30D00.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/0CEC90E8-2243-E011-9F98-0030487CD17C.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/0CF5FF83-D743-E011-8779-003048F1C592.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/0E03959C-F742-E011-8F44-003048F02C8A.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/0E4AF17D-E142-E011-ADE1-001D09F2527B.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/0E71AC82-E142-E011-8B8D-001D09F282F5.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/0E783B79-E142-E011-B498-001617E30CC8.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/0E7F953C-AA41-E011-9AD1-001D09F24024.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/0E9E0850-9542-E011-A7C8-003048CF65A6.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/0ED2D35E-DC42-E011-A34B-003048F11828.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/0EE09775-7B42-E011-845C-003048F01120.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/0EF41E59-9E41-E011-B895-001D09F2915A.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/1052302C-6342-E011-8FAD-003048F00984.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/105E4EF1-8242-E011-B504-003048CF927C.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/107200D7-2341-E011-998E-003048CF8C4A.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/1086199C-F743-E011-8144-0025901D5C8E.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/1091DF99-2641-E011-A23C-003048F1C7F2.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/10A477E6-B442-E011-91B1-001D09F282F5.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/10F152DC-8D41-E011-9E13-0025901AF6EA.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/10F7369D-3742-E011-B169-001617C3B5D8.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/12002C4D-5E43-E011-874A-0025901D5AD2.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/121D9BE7-1443-E011-82A4-0030487CC722.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/1230160E-8E42-E011-87BD-003048F1BF16.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/1246DC14-4242-E011-9DD7-0025901AF658.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/1257E854-4442-E011-B96A-001D09F24D4E.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/128C9E94-B442-E011-A7E0-003048CBAED4.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/12ACF74F-2741-E011-843E-003048F02C66.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/12BE3D6F-2841-E011-A863-003048F0E7B0.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/12C0ABCD-2C41-E011-BF8F-0030487C7828.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/12E4496A-3A43-E011-A4B5-001D09F25208.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/12F1011A-D542-E011-8B4E-003048F01154.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/140308D6-8043-E011-A21B-003048F1BF92.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/145D8833-6C43-E011-91D7-0025901D5CBE.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/1491697D-1D42-E011-9A5D-001D09F24DA8.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/1637D57F-D442-E011-AC37-003048F1BEB2.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/165FA98C-8943-E011-9D14-003048F00AEC.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/1663E7DC-9243-E011-BEEB-003048CFA94A.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/168DA080-1242-E011-B8B8-003048F02C66.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/16C1E0DA-0B43-E011-8099-001D09F291D2.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/16C4F144-2A42-E011-A4E1-003048F23776.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/180172FC-9942-E011-BB1B-0025901AF95A.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/180F3D5E-9142-E011-ABE2-0025901AECBA.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/183FDB0F-D542-E011-A4EF-003048CF9B0C.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/184B424A-9043-E011-B47D-001D09F253C0.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/186B81B6-2641-E011-8300-0030487C5C54.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/1887D90C-C541-E011-B3D2-001D09F28F25.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/189055F8-9942-E011-B368-003048F23860.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/18923792-3443-E011-82F4-001D09F2546F.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/18C0E17A-DC43-E011-886B-001D09F25393.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/18D60C8B-BD43-E011-88AB-003048F1C7BC.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/18F219E4-3643-E011-BBC3-003048F00B94.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/18FEE243-B742-E011-A33C-003048F16B86.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/18FF109F-3742-E011-9912-003048D3756A.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/1A33DF74-0D42-E011-8272-001D09F2441B.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/1A769A6D-2A42-E011-9052-003048F23D66.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/1A787429-8E41-E011-BE08-003048C9D2CE.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/1A7F7DEE-9343-E011-AEDA-0030487C7392.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/1A8926DA-4642-E011-A687-003048F0E1A8.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/1AA29906-D942-E011-AC12-0030487C5CF0.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/1ACD7391-8943-E011-8D58-0025901AF58E.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/1AF906BA-9842-E011-81CC-003048F00B9E.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/1C0060DA-C443-E011-878D-0025901D5D88.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/1C0134F3-E142-E011-B44F-0025901D626C.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/1C05A99F-2F43-E011-BE4D-0030487C6E94.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/1C189232-1F42-E011-BD4B-0030487C5CE2.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/1C671740-D441-E011-9662-003048F0E564.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/1C94B9D1-7341-E011-B3B8-0025901B036E.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/1C9C96B8-5A43-E011-A9F9-003048FEAE14.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/1CBDC98E-5E42-E011-BE10-001D09F251CC.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/1E2D92F9-2341-E011-9069-000423D98868.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/1E319CD1-4142-E011-BAFD-0030486733D8.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/1E37DA7D-D743-E011-BBA9-0030487A18D8.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/1E3B3390-B442-E011-B22E-003048CF4986.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/1E981C1F-3443-E011-A237-0030487CD7EA.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/1E987E3F-1F44-E011-8CDF-003048F23D72.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/1EA1388D-3C43-E011-815D-00304879FC6C.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/1ECAC4B8-F143-E011-BD38-0030487C600A.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/20172870-6043-E011-83BA-003048F17C14.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/202C70FC-2341-E011-8638-000423D94A04.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/208EA78C-9343-E011-846D-003048F0E31A.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/209E2493-7343-E011-BE46-0030487C9108.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/20B411A0-E543-E011-A9BC-003048F17C82.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/20BAFFA7-7841-E011-850C-003048F01E88.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/22018481-3443-E011-AEE6-0019B9F70468.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/221E95F0-2442-E011-97EC-003048F122C2.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/223C18D3-5F42-E011-BE7E-003048F23C02.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/2265EBAC-1A43-E011-B275-003048F0113A.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/229A536A-BF43-E011-87D1-003048C9C79E.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/22BEA1C8-7044-E011-BD9A-003048F1C418.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/22EBF6C5-6043-E011-925B-0030487C8DAA.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/22FC72B1-2641-E011-842A-003048F11882.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/2406A9A8-6343-E011-A921-0025901D5CDC.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/2418F1AF-3141-E011-AA3E-001D09F29849.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/242EDFF2-2B41-E011-A8C6-0025901AF348.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/244F578A-7643-E011-A633-0025901D5D74.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/246A798E-D142-E011-A630-001617DC1F70.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/2486A124-3442-E011-AD50-001D09F29597.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/24C51268-D741-E011-A7EF-003048F16B9C.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/24DACE9D-3343-E011-8EDF-003048F11902.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/2675563A-BD43-E011-8D28-0030487CD744.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/267BE01A-3443-E011-9B91-0030487C778E.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/26ACBD80-BF43-E011-AA00-003048D37520.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/26DFF8E0-0A43-E011-840A-003048F11C28.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/26E58E5E-E643-E011-86D7-003048D37538.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/26EF4ACE-2B41-E011-AB41-0030487C90D4.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/28190F96-D142-E011-BECA-001D09F251D1.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/28347AD9-8943-E011-B42F-003048F16F44.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/2845641C-2A42-E011-AF59-001D09F2B30B.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/2858A370-F043-E011-BFB2-003048F237F8.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/28A9CF7F-DC43-E011-8BB1-001D09F24D8A.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/28ACE6F8-9443-E011-B14C-003048F01158.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/28CB3DB3-3C43-E011-9A2E-001D09F2AF1E.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/28FBCD2D-C543-E011-A0E5-003048F00AEA.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/2A17FD41-C541-E011-A71D-001D09F2924F.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/2A1E058F-5E42-E011-9200-001D09F24E39.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/2A3E1EB3-D743-E011-8064-003048F1E1AC.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/2A4E071E-8E42-E011-99F6-003048F16FFE.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/2A4F3CD7-8F42-E011-B1CC-003048F01070.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/2A75816D-F143-E011-B846-003048D374F2.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/2A78564F-7641-E011-B2CC-003048F117EC.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/2A7FEAFA-F043-E011-9343-001D09F2AD4D.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/2A838AE9-8242-E011-A26C-003048F1C81A.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/2AEB9119-E743-E011-AD2D-003048D2C0F0.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/2AF04A3E-D441-E011-B583-003048F17C34.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/2C2134D4-9942-E011-AFDE-0025901B0FA6.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/2C328B28-4742-E011-BF25-003048F23980.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/2C3FBA1D-7641-E011-943E-001D09F2424A.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/2C4DA177-7B42-E011-930D-003048F02C88.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/2C5565C3-2341-E011-8326-003048F2395E.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/2C6CC26A-BF43-E011-9633-003048D37358.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/2C82D30E-9543-E011-89BB-003048F1C820.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/2CDB52B6-1A43-E011-B456-0025901AF1C4.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/2E27741E-3443-E011-9FC6-00304879FA4C.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/2E58A557-AC43-E011-9F14-003048FEB97A.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/2E674B8B-1443-E011-A468-000423D94494.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/2E9CB329-5B43-E011-8C29-0025901AF3AC.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/2EEC469A-2F43-E011-9A38-0025901AF958.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/30091136-1F42-E011-AFBA-0030487CD700.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/30328E5A-4B41-E011-8CE5-0025901B0920.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/30366C0D-1F42-E011-990E-003048F024F6.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/30841D40-D441-E011-9AD0-0025901AF65A.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/30873885-8744-E011-B276-0025901AF918.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/30AE658A-3443-E011-91DD-001D09F25208.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/30F1B0B0-B841-E011-9A68-003048F0103C.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/32257757-A241-E011-9F12-003048F2382C.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/326DE2F2-C042-E011-A576-003048F1CA12.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/328EF90C-E143-E011-8769-001D09F248F8.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/32929106-D942-E011-B9EF-003048F23D8E.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/32988D65-A641-E011-9557-001D09F24399.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/32A88B31-C142-E011-B8FE-003048CFAD0C.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/32AF56B9-1143-E011-901A-0019B9F70607.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/32DDEE26-3442-E011-A6D9-001D09F251BD.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/32DF4CED-F941-E011-84BC-003048F009CA.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/32E56C28-C141-E011-8091-0025901AF1CA.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/32FCE337-5E43-E011-9219-003048F236E8.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/343D05CA-7841-E011-B616-003048F1B26E.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/34535B03-B942-E011-94FC-003048F010FC.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/34568143-BD43-E011-A7AD-003048F0E1CC.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/3468A637-0C42-E011-ADA6-003048D3732C.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/346D9634-F543-E011-8BEF-0030487A18F2.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/34B6BEA2-3443-E011-B601-003048F02C64.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/34D521D3-C441-E011-8B08-0025901D6270.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/362005C8-2142-E011-BFDD-003048F1CA1C.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/362B5A94-1D42-E011-A5A2-0030486780E6.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/364E7D52-6041-E011-B914-003048F02C88.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/3691CC4B-A241-E011-AF86-0019B9F730D2.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/36C508B6-F941-E011-9FCC-003048F1C1B8.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/389118CE-2C41-E011-B292-0030487CD162.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/38B3F25A-9E41-E011-917B-000423D94908.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/3A1E7DF7-8043-E011-9D35-0030487C9118.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/3A75B752-1743-E011-AB48-003048F1C9B2.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/3AC00891-1443-E011-8336-0030487C8C54.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/3AD1187E-5B43-E011-92DE-003048F0E304.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/3AD26ED4-8543-E011-B65D-003048F1B91C.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/3AE2301F-8E41-E011-BA9C-003048F24358.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/3AE41CCE-C643-E011-8F06-000423D9997E.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/3C0600B1-0B42-E011-8C63-001D09F291D7.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/3C0D26E4-8242-E011-B68F-0025901AF384.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/3C4782C4-2A42-E011-9503-001617DBD556.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/3C8645F4-3343-E011-B0C1-0030487C5C6C.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/3C890852-CE43-E011-9DBD-003048F0E320.root',
'root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0000/3C954C31-B442-E011-B940-001D09F28EA3.root',
 ) 
)


process.source.lumisToProcess = CfgTypes.untracked(CfgTypes.VLuminosityBlockRange())
process.source.lumisToProcess.extend(myLumis)

#Global Tag: change the name according to the instructions
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
##process.GlobalTag.connect = cms.string('sqlite_file:/cvmfs/cms-opendata-conddb.cern.ch/GR_R_39X_V6B.db')
process.GlobalTag.globaltag = 'GR_R_39X_V6B::All'
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load("Configuration.StandardSequences.MagneticField_cff")
process.HiForest.GlobalTagLabel = process.GlobalTag.globaltag

#Define the output root file (change each run not to overwrite previous output)
process.TFileService = cms.Service("TFileService",
                                   fileName=cms.string("HiForestAOD_DATAtest.root"))

#Init Trigger Analyzer
process.hltanalysis = cms.EDAnalyzer('TriggerInfoAnalyzer',
                              processName = cms.string("HLT"),
                              triggerName = cms.string("@"),         
                              ##datasetName = cms.string("HIAllPhysics"),  #'HICorePhysics' to look at Core Physics only
                              datasetName = cms.string("HICorePhysics"),
                              triggerResults = cms.InputTag("TriggerResults","","HLT"),
                              triggerEvent   = cms.InputTag("hltTriggerSummaryAOD","","HLT")                             
                              )

##Select triggered events here
import HLTrigger.HLTfilters.hltHighLevel_cfi
process.hltMBOrBSC = HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone()
process.hltMBOrBSC.HLTPaths = ["HLT_HIMinBiasHfOrBSC_Core*"]
process.hltMBOrBSC.andOr = cms.bool(True)  # True = OR, False = AND between the HLT paths
process.hltMBOrBSC.throw = cms.bool(False) # throw exception on unknown path names

#Collect event data
process.demo = cms.EDAnalyzer('AnalyzerHBT') 
process.dump=cms.EDAnalyzer('EventContentAnalyzer') #easy check of Event structure and names without using the TBrowser

process.ana_step = cms.Path(process.hltanalysis+process.hltMBOrBSC+
		  	    #process.dump+  #uncomment if necessary to check the name. Do not forget to change the number of events to '1'
			    process.demo+
                            process.HiForest 
)

