import numpy as np
from sklearn.model_selection import train_test_split
import ktrain
from ktrain import text
from azureml.core import Run
from sklearn.metrics import accuracy_score
from azureml.core import Dataset

#Get the experiment run context
run = Run.get_context()
exp = run.experiment
ws = run.experiment.workspace

#register dataset
print("Loading training data...")
default_ds = ws.get_default_datastore()
meld_dd_ds = Dataset.Tabular.from_delimited_files(path=(default_ds, 'meld-dd-sample.csv'))
meld_dd_ds = meld_dd_ds.register(workspace=ws, 
                                name='MELD-DD dataset',
                                description='MELD-DD data',
                                tags = {'format':'CSV'},
                                create_new_version=True)

df = meld_dd_ds.to_pandas_dataframe()

df = df[['Emotion','Statement']]

y = df.pop('Emotion')
X = df

X_train,X_test,y_train,y_test = train_test_split(X.to_numpy().ravel() ,y.to_numpy().ravel(),test_size=0.5)

#Hyperparameter values
learning_rate = 5e-5
epoch = 1

Emotions = ['joy', 'neutral']

MODEL_NAME = 'distilbert-base-uncased'

t = text.Transformer(MODEL_NAME, maxlen=200, class_names=Emotions)
trn = t.preprocess_train(X_train, y_train)
val = t.preprocess_test(X_test, y_test)
model = t.get_classifier()
learner = ktrain.get_learner(model, train_data=trn, val_data=val, batch_size=24)

print("Learning_rate: " + str(learning_rate))
print("Epoch: " + str(epoch))

learner.fit_onecycle(learning_rate, epoch)
print("Results")

learner.validate(class_names=t.get_classes())

predictor = ktrain.get_predictor(learner.model, preproc=t) 

y_scores = predictor.predict_proba(X_test)
y_scores= np.argmax(y_scores, axis=1)
y_real= np.argmax(val.y, axis=1)

acc = accuracy_score(y_real, y_scores)
print('Accuracy: ' + str(acc))
run.log('Accuracy', np.float(acc))

model_name = 'mgsa-ed'

predictor.save(model_name)
print('MODEL SAVED')

# upload the model file explicitly into artifacts
run.upload_folder(name="./outputs", path= './' + model_name)
print("Uploaded the model {} to experiment {}".format(model_name, run.experiment.name))

run.complete()