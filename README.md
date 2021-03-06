# ALPHA
A Light Post-Heppy Analyzer

## Git instructions
In your working area, first set up the CMSSW release:
```bash
cmsrel CMSSW_8_0_12
cd CMSSW_8_0_12/src/
cmsenv
git cms-init
```
Merge the most recent MET filters and EGM smearing and scale
```bash
git cms-merge-topic -u cms-met:CMSSW_8_0_X-METFilterUpdate
git cms-merge-topic -u emanueledimarco:ecal_smear_fix_80X
git cms-addpkg EgammaAnalysis/ElectronTools
cd EgammaAnalysis/ElectronTools/data
git clone -b ICHEP2016_approval_7p65fb https://github.com/emanueledimarco/ScalesSmearings.git
cd $CMSSW_BASE/src
mkdir Analysis
cd Analysis
```
then, clone the ALPHA git repository:
```bash
git clone https://github.com/CMS-PD/ALPHA
```
and get the code for KinFitter:
```bash
cd $CMSSW_BASE/src/Analysis/ALPHA
sh setup.sh
```

See also the TWiki for developers git instructions: [https://twiki.cern.ch/twiki/bin/view/CMS/ALPHA](https://twiki.cern.ch/twiki/bin/view/CMS/ALPHA)

## Run instructions
Compile the code:
```bash
scram b -j 8
```
and run it:
```bash
cmsRun python/Diboson.py
```