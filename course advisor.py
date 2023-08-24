
# Define the grading scale
grading_scale = {
    'A+': 4.0,
    'A' : 4.0,
    'A-': 3.67,
    'B+': 3.33,
    'B': 3.0,
    'B-': 2.67,
    'C+': 2.33,
    'C': 2.0,
    'C-': 1.67,
    'D+': 1.33,
    'D': 1.0,
    'F': 0.0
}

def calculate_gpa(courses):
    total_credit = 0
    total_grade_points = 0
    
    for course in courses:
        course_name, credits, grade = course
        credit_points = grading_scale.get(grade, 0)
        
        total_credit += credits
        total_grade_points += credits * credit_points

    if total_credit == 0:
        return 0  # To avoid division by zero
    
    gpa = total_grade_points / total_credit
    return round(gpa, 2)

# Example usage
courses = [("Software Engineering 1", 3, "B+"), ("Web Programming 2", 3, "B+"), ("Communications and Networking", 3, "B"), ("Web Programming 1", 3, "B"), ("Data Structures", 3, "C+"), ("Computer Systems", 3, "B-"), ("Programming 2", 3, "B-"), ("Databases 1", 3, "C-"), ("Calculus", 3, "B-"), ("Programming 1", 3, "D"), ("Art History", 3, "A"), ("Introduction to Sociology", 3, "A-"), ("Programming Fundamentals", 3, "C"), ("Introduction to Statistics", 3, "B+"), ("Principles of Business Management", 3, "B-"), ("Introduction to Health Psychology (previously known as Introduction to Human Psychology)", 3, "A-"), ("College Algebra", 3, "B"), ("English Composition 2", 3, "B"), ("Online Education Strategies", 3, "B-"), ("Data Mining and Machine Learning", 3, "A-"), ("Operating Systems 1", 3, "B+")]
gpa = calculate_gpa(courses)
print(f"Your GPA is: {gpa}")

def grades_needed_to_graduate(target_gpa, current_gpa, total_credits_completed, remaining_credits):
    # Calculate the total grade points needed to achieve the target GPA
    target_grade_points = target_gpa * (total_credits_completed + remaining_credits)
    
    # Calculate the remaining grade points needed
    remaining_grade_points = target_grade_points - (current_gpa * total_credits_completed)
    
    # Calculate the required GPA for the remaining courses
    required_gpa = remaining_grade_points / remaining_credits
    
    return required_gpa


target_gpa = 3.0  
current_gpa = gpa  # my current GPA
total_credits_completed = 63  
remaining_credits = 120 - total_credits_completed  

required_gpa = grades_needed_to_graduate(target_gpa, current_gpa, total_credits_completed, remaining_credits)

print(f"To graduate with a {target_gpa} GPA, I need to maintain a GPA of {required_gpa:.2f} in your remaining {remaining_credits} credits.")