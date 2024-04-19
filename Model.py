import pickle
import Data
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score


def init_model():
    print("Training model....")
    # Assuming loadData.load_data returns a list of dictionaries
    train_data = Data.load_data('./datasets/train_v1.jsonl')
    # test_data = Data.load_data('./datasets/test_v1.jsonl')
    val_data = Data.load_data('./datasets/val_v1.jsonl')

    # Create a TF-IDF vectorizer
    vectorizer = TfidfVectorizer(ngram_range=(1, 2),
                                 min_df=3, max_df=0.9, strip_accents='unicode', use_idf=True,
                                 smooth_idf=True, sublinear_tf=True, lowercase=False)
    # vectorizer = TfidfVectorizer(lowercase=False)

    train_data_df = pd.DataFrame(train_data)
    # test_data_df = pd.DataFrame(test_data)
    val_data_df = pd.DataFrame(val_data)

    text_list = [" ".join(doc) for doc in train_data_df["Text"].tolist()]
    # Fit the vectorizer on the training data
    x_train = vectorizer.fit_transform(text_list)
    y_train = train_data_df["Document Tag"].tolist()

    x_test = vectorizer.transform([" ".join(doc)
                                  for doc in val_data_df["Text"].tolist()])
    y_test = val_data_df["Document Tag"].tolist()

    svc = SVC()
    # Transform text data into numerical features
    svc.fit(x_train, y_train)
    print("Model trained successfully")

    print("Saving model....")

    model_pkl_file = "vectorizer_model.pkl"
    with open(model_pkl_file, 'wb') as file:
        pickle.dump(vectorizer, file)
        print("Model saved as {}".format(model_pkl_file))

    model_pkl_file = "fake_news_svm_model.pkl"
    with open(model_pkl_file, 'wb') as file:
        pickle.dump(svc, file)
        print("Model saved as {}".format(model_pkl_file))


def load_model():
    try:
        print("Loading model....")
        model_pkl_file = "vectorizer_model.pkl"
        with open(model_pkl_file, 'rb') as file:
            vectorizer = pickle.load(file)
            print("Model loaded from {}".format(model_pkl_file))

        model_pkl_file = "fake_news_svm_model.pkl"
        with open(model_pkl_file, 'rb') as file:
            model = pickle.load(file)
            print("Model loaded from {}".format(model_pkl_file))
        print("Model loaded successfully")
        return vectorizer, model
    except:
        print("Model not found.")
        print("Start Re-training model....")
        init_model()
        print("Model Re-trained successfully")
        return load_model()


def simple_test():
    vectorizer, model = load_model()
    new_data = ["กิน", "มะนาว", "โซดา", "เพื่อ", "รักษา", "มะเร็ง"]
    x_new = vectorizer.transform([" ".join(new_data)])
    y_new = model.predict(x_new)
    print("Test Prediction with : {}".format(new_data))
    print("Predicted Label : {}".format(y_new))


def get_metrics(model, vectorizer):
    val_data = Data.load_data('./datasets/val_v1.jsonl')
    val_data_df = pd.DataFrame(val_data)
    x_test = vectorizer.transform([" ".join(doc)
                                  for doc in val_data_df["Text"].tolist()])
    y_test = val_data_df["Document Tag"].tolist()
    y_pred = model.predict(x_test)
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='weighted')
    recall = recall_score(y_test, y_pred, average='weighted')
    f1 = 2 * (precision * recall) / (precision + recall)
    result = {
        "accuracy": accuracy,
        "precision": round(precision, 2),
        "recall": round(recall, 2),
        "f1": round(f1, 2)
    }
    return result
