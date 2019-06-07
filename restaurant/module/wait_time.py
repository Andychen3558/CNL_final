def waiting_time_evaluate(timeout, skip_probability, arrive_time, average_dining_time, table_number):
	total_number = len(arrive_time)
	if total_number == 0:
		return []
	print("timeout:{}, arrive_time:{}, total_number:{}".format(timeout, arrive_time, total_number))
	time = [0.0 for i in range(total_number)]
	max_reserve = calculate_max_reserve(timeout, table_number, average_dining_time)
	for i in range(total_number):
		if i == 0:
			time[i] = float(average_dining_time) / float(table_number - max_reserve)
		else:
			temp1 = time[i - 1] + skip_probability * timeout + (1 - skip_probability) * min(arrive_time[i - 1], timeout)
			temp2 = time[i - 1] + float(average_dining_time) / (table_number - max_reserve)
			time[i] = min(temp1, temp2)
			time[i - 1] = int(time[i - 1])
	time[total_number - 1] = int(time[total_number - 1])
	return time
def calculate_max_reserve(timeout, table_number, average_dining_time):
	k = 0
	value = 0.0
	while(value < timeout):
		k += 1
		value += (float(average_dining_time) / (table_number - k))
	return k


def update_eattime(eattime_yesterday, eattimes_today):
	# eattime_yesterday: the estimated eattime from yesterday
	# eattimes_today: everyone's eattime for current day
	alpha_1 = 0.05
	avg_eattime = sum(eattimes_today) / (len(eattimes_today) + 1e-8)
	return eattime_yesterday + alpha_1*(avg_eattime - eattime_yesterday)


def update_arrivetime(arrivetime_history, arrivetime_update):# minimum timeout
	alpha_2 = 0.3
	return arrivetime_history + alpha_2*(arrivetime_update-arrivetime_history)
	
def update_skip_prob(reservations_history, skips_history):
	# array of number of reservations in history
	# array of number of skips in history

	# ML estimate
	new_estimate = sum(skips_history) / (sum(reservations_history) + 1e-8)
	return new_estimate
