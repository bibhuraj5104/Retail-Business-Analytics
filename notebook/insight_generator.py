from pathlib import Path
from datetime import datetime
import pandas as pd

# ==============================
# Locate Project Folder
# ==============================

BASE_DIR = Path(__file__).resolve().parent.parent
csv_path = BASE_DIR / "dataset" / "customer_shopping_behavior.csv"

df = pd.read_csv(csv_path)

# ==============================
# Create Age Group
# ==============================

bins = [0, 25, 35, 50, 100]
labels = ["Young Adult", "Adult", "Middle-aged", "Senior"]

df["Age Group"] = pd.cut(df["Age"], bins=bins, labels=labels)

report = []

# ==================================
# Highest Revenue Category
# ==================================

category = (
    df.groupby("Category")["Purchase Amount (USD)"]
    .sum()
    .idxmax()
)

report.append({
    "Priority":"High",
    "Type":"Category",
    "Insight":f"{category} generated the highest revenue.",
    "Recommendation":f"Increase inventory and marketing for {category}.",
    "Business Impact":"Revenue Growth"
})

# ==================================
# Best Season
# ==================================

season = (
    df.groupby("Season")["Purchase Amount (USD)"]
    .sum()
    .idxmax()
)

report.append({
    "Priority":"Medium",
    "Type":"Season",
    "Insight":f"{season} recorded the highest revenue.",
    "Recommendation":f"Launch promotional campaigns during {season}.",
    "Business Impact":"Seasonal Sales"
})

# ==================================
# Preferred Shipping
# ==================================

shipping = df["Shipping Type"].value_counts().idxmax()

report.append({
    "Priority":"Medium",
    "Type":"Shipping",
    "Insight":f"{shipping} is the most preferred shipping method.",
    "Recommendation":f"Improve logistics for {shipping}.",
    "Business Impact":"Customer Satisfaction"
})

# ==================================
# Preferred Payment
# ==================================

payment = df["Payment Method"].value_counts().idxmax()

report.append({
    "Priority":"Low",
    "Type":"Payment",
    "Insight":f"{payment} is the most used payment method.",
    "Recommendation":f"Provide cashback offers for {payment}.",
    "Business Impact":"Customer Retention"
})

# ==================================
# Highest Spending Gender
# ==================================

gender = (
    df.groupby("Gender")["Purchase Amount (USD)"]
    .mean()
    .idxmax()
)

report.append({
    "Priority":"Medium",
    "Type":"Customer",
    "Insight":f"{gender} customers spend the highest on average.",
    "Recommendation":f"Run personalized campaigns for {gender} customers.",
    "Business Impact":"Targeted Marketing"
})

# ==================================
# Highest Revenue Age Group
# ==================================

age_group = (
    df.groupby("Age Group")["Purchase Amount (USD)"]
    .sum()
    .idxmax()
)

report.append({
    "Priority":"High",
    "Type":"Age Group",
    "Insight":f"{age_group} customers generate the highest revenue.",
    "Recommendation":f"Launch loyalty programs for {age_group}.",
    "Business Impact":"Customer Loyalty"
})

# ==================================
# Average Purchase
# ==================================

avg_purchase = round(df["Purchase Amount (USD)"].mean(),2)

report.append({
    "Priority":"iLow",
    "Type":"Purchase",
    "Insight":f"Average purchase amount is ${avg_purchase}.",
    "Recommendation":"Increase average order value using product bundles.",
    "Business Impact":"Upselling"
})

# ==================================
# Last Updated
# ==================================

last_updated = datetime.now().strftime("%d-%m-%Y %H:%M")

result = pd.DataFrame(report)

result["Last Updated"] = last_updated

# ==================================
# Save CSV
# ==================================

output = BASE_DIR / "dataset" / "business_recommendations.csv"

result.to_csv(output,index=False)

print(result)

print("\nBusiness Recommendation Engine Updated Successfully!")