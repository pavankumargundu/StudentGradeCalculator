print("==============================================")
print("      B.TECH CSE R23 SGPA CALCULATOR")
print("==============================================")

# Grade points according to R23
grade_points = {
    "S": 10,
    "A": 9,
    "B": 8,
    "C": 7,
    "D": 6,
    "E": 5,
    "F": 0,
    "AB": 0,
    "Completed": 0
}

subjects = [
    ("r231101", "Communicative English", 3),
    ("r231101", "Communicative English Lab", 1),
    ("r231103", "Chemistry", 3),
    ("r231103", "Chemistry Lab", 1),
    ("r231105", "Linear algebra & calculus", 3),
    ("r231105", "Engineering workshop Lab", 1.5),
    ("r231106", "Basic Civil & Mechanical Engineering", 3),
    ("r231106", "Computer Programming Lab", 1.5),
    ("r231107", "Introduction to Programming", 3),
    ("r231107", "Health & Wellness Yoga & Sports", 0.5),
    ("r231201", "Engineering Physics", 3),
    ("r231201", "IT workshop Lab", 1),
    ("r231202", "Differntial Equations & VEctor Calculus", 3),
    ("r231202", "Engineering Physics Lab", 1),
    ("r231203", "Basic Electrical & Electronics Engineering", 3),
    ("r231203", "Basic Electrical & Electronics Engineering Workshop Lab", 1.5),
    ("r231204", "Engineering Grapics", 3),
    ("r231204", "NSS/NCC/Scouts & Guides/Community Service", 0.5),
    ("r231205", "Data Structures", 3),
    ("r231205", "Data Structures Lab", 1.5),
    ("r2321012", "Universal Human Values", 3),
    ("r2321051", "Discrete Mathematics & Graph Theory", 3),
    ("r2321052", "Digital Logic & Computer Organization", 3),
    ("r2321053", "Advance Data Structers", 3),
    ("r2321054", "Object Oriented Programming Throuh Java", 3),
    ("r2321055", "Advance Data Structers Lab", 1.5),
    ("r2321056", "Object Oriented Programming Throuh Java Lab", 1.5),
    ("r2321057", "Python Programming Lab", 2),
    ("R2322019", "Design Thinking & Innovation", 2),
    ("R2322051", "Managerial Economics and Financial Analysis", 2),
    ("R2322052", "Probability & Statistics", 3),
    ("R2322053", "Operating Systems", 3),
    ("R2322054", "Database Management Systems", 3),
    ("R2322055", "Software Engineering", 3),
    ("R2322056", "Operating Systems Lab", 1.5),
    ("R2322057", "Database Management Systems Lab", 1.5),
    ("R2322058", "Full Stack Development-I", 2),
    ("R233101E", "Construction Technology and Management", 3),
    ("R2331051", "Data Warehousing & Data Mining", 3),
    ("R2331052", "Computer Networks", 3),
    ("R2331053", "Formal Languages and Automata Theory", 3),
    ("R2331054", "Datamining Lab", 1.5),
    ("R2331055", "Computer Networks Lab", 1.5),
    ("R2331056", "Full Stack Development-2", 2),
    ("R2331057", "User Interface Design Using Flutter", 1),
    ("R2331059", "Evaluation of Community Service Internship", 2),
    ("R233105A", "Object Oriented Analysis and Design", 3),
    ("R2332055", "Cryptography & Network Security Lab", 1.5),
    ("R2332055C", "DevOps", 3),
    ("R2332053J", "Industrial Management", 3),
    ("R2332054", "Cloud Computing Lab", 1.5),
    ("R2332052", "Cloud Computing", 3),
    ("R233205F", "Software Project Management", 3),
    ("R2332056", "Soft Skills / Swayam Plus - 21st Century Employability Skills", 2),
    ("R2332053", "Cryptography & Network Security", 3),
    ("R2332051", "Compiler Design", 3),
    ("R2332057", "Technical Paper Writing & IPR", 0),
]


total_credits = 0
total_points = 0

print("\nEnter your grades:")
print("S=10  A=9  B=8  C=7  D=6  E=5  F=0  AB=0\n")

for code, name, credits in subjects:
    print("----------------------------------------------")
    print("Code    :", code)
    print("Subject :", name)
    print("Credits :", credits)

    grade = input("Enter grade: ").strip().upper()

    while grade not in grade_points:
        print("Invalid grade! Use S, A, B, C, D, E, F, Completed or AB.")
        grade = input("Enter grade: ").strip().upper()

    point = grade_points[grade]
    total_credits += credits
    total_points += credits * point

if total_credits == 0:
    sgpa = 0
else:
    sgpa = total_points / total_credits

print("\n==============================================")
print("                 RESULT")
print("==============================================")
print("Total Credits :", total_credits)
print("Total Points  :", total_points)
print("SGPA          :", round(sgpa, 2))
print("==============================================")

