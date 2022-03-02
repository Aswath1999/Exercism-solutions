def round_scores(student_scores):
    """
    :param student_scores: list of student exam scores as float or int.
    :return: list of student scores *rounded* to nearest integer value.
    """
    return [round(num) for num in student_scores]


def count_failed_students(student_scores):
    """
    :param student_scores: list of integer student scores.
    :return: integer count of student scores at or below 40.
    """
    count=0
    for i in student_scores:
        if i<=40:
            count+=1
    return count
        

def above_threshold(student_scores, threshold):
    """
    :param student_scores: list of integer scores
    :param threshold :  integer
    :return: list of integer scores that are at or above the "best" threshold.
    """
    best=[]
    for i in student_scores:
        if i>=threshold:
            best.append(i)
    return best


def letter_grades(highest):
    """
    :param highest: integer of highest exam score.
    :return: list of integer score thresholds for each F-A letter grades.
    """
    grade=round((highest-40)/4)
    return [(41+i*grade)for i in range(4)]
def student_ranking(student_scores, student_names):
    """
     :param student_scores: list of scores in descending order.
     :param student_names: list of names in descending order by exam score.
     :return: list of strings in format ["<rank>. <student name>: <score>"].
     """
    studentscore=zip(range(len(student_scores)),student_scores,student_names)
    return [f'{i+1}. {k}: {j}' for i,j,k in studentscore]

    # return [f'{i}. {k}: {j}' for i,(j,k) in enumerate(zip(student_scores,student_names),1)]

    


def perfect_score(student_info):
    """
    :param student_info: list of [<student name>, <score>] lists
    :return: First [<student name>, 100] found OR "No perfect score."
    """
    for i,j in student_info:
        if j==100:
            return [i,j]
    return "No perfect score."

