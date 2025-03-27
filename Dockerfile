# Use an official Python image as a base
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port on which Streamlit runs
EXPOSE 8501

# Command to run the app
CMD ["streamlit", "run", "qa_chatbot.py"]