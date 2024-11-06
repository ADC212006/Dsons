import requests
import os

# List of URLs to download
urls = [
    "http://58.65.161.110/avatar114/assets/mm/Intro_-11.mp3",
    "http://58.65.161.110/avatar114/assets/mm/Doing_great_-_2.mp3",
    "http://58.65.161.110/avatar114/assets/mm/Are_you_there_-_12.mp3",
    "http://58.65.161.110/avatar114/assets/mm/Not_Interested-1_-_11.mp3",
    "http://58.65.161.110/avatar114/assets/mm/Greeting_011.mp3",
    "http://58.65.161.110/avatar114/assets/mm/Glad_to_hear_-_12.mp3",
    "http://58.65.161.110/avatar114/assets/mm/Anyone_online_-_3.mp3",
    "http://58.65.161.110/avatar114/assets/mm/Not_Interested-2_-_11.mp3",
    "http://58.65.161.110/avatar114/assets/mm/1_(1).mp3",
    "http://58.65.161.110/avatar114/assets/mm/Oh_sorry_-_1.mp3",
    "http://58.65.161.110/avatar114/assets/mm/Is_that_okay_-_2.mp3",
    "http://58.65.161.110/avatar114/assets/mm/Busy_1_-_2.mp3",
    "http://58.65.161.110/avatar114/assets/mm/Name_-_11.mp3",
    "http://58.65.161.110/avatar114/assets/mm/Fantastic_-_1.mp3",
    "http://58.65.161.110/avatar114/assets/mm/Hear_me_-_2.mp3",
    "http://58.65.161.110/avatar114/assets/mm/Busy_2_-1.mp3",
    "http://58.65.161.110/avatar114/assets/mm/2_(1).mp3",
    "http://58.65.161.110/avatar114/assets/mm/Great_-_1.mp3",
    "http://58.65.161.110/avatar114/assets/mm/What_was_that_-_1.mp3",
    "http://58.65.161.110/avatar114/assets/mm/Busy-3_-_1.mp3",
    "http://58.65.161.110/avatar114/assets/mm/Age_-_1.mp3",
    "http://58.65.161.110/avatar114/assets/mm/Yes_-_1.mp3",
    "http://58.65.161.110/avatar114/assets/mm/Have_coverage_-_2.mp3",
    "http://58.65.161.110/avatar114/assets/mm/Banking_Rebuttal_-_2.mp3",
    "http://58.65.161.110/avatar114/assets/mm/DOB_-_1.mp3",
    "http://58.65.161.110/avatar114/assets/mm/No_-_1.mp3",
    "http://58.65.161.110/avatar114/assets/mm/Add_Coverage_-_1.mp3",
    "http://58.65.161.110/avatar114/assets/mm/Health_duration_-_2.mp3",
    "http://58.65.161.110/avatar114/assets/mm/State_-11.mp3",
    "http://58.65.161.110/avatar114/assets/mm/Okay_-_1.mp3",
    "http://58.65.161.110/avatar114/assets/mm/Call_back_-_1.mp3",
    "http://58.65.161.110/avatar114/assets/mm/Debit_Card_Link_1.mp3",
    "http://58.65.161.110/avatar114/assets/mm/Health_-_2.mp3",
    "http://58.65.161.110/avatar114/assets/mm/No_problem_-_1.mp3",
    "http://58.65.161.110/avatar114/assets/mm/Zipcode_-_11.mp3",
    "http://58.65.161.110/avatar114/assets/mm/Mail_me_-_2.mp3",
    "http://58.65.161.110/avatar114/assets/mm/Banking_-_21.mp3",
    "http://58.65.161.110/avatar114/assets/mm/Hold_for_me_-_1.mp3",
    "http://58.65.161.110/avatar114/assets/mm/Location_-_1.mp3",
    "http://58.65.161.110/avatar114/assets/mm/DNC_-_1.mp3",
    "http://58.65.161.110/avatar114/assets/mm/Transfer_-_1.mp3",
    "http://58.65.161.110/avatar114/assets/mm/51.mp3",
    "http://58.65.161.110/avatar114/assets/mm/Agent_name_-_1.mp3",
    "http://58.65.161.110/avatar114/assets/mm/32.mp3",
    "http://58.65.161.110/avatar114/assets/mm/Disclaimer_-_1.mp3",
    "http://58.65.161.110/avatar114/assets/mm/2.mp3",
    "http://58.65.161.110/avatar114/assets/mm/Company_name_-_11.mp3",
    "http://58.65.161.110/avatar114/assets/mm/10.mp3",
    "http://58.65.161.110/avatar114/assets/mm/Disclaimer_Repeat_-_1.mp3",
    "http://58.65.161.110/avatar114/assets/mm/13.mp3",
    "http://58.65.161.110/avatar114/assets/mm/31.mp3",
    "http://58.65.161.110/avatar114/assets/mm/41.mp3",
    "http://58.65.161.110/avatar114/assets/mm/11.mp3",
    "http://58.65.161.110/avatar114/assets/mm/Rate_Above_70.mp3",
    "http://58.65.161.110/avatar114/assets/mm/12.mp3",
    "http://58.65.161.110/avatar114/assets/mm/7.mp3",
    "http://58.65.161.110/avatar114/assets/mm/Follow_Up.mp3",
    "http://58.65.161.110/avatar114/assets/mm/Rate_Below_70.mp3",
    "http://58.65.161.110/avatar114/assets/mm/Hw_Mch_Cov-2.mp3",
    "http://58.65.161.110/avatar114/assets/mm/Direct_exp_card.mp3",
    "http://58.65.161.110/avatar114/assets/mm/15.mp3",
    "http://58.65.161.110/avatar114/assets/mm/21.mp3",
    "http://58.65.161.110/avatar114/assets/mm/Call_you_back.mp3",
    "http://58.65.161.110/avatar114/assets/mm/14_-_LIVE_PERSON.mp3"
]

# Directory to save the downloaded files
save_directory = "downloaded_audio"
os.makedirs(save_directory, exist_ok=True)

# Function to download and save a single file
def download_file(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        file_path = os.path.join(save_directory, url.split('/')[-1])
        with open(file_path, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded {url.split('/')[-1]}")
    except requests.RequestException as e:
        print(f"Failed to download {url.split('/')[-1]}: {str(e)}")

# Download each file
for url in urls:
    download_file(url)

print("All files downloaded.")
