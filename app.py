from src.agents import SchedulingAgents
from src.tasks import SchedulingTask
from src.get_playlist import get_random_playlist
import streamlit as st

def main():
    st.set_page_config(initial_sidebar_state="expanded")  
    st.title("🏋️‍♂️GymTunes : Never miss a beat")
    st.text("Schedule a random Spotify playlist for your gym session")

    st.divider()
    a = st.sidebar
    with a:
        st.markdown("""
        ## About
        I struggle a lot when I go to gym and I don't have a playlist to listen to. So I created this app to help me schedule a google calendar event with a random Spotify playlist based on my mood/vibe whenever I want. 
                    
        ## How?
        I made this simple application using Composio for connecting with Google Calendar(using Cohere agent), Spotipy to extract playlists, and streamlit to make the UI. Just enter your mood, enter the time you go to gym, and you'll have a playlist ready for you in your Google calendar.
        
        #### Note:
        Support for Google Calendar in Composio is [not there yet](https://docs.composio.dev/apps/google-calendar)
        """
        )

        c_api = st.text_input("COHERE_API_KEY")
        sp_cid = st.text_input("SPOTIPY_CLIENT_ID")
        sp_cs = st.text_input("SPOTIPY_CLIENT_SECRET")

        if st.button("Submit"):
            assert c_api != "", "COHERE_API_KEY cannot be empty" 
            assert sp_cid != "", "SPOTIPY_CLIENT_ID cannot be empty"
            assert sp_cs != "", "SPOTIPY_CLIENT_SECRET cannot be empty"
            st.success("API keys submitted successfully")
        st.markdown(""" 
            ## Improvements 
            - As soon as Composio has a Google Calendar agent, I'll add that feature.
            - Add more features like adding the playlist to your Spotify account"""
        )
    st.text("Enter your vibe, it could be anything like 'workout', 'chill' or 'bollywood' :) ")
    mood = st.text_input("Vibe?")
    st.text("Enter the time you go to gym. We'll schedule the event with that playlist for you.")
    time_for_play = st.time_input("Time?")
    


    if st.button("Schedule"):
        # initiate the agents

        sched_agent = SchedulingAgents().schedule_event_agent(cohere_api_key=c_api)

        # get the description from the test_spotify function
        desc = get_random_playlist(mood, client_id=sp_cid, client_secret=sp_cs)

        # initiate the tasks
        scheduling_task = SchedulingTask().generate_schedule_task(sched_agent, desc, time_for_play)


        scheduling_task.execute()
        st.spinner("Loading...")
        st.success("Task scheduled successfully")

if __name__ == '__main__':
    main()