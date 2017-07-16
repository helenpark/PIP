# If we rob house[i], we couldn't rob house[i-1], but we could rob house[i-2].
# If we don't rob house[i], we could rob house[i-1].
# Choose the one gets more money.

rob_house[i]= max(house[i] + rob_house[i-2], rob_house[i-1])