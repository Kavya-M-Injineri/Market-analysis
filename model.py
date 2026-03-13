import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import os

df = pd.read_csv("merged_data.csv")

# Create Next Day PnL
# Sort by Account and Date
df.sort_values(by=['Account', 'date'], inplace=True)
df['next_day_pnl'] = df.groupby('Account')['daily_pnl'].shift(-1)
# Drop na (last day for each account)
df = df.dropna(subset=['next_day_pnl']).copy()

# Target: 1 if Next Day PnL > 0 else 0
df['target'] = (df['next_day_pnl'] > 0).astype(int)

# Features
features = ['num_trades', 'avg_trade_size', 'total_volume', 'win_rate']

# Handle categorical sentiment
sentiment_dummies = pd.get_dummies(df['sentiment_class'], prefix='sentiment')
df = pd.concat([df, sentiment_dummies], axis=1)

feature_cols = features + list(sentiment_dummies.columns)

df = df.dropna(subset=feature_cols)

X = df[feature_cols]
y = df['target']

if len(X) < 10:
    print("Not enough data to train model.")
    exit(0)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# Feature importances
importances = clf.feature_importances_
importance_df = pd.DataFrame({'Feature': feature_cols, 'Importance': importances})
importance_df = importance_df.sort_values(by='Importance', ascending=False)

plt.figure(figsize=(10,6))
sns.barplot(data=importance_df, x='Importance', y='Feature')
plt.title('Feature Importances for Predicting Next-Day Profitability')
plt.tight_layout()
os.makedirs('charts', exist_ok=True)
plt.savefig('charts/feature_importances.png')
plt.close()

print("Model training complete. Feature importances saved to 'charts/feature_importances.png'.")
