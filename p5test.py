import numpy as np 
from icecream import ic

#test slicing arrays
exam_average = np.array([36,42,40,42,36,34, 35,40,40,43,36,38, 38,46,45,40,38,42, 42,42,43,30,45,47])
per_year_divided = exam_average.reshape(4,6)

year1_score = per_year_divided[0]
year2_score = per_year_divided[1]
year3_score = per_year_divided[2]
year4_score = per_year_divided[3]

school_average1 = round(np.mean(exam_average), 2)
year1_ave = round(np.mean(year1_score), 2)
year2_ave = round(np.mean(year2_score), 2)
year3_ave = round(np.mean(year3_score), 2)
year4_ave = round(np.mean(year4_score), 2)
school_average2 = np.mean([year1_ave, year1_ave, year3_ave, year4_ave])

print(f" 1st Year: {year1_score} ({year1_ave})\n", f"2nd Year: {year2_score} ({year2_ave})\n", f"3rd Year: {year3_score} ({year3_ave})\n", f"4th Year: {year4_score} ({year4_ave})")
print(f"\nSchool's Average: {school_average1, school_average2}")