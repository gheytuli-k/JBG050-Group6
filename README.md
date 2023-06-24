# JBG050-Group6
This is a repository for the course Data Challenge 2(JBG050) of Group 6 <br>

1. **Download the data**<br>
- The original datasets are available on UK police website: https://data.police.uk/data/<br>
- Choose Archive and download the data from December 2010 to January 2023<br>
- The bus stop locations data can be downloaded from official website: https://data.london.gov.uk/dataset/tfl-bus-stop-locations-and-routes <br>

2. **Reorganize the data storage**<br>
We have reorganized the dataset folders for improved organization. Each folder now contains records spanning across all months. Specifically, the Crime Data, Outcome Data, and Street Data folders now encompass comprehensive data for all months. <br>
- Run 'data_storage.py' file<br>

3. **Data preprocessing**<br>
The 'data_preprocessing.ipynb' contains codes for initial data preprocessing and exploration of crime trends. The necessary data is stored as SQL database after running the codes for future use in crime types analysis and model prediction. <br>
- Run 'data_preprocessing.ipynb' <br>

4. **Crime types analysis**<br>
- The 'Crime types analysis.ipynb' notebook is designed to analyze the correlations among various crime types and perform K-means clustering based on their locations.<br>
- The visualizations in the form of maps have been incorporated. Please note that the plots are not directly displayed on the GitHub page. To view them, the notebook needs to be rerun to generate and display the visualizations. <br>
- Run 'Crime types analysis.ipynb' <br>

5. **Prediction models for Hendon&West Hendon**<br>
- The different types of prediction models and performance results are contained in the 'Prediction Model.ipynb'<br>
- Run 'Prediction Model.ipynb' <br>

5. **Prediction models for Barnet**<br>
- Model training for the burglary prediction of whole Barnet <br>
- Run 'BarnetModel.ipynb'

6. **Barnet burlgary location analysis**<br>
- All the analysis that was done on the location of the burglaries and their geographical placement in LSOAs <br>
- Run 'Barnet visual.ipynb'

7. **Relation between busstops and burglaries**<br>
- All the analysis around the relation of busstops locations and the burlgaries location <br>
- Run 'BusStop.ipynb'
