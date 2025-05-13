from collections import deque

class Node:
    def __init__(self, ride):
        self.ride = ride
        self.next = None

class RideHistory:
    def __init__(self):
        self.head = None

    def add_ride(self, ride):
        new_node = Node(ride)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def display(self):
        print("\nCompleted Ride History:")
        current = self.head
        count = 1
        while current:
            ride = current.ride
            print(f"{count}. From {ride['from']} to {ride['to']} | Fare: Rs {ride['fare']:.2f}")
            current = current.next
            count += 1
        if count == 1:
            print("No completed rides yet.")

class RideSharingSystem:
    """Main Ride Sharing System class."""
    def __init__(self):
        self.ride_queue = deque()  
        self.completed_rides = RideHistory()  
        self.distances = {
            'Lahore': {'Karachi': 1200, 'Islamabad': 400},
            'Karachi': {'Lahore': 1200, 'Islamabad': 1400},
            'Islamabad': {'Lahore': 400, 'Karachi': 1400}
        }

    def predict_fare(self, distance):
        """Calculate fare based on distance."""
        return distance * 50  

    def request_ride(self, source, destination):
        """Get the distance between source and destination."""
        if source not in self.distances or destination not in self.distances[source]:
            print("Invalid route. Using default distance of 5 km.")
            return 5
        return self.distances[source][destination]

    def book_ride(self):
        """Book a new ride."""
        source = input("Enter source (Lahore, Karachi, Islamabad): ").capitalize()
        destination = input("Enter destination (Lahore, Karachi, Islamabad): ").capitalize()

        distance = self.request_ride(source, destination)
        fare = self.predict_fare(distance)

        ride = {
            'from': source,
            'to': destination,
            'fare': round(fare, 2)
        }

        self.ride_queue.append(ride)
        print(f"Ride added to queue. Estimated fare: Rs {fare:.2f}\n")

    def serve_ride(self):
        """Serve the next ride in the queue."""
        if not self.ride_queue:
            print("No rides to serve.\n")
            return
        ride = self.ride_queue.popleft()
        self.completed_rides.add_ride(ride)
        print(f"🚕 Ride from {ride['from']} to {ride['to']} completed. Fare: Rs {ride['fare']:.2f}\n")

    def view_completed_rides(self):
        """View all completed rides."""
        self.completed_rides.display()

    def main_menu(self):
        """Main menu for the ride sharing system."""
        while True:
            print("\n🚗 Ride Sharing Menu")
            print("1. Book a Ride")
            print("2. Serve Next Ride")
            print("3. View Completed Rides")
            print("4. Exit")

            choice = input("Select an option: ")

            if choice == '1':
                self.book_ride()
            elif choice == '2':
                self.serve_ride()
            elif choice == '3':
                self.view_completed_rides()
            elif choice == '4':
                print("👋 Exiting. Thank you!")
                break
            else:
                print("❌ Invalid choice. Please try again.\n")

if __name__ == "__main__":
    system = RideSharingSystem()
    system.main_menu()