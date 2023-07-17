"""
Program: investmentGUI.py
Author: Joseph Reccardo 7/14/2023

Standard Python language GUI-based version of the investment calculator app which takes input from the user and returns a breakdown year by year, the new total balance, as well as the total amout earned from interest in tabular format.

NOTE: The file breezypythongui.py MUST be in the same directory as this file for the app to run correctly!
"""

from breezypythongui import EasyFrame
# Other imports go here

# Class Header
class TextAreaDemo(EasyFrame):
	# Definition of our class constructor method
	def __init__(self):
		#Call to the Easy Frame constructor method
		EasyFrame.__init__(self, title = "Investment Calculator")

		#Create and add the components to the window
		self.addLabel(text = "Initial amount:", row = 0, column = 0)
		self.addLabel(text = "Number of years:", row = 1, column = 0)
		self.addLabel(text = "Intrest rate percent %:", row = 2, column = 0)

		self.amount = self.addFloatField(value = 0.0, row = 0, column = 1)
		self.period = self.addIntegerField(value = 0, row = 1, column = 1, width = 20)
		self.rate = self.addFloatField(value = 0.0, row = 2, column = 1)

		self.compute = self.addButton(text = "Compute", row = 3, column = 0, columnspan = 2, command = self.compute)
		self.compute["background"] = "SlateBlue"
		self.compute["foreground"] = "SeaShell"
		self.compute["width"] = 15

		self.outputArea = self.addTextArea(text = "", row = 4, column = 0, columnspan = 2, width = 50, height = 15)

	#Definition of the compute() function
	def compute(self):
		"""Computes the investment schedule based on the inputs and outputs of the schedule"""
		#Obtain and validate the inputs
		startBalance = self.amount.getNumber()
		years = self.period.getNumber()
		rate = self.rate.getNumber() / 100
		
		if startBalance == 0 or rate == 0 or years == 0:
			return

		#Initialize the accumulator varible for the interest over time.
		totalInterest = 0.0

		#Display the header in tabular format for the output
		result = "%4s%18s%10s%16s\n" % ("Year", "Starting Balance", "Interst", "Ending Balance")

		#Compute and append (add to the end) the results for each year.
		for year in range(1, years + 1):
			interest = startBalance * rate
			endBalance = startBalance + interest
			result += "%4d%18.2f%10.2f%16.2f\n" % (year, startBalance, interest, endBalance)
			startBalance = endBalance
			totalInterest += interest

		#Append the totals for the entire investment period
		result += "Ending balance: $%0.2f\n" % endBalance
										#The perecent sign names the column
		result += "Total interest earned: $%0.2f\n" % totalInterest

		#Output the final result
		self.outputArea["state"] = "normal"
		self.outputArea.setText(result)
		self.outputArea["state"] = "disabled"

# Global definition of the main() method
def main():
	TextAreaDemo().mainloop()

# Global call to main() for program entry
if __name__ == '__main__':
	main()