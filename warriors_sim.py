import random
import matplotlib.pyplot as plt 
win_prob = 0.8

def warriors_win(x, prob):
    if x <= prob:
        return 1
    else:
        return 0
    
def simulate_season():
    seasonal_wins = []
    for i in range(82):
        x = random.random() # 0 <= x < 1
        seasonal_wins.append(warriors_win(x, win_prob))
    return seasonal_wins
    
def no_consecutive_losses(seasonal_wins):
    prev_result = seasonal_wins[0]
    for i in range(1, len(seasonal_wins)):
        if prev_result == 0 and seasonal_wins[i] == prev_result:
            return False
        prev_result = seasonal_wins[i]
    return True 

def count_consecutive_losses(seasonal_wins):
    count = 0
    prev_result = seasonal_wins[0]
    for i in range(1, len(seasonal_wins)):
        if prev_result == 0 and seasonal_wins[i] == prev_result:
            count += 1
        prev_result = seasonal_wins[i]
    return count 

def run_experiment(num_trials):
    count = 0
    seasonal_consecutive_losses = []
    for i in range(num_trials):
        wins = simulate_season()
        if no_consecutive_losses(wins):
            count += 1
        seasonal_consecutive_losses.append(count_consecutive_losses(wins))
    freq = float(count) / num_trials
    return freq, seasonal_consecutive_losses

num_trials_lst = [100, 500, 1000, 2500, 5000, 10000, 25000, 50000, 75000, 100000, 250000, 500000, 750000, 1000000]
freqs = []
consecutive_losses = []
for num_trials in num_trials_lst:
    freq, seasonal_consecutive_losses = run_experiment(num_trials)
    freqs.append(freq)
    consecutive_losses.extend(seasonal_consecutive_losses)

print freqs 
print sum(freqs) / float(len(freqs))

plt.plot(num_trials_lst, freqs) 
plt.plot(num_trials_lst, [0.059,]*len(num_trials_lst))
plt.xlabel('number of trials')
plt.ylabel('estimated probability')
plt.title('Estimated probability of nonconsecutive losses')
plt.show()
plt.hist(consecutive_losses, bins=20, normed=True)
plt.xlabel('consecutive losses')
plt.ylabel('relative frequency')
plt.title('Number of consecutive losses in 82 games simulated')
plt.show()