size = 8

def FCFS(arr, head):

	seek_count = 0
	distance, cur_track = 0, 0

	for i in range(size):
		cur_track = arr[i]

		distance = abs(cur_track - head)

		seek_count += distance

		head = cur_track
	
	print("Total number of seek operations = ",
								seek_count)

	print("Seek Sequence is")

	for i in range(size):
		print(arr[i])

if __name__ == '__main__':

	arr = [ 176, 79, 34, 60,
			92, 11, 41, 114 ]
	head = 50;

	FCFS(arr, head)