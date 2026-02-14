"""
Author: Ashkan Pazaj
Assignment: #1
"""

# Step b: Create 4 variables with their data types commented inline
gym_member = "Alex Alliton"      # str
preferred_weight_kg = 20.5       # float
highest_reps = 25                # int
membership_active = True         # bool

# Step c: workout_stats (dict) - keys are friend names (str), values are tuples of 3 ints (yoga, running, weightlifting)
workout_stats = {
    "Alex": (30, 45, 20),
    "Jamie": (25, 35, 40),
    "Taylor": (40, 30, 55),
}

# Step d: Calculate total workout minutes for each friend and add to dictionary
friends = [name for name in workout_stats if not name.endswith("_Total")]
for friend_name in friends:
    total_minutes = sum(workout_stats[friend_name])
    workout_stats[f"{friend_name}_Total"] = total_minutes

# Step e: workout_list (list) - 2D nested list of ints; rows = friends, columns = activities (yoga, running, weightlifting)
workout_list = []
for friend_name in friends:
    yoga, running, weightlifting = workout_stats[friend_name]
    workout_list.append([yoga, running, weightlifting])

# Step f: Slice workout_list
# Extract and print yoga and running minutes for all friends
yoga_and_running_all = [row[0:2] for row in workout_list]
print("Yoga and running minutes for all friends:", yoga_and_running_all)

# Extract and print weightlifting minutes for the last two friends
weightlifting_last_two = [row[2] for row in workout_list[-2:]]
print("Weightlifting minutes for the last two friends:", weightlifting_last_two)

# Step g: Check if any friend's total workout minutes are >= 120
for friend_name in friends:
    total_key = f"{friend_name}_Total"
    if workout_stats[total_key] >= 120:
        print(f"Great job staying active, {friend_name}!")

# Step h: Allow user to input a friend's name and look up their stats
lookup_name = input("\nEnter a friend's name to look up: ").strip()
if lookup_name in workout_stats:
    yoga, running, weightlifting = workout_stats[lookup_name]
    total_minutes = workout_stats[f"{lookup_name}_Total"]
    print(f"\nWorkout stats for {lookup_name}:")
    print(f"  Yoga: {yoga} minutes")
    print(f"  Running: {running} minutes")
    print(f"  Weightlifting: {weightlifting} minutes")
    print(f"  Total: {total_minutes} minutes")
else:
    print(f"Friend {lookup_name} not found in the records.")

# Step i: Print the friend with the highest and lowest total workout minutes
friend_totals = {name: workout_stats[f"{name}_Total"] for name in friends}

highest_friend = max(friend_totals, key=friend_totals.get)
lowest_friend = min(friend_totals, key=friend_totals.get)

print("\nSummary:")
print(f"Highest total workout minutes: {highest_friend} ({friend_totals[highest_friend]} minutes)")
print(f"Lowest total workout minutes: {lowest_friend} ({friend_totals[lowest_friend]} minutes)")