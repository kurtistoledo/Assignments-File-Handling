# Lesson 5: File Handling
# 3. Advanced Python Data Processing and Analysis Challenge

def read_travel_blogs(filename):
    try:
        with open(filename, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return []

def analyze_sentiment(blogs):
    positive_words = ["amazing", "enjoy", "beautiful", "fantastic", "memorable"]
    negative_words = ["disappointing", "poor", "lackluster", "crowded"]

    positive_count = 0
    negative_count = 0

    for blog in blogs:
        words = blog.lower().split()
        for word in words:
            if word in positive_words:
                positive_count += 1
            elif word in negative_words:
                negative_count += 1

    return positive_count, negative_count

# Example usage
travel_blogs_file = "travel_blogs.txt"
blogs = read_travel_blogs(travel_blogs_file)
if blogs:
    positive, negative = analyze_sentiment(blogs)
    print(f"Positive words count: {positive}")
    print(f"Negative words count: {negative}")
else:
    print("No travel blogs found.")
