# week2 commands: 
During this week you learn to to track/organsie experients, than make easier to
optimise your model and find the best one. Then you learn to mangane(register) your models.

MLflow: 
* mlflow server --backend-store-uri sqlite:///mlflow.db 
 for the homework the DB is homework.db  not the forgete to the source the env. 
 and to start the server  in the right folder  with  the following command
 mlflow server --backend-store-uri sqlite:///homework.db 

* log paramters/results: mlflow.log(params:dict) => nice UI viszualization
* log save the model: mlflow.<libratry-model>.log_model(model, path)


Data Source for the HM: 
* https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page


