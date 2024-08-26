import csv
import os

def match_mentors_mentees(filepath):
    mentors = []
    mentees = []
    with open(filepath, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Mentor/Mentee'] == "Mentor":
                mentors.append(row)
            else:
                mentees.append(row)

    mentor_mentee_pairs = []
    matched_mentors = set()
    matched_mentees = set()
    for mentee in mentees:
        if mentee['First and Last Name'] in matched_mentees:
            continue
        interests = set(mentee['Interests'].split(','))
        ai_interests = set(mentee['AI Interests'].split(','))
        best_match = None
        best_match_score = 0
        for mentor in mentors:
            if mentor['First and Last Name'] in matched_mentors:
                continue
            mentor_interests = set(mentor['Interests'].split(','))
            mentor_ai_interests = set(mentor['AI Interests'].split(','))
            score = len(interests.intersection(mentor_interests)) + len(ai_interests.intersection(mentor_ai_interests))
            if score > best_match_score:
                best_match = mentor
                best_match_score = score
        if best_match:
            matched_mentors.add(best_match['First and Last Name'])
            matched_mentees.add(mentee['First and Last Name'])
            mentor_mentee_pairs.append((best_match, mentee))
    return mentor_mentee_pairs

pairs = match_mentors_mentees(os.path.join(os.environ['HOME'], 'Desktop', 'mentormatch', 'mentordata.csv'))
for mentor, mentee in pairs:
    print("Mentor: {0} {1} <{2}>".format(mentor['First and Last Name'], mentor['Email'], mentor['LinkedIn']))
    print("Mentee: {0} {1} <{2}>".format(mentee['First and Last Name'], mentee['Email'], mentee['LinkedIn']))
    print()


