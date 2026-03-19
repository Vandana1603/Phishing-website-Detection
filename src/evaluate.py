from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score

def evaluate_models(models, X_test, y_test):
    for name, model in models.items():
        y_pred = model.predict(X_test)

        print(f"\n  {name}")
        print("Confusion Matrix:")
        print(confusion_matrix(y_test, y_pred))

        print("\nClassification Report:")
        print(classification_report(y_test, y_pred))

        try:
            y_prob = model.predict_proba(X_test)[:, 1]
            print("ROC-AUC:", roc_auc_score(y_test, y_prob))
        except:
            print("ROC-AUC not available")