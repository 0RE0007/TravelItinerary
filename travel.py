import streamlit as st
import random

def generate_itinerary(num_days):
    destinations = ["Paris", "Tokyo", "New York", "London", "Rome"]
    activities = {
        "Sightseeing": ["Eiffel Tower", "Tokyo Tower", "Central Park", "Big Ben", "Colosseum"],
        "Museum": ["Louvre Museum", "National Museum of Tokyo", "The Met", "British Museum", "Vatican Museums"],
        "Cuisine": ["French Cuisine", "Sushi Bars", "Pizza Joints", "Fish and Chips", "Italian Restaurants"]
    }

    itinerary = {}

    for day in range(1, num_days + 1):
        destination = random.choice(destinations)
        day_activities = {
            "Destination": destination,
            "Activities": {}
        }

        for activity_type, places in activities.items():
            selected_place = random.choice(places)
            day_activities["Activities"][activity_type] = selected_place

        itinerary[f"Day {day}"] = day_activities

    return itinerary

def main():
    st.title("Travel Itinerary Generator")

    num_days = st.slider("Select the number of days for your trip:", min_value=1, max_value=10, value=1)

    if st.button("Generate Itinerary"):
        generated_itinerary = generate_itinerary(num_days)
        st.subheader("Generated Itinerary:")
        
        for day, activities in generated_itinerary.items():
            st.write(f"\n{day}:")
            st.write(f"  Destination: {activities['Destination']}")
            st.write("  Activities:")
            
            for activity_type, place in activities['Activities'].items():
                st.write(f"    {activity_type}: {place}")

if __name__ == "__main__":
    main()
