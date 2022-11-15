from datetime import date, timedelta
import PySimpleGUI as sg      


def calculate_deadline(courses, weeks, deadline, course_progress, week_progress):
	# progress = input('What Course / Week are you at now? (enter as "1 4" for course 1, week 4): ')
	# course_progress, week_progress = int(progress.split()[0]), int(progress.split()[1])

	today = date.today()

	deadline = date(int(deadline.split('/')[2]), int(deadline.split('/')[0].lstrip('0')), int(deadline.split('/')[1].lstrip('0')))
	n_days_left = (deadline - today).days 

	courses = int(courses)
	weeks_per_course = int(weeks)

	if course_progress > courses:
		raise ValueError('Number of courses progressed exceeds actual courses')
	elif week_progress > weeks_per_course:
		raise ValueError('Number of weeks progressed exceeds actual weeks')

	t_per_course = n_days_left / (courses - (course_progress - 1))
	t_per_week = n_days_left / ((weeks_per_course * courses - ((course_progress - 1 ) * weeks_per_course + week_progress - 1))) 

	window['-ML1-'].print('You have entered Course', course_progress, 'and Week', week_progress, '\n')
	window['-ML1-'].print('Today is', today, 'and the deadline is on', deadline, '\n')
	window['-ML1-'].print('You have', n_days_left, 'days to complete', (courses - (course_progress - 1)), 'courses.\n')
	window['-ML1-'].print('You have', round(t_per_course, 1), 'days per course and', round(t_per_week, 1), 'days per week. Good Luck.\n')

	# print('You have entered Course', course_progress, 'and Week', week_progress, '\n')
	# print('Today is', today, 'and the deadline is on', deadline, '\n')
	# print('You have', n_days_left, 'days to complete', (courses - (course_progress - 1)), 'courses.\n')
	# print('You have', round(t_per_course, 1), 'days per course and', round(t_per_week, 1), 'days per week. Good Luck.\n')


	total_weeks = 1

	for i in range(course_progress, courses + 1):

		window['-ML1-'].print('Course', i)

		for j in range(week_progress, weeks_per_course):

			window['-ML1-'].print('\tC' + str(i), 'Finish Week', j, 'by', today + timedelta(days= t_per_week * total_weeks ))

			total_weeks += 1
				
		week_progress = 1

		window['-ML1-'].print('Finish Course', i, 'and Week', weeks_per_course ,'by', today + timedelta(days= t_per_week * total_weeks ), '\n')

		
		total_weeks += 1

# calculate_deadline(6,6, '11/11/22', 2, 2)
# quit()

# while input('Enter "quit" to quit, otherwise enter any key to continue to calculate_deadline: ') != 'quit':
# 	print()
# 	try:
# 		calculate_deadline()
# 	except Exception as e:
# 		print('\n!!!!!!!!!!!!!!!!!!!!!!! ERROR !!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
# 		print(e)4
# 		print('-----------------------------------------------------------\n')


sg.theme('DarkAmber')

layout = [[sg.Push(), sg.Text('Enter Total Courses Amount'), sg.Combo(['1','2','3','4','5','6','7','8','9'], key='-IN2-'), sg.Push()],
		  [sg.Push(), sg.Text('Enter Total Weeks Amount'), sg.Combo(['1','2','3','4','5','6','7','8','9'], key='-IN3-'), sg.Push()],
		  [sg.Push(), sg.CalendarButton('Select Deadline',  target='-IN4-', format='%m/%d/%Y'), sg.Input(key='-IN4-', size=(20,1)), sg.Push()],
		  [sg.Text('What Course / Week are you at now? (enter as "1 4" for course 1, week 4): ')],
          [sg.Push(), sg.Input(key='-IN1-'), sg.Button('Show', bind_return_key=True), sg.Push()],       
          [sg.Push(), sg.MLine(key='-ML1-', size=(50,20)), sg.Push()]]

window = sg.Window('Calculate Deadline', layout)

while True:  # Event Loop
	try:
		event, values = window.read()
		if event == sg.WIN_CLOSED or event == 'Exit':
			break
		if event == 'Show':

			window['-ML1-'].Update('')
			v = values['-IN1-']
			course_progress, week_progress = int(v.split()[0]), int(v.split()[1])
			
			c = values['-IN2-']
			w = values['-IN3-']
			d = values['-IN4-']

			calculate_deadline(c, w, d, course_progress, week_progress)
			window['-IN1-'].Update('')

	except Exception as e:
		print(e)
		window['-ML1-'].print('Error: ', e, '\n\nTry Again.')		
		window['-IN1-'].Update('')
    	
window.close()

