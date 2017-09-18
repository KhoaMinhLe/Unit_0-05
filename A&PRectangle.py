# Created by: Khoa Le
# Created on September 18 2017
# Created for ICS3U
# This program is the "Area and Perimeter of a Rectangle" with GUI

import ui

def answer_touch_up_inside(sender):
	view['area_answer_label'].text = str(5*3) + ("cm^2")
	view['perimeter_answer_label'].text = str(2*(5+3)) + ("cm")

view = ui.load_view()
view.present('sheet')
