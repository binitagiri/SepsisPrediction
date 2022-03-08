
# Early detection of sepsis from clinical data

# Problem Statement

Sepsis is a life-threatening condition that occurs when the body's response to infection causes tissue damage, organ failure, or death.
Early detection and antibiotic treatment of sepsis are critical for improving sepsis outcomes, where each hour of delayed treatment has been associated with roughly an 4-8% increase in mortality

# Goal

Design and implement a working, open-source algorithm that can, based only on the clinical data provided, automatically identify a patient's risk of sepsis and make a positive or negative prediction of sepsis for every time interval. 
## Dataset

## Vital signs (columns 1-8)

| Parameter | Description    | 
| :-------- | :------- | 
| HR | Heart rate (beats per minute)| 
| O2Sat | Pulse oximetry (%)| 
| Temp | Temperature (Deg C)| 
| SBP | Systolic BP (mm Hg)| 
| MAP | Mean arterial pressure (mm Hg)| 
| DBP | Diastolic BP (mm Hg)| 
| Resp | Respiration rate (breaths per minute)| 
| EtCO2 | End tidal carbon dioxide (mm Hg)| 

## Laboratory values (columns 9-34)

| Parameter | Description    | 
| :-------- | :------- | 
| BaseExcess |Measure of excess bicarbonate (mmol/L)|
| HCO3 | Bicarbonate (mmol/L)| 
| FiO2 | Fraction of inspired oxygen (%)| 
| pH | N/A|
| PaCO2 | Partial pressure of carbon dioxide from arterial blood (mm Hg)| 
| SaO2 | Oxygen saturation from arterial blood (%)| 
| AST | Aspartate transaminase (IU/L)|
| BUN | Blood urea nitrogen (mg/dL)| 
| Alkalinephos | Alkaline phosphatase (IU/L)| 
| Calcium | (mg/dL)|
| Chloride | (mg/dL)| 
| Creatinine | (mg/dL)| 
| Bilirubin_direct | Bilirubin direct (mg/dL)|
| Glucose | Serum glucose (mg/dL)| 
| Lactate | Lactic acid (mg/dL)| 
| Magnesium | (mmol/dL)|
| Phosphate | (mg/dL)| 
| Potassium | (mmol/L)| 
| Bilirubin_total | Total bilirubin (mg/dL)|
| TroponinI | Troponin I (ng/mL)| 
| Hct | Hematocrit (%)| 
| Hgb | Hemoglobin (g/dL)|
| PTT | partial thromboplastin time (seconds)| 
| WBC | Leukocyte count (count*10^3/µL)| 
| Fibrinogen | (mg/dL)| 
| Platelets | (count*10^3/µL)| 

## Demographics (columns 35-40)

| Parameter | Description    | 
| :-------- | :------- | 
| Age | Years (100 for patients 90 or above)| 
| Gender | Female (0) or Male (1)| 
| Unit1 | Administrative identifier for ICU unit (MICU)| 
| Unit2 | Administrative identifier for ICU unit (SICU)| 
| HospAdmTime| Hours between hospital admit and ICU admit| 
| ICULOS| ICU length-of-stay (hours since ICU admit)| 

## Outcome (column 41)

| Parameter | Description    | 
| :-------- | :------- | 
| SepsisLabel | 1 for Sepsis Patients , 0 for Non Sepsis Patients| 





## Dataset Summary

There are a total of 40336 patients. Out of these patients, 2932 patients contracted sepsis. Out of the sepsis patients , 2506 had contracted sepsis after ICU admission and 426 patients before ICU admission.
## Missing Value Analysis

The dataset has  1,552,210 rows and a huge volume of missing values which makes this dataset highly imbalanced.

![alt text](https://github.com/binitagiri/SepsisPrediction/blob/main/Images/MissingValueC.png?raw=true)

For most of the laboratory values , data is missing for more than 90% . 

## Exploratory data analysis

Histograms , box plots , correlation matrix , SIRS calculation , trend per hour , single variable analysis , multivariate analysis etc  were performed using Tableau and Python for data visualisation to have a sense of data and domain we are dealing with.

## Data Preprocessing

Based on the initial analysis , the below tasks were performed as part of data preprocessing
Missing value imputation.
Feature reduction.
Downsampling based on type of patient.
Upsampling based on sepsislabel. 

## Missing value imputation

The below missing imputation techniques were tried and the imputation with best results were selected.

  1) Forward fill/backward fill based on PatientID
  2) Linear interpolation based on PatientID
  3) KNN
  4) MICE

Linear interpolated dataset was giving the best result and hence it was chosen for modeling.

## Feature reduction

After linear interpolation, there were still many records with null values. On further analysis , it was found that there were many patients with a laboratory record which is not even recorded once

![alt text](https://github.com/binitagiri/SepsisPrediction/blob/main/Images/MissingValueP.png?raw=true)
Columns which are not recorded for 40% of patients were deleted.

'EtCO2','Bilirubin_direct','TroponinI','Fibrinogen','sepsisType','Unit1',
      'Unit2'

## Downsampling based on type of patient

The dataset has 3 types of patients - non sepsis patients , sepsis before ICU admission , sepsis after ICU admission. To reduce the imbalance of data , we downsampled the data to contain only patients who entered sepsis stage (2932 patients).

## Upsampling based on sepsislabel

Data was still imbalanced in terms of the dependent variable SepsisLabel.
![alt text](https://github.com/binitagiri/SepsisPrediction/blob/main/Images/Upsampling.png?raw=true)

SMOTE was applied on the dataset to upsample the data for sepsisLabel=1.

## Modeling

Since the pre processed data still had a huge number of null values , we were in a lookout for a model which can handle null values. XGBoostClassifier was the selected model and it suited best for binary classification model.The evaluation metric used is AUCROC.

## References:

1.https://physionet.org/content/challenge-2019/1.0.0/
2.https://www.researchgate.net/figure/Early-identification-and-management-algorithm_fig1_337829729
2. https://youtu.be/dgYo6WnOS3E

