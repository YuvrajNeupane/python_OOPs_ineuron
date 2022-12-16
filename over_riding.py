class ineuron:
    def student(self):
        print("Print the all student details. ")
    def achivers(self):
        print( 'Print the all the achivers details.')
    def hall_of_fame(self):
        print( 'Print the all the hall of fame details.')


class ineuron_vision(ineuron):
    def student(self):
        print('These are the filtered student list.')

iv = ineuron_vision()
iv.student()
i = ineuron()
i.student()
