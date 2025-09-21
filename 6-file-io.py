import csv
college_data = {'University Name': ['University of Washington', 'University of Michigan', 'University of Virigina'],
                'In-State Tuition (USD)': [13406, 17228, 20986],
                'Acceptance Rate (%)': [42.5, 17.9, 16.9]}

with open('college_data.csv', 'w', newline='') as f:
    fields = ['University Name', 'In-State Tuition (USD)', 'Acceptance Rate (%)']
    
    writer = csv.DictWriter(f, fields)
    writer.writeheader()
    
    num_rows = len(next(iter(college_data.values())))
    
    for i in range(num_rows):
        row_dict = {}
        for key in college_data.keys():
            row_dict[key] = college_data[key][i]
        writer.writerow(row_dict)
