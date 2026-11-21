# Cinema Ticket Sale project
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#  1. Sales data (pandas)
data = {
    "Customer": ["Arun", "Ravi", "Priya", "Kumar", "Divya", "Meena"],
    "Movie": ["Leo", "Jailer", "Leo", "Vikram", "Jailer", "Leo"],
    "Tickets": [2, 4, 3, 1, 5, 2],
    "Price": [200, 250, 200, 180, 250, 200]
}
df = pd.DataFrame(data)

# total bill for each booking
df["Total"] = df["Tickets"] * df["Price"]
print(df)

print("Average bill:", df["Total"].mean())
print("Highest bill:", df["Total"].max())
print("Lowest bill:", df["Total"].min())
print("Total tickets sold:", df["Tickets"].sum())
print("Total revenue:", df["Total"].sum())

# customer who paid the most
top = df.loc[df["Total"].idxmax()]
top = top.to_frame().T
print("\nTop customer:")
print(top.to_string(index=False))

# which movie earns more? (management wants to know)
movie_rev = df.groupby("Movie")["Total"].sum()
movie_rev = movie_rev.reset_index()
print("\nRevenue by movie:")
print(movie_rev.to_string(index=False))

# bookings with more than 3 tickets
big = df[df["Tickets"] > 3]
print("\nBig bookings:")
print(big[["Customer", "Tickets"]].to_string(index=False))

print("\nMean =", df["Total"].mean())
print("Standard deviation =", df["Total"].std())

# chart
plt.bar(movie_rev["Movie"], movie_rev["Total"])
plt.title("Movie Revenue")
plt.xlabel("Movie")
plt.ylabel("Revenue")
plt.show()

# save and read csv
df.to_csv("sales.csv", index=False)
df2 = pd.read_csv("sales.csv")
print("\nData read from csv:")
print(df2.head(3))

#  2. List
movies = ["Leo", "Jailer", "Vikram"]
print("\nMovies:", movies)
print("Length:", len(movies))
print("First:", movies[0], " Last:", movies[-1])
print("Slice [0:2]:", movies[0:2])
print("Is Leo in list?", "Leo" in movies)

movies[0] = "Kanguva"          # lists can be changed
movies.append("Amaran")
movies.insert(1, "Varisu")
movies.extend(["Thunivu", "Maaveeran"])
movies.remove("Jailer")
print("After changes:", movies)
print("pop():", movies.pop())
print("index of Amaran:", movies.index("Amaran"))
movies.sort()
print("sorted:", movies)
movies.reverse()
print("reversed:", movies)
backup = movies.copy()
movies.clear()
print("cleared:", movies, " backup:", backup)

prices = [200, 150, 300, 250, 100]
print("min", min(prices), "max", max(prices), "sum", sum(prices))

#3. Dictionary 
ticket = {"name": "Ravi", "movie": "Leo", "seats": 2}
print("\nTicket:", ticket)
print("Name:", ticket["name"])
print("Phone:", ticket.get("phone", "Not found"))

ticket["seats"] = 3             # change
ticket["screen"] = "Screen 1"   # add
ticket.update({"seats": 4, "show": "Evening"})
print("keys:", ticket.keys())
print("values:", ticket.values())
print("pop:", ticket.pop("show"))
print("popitem:", ticket.popitem())
print("Now:", ticket)

price_list = {"Leo": 200, "Jailer": 250, "Vikram": 180}
for movie, p in price_list.items():
    print(movie, "-> Rs.", p)
print("Costliest ticket:", max(price_list.values()))

#  4. Set 
morning = {1, 2, 3, 4}          # booked seats
evening = {3, 4, 5, 6}
print("\nUnion:", morning | evening)
print("Intersection:", morning & evening)
print("Only morning:", morning - evening)
print("Not common:", morning ^ evening)

morning.add(10)
morning.discard(1)
print("Morning seats:", morning)

names = ["Arun", "Ravi", "Arun", "Priya", "Ravi"]
print("Unique customers:", list(set(names)))

#5. Tuple 
timings = ("10:00 AM", "02:00 PM", "06:00 PM", "09:30 PM")
print("\nTimings:", timings)
print("Last show:", timings[-1])
try:
    timings[0] = "11:00 AM"
except TypeError as e:
    print("Error:", e)

name, movie, seat = ("Ravi", "Leo", "A5")   # unpacking
print(name, movie, seat)

# 6. NumPy
tickets = np.array([2, 4, 3, 1, 5])
price = np.array([200, 250, 200, 180, 250])
print("\nBills:", tickets * price)
print("Revenue:", (tickets * price).sum())

shows = np.array([[10, 20, 30],
                  [40, 50, 60]])       # rows = screens
print("Shape:", shows.shape, " Dimensions:", shows.ndim)
print("arange:", np.arange(1, 11, 2))
print("linspace:", np.linspace(1, 10, 5))
print("zeros:", np.zeros(3))

#  7. Functions 
def total_amount(count, rate):
    return count * rate

def discount(amount, percent=10):
    return amount - (amount * percent / 100)

def gst(amount, rate=18):
    return amount + (amount * rate / 100)

print("\n--- Billing ---")
count = int(input("Number of tickets: "))
rate = float(input("Price of one ticket: "))
amount = total_amount(count, rate)
print("Amount:", amount)
print("After discount:", discount(amount))
print("With GST:", gst(amount))

# 8. Ticket counter 
seats_left = {"Leo": 50, "Jailer": 40, "Vikram": 30}

def sell(customer, movie, count):
    if movie not in price_list:
        return "Movie not found"
    if count > seats_left[movie]:
        return "Not enough seats"
    seats_left[movie] -= count
    return customer + " paid Rs." + str(count * price_list[movie])

print("\n--- Ticket Counter ---")
while True:
    who = input("Customer name (exit to stop): ")
    if who == "exit":
        break
    film = input("Movie: ")
    num = int(input("Tickets: "))
    print(sell(who, film, num))
    print("Seats left:", seats_left)

print("Program finished")
