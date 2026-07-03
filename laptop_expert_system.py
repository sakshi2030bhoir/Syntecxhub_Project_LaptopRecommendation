# Laptop Recommendation Expert System
# Rule-Based Expert System using Forward Chaining

rules = [
    ({"gaming", "budget_high"}, "high_performance_user"),
    ({"high_performance_user"}, "gaming_laptop"),

    ({"programming", "portability"}, "developer_user"),
    ({"developer_user", "budget_medium"}, "developer_laptop"),

    ({"video_editing", "budget_high"}, "creator_user"),
    ({"creator_user"}, "creator_laptop"),

    ({"office_work", "battery_life"}, "business_laptop"),

    ({"student_use", "budget_low"}, "student_laptop"),

    ({"portability", "battery_life"}, "ultrabook_user"),
    ({"ultrabook_user"}, "ultrabook")
]

recommendations = {
    "gaming_laptop": [
        "ASUS ROG Strix",
        "Lenovo Legion",
        "Acer Predator"
    ],

    "developer_laptop": [
        "Lenovo ThinkPad",
        "Dell XPS",
        "MacBook Air"
    ],

    "creator_laptop": [
        "MacBook Pro",
        "ASUS ProArt",
        "Dell XPS 17"
    ],

    "business_laptop": [
        "Dell Latitude",
        "HP EliteBook",
        "Lenovo ThinkPad T14"
    ],

    "student_laptop": [
        "Acer Aspire",
        "HP 15",
        "Lenovo IdeaPad"
    ],

    "ultrabook": [
        "ASUS Zenbook",
        "LG Gram",
        "MacBook Air"
    ]
}

facts = set()

print("\n========== Laptop Recommendation Expert System ==========\n")

# Budget
print("Select Budget:")
print("1. Low (< ₹50,000)")
print("2. Medium (₹50,000 - ₹1,00,000)")
print("3. High (> ₹1,00,000)")

budget = input("Enter choice (1/2/3): ")

if budget == "1":
    facts.add("budget_low")
elif budget == "2":
    facts.add("budget_medium")
elif budget == "3":
    facts.add("budget_high")
else:
    print("Invalid choice!")
    exit()

# Purpose
print("\nSelect Purpose:")
print("1. Gaming")
print("2. Programming")
print("3. Video Editing")
print("4. Office Work")
print("5. Student Use")

purpose = input("Enter choice (1/2/3/4/5): ")

if purpose == "1":
    facts.add("gaming")
elif purpose == "2":
    facts.add("programming")
elif purpose == "3":
    facts.add("video_editing")
elif purpose == "4":
    facts.add("office_work")
elif purpose == "5":
    facts.add("student_use")
else:
    print("Invalid choice!")
    exit()

# Portability
portability = input("\nNeed portability? (yes/no): ").lower()

if portability == "yes":
    facts.add("portability")

# Battery
battery = input("Need long battery life? (yes/no): ").lower()

if battery == "yes":
    facts.add("battery_life")

print("\n========== Your Requirements ==========")

for fact in facts:
    print("-", fact)

print("\n========== Reasoning Process ==========\n")

changed = True

while changed:
    changed = False

    for conditions, conclusion in rules:

        if conditions.issubset(facts):

            if conclusion not in facts:

                facts.add(conclusion)

                print(
                    f"Rule Applied: {conditions} -> {conclusion}"
                )

                changed = True

print("\n========== Expert Opinion ==========\n")

recommendation_found = False

for category in recommendations:

    if category in facts:

        recommendation_found = True

        print("Recommended Category:")
        print(category.replace("_", " ").title())

        print("\nSuggested Laptop Models:")

        for laptop in recommendations[category]:
            print("•", laptop)

        break

if not recommendation_found:
    print("No suitable recommendation found.")

print("\nThank you for using the system.")